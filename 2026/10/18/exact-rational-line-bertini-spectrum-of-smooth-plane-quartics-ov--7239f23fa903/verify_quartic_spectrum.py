#!/usr/bin/env python3
"""Exact binary quartic Bertini-spectrum and projective-orbit verification.

Requires only Python 3; no finite-extension sampling or third-party packages.
A degree-ten Macaulay map tests geometric smoothness over an algebraic closure.
"""
import collections
import itertools

MONS = [(a, b, 4 - a - b) for a in range(4, -1, -1)
        for b in range(4 - a, -1, -1)]


def monomials(degree):
    return [(a, b, degree-a-b) for a in range(degree, -1, -1)
            for b in range(degree-a, -1, -1)]


LOW = {d: monomials(d) for d in (6, 7, 10)}
INDEX = {d: {m: i for i, m in enumerate(LOW[d])} for d in LOW}


def addexps(u, v):
    return tuple(u[i] + v[i] for i in range(3))


F_SHIFT = [[1 << INDEX[10][addexps(a, b)] for b in LOW[6]]
           for a in MONS]
DF_SHIFT = [[[1 << INDEX[10][addexps(tuple(a[i] - (i == j)
                                            for i in range(3)), b)] for b in LOW[7]]
             if a[j] & 1 else None for a in MONS] for j in range(3)]


def rank(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = vector
                break
            vector ^= pivots[pivot]
    return len(pivots)


def smooth(mask):
    active = [i for i in range(15) if (mask >> i) & 1]
    columns = []
    for j in range(28):
        vector = 0
        for i in active:
            vector ^= F_SHIFT[i][j]
        columns.append(vector)
    for coordinate in range(3):
        for j in range(36):
            vector = 0
            for i in active:
                row = DF_SHIFT[coordinate][i]
                if row is not None:
                    vector ^= row[j]
            columns.append(vector)
    return rank(columns) == 66


def coordinates(x):
    return tuple((x >> i) & 1 for i in range(3))


LINES = sorted(set(tuple(sorted((u, v, u ^ v)))
                   for u in range(1, 8) for v in range(1, 8) if u != v))
assert len(LINES) == 7


def mon_restriction(monom, u, v):
    U, V = coordinates(u), coordinates(v)
    result = [1]
    for j, exp in enumerate(monom):
        for _ in range(exp):
            nxt = [0] * (len(result) + 1)
            for i, value in enumerate(result):
                nxt[i] ^= value * U[j]
                nxt[i+1] ^= value * V[j]
            result = nxt
    return sum(value << i for i, value in enumerate(result))


RESTRICTIONS = [[mon_restriction(m, line[0], line[1]) for m in MONS]
                for line in LINES]


def is_transverse(binary_quartic):
    a, b, c, d, e = [(binary_quartic >> i) & 1 for i in range(5)]
    if b == 0 and d == 0:
        return False
    if b == 1 and d == 0:
        return e == 1
    if b == 0 and d == 1:
        return a == 1
    return (a ^ c ^ e) == 1


def transverse_count(mask):
    total = 0
    for restriction in RESTRICTIONS:
        polynomial = 0
        for i in range(15):
            if (mask >> i) & 1:
                polynomial ^= restriction[i]
        total += is_transverse(polynomial)
    return total


def point_count(mask):
    count = 0
    for point in range(1, 8):
        x = coordinates(point)
        value = 0
        for i, mon in enumerate(MONS):
            if (mask >> i) & 1:
                value ^= (x[0]**mon[0] * x[1]**mon[1] * x[2]**mon[2])
        count += (value == 0)
    return count


def mulpol(left, right):
    product = {}
    for m in left:
        for n in right:
            exp = addexps(m, n)
            product[exp] = product.get(exp, 0) ^ 1
    return {m: 1 for m, value in product.items() if value}


def transform(mask, columns):
    substitutions = [
        {tuple(int(c == j) for c in range(3)): 1
         for j in range(3) if ((columns[j] >> coordinate) & 1)}
        for coordinate in range(3)
    ]
    polynomial = {}
    for i, exponents in enumerate(MONS):
        if not ((mask >> i) & 1):
            continue
        summand = {(0, 0, 0): 1}
        for j, power in enumerate(exponents):
            for _ in range(power):
                summand = mulpol(summand, substitutions[j])
        for exp in summand:
            polynomial[exp] = polynomial.get(exp, 0) ^ 1
    return sum((1 << MONS.index(exp)) for exp, value in polynomial.items() if value)


def verify():
    smooth_forms = [f for f in range(1, 32768) if smooth(f)]
    assert len(smooth_forms) == 10920
    dist = collections.Counter(transverse_count(f) for f in smooth_forms)
    expected = {0: 25, 1: 168, 2: 588, 3: 2604,
                4: 3885, 5: 2940, 6: 686, 7: 24}
    assert dict(dist) == expected, (dist, expected)
    expected_joint = {
        (0,0):1,(0,5):84,(0,6):56,(0,7):24,
        (1,3):84,(1,5):504,(1,6):420,
        (2,3):84,(2,4):756,(2,5):1596,(2,6):210,
        (3,3):420,(3,4):2184,(3,5):756,
        (4,3):1596,(4,4):945,
        (5,2):588,(5,3):420,(6,1):168,(7,0):24}
    joint = collections.Counter((point_count(f), transverse_count(f)) for f in smooth_forms)
    assert dict(joint) == expected_joint
    group = [(a,b,c) for a,b,c in itertools.product(range(1,8),repeat=3)
             if rank([a,b,c]) == 3]
    assert len(group) == 168
    seen = set()
    orbits = []
    S = set(smooth_forms)
    for f in smooth_forms:
        if f in seen:
            continue
        orbit = {transform(f,g) for g in group}
        assert orbit <= S
        seen.update(orbit)
        orbits.append((len(orbit),transverse_count(f),f))
    assert seen == S and len(orbits) == 78
    by_t = collections.Counter(t for size,t,f in orbits)
    assert dict(by_t) == {0:2,1:1,2:4,3:19,4:26,5:19,6:6,7:1}
    assert sorted((size,point_count(f)) for size,t,f in orbits if t==0) == [(1,0),(24,7)]
    assert {f for f in smooth_forms if transverse_count(f)==0} == {
        21945} | {transform(6670,g) for g in group}
    print('PASS: 32767 binary quartics exhausted; 10920 geometrically smooth')
    print('PASS: rational transverse-line histogram:',dict(sorted(dist.items())))
    print('PASS: rational-point/transverse-line joint spectrum:',dict(sorted(joint.items())))
    print('PASS: 78 projective orbits; orbit counts by transverse lines:',dict(sorted(by_t.items())))
    print('PASS: precisely 25 transverse-free smooth quartics, orbit sizes 1 and 24')
    return orbits


if __name__ == '__main__':
    verify()
