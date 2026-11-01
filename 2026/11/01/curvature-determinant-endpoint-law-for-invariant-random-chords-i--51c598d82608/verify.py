"""Numerical/symbolic checks for the curvature-matrix long-chord endpoint law.

Requires numpy, scipy and sympy. This is corroboration, not a substitute for proof.
"""
from math import pi, gamma, sqrt
import numpy as np
from scipy.special import roots_legendre
import sympy as sp


def unit_ball(k):
    return pi**(k/2)/gamma(k/2+1)


def endpoint_matrix(Bminus, Bplus, D):
    q = Bminus.shape[0]
    I = np.eye(q)
    F = np.block([[I, -D/2*I], [I, D/2*I]])
    H = np.block([[Bminus-I/D, I/D], [I/D,Bplus-I/D]])
    return F.T @ H @ F / 2


def tail_mass_coefficient(Bminus, Bplus, D):
    q = Bminus.shape[0]
    Rminus = np.linalg.inv(Bminus)
    Rplus = np.linalg.inv(Bplus)
    G = D*np.eye(q)-Rminus-Rplus
    assert np.linalg.eigvalsh(G).min()>0
    M = endpoint_matrix(Bminus,Bplus,D)
    direct = unit_ball(2*q) / np.sqrt(np.linalg.det(M))
    formula = (2**q * unit_ball(2*q) / D**(q/2)
               * np.sqrt(np.linalg.det(Rminus)*np.linalg.det(Rplus)/np.linalg.det(G)))
    return direct, formula


def exact_matrix_checks():
    for q in (1,2,3):
        A=sp.Matrix([[sp.Integer(5 if i==j else 1 if abs(i-j)==1 else 0) for j in range(q)] for i in range(q)])
        C=sp.Matrix([[sp.Integer(6+i if i==j else 1 if abs(i-j)==1 else 0) for j in range(q)] for i in range(q)])
        Rm=A.inv(); Rp=C.inv()
        D=sp.Integer(3)
        I=sp.eye(q)
        F=(I.row_join(-D*I/2)).col_join(I.row_join(D*I/2))
        H=(A-I/D).row_join(I/D).col_join((I/D).row_join(C-I/D))
        M=F.T*H*F/2
        expected=sp.Rational(1,4)**q*D**q*A.det()*C.det()*(D*I-Rm-Rp).det()
        assert sp.simplify(M.det()-expected)==0
        G=D*I-Rm-Rp
        assert all(G[:k,:k].det()>0 for k in range(1,q+1))
        print('exact determinant q=',q,'det=',M.det())


def ellipsoid_near_diameter_mass(axes, eps, order=180):
    """Exact invariant line measure of ellipsoid chords above D-eps,
    evaluated numerically using angular quadrature for dimensions 2 and 3.
    """
    d=len(axes); q=d-1; a=axes[0]; L=2*a-eps
    inv=np.array(axes)**-2
    gap=4/L**2-inv[0]
    glx, glw=roots_legendre(order)
    sx=(glx+1)/2; sw=glw/2
    if d==2:
        # unoriented angle with primary-axis direction in [-pi/2,pi/2]
        h=inv[1]-inv[0]
        vmax=min(pi/2, np.arcsin(np.sqrt(gap/h)))
        angle=sx*vmax
        alpha=inv[0]+h*np.sin(angle)**2
        term=np.maximum(0,1-L**2*alpha/4)**0.5
        return unit_ball(q)*np.prod(axes)*2*vmax*np.sum(sw*np.sqrt(alpha)*term)
    assert d==3
    # x_0-positive hemisphere: u=(sqrt(1-r²), r cos(phi), r sin(phi)).
    # d sphere area = r/sqrt(1-r²) dr dphi.
    # Integrand after substitution r=rmax*s, rmax²=gap/h(phi).
    phi=2*pi*sx
    ans=0.
    for ph, wp in zip(phi,sw):
        h=(inv[1]-inv[0])*np.cos(ph)**2+(inv[2]-inv[0])*np.sin(ph)**2
        rmax=np.sqrt(gap/h)
        rr=rmax*sx
        alpha=inv[0]+h*rr**2
        term=np.maximum(0,1-L**2*alpha/4)**(q/2)
        ans+=(2*pi*wp)*np.sum(sw*rr*rmax/np.sqrt(1-rr**2)*np.sqrt(alpha)*term)
    return unit_ball(q)*np.prod(axes)*ans


def exact_ellipsoid_prediction(axes):
    d=len(axes);q=d-1;D=2*axes[0]
    R=np.diag([b*b/axes[0] for b in axes[1:]])
    B=np.linalg.inv(R)
    return tail_mass_coefficient(B,B,D)[1]

if __name__ == '__main__':
    exact_matrix_checks()
    for axes in ([2.,1.], [2.,1.4,0.9], [3.,2.4,1.2]):
        expected=exact_ellipsoid_prediction(axes)
        print('axes',axes,'predicted raw coefficient',expected)
        for eps in (.04,.015,.005):
            val=ellipsoid_near_diameter_mass(axes,eps)
            ratio=val/eps**(len(axes)-1)
            print(' eps',eps,'numerical coefficient',ratio,'ratio',ratio/expected)
        assert abs(ratio/expected-1)<.02
    print('CHECKS PASSED')
