"""Independent checks for the perimeter law of central sections of a triaxial ellipsoid.
Run: python ellipsoid_section_perimeter_checker.py
Requires numpy and scipy. Finite tests corroborate, not replace, the proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipe


def perimeter(A, C):
    if A < C:
        A, C = C, A
    return 4*A*float(ellipe(1-(C/A)**2))


def partials(A, C):
    g = lambda theta: math.hypot(A*math.cos(theta), C*math.sin(theta))
    Da = 4*quad(lambda th: A*math.cos(th)**2/g(th),0,math.pi/2,epsabs=1e-13)[0]
    Dc = 4*quad(lambda th: C*math.sin(th)**2/g(th),0,math.pi/2,epsabs=1e-13)[0]
    return Da,Dc


def section_perimeter(u,axes):
    """Calculate via eigenvalues of the restricted inverse-squared axis matrix."""
    u=np.asarray(u,dtype=float)
    u=u/np.linalg.norm(u)
    q=1/np.square(np.asarray(axes,dtype=float))
    tr=np.sum(q)-np.dot(q,u*u)
    det=np.dot(np.array([q[1]*q[2],q[0]*q[2],q[0]*q[1]]),u*u)
    delta=max(0.,tr*tr-4*det)**.5
    eiglo=(tr-delta)/2
    eighi=(tr+delta)/2
    return perimeter(1/math.sqrt(eiglo),1/math.sqrt(eighi))


def section_perimeter_direct(u,axes):
    u=np.array(u,dtype=float);u/=np.linalg.norm(u)
    v=np.cross(u,np.array([0.,1.,0.]))
    if np.linalg.norm(v)<1e-7:v=np.cross(u,[1.,0.,0.])
    v/=np.linalg.norm(v);w=np.cross(u,v)
    B=np.stack([v,w],axis=1)
    eig=np.linalg.eigvalsh(B.T@np.diag(1/np.square(axes))@B)
    return perimeter(1/math.sqrt(eig[0]),1/math.sqrt(eig[1]))


def run():
    rng=np.random.default_rng(43107)
    for axes in ((3.,2.,1.),(2.,1.7,1.1),(1.2,1.1,.9)):
        for k in range(500):
            u=rng.normal(size=3)
            a=section_perimeter(u,axes)
            b=section_perimeter_direct(u,axes)
            assert abs(a-b)<2e-10,(a,b)
        A,B,C=axes
        pmin=perimeter(B,C); ps=perimeter(A,C); pmax=perimeter(A,B)
        assert pmin<ps<pmax
        for k in range(1500):
            u=rng.normal(size=3)
            p=section_perimeter(u,axes)
            assert pmin-1e-9<=p<=pmax+1e-9,(pmin,p,pmax)
        dA,dC=partials(A,C)
        mu=A*(A*A-B*B)*dA/(B*B)
        nu=C*(B*B-C*C)*dC/(B*B)
        assert mu>0 and nu>0
        h=1e-3
        base=section_perimeter([0.,1.,0.],axes)
        px=section_perimeter([h,math.sqrt(1-h*h),0.],axes)
        pz=section_perimeter([0.,math.sqrt(1-h*h),h],axes)
        errx=abs((px-base)/h**2+mu/2)/(mu/2)
        errz=abs((pz-base)/h**2-nu/2)/(nu/2)
        assert errx<4e-5 and errz<4e-5,(axes,errx,errz)
        print('SADDLE_HESSIAN_OK',axes,'P*',format(ps,'.9f'),'density log coefficient',format(1/(math.pi*math.sqrt(mu*nu)),'.9f'))
    # Analytic normal form: the density of t=(nu*z^2-mu*x^2)/2 for two
    # antipodal saddles under normalized spherical area has leading coefficient.
    mu,nu=14.053208218495406,1.5917449843191998
    coeff=1/(math.pi*math.sqrt(mu*nu))
    assert abs(coeff-0.06730163915975881)<1e-14
    print('NORMAL_FORM_LOGARITHMIC_COEFFICIENT_OK')
    print('INDEPENDENT_SECTION_EIGENVALUE_AND_SADDLE_CHECKS_OK')

if __name__=='__main__':run()
