"""Reproduce algebraic and finite checks for two-periodic cycle mixing."""
from fractions import Fraction
import math
import numpy as np
import sympy as sp


def transition(n, a, b, r):
    """N-by-N row-stochastic matrix on an even cycle with alternating edges."""
    w = [a if i % 2 == 0 else b for i in range(n)]
    p = sp.zeros(n)
    for i in range(n):
        p[i, i] = 1 - w[i] - w[(i - 1) % n]
        p[i, (i + 1) % n] = w[i] + r
        p[i, (i - 1) % n] = w[(i - 1) % n] - r
    return p


def check_symbolic():
    a,b,r = sp.symbols('a b r', real=True); z=sp.Symbol('z')
    c=a+b; d=a-b; s=1-c
    assert sp.simplify(transition(4,a,b,r).charpoly(z).as_expr() -
        (z-1)*(z-(1-2*c))*((z-s)**2-d*d+4*r*r)) == 0
    # For a six-cycle, the nonzero Bloch modes have angles ±2pi/3.
    X=c*c/4; Y=3*(d*d-4*r*r)/4
    imag=sp.sqrt(3)*r*c
    desired=(z-1)*(z-(1-2*c))*(((z-s)**2-(X+Y))**2+imag**2)
    assert sp.simplify(transition(6,a,b,r).charpoly(z).as_expr()-desired)==0
    C,D,R,T,S=sp.symbols('C D R T S', real=True)
    X=C*C*T*T; Y=(D*D-4*R*R)*S*S
    Im=4*R*C*S*T
    assert sp.expand((X+Y)**2+Im**2-(X-Y)**2-4*X*D*D*S*S)==0
    k=sp.symbols('k',real=True)
    cstar=2/(3-k)
    rhostar=(1+k)/(3-k)
    assert sp.simplify(1-cstar*(1-k)-rhostar)==0
    assert sp.simplify(2*cstar-1-rhostar)==0
    return 4


def check_defect():
    a=sp.Rational(5,12);b=sp.Rational(1,4);r=sp.Rational(1,12)
    P=transition(4,a,b,r)
    assert all(sum(P.row(i))==1 for i in range(4))
    assert all(sum(P.col(j))==1 for j in range(4))
    assert P!=P.T
    assert sp.simplify(P.charpoly().as_expr() - (sp.Symbol('lambda')-1)*(sp.Symbol('lambda')+sp.Rational(1,3))*(sp.Symbol('lambda')-sp.Rational(1,3))**2) == 0
    assert (P-sp.Rational(1,3)*sp.eye(4)).nullspace().__len__() == 1
    return 1


def check_samples():
    count=0
    for n in (4,6,8,10,12):
        theta=2*math.pi/n
        target=(1+math.cos(theta))/(3-math.cos(theta))
        for p in range(13):
            for q in range(13-p):
                a=p/12; b=q/12
                for r in (-min(a,b),-min(a,b)/2,0,min(a,b)/2,min(a,b)):
                    mat=np.array(transition(n,a,b,r).tolist(),dtype=float)
                    assert np.max(np.abs(mat.sum(axis=0)-1))<1e-12
                    assert np.max(np.abs(mat.sum(axis=1)-1))<1e-12
                    assert mat.min()>-1e-12
                    spectrum=np.linalg.eigvals(mat)
                    nearest=int(np.argmin(abs(spectrum-1)))
                    rho=max(abs(e) for j,e in enumerate(spectrum) if j!=nearest)
                    assert rho+1e-8>=target,(n,p,q,r,rho,target)
                    count+=1
    return count


if __name__=='__main__':
    c=check_symbolic()
    d=check_defect()
    n=check_samples()
    print('VERIFY_OK symbolic_identities=%d defective_four_cycle=%d finite_parameter_checks=%d' % (c,d,n))
