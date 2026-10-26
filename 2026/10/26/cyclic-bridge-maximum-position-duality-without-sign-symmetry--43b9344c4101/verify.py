"""Exact finite checks for cyclic bridge maximum–position identities.

No statistical sampling is used. The infinite theorem rests on the accompanying
algebraic proof; enumeration only guards finite cases and boundaries.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product


def features(a, k):
    s = 0
    highest = 0
    kth = None
    for j, x in enumerate(a, 1):
        s += x
        highest = max(highest, s)
        if j == k:
            kth = s
    assert s == 0
    return highest, kth


def orbit(a):
    n = len(a)
    return [a[j:] + a[:j] for j in range(n)]


def verify_orbit(a):
    n = len(a)
    rows = orbit(a)
    for k in range(1, n):
        pairs = [features(b, k) for b in rows]
        assert sum(x for _, x in pairs) == 0
        assert 2 * sum(m * x for m, x in pairs) == sum(x*x for _, x in pairs)
        dual = orbit(tuple(-v for v in reversed(a)))
        both = rows + dual
        distribution = Counter((2*m - x, x) for m, x in map(lambda b: features(b, k), both))
        reflected = Counter((w, -x) for (w, x), count in distribution.items() for _ in range(count))
        assert distribution == reflected
    return n-1


checks = 0
orbits = 0
for n in range(2, 8):
    for a in product((-2, -1, 0, 1, 2), repeat=n):
        if sum(a):
            continue
        checks += verify_orbit(a)
        orbits += 1

walks = 0
for n in range(2, 14, 2):
    for plus in combinations(range(n), n//2):
        plus = set(plus)
        a = tuple(1 if i in plus else -1 for i in range(n))
        walks += 1
        # The odd-transform identity holds separately for every symmetric bridge law.
    for k in range(1, n):
        pairs = []
        for plus in combinations(range(n), n//2):
            plus = set(plus)
            a = tuple(1 if i in plus else -1 for i in range(n))
            pairs.append(features(a, k))
        mean_mx = Fraction(sum(m*x for m, x in pairs), len(pairs))
        theoretical = Fraction(k*(n-k), 2*(n-1))
        assert mean_mx == theoretical, (n,k,mean_mx,theoretical)
        for p in (1,3,5):
            assert 2*sum(m*x**p for m,x in pairs) == sum(x**(p+1) for _,x in pairs)

skew = [(2,-1,-1), (-1,-1,2), (-1,2,-1)]
assert Counter(features(a,1)[1] for a in skew) != Counter(-features(a,1)[1] for a in skew)
assert 2*sum(features(a,1)[0]*features(a,1)[1] for a in skew) == sum(features(a,1)[1]**2 for a in skew)

print(f"PASS: {orbits} zero-sum integer strings, {checks} exact orbit-lag pairs; {walks} symmetric-walk bridges; odd powers 1,3,5; skew boundary.")
