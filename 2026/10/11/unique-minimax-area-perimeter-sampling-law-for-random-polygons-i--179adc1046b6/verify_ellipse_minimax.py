"""Reproduce quadrature sanity checks for an ellipse sampling minimax identity.
Uses only Python standard library.  The analytic proof, not these finite checks,
establishes the continuous parameter statements.
"""
from math import pi, sin, cos, sqrt

N = 32768
ANGLES = [(2*pi)*(j+0.5)/N for j in range(N)]
COS2 = [cos(2*t) for t in ANGLES]

def average(vals):
    return sum(vals)/len(vals)

def evaluate(e):
    E = [1-2*e*c+e*e for c in COS2]
    C = average([v**(-.5) for v in E])
    W = [v**(-1.5)/C**3 for v in E]
    H0 = average([v**(1/3) for v in W])
    assert abs(H0-1)<5e-13

    def H(lam):
        return average([(lam+(1-lam)*w)**(1/3) for w in W])
    def D(lam):
        return average([(1-w)*(lam+(1-lam)*w)**(-2/3) for w in W])
    if e:
        assert D(0)>0 and D(1)<0
        lo,hi=0.,1.
        for _ in range(55):
            mid=(lo+hi)/2
            if D(mid)>0: lo=mid
            else: hi=mid
        lam=(lo+hi)/2
    else: lam=.5
    A = [lam+(1-lam)*w for w in W]
    h=average([z**(1/3) for z in A])
    q=[z**(1/3)/h for z in A]
    ra=average([z**(-2) for z in q])
    rp=average([w*z**(-2) for w,z in zip(W,q)])
    M=h**3
    assert abs(M-ra)<3e-10
    assert abs(M-rp)<3e-10
    C14=average([v**(-.25) for v in E])
    lower=2-C14/sqrt(C)
    assert M>=lower-3e-12
    qP=[v**(-.5)/C for v in E]
    assert abs(average(qP)-1)<3e-13
    return lam,M,lower

for e in (0.,.005,.01,.02,.05,.1,.25,.5,.8,.95):
    lam,M,L=evaluate(e)
    print('e=%.3f lambda=%.9f M=%.12f gap_lower=%.12f' % (e,lam,M,L))
    if 0<e<=.02:
        assert abs((M-1)/e**2-.375)<.0003
print('ELLIPSE_MINIMAX_STANDARD_LIBRARY_CHECKS_OK')
