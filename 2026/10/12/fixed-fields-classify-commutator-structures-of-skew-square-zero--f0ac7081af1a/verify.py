"""Finite-field checks for twisted square-zero ring commutator classifications.

Run with Python 3: python verify.py
All arithmetic and assertions are contained in this file.
"""
from collections import Counter
from itertools import product

POLYS = {2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101}

def mul(a, b, degree):
    q = 1 << degree
    poly = POLYS[degree]
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= poly
    return z

def power(a, n, degree):
    out = 1
    while n:
        if n & 1:
            out = mul(out, a, degree)
        a = mul(a, a, degree)
        n >>= 1
    return out

def commutator(x, y, degree, twist):
    a, b = x
    c, d = y
    ap = power(a, 1 << twist, degree)
    cp = power(c, 1 << twist, degree)
    return mul(d, a ^ ap, degree) ^ mul(b, c ^ cp, degree)

def trial(degree, twist):
    q = 1 << degree
    assert 0 < twist < degree
    field = range(q)
    assert all(power(a, q - 1, degree) == 1 for a in range(1, q))
    sig = {a: power(a, 1 << twist, degree) for a in field}
    fixed = [a for a in field if sig[a] == a]
    s = len(fixed)
    assert s > 1 and s < q
    elements = list(product(field, repeat=2))
    delta = [a ^ sig[a] for a in field]
    fibers = [0] * q
    centralizers = {}
    for x in elements:
        c = []
        for y in elements:
            z = mul(y[1], delta[x[0]], degree) ^ mul(x[1], delta[y[0]], degree)
            fibers[z] += 1
            if z == 0:
                c.append(y)
        centralizers[x] = frozenset(c)
    expected = q * (q*q - s*s)
    assert fibers[0] == expected + q*q*s*s, (degree, twist, fibers[0])
    assert all(t == expected for t in fibers[1:])
    sizes = Counter(len(v) for v in centralizers.values())
    assert sizes == Counter({q*q: s, q: q*(q-s), q*s: s*(q-1)}), (degree, twist, sizes)
    distinct = set(centralizers.values())
    assert len(distinct) == q+2, (degree, twist, len(distinct))
    center = frozenset((a, 0) for a in fixed)
    assert {x for x in elements if len(centralizers[x]) == q*q} == set(center)
    noncentral_sets = [sset - center for sset in distinct if len(sset) != q*q]
    assert Counter(len(ss) for ss in noncentral_sets) == Counter({q-s: q, s*(q-1): 1})
    assert len(set().union(*noncentral_sets)) == q*q-s
    assert sum(map(len, noncentral_sets)) == q*q-s
    return (q, twist, s, sizes, fibers[0])

def test_additive_commutator_equivalence():
    """Construct an additive commutator-preserving bijection for two F32 twists."""
    degree, q = 5, 32
    sigma = [power(a, 2, degree) for a in range(q)]
    tau = [power(a, 4, degree) for a in range(q)]
    ds = [a ^ sigma[a] for a in range(q)]
    dt = [a ^ tau[a] for a in range(q)]
    # The four-dimensional complement E of F2 is the even-bit subspace.
    basis = [2, 4, 8, 16]
    images = [next(w for w in range(0, q, 2) if dt[w] == ds[v]) for v in basis]
    def T(a):
        z = a & 1
        for i, v in enumerate(basis):
            if a & v:
                z ^= images[i]
        return z
    assert len({T(a) for a in range(q)}) == q
    assert T(0) == 0 and T(1) == 1
    assert all(dt[T(a)] == ds[a] for a in range(q))
    for a in range(q):
        for c in range(q):
            for b in range(q):
                left = mul(b, ds[c], degree)
                right = mul(b, dt[T(c)], degree)
                assert left == right
                assert mul(b, ds[a], degree) == mul(b, dt[T(a)], degree)
    print('F32_COMMUTATOR_PRESERVING_BIJECTION_OK', images)

if __name__ == '__main__':
    outcomes = []
    for degree, twist in [(2,1),(3,1),(3,2),(4,1),(4,2),(4,3),(5,1),(5,2)]:
        outcome = trial(degree, twist)
        outcomes.append(outcome)
        print('q=%d twist=%d fixed=%d centralizer_counts=%s zero_fiber=%d' % outcome)
    assert outcomes[6][2] == outcomes[7][2] == 2
    test_additive_commutator_equivalence()
    print('VERIFY_OK')
