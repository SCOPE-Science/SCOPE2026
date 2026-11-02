"""Independent exact-rational checks for the first mixed/split EKSM comparison.
Run with: python3 verify.py
Standard library only. This tests identities and finite examples, not the infinite theorem.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isfinite
from random import Random


def avg(values, weights):
    return sum((w * x for w, x in zip(weights, values)), F(0))


def spectral_ratio_sq(lam, weights):
    assert len(lam) == len(weights) >= 3
    assert all(x > 0 for x in lam) and all(w > 0 for w in weights)
    assert sum(weights) == 1 and len(set(lam)) >= 3
    m = avg([1 / x for x in lam], weights)
    t = avg(lam, weights)
    s = avg([x*x for x in lam], weights)
    den = 1 - 2*m*t + m*m*s
    assert den > 0
    return m*m*s / den


def direct_ratio_sq(lam, weights):
    """Compute both orthogonalized candidates from weighted Gram projections."""
    m = avg([1 / x for x in lam], weights)
    inv_residual = [1/x - m for x in lam]
    sig2 = avg([v*v for v in inv_residual], weights)
    assert sig2 > 0
    def projected_residual_sq(h):
        mean_h = avg(h, weights)
        cross = avg([a*b for a,b in zip(h,inv_residual)], weights)
        return avg([a*a for a in h], weights) - mean_h*mean_h - cross*cross/sig2
    s_vec = list(lam)
    # scaling the mixed candidate by sigma does not change its rho
    m_vec = [1-m*x for x in lam]
    rs = projected_residual_sq(s_vec)
    rm = projected_residual_sq(m_vec)
    assert rs > 0 and rm > 0
    rho_s2 = rs / avg([x*x for x in s_vec], weights)
    rho_m2 = rm / avg([x*x for x in m_vec], weights)
    return rho_m2/rho_s2


def q(k,p):
    return (k-1)**2*p*(1-p)*(1+(k*k-1)*p) / ((1+(k-1)*p)**2 * (k*k-(k*k-1)*p))


def p_cubic(k,p):
    return (k*(1-p)**3 + k*k*(2*k-1)*p*(1-p)**2 +
            (k-2)*p*p*(1-p) - k*k*p**3)


def derivative_cross_product(k,p):
    a=k-1; b=k*k-1
    aa=1+a*p; bb=k*k-b*p
    n=(k-1)**2*p*(1-p)*(1+b*p)
    nd=(k-1)**2*((1-2*p)*(1+b*p)+b*p*(1-p))
    d=aa*aa*bb
    dd=2*a*aa*bb-b*aa*aa
    return nd*d-n*dd


def check():
    rng=Random(34202610)
    direct=0
    derivatives=0
    inequalities=0
    for n in range(3,9):
        for z in range(130):
            choices=sorted(rng.sample(range(1,100),n))
            lam=[F(x,rng.randrange(1,11)) for x in choices]
            if len(set(lam)) < 3: continue
            a=[rng.randrange(1,100) for _ in range(n)]
            weights=[F(x,sum(a)) for x in a]
            assert spectral_ratio_sq(lam,weights)==direct_ratio_sq(lam,weights)
            direct+=1
            # A uniform spectral enclosure gives a non-sharp finite test bound.
            lo=min(lam); hi=max(lam)
            k=hi/lo
            p=F(rng.randrange(1,1000),1000)
            assert F(0)<=q(k,p)<1
            inequalities+=1
    for kval in [F(x,y) for x in (2,3,4,7,13,33) for y in (1,2) if x>y]:
        for i in range(1,150):
            pp=F(i,150)
            lhs=derivative_cross_product(kval,pp)
            rhs=kval*(kval-1)**2*p_cubic(kval,pp)*(1+(kval-1)*pp)
            assert lhs==rhs
            derivatives+=1
    # Bernstein/Descartes representation of the stationary cubic.
    for kval in [F(11,10),F(3,2),F(2),F(7),F(100)]:
        for i in range(1,300):
            pp=F(i,300)
            x=pp/(1-pp)
            poly=kval+kval*kval*(2*kval-1)*x+(kval-2)*x*x-kval*kval*x**3
            assert p_cubic(kval,pp)==(1-pp)**3*poly
    print('exact direct channel comparisons:',direct)
    print('exact q interval checks:',inequalities)
    print('exact derivative-identity checks:',derivatives)
    print('exact Bernstein-polynomial checks:',5*299)
    print('All exact-rational supplementary checks passed.')

if __name__=='__main__': check()
