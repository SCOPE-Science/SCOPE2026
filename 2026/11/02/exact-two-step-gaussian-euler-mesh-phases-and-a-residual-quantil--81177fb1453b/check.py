"""Standalone numerical checks for a two-step Gaussian-flow Euler theorem.

Only Python's standard library is needed. Numerical tests supplement, but do
not replace, the analytic proof given in RESULT.md.
"""
import math
import random


def multiplier(c, t):
    return 1.0 - c*t*(1.0-t)


def endpoint_error(c, t):
    return abs(abs(multiplier(c, t)) - math.exp(-c/2.0))


def roots(c, sign):
    r = math.exp(-c/2.0)
    z = 1.0 - 4.0*(1.0-sign*r)/c
    if z < -1.0e-13:
        return []
    if abs(z) <= 1.0e-13:
        return [0.5]
    d = math.sqrt(z)
    return [(1.0-d)/2.0, (1.0+d)/2.0]


def bisect(f, a, b):
    fa, fb = f(a), f(b)
    assert fa*fb <= 0
    for _ in range(90):
        m = (a+b)/2.0
        fm = f(m)
        if fa*fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a+b)/2.0


def simpson(f, a, b, n=16000):
    assert n%2 == 0
    h = (b-a)/n
    return h/3.0*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2)) + 2*sum(f(a+i*h) for i in range(2,n,2)))


def weighted_median(epsilon=0.0, regularizer=0.0):
    # For dot x = -(4t+epsilon)x, K(1,t)R(t) is, up to a
    # positive constant, abs((4t+epsilon)**2-4).
    f = lambda s: math.sqrt(abs((4*s+epsilon)**2-4) + regularizer)
    total = simpson(f,0,1)
    return bisect(lambda t: simpson(f,0,t)-total/2, 0,1)


def perturbed_multiplier(epsilon,t):
    return (1-epsilon*t)*(1-(4*t+epsilon)*(1-t))


def main():
    cp=bisect(lambda c:c-4*(1-math.exp(-c/2)),3,4)
    cr=bisect(lambda c:c-4*(1+math.exp(-c/2)),4,5)
    assert abs(cp-3.1872485200800806)<1e-12
    assert abs(cr-4.4354302115141815)<1e-12
    for c, expected in [(1,0),(cp,1),(3.5,2),(cr,3),(5,4)]:
        rr=roots(c,1)+roots(c,-1)
        assert len(rr)==expected,(c,len(rr),rr)
        for t in rr:
            assert 0<t<1 and endpoint_error(c,t)<3e-12
    rng=random.Random(7091)
    for _ in range(4000):
        c=rng.uniform(.001,18)
        t=rng.uniform(.0001,.9999)
        x=rng.uniform(-2,2)
        x1=x # first Euler update, as drift vanishes at 0
        x2=x1+(1-t)*(-c*t*x1)
        assert abs(x2-multiplier(c,t)*x)<1e-13
        expected=max(0.0,1-c/4-math.exp(-c/2))
        roots_plus=roots(c,1)
        if roots_plus:
            candidate=min(endpoint_error(c,u) for u in roots_plus)
        else:
            candidate=endpoint_error(c,.5)
        assert abs(candidate-expected)<1e-12
    q=weighted_median()
    gap=math.exp(-2)-(2*q-1)**2
    assert .5<q<2/3 and gap>math.exp(-2)-1/9>0
    assert abs(q-.63916669266)<3e-5
    left=(1-math.exp(-1))/2
    right=(1+math.exp(-1))/2
    assert endpoint_error(4,left)<1e-14 and endpoint_error(4,right)<1e-14
    # Strict contraction and positive profile-regularization do not eliminate
    # the counterexample; root continuation supplies an exact oracle grid.
    for eps,regularizer in [(1e-3,1e-3),(1e-4,1e-5),(1e-5,1e-6)]:
        z=weighted_median(eps,regularizer)
        err=abs(abs(perturbed_multiplier(eps,z))-math.exp(-2-eps))
        assert err>0.045,(eps,z,err)
        for x in (left,right):
            a,b=x-.04,x+.04
            s=bisect(lambda t: perturbed_multiplier(eps,t)-math.exp(-2-eps),a,b)
            assert abs(perturbed_multiplier(eps,s)-math.exp(-2-eps))<2e-14
    # Pairwise error at a negative multiplier has the exact value 4e^{-c}.
    for c in [cr+0.01,5.,8.,15.]:
        for t in roots(c,-1):
            r=math.exp(-c/2)
            assert abs(multiplier(c,t)+r)<3e-14
            assert abs((multiplier(c,t)-r)**2-4*math.exp(-c))<3e-13
    print('PASS: exact phase threshold, root counts, 4000 propagation identities,')
    print('      local-surrogate median, positive regularization and strict contraction')
    print('      q =',format(q,'.12f'),'E4(q) =',format(gap,'.12f'))
    print('      c_pos =',format(cp,'.12f'),'c_rev =',format(cr,'.12f'))


if __name__=='__main__':
    main()
