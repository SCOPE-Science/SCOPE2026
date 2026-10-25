"""Exact finite checks of an inverse OR-coextinction theorem.
Run using Python 3 standard library: python verify.py
The general claims are established analytically in RESULT.md, not by enumeration.
"""
from fractions import Fraction
from itertools import product
from math import gcd
from functools import reduce
import random, json

RNG = random.Random(245702)
COUNTS = {"profiles": 0, "direct_outcomes": 0, "subset_checks": 0,
          "full_recovery": 0, "lower_order_witnesses": 0,
          "fixed_census_recovery": 0, "primitive_scales": 0,
          "rejected_infeasible": 0, "exact_census_fibers": 0, "interval_candidates": 0, "three_plant_example": 0}

def pop(x): return x.bit_count()

def zero_counts(x, m):
    size = 1 << m
    return [sum(v for t, v in enumerate(x) if t and (t & s))
            for s in range(size)]

def inverse_cov(u, m):
    n = u[(1 << m) - 1]
    f = [n-u[((1 << m)-1)^a] for a in range(1 << m)]
    xx = f[:]
    for i in range(m):
        for s in range(1 << m):
            if s & (1 << i): xx[s] -= xx[s ^ (1 << i)]
    assert xx[0] == 0
    return xx

def gcd_positive(xx):
    return reduce(gcd, (v for v in xx if v > 0))

def direct_probabilities(xx, m, q):
    tags = [t for t, k in enumerate(xx) for _ in range(k)]
    n = len(tags); assert n <= 12
    probs = [Fraction(0) for _ in range(1 << m)]
    for pattern in range(1 << n):
        survive = 0
        for j, t in enumerate(tags):
            if pattern & (1 << j): survive |= t
        z = ((1 << m)-1)^survive
        k = pop(pattern)
        probs[z] += (1-q)**k * q**(n-k)
        COUNTS['direct_outcomes'] += 1
    return probs

def test(xx,m):
    assert xx[0] == 0 and sum(xx) >= 1
    n=sum(xx)
    u=zero_counts(xx,m)
    recovered=inverse_cov(u,m)
    assert recovered == xx
    COUNTS['full_recovery']+=1
    # All proper extinction margins determine a consecutive interval of compatible censuses.
    t=u[:];t[-1]=0
    base=inverse_cov(t,m)
    lower=max([1]+[-base[mask] for mask in range(1,1<<m) if pop(mask)%2])
    upper=min([base[mask] for mask in range(1,1<<m) if pop(mask)%2==0])
    assert lower<=n<=upper
    for candidate in range(lower,upper+1):
        inferred=[0]+[base[mask]+(1 if pop(mask)%2 else -1)*candidate for mask in range(1,1<<m)]
        assert min(inferred)>=0 and sum(inferred)==candidate
        assert zero_counts(inferred,m)[:-1]==u[:-1]
        COUNTS['interval_candidates']+=1
    for candidate in (lower-1,upper+1):
        if candidate>=1:
            inferred=[0]+[base[mask]+(1 if pop(mask)%2 else -1)*candidate for mask in range(1,1<<m)]
            assert min(inferred)<0
    COUNTS['exact_census_fibers']+=1
    n=sum(xx)
    # The m-way extinction moment is replaced with census size, all others retained.
    u2=u[:];u2[-1]=n
    assert inverse_cov(u2,m)==xx
    COUNTS['fixed_census_recovery'] += 1
    g=gcd_positive(xx)
    primitive=[x//g for x in xx]
    assert gcd_positive(primitive)==1
    assert zero_counts(primitive,m)==[v//g for v in u]
    COUNTS['primitive_scales']+=1
    q=Fraction(2,5)
    # Probability that all plants in each nonempty subset are extinct equals q to the union size.
    if n<=12:
        probs=direct_probabilities(xx,m,q)
        assert sum(probs)==1
        for subset in range(1,1<<m):
            e=sum(pr for z,pr in enumerate(probs) if (z&subset)==subset)
            assert e==q**u[subset]
            COUNTS['subset_checks']+=1
    COUNTS['profiles']+=1

# All simple incidence patterns on three observed species.
for v in product((0,1),repeat=7):
    if not any(v): continue
    test([0]+list(v),3)
# Repeated latent-neighbor types, and systems with more observed species.
for m, trials in ((2,120),(3,160),(4,180),(5,150),(6,120)):
    for _ in range(trials):
        N=RNG.randrange(1, min(12,2*m+5))
        xx=[0]*(1<<m)
        for __ in range(N): xx[RNG.randrange(1,1<<m)] += 1
        test(xx,m)
# Sharpness of the moment threshold m-1, at each m=3..9.
for m in range(3,10):
    B=m-1
    even=[0]*(1<<m); odd=[0]*(1<<m)
    for b in range(1<<B):
        t=b|(1<<B)
        (even if pop(b)%2==0 else odd)[t]+=1
    assert sum(even)==sum(odd)==(1<<(m-2))
    ue=zero_counts(even,m); uo=zero_counts(odd,m)
    for s in range(1,1<<m):
        if pop(s)<=m-2: assert ue[s]==uo[s]
    assert ue[(1<<(m-1))-1]!=uo[(1<<(m-1))-1]
    assert even != odd
    COUNTS['lower_order_witnesses']+=1
# Three named plants: identical single and pairwise extinction marginals,
# but three consecutive possible pollinator census sizes.
for n in (6,7,8):
    xx=[0]+[1+(1 if pop(mask)%2 else -1)*(n-7) for mask in range(1,8)]
    assert sum(xx)==n and min(xx)>=0
    ux=zero_counts(xx,3)
    assert ux[1:7]==[4,4,6,4,6,6]
    COUNTS['three_plant_example']+=1
# Realizable first-order survival moments are not arbitrary.
# Two species each with one pollinator incident implies union size cannot equal 3.
assert min(inverse_cov([0,1,1,3],2))<0
COUNTS['rejected_infeasible']+=1

print(json.dumps({"status":"passed","exact_arithmetic":"Fraction and integer arithmetic",
                  "scope":"finite tests of reconstruction and sharpness, not proof of universal statements",
                  "counts":COUNTS},sort_keys=True,separators=(',',':')))
