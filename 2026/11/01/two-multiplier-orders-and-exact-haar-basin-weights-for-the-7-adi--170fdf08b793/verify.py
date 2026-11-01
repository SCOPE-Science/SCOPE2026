"""Finite-ring tests of the 7-adic quadratic-shell and Haar-basin theorem.

No finite calculation is used as a substitute for the infinite lifting proof.
"""
from collections import Counter, defaultdict

P = 7

def residue_roots(modulus):
    roots = [x for x in range(modulus) if (x*x-x+1) % modulus == 0]
    assert len(roots) == 2
    return (next(x for x in roots if x % P == 3),
            next(x for x in roots if x % P == 5))

def valuation_mod(y, power):
    if y % (P**power) == 0:
        return power
    m = 0
    while y % P == 0:
        y //= P
        m += 1
    return m

def label(y, a, b, k):
    mod = P**k
    ma = valuation_mod((y-a) % mod, k)
    mb = valuation_mod((y-b) % mod, k)
    if ma == k:
        return ('fixed_a',)
    if mb == k:
        return ('fixed_b',)
    if ma > 0:
        t = ((y-a) // (P**ma)) % P
        return ('a', ma, min(t, P-t))
    if mb > 0:
        return ('b', mb)
    raise AssertionError(('unclassified',y,k))

# Explicit linear multiplier and quadratic-coefficient congruences.
a49,b49 = residue_roots(49)
assert (a49,b49) == (31,19)
assert (pow(2*a49,2,49),pow(2*b49,6,49)) == (22,15)
for r,e in [(a49,2),(b49,6)]:
    lam = (2*r)%7
    assert pow(lam,e,7) == 1 and all(pow(lam,j,7)!=1 for j in range(1,e))
    aa,bb = 1,0
    for _ in range(e):
        bb = (lam*bb+aa*aa)%7
        aa = (lam*aa)%7
    assert aa == 1 and bb == 0

for k in range(2,6):
    mod = P**k
    a,b = residue_roots(mod)
    labels = {}
    cycles = {}
    counts = Counter()
    period_sets = defaultdict(set)
    for x in range(mod):
        seen = {}
        path = []
        y = x
        while y not in seen and y not in labels:
            seen[y] = len(path)
            path.append(y)
            y = (y*y+1) % mod
        if y in labels:
            c,per = labels[y],cycles[y]
        else:
            start = seen[y]
            cyc = path[start:]
            per = len(cyc)
            c = label(y,a,b,k)
            assert all(label(v,a,b,k)==c for v in cyc)
        for v in path:
            labels[v] = c
            cycles[v] = per
        counts[labels[x]] += 1
        period_sets[labels[x]].add(cycles[x])
    assert sum(counts.values()) == mod
    for m in range(1,k):
        for u in (1,2,3):
            key=('a',m,u)
            assert counts[key] == 4*P**(k-m-1), (k,key,counts[key])
            assert period_sets[key] == {2*P**(k-m-1)}
        key=('b',m)
        expected=(31*P**(k-2)) if m==1 else (24*P**(k-m-1))
        assert counts[key]==expected, (k,key,counts[key],expected)
        assert period_sets[key]=={6*P**(k-m-1)}
    assert counts[('fixed_a',)]==2 and counts[('fixed_b',)]==4
    print(f'k={k}: modulus={mod}; alpha-shell components={3*(k-1)}; beta-shells={k-1}; all counts and orbit lengths match')

print('Z7_QUADRATIC_MINIMAL_BASINS_VERIFY_OK')
