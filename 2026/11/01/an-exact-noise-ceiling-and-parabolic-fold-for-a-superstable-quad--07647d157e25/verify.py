"""Finite independent diagnostics for a noise-forced quadratic map.

These numerical checks are illustrations, not proofs of the all-parameter theorem.
Requires only Python 3's standard library.
"""
from math import sqrt, isclose
from random import Random

E_CRIT = sqrt(73-22*sqrt(11))/4
U_CRIT = (51+64*E_CRIT**3-16*E_CRIT**2-556*E_CRIT)/88

def p(u,e):
    return 3*e-e*e+2*(1-e)*u*u-u**4-u

def g(u,e):
    return p(u,e)+u

def gp(u,e):
    return 4*u*(1-e-u*u)

def bisect(f,a,b):
    fa=f(a)
    assert fa*f(b)<0
    for _ in range(75):
        mid=(a+b)/2
        if f(mid)*fa>0: a,fa=mid,f(mid)
        else: b=mid
    return (a+b)/2

def image_interval(lo,hi,e):
    near=min(lo*lo,hi*hi) if not lo<=0<=hi else 0.
    far=max(lo*lo,hi*hi)
    return 1-far-e, 1-near+e

def check():
    tests=0
    assert 0.046<E_CRIT<0.047 and .286<U_CRIT<.288
    assert abs(p(U_CRIT,E_CRIT))<1e-13 and abs(gp(U_CRIT,E_CRIT)-1)<1e-13; tests+=4
    for e in [E_CRIT * j/24 for j in range(1,24)]:
        lower=3*e+e*e
        u=bisect(lambda x:p(x,e),lower,U_CRIT)
        a=-3*e-e*e
        v=1-u*u-e; w=1+e
        assert 0 < lower<u<v<1<w and abs(a)<u
        assert isclose(g(u,e),u,rel_tol=0,abs_tol=2e-14)
        lo,hi=image_interval(a,u,e)
        assert isclose(lo,v,abs_tol=2e-14) and isclose(hi,w,abs_tol=2e-14)
        lo,hi=image_interval(v,w,e)
        assert isclose(lo,a,abs_tol=2e-14) and isclose(hi,u,abs_tol=2e-14)
        assert 0<gp(u,e)<1
        tests+=9
    # The upper branch exists near the fold and repels boundary-map deviations.
    for fraction in [.001,.01,.05,.10]:
        e=E_CRIT*(1-fraction)
        up=bisect(lambda x:p(x,e),U_CRIT,.62)
        assert up>U_CRIT and gp(up,e)>1
        assert up<1-up*up-e
        tests+=3
    # Tangent factorisation at criticality: p=(u-u*)^2 H(u).
    h=lambda u:2*(1-E_CRIT)-3*U_CRIT**2-2*U_CRIT*u-u*u
    assert h(1)>0
    rng=Random(728)
    for _ in range(500):
        u=rng.random()
        assert abs(p(u,E_CRIT)-(u-U_CRIT)**2*h(u))<2e-14
        assert h(u)>0
        tests+=2
    # Above threshold the comparison polynomial has no nonpositive values.
    for e in [.0465,.047,.048,.049,.05]:
        for j in range(201):
            u=j/200
            assert p(u,e)>0
            tests+=1
    # Fold scaling and critical parabolic n^-1 law (asymptotic numeric checks).
    B=4*(1-E_CRIT)-12*U_CRIT*U_CRIT
    E=3-2*E_CRIT-2*U_CRIT*U_CRIT
    c=sqrt(2*E/B)
    for delta in [1e-5,1e-6,1e-7]:
        e=E_CRIT-delta
        ul=bisect(lambda x:p(x,e),3*e+e*e,U_CRIT)
        ur=bisect(lambda x:p(x,e),U_CRIT,.35)
        assert abs((ur-ul)/(2*sqrt(delta))/c-1)<.015
        tests+=1
    u=U_CRIT-.02
    for _ in range(120000):
        u=g(u,E_CRIT)
    assert abs((U_CRIT-u)*120000*B/2-1)<.02
    tests+=1
    print(f'PASS {tests} diagnostics; epsilon_crit={E_CRIT:.15f}; '
          f'u_crit={U_CRIT:.15f}; gap={1-U_CRIT**2-E_CRIT-U_CRIT:.15f}; '
          f'fold_coefficient={c:.12f}')

if __name__=='__main__':
    check()
