"""Reproducibility checks for flat Klein-bottle intrinsic distance laws.

Pure Python (standard library). The general theorem is proved analytically;
finite computations here test the quotient reduction and limiting coefficient.
"""
from fractions import Fraction
from math import sqrt, pi
from random import Random


def circ(u, L):
    u = u % L
    return min(u, L - u)


def reduced_squared(p, q, L, H):
    x, y = p
    xx, yy = q
    v = abs(y - yy)
    a = circ(x - xx, L)
    b = circ(x + xx, L)
    return min(a*a + v*v, b*b + (H-v)**2)


def deck_squared(p, q, L, H):
    x, y = p
    xx, yy = q
    candidates = []
    for m in range(-2, 3):
        for n in range(-2, 3):
            candidates.append((x-xx-m*L)**2 + (y-yy-2*n*H)**2)
            candidates.append((x+xx-m*L)**2 + (y-yy-(2*n+1)*H)**2)
    return min(candidates)


def simpson(f, lo, hi, n=4000):
    assert n % 2 == 0
    h = (hi-lo)/n
    total = f(lo) + f(hi)
    for j in range(1,n):
        total += (4 if j % 2 else 2)*f(lo+j*h)
    return total*h/3


def cdf(L, H, r):
    a = L/2
    def g(v):
        if v >= r:
            return 0.
        return min(1., sqrt(max(0., r*r-v*v))/a)
    return simpson(lambda v: 2*(H-v)/(H*H)*
                   (g(v)+g(H-v)-g(v)*g(H-v)), 0., H, 12000)


def diameter_tail(L, H, s):
    a=L/2
    d2=(L*L+H*H)/4
    assert 0 < s < min(H*H/4, L*L/8)
    q=d2-s
    lo=sqrt(H*H/4-s)
    hi=H-lo
    def surv(t):
        w=q-t*t
        if w<=0: return 1.
        if w>=a*a: return 0.
        return max(0.,1.-sqrt(w)/a)
    return simpson(lambda v:2*(H-v)/(H*H)*surv(v)*surv(H-v),lo,hi,6000)


def main():
    rng=Random(20261024)
    checks=0
    for l_int,h_int in [(2,1),(1,2),(3,5),(5,3),(7,7)]:
        L=Fraction(l_int,2)
        H=Fraction(h_int,3)
        for _ in range(700):
            p=(L*Fraction(rng.randrange(1000),1000), H*Fraction(rng.randrange(1000),1000))
            q=(L*Fraction(rng.randrange(1000),1000), H*Fraction(rng.randrange(1000),1000))
            assert reduced_squared(p,q,L,H)==deck_squared(p,q,L,H)
            checks+=1
        p=(L/2,3*H/4)
        q=(Fraction(0),H/4)
        assert reduced_squared(p,q,L,H)==(L*L+H*H)/4
        checks+=1
    print('exact quotient and diameter checks:',checks)
    for L,H in [(1.,2.),(2.,1.),(1.,1.),(3.,4.)]:
        r=min(L,H)/5
        observed=cdf(L,H,r)
        expected=pi*r*r/(L*H)
        assert abs(observed-expected)<5e-7,(L,H,observed,expected)
        s=1e-4*min(L*L,H*H)
        K=16/(3*L**4*H**2)
        numerical=diameter_tail(L,H,s)/s**3
        assert abs(numerical/K-1)<0.003,(L,H,numerical,K)
        print(f'L={L:g}, H={H:g}; small CDF={observed:.12g}; tail coefficient={numerical:.10g}, predicted={K:.10g}')
    # Equal area and diameter do not alone distinguish these metrics.
    assert (2*1)==(1*2)
    assert (2**2+1**2)==(1**2+2**2)
    assert Fraction(16,3*2**4*1**2)==Fraction(1,3)
    assert Fraction(16,3*1**4*2**2)==Fraction(4,3)
    # An independent direct-pair Monte Carlo check of the complete CDF.
    rng=Random(410041)
    L,H=2.,1.
    thresholds=[0.3,0.7,1.0]
    cnt=[0]*len(thresholds)
    N=180000
    for _ in range(N):
        p=(L*rng.random(),H*rng.random())
        q=(L*rng.random(),H*rng.random())
        d2=reduced_squared(p,q,L,H)
        for j,r in enumerate(thresholds):
            if d2<=r*r: cnt[j]+=1
    for r,c in zip(thresholds,cnt):
        empirical=c/N
        predicted=cdf(L,H,r)
        assert abs(empirical-predicted)<0.007,(r,empirical,predicted)
        print(f'r={r:g}, empirical CDF={empirical:.6f}, exact-integral CDF={predicted:.6f}')
    print('ALL CHECKS PASSED')


if __name__=='__main__':
    main()
