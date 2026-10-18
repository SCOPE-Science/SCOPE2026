"""Exact enumeration for idempotent--nilpotent products over dual-number fields.

Execute: python verify.py
Uses only the Python standard library.  The argument q is 2, 3, or 4.
For q=4 the coefficient field is F_2[z]/(z^2+z+1).
"""
from collections import Counter
from itertools import product


def field_arithmetic(q):
    if q in (2, 3):
        return (lambda a, b: (a + b) % q,
                lambda a, b: (a * b) % q)
    if q == 4:
        add = lambda a, b: a ^ b
        def mul(a, b):
            c = 0
            for i in range(2):
                for j in range(2):
                    if ((a >> i) & 1) and ((b >> j) & 1):
                        c ^= 1 << (i+j)
            if c & 8:
                c ^= 0b1110  # z*(z^2+z+1)
            if c & 4:
                c ^= 0b111  # z^2+z+1
            return c
        return add, mul
    raise ValueError('q must be 2, 3, or 4')


def verify(q):
    fa, fm = field_arithmetic(q)
    ne = q * q
    ra = [[0]*ne for _ in range(ne)]
    rm = [[0]*ne for _ in range(ne)]
    for a in range(ne):
        for b in range(ne):
            ra[a][b] = fa(a % q, b % q) + q * fa(a // q, b // q)
            rm[a][b] = fm(a % q, b % q) + q * fa(fm(a % q, b // q), fm(a // q, b % q))

    def matmul(a, b):
        x, y, z, w = a
        X, Y, Z, W = b
        return (ra[rm[x][X]][rm[y][Z]], ra[rm[x][Y]][rm[y][W]],
                ra[rm[z][X]][rm[w][Z]], ra[rm[z][Y]][rm[w][W]])

    def fsub(x, y):
        return fa(x, fm(q-1, y)) if q != 4 else x ^ y

    def nilpotent(a):
        x, y, z, w = [v % q for v in a]
        return fa(x, w) == 0 and fsub(fm(x, w), fm(y, z)) == 0

    def rank_field(a):
        x, y, z, w = a
        d = fsub(fm(x,w), fm(y,z))
        return 2 if d else (1 if any(a) else 0)

    def det_ring(a):
        x, y, z, w = a
        c, d = rm[x][w], rm[y][z]
        return fsub(c % q, d % q) + q*fsub(c // q, d // q)

    def expected(a):
        b = tuple(v % q for v in a)
        if not any(a):
            return q**6*(q+2)+1, 'zero'
        if not any(b):
            rb = rank_field(tuple(v // q for v in a))
            return (q**6+1 if rb == 1 else 1), f'radical-rank-{rb}'
        if rank_field(b) == 2:
            return 0, 'invertible-reduction'
        if det_ring(a) != 0:
            return (1 if fa(b[0], b[3]) == 0 else 0), 'primitive-det-nonzero'
        if fa(b[0], b[3]) == 0:
            return q**4+1, 'primitive-singular-nilpotent-reduction'
        return (q-1)*q**3, 'primitive-singular-nonnilpotent-reduction'

    mats = list(product(range(ne), repeat=4))
    E = [a for a in mats if matmul(a, a) == a]
    N = [a for a in mats if nilpotent(a)]
    assert len(E) == q**3*(q+1)+2
    assert len(N) == q**6
    fin = Counter()
    fni = Counter()
    for e in E:
        for n in N:
            fin[matmul(e, n)] += 1
            fni[matmul(n, e)] += 1
    profile = Counter()
    sizes = Counter()
    for a in mats:
        want, key = expected(a)
        assert fin[a] == want, ('IN', q, a, key, want, fin[a])
        assert fni[a] == want, ('NI', q, a, key, want, fni[a])
        profile[key] += 1
        sizes[want] += 1
    expected_image = q**4*(2*q*q-1)
    assert sum(x > 0 for x in fin.values()) == expected_image
    assert len(fin) == expected_image and len(fni) == expected_image
    assert sum(fin.values()) == len(E) * len(N)
    assert sum(fni.values()) == len(E) * len(N)
    print(f'q={q}: matrices={len(mats)}, idempotents={len(E)}, '
          f'nilpotents={len(N)}, ordered_pairs={len(E)*len(N)}, '
          f'positive_targets={len(fin)}')
    print('  stratum sizes:', dict(sorted(profile.items())))
    print('  fiber multiplicities:', dict(sorted(sizes.items())))


if __name__ == '__main__':
    for q in (2, 3, 4):
        verify(q)
    print('VERIFY_OK')
