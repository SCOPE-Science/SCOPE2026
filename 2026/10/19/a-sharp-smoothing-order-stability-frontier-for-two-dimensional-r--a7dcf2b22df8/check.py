"""Standalone reproducibility checks for sharp two-grid smoothing-order norms.
Only mathematical verification; the analytical proof establishes global results.
Requires Python 3 and NumPy.
"""
import math
import numpy as np


def operators(kappa, sine):
    s=float(sine); c=math.sqrt(max(0.,1-s*s))
    A=np.diag([1.,kappa]); p=np.array([[c],[s]])
    W=A@A
    C=np.eye(2)-p@((p.T@W)/(p.T@W@p))
    D=np.eye(2)-A/kappa
    return C@D,D@C


def norms(kappa, sine):
    s=float(sine); c=math.sqrt(max(0.,1-s*s))
    den=c*c+(kappa*kappa)*s*s
    d=1.-1./kappa
    return (d*s*math.hypot(kappa*kappa*s,c)/den,
            d*(kappa*kappa)*s/den)


def ceiling(kappa):
    d=1-1/kappa
    return d, d*(1. if kappa<=math.sqrt(2.) else kappa*kappa/(2.*math.sqrt(kappa*kappa-1.)))


def run():
    count=0
    for kappa in (1.001,1.1,math.sqrt(2.),1.5,2.,2.875129794,3.,5.,10.,100.):
        for j in range(151):
            s=j/150
            pre,post=operators(kappa,s)
            npre,npost=norms(kappa,s)
            assert abs(np.linalg.norm(pre,2)-npre) < 2.e-10*max(1,npre)
            assert abs(np.linalg.norm(post,2)-npost) < 2.e-10*max(1,npost)
            assert npre <= ceiling(kappa)[0]+2.e-11
            assert npost <= ceiling(kappa)[1]+2.e-11
            assert np.max(np.abs(np.sort(np.linalg.eigvals(pre))-np.sort(np.linalg.eigvals(post))))<2.e-9
            lam=(1-1/kappa)*kappa*kappa*s*s/(1+(kappa*kappa-1)*s*s)
            for T in (pre,post):
                assert np.linalg.norm(T@T-lam*T)<2.e-9*max(1.,np.linalg.norm(T)**2)
            count+=1
        sstar=(1. if kappa<=math.sqrt(2) else 1/math.sqrt(kappa*kappa-1))
        a,b=operators(kappa,sstar)
        lo,hi=ceiling(kappa)
        assert abs(np.linalg.norm(b,2)-hi)<2e-9*max(1,hi)
        assert abs(norms(kappa,1)[0]-lo)<2e-9*max(1,lo)
    root=2.875129794
    import scipy.optimize
    r=scipy.optimize.brentq(lambda x:x**3-x**2-4*x-4,2.8,3)
    assert abs(r-root)<1e-8
    for kap in [2.5,2.8,3.0,4.0]:
        _,p=ceiling(kap)
        assert (p>1)==(kap>r)
    print(f'PASS {count} rank-one normal-equation matrix tests; exact extrema and threshold checks')

if __name__=='__main__':run()
