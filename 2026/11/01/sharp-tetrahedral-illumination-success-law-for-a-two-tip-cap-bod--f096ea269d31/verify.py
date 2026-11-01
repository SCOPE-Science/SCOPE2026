"""Independent finite diagnostics for two-tip tetrahedral spherical-cap formula.
Scientific proof is in RESULT.md; randomized checks are not an infinite proof.
Requires Python 3, NumPy, SciPy, mpmath.
"""
import math
import numpy as np
from scipy.integrate import quad
import mpmath as mp

VERTICES = np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)/math.sqrt(3)
D = math.acos(1/3)
G = math.acos(-1/3)
A0, A1 = D/2, G/2


def lens_closed(alpha):
    if alpha <= A0:
        return 0.0
    assert alpha <= A1 + 1e-12
    b = math.acos(max(-1., min(1., 1/(math.sqrt(2)*math.tan(alpha)))))
    z = math.cos(alpha)
    eta = math.acos(max(-1., min(1., (1/3-z*z)/(1-z*z))))
    return 2*math.pi-2*eta-4*z*b


def lens_quadrature(alpha):
    if alpha <= A0:
        return 0.
    def integrand(t):
        c = (math.cos(alpha)-math.cos(D)*math.cos(t))/(math.sin(D)*math.sin(t))
        return 2*math.acos(max(-1.,min(1.,c)))*math.sin(t)
    return quad(integrand, D-alpha, alpha, epsabs=5e-12, epsrel=1e-11)[0]


def probability_exact(r):
    alpha = math.asin(1/r)
    if alpha <= A0:
        return 0.0
    if alpha <= A1 + 1e-12:
        return 3*lens_closed(alpha)/math.pi
    if alpha >= D:
        return 1.
    raise ValueError('only bounds, not an exact formula, on the intermediate interval')


def run():
    assert np.max(np.abs(VERTICES@VERTICES.T-(4/3*np.eye(4)-np.ones((4,4))/3)))<2e-15
    assert sum(i!=j for i in range(4) for j in range(4))==12
    assert abs(math.sin(A0)-1/math.sqrt(3))<1e-14
    assert abs(math.sin(A1)-math.sqrt(2/3))<1e-14
    assert abs(math.sin(D)-2*math.sqrt(2)/3)<1e-14
    assert abs(probability_exact(math.sqrt(3/2))-(3-4/math.sqrt(3)))<1e-12
    for r in [1.23,1.25,1.30,1.40,1.55,1.62,1.70]:
        alpha=math.asin(1/r)
        assert abs(lens_closed(alpha)-lens_quadrature(alpha))<4e-11,(r,lens_closed(alpha),lens_quadrature(alpha))
        p=probability_exact(r)
        assert 0<p<1
    assert probability_exact(1.03)==1
    assert probability_exact(math.sqrt(3)+0.1)==0
    mp.mp.dps=90
    rc=mp.sqrt(3)
    coeff=4*mp.sqrt(2)/(mp.pi*3**(mp.mpf(3)/4))
    def p_mp(r):
        a=mp.asin(1/r); c=mp.cos(a)
        b=mp.acos(mp.cot(a)/mp.sqrt(2))
        eta=mp.acos((mp.mpf(1)/3-c*c)/(1-c*c))
        return 3*(2*mp.pi-2*eta-4*c*b)/mp.pi
    for k in [4,5,6,7]:
        dr=mp.mpf(10)**(-k)
        ratio=p_mp(rc-dr)/(coeff*dr**(mp.mpf(3)/2))
        assert abs(ratio-1) < mp.mpf('1.31')*dr,(k,ratio)
    rng=np.random.default_rng(19027)
    axes=rng.normal(size=(280000,3))
    axes/=np.linalg.norm(axes,axis=1)[:,None]
    dot=axes@VERTICES.T
    for r in [1.03,1.23,1.3,1.5,1.67,1.75]:
        threshold=math.sqrt(1-1/r**2)
        empirical=np.mean((np.max(dot,axis=1)>threshold)&(np.min(dot,axis=1)<-threshold))
        theoretical=probability_exact(r)
        assert abs(empirical-theoretical)<0.0065,(r,empirical,theoretical)
    print('PASS: tetrahedral inner products, geometry thresholds, lens quadrature,')
    print('critical asymptotic, and reproducible randomized consistency checks')

if __name__=='__main__':
    run()
