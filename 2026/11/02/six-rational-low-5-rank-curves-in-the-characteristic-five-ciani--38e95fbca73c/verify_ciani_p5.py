"""Exact finite-field cross-checks for characteristic-five Ciani low-rank strata.

Self-contained Python 3; no external packages. Infinite-field statements in
RESULT.md follow from polynomial identities, not from this finite enumeration.
"""
from collections import Counter
from itertools import product

P = 5
F25 = tuple((a, b) for a in range(P) for b in range(P))
ZERO = (0, 0)

def const(n):
    return (n % P, 0)

def add(a, b):
    return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)

def neg(a):
    return ((-a[0]) % P, (-a[1]) % P)

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    # F_25 = F_5[u]/(u*u-2); the element 2 is a nonsquare.
    return ((a[0]*b[0] + 2*a[1]*b[1]) % P,
            (a[0]*b[1] + a[1]*b[0]) % P)

def power(a, n):
    v = const(1)
    for _ in range(n):
        v = mul(v, a)
    return v

def div(a, b):
    assert b != ZERO
    return mul(a, power(b, 23))  # b**24 = 1 for nonzero b.

def sq(a):
    return mul(a, a)

def smooth(a, b, c):
    if any(sq(v) == const(4) for v in (a, b, c)):
        return False
    return sub(sub(add(add(sq(a), sq(b)), sq(c)), mul(mul(a, b), c)), const(4)) != ZERO

def f(a, b, c):
    # Quotient of the coordinate-a sign involution.
    return add(add(add(add(mul(sq(a), sq(b)), mul(const(2), sq(a))),
                       mul(const(2), sq(b))), sq(c)),
               sub(const(2), mul(mul(a, b), c)))

def divisor_hits(a, b, c):
    return tuple(f(*args) == ZERO for args in ((a, b, c), (a, c, b), (b, c, a)))

def components(points):
    # Six parameter maps with intersections only at superspecial points.
    out = []
    for i in range(3):
        for eps in (1, -1):
            comp = set()
            for b in points:
                if b == ZERO or sq(b) in (const(4), const(3)):
                    continue
                numerator = (add(mul(const(4), sq(b)), const(1))
                             if eps == 1 else add(sq(b), const(4)))
                a = div(numerator, add(sq(b), const(2)))
                base = (a, b, mul(const(eps), b))
                triple = (base if i == 0 else
                          (base[1], base[2], base[0]) if i == 1 else
                          (base[2], base[0], base[1]))
                assert smooth(*triple)
                assert sum(divisor_hits(*triple)) >= 2
                comp.add(triple)
            out.append(comp)
    return out

for points in [tuple(const(i) for i in range(5)), F25]:
    q = len(points)
    all_smooth = {}
    for a, b, c in product(points, repeat=3):
        if smooth(a, b, c):
            all_smooth[(a, b, c)] = sum(divisor_hits(a, b, c))
    counts = Counter(all_smooth.values())
    e = int(q == 25)
    assert counts[3] == 8 * e
    assert counts[2] == 6 * (q - 3) - 36 * e
    assert len(all_smooth) == q**3 - 7*q*q + 18*q - 17
    comps = components(points)
    assert len(comps) == 6
    assert all(len(comp) == q - 3 - 2*e for comp in comps)
    union = set().union(*comps)
    assert union == {pt for pt, s in all_smooth.items() if s >= 2}
    multiplicities = Counter(pt for comp in comps for pt in comp)
    assert Counter(multiplicities.values()) == Counter({1: counts[2], 3: counts[3]})
    assert all(all_smooth[pt] == 3 for pt, n in multiplicities.items() if n == 3)
    print(f'FIELD {q}: smooth={len(all_smooth)}, quotient-SS-distribution={dict(sorted(counts.items()))}')
    print(f'FIELD {q}: six_components={[len(c) for c in comps]}, union={len(union)}, triple={counts[3]}, rank1={counts[2]}')

roots = [v for v in F25 if sub(sub(sq(v), mul(const(2), v)), const(2)) == ZERO]
assert len(roots) == 2 and all(v[1] != 0 for v in roots)
for t in roots:
    assert t not in (const(1), const(2), const(3))
    assert mul(sq(t), sub(mul(const(4), t), const(3))) != ZERO
print('SUPERSPECIAL_QUADRATIC: two simple non-rational roots; eight marked triple points')
print('VERIFY_OK')
