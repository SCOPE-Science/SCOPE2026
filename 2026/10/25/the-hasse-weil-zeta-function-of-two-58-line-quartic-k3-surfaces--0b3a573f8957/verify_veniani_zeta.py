#!/usr/bin/env python3
"""Exact standalone verifier for the arithmetic of Veniani's 58-line quartics.

Python 3 standard library only.  No external files, network, computer algebra,
or stored computation transcripts are required.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache

Q = 3 ** 8
RADIX = tuple(3 ** i for i in range(8))


def digits(x):
    return tuple((x // RADIX[i]) % 3 for i in range(8))


DIGITS = [digits(x) for x in range(Q)]


def add(a, b):
    da, db = DIGITS[a], DIGITS[b]
    return sum(RADIX[i] * ((da[i] + db[i]) % 3) for i in range(8))


def sub(a, b):
    da, db = DIGITS[a], DIGITS[b]
    return sum(RADIX[i] * ((da[i] - db[i]) % 3) for i in range(8))


@lru_cache(maxsize=200000)
def mul(a, b):
    da, db = DIGITS[a], DIGITS[b]
    c = [0] * 15
    for i in range(8):
        if da[i]:
            for j in range(8):
                if db[j]:
                    c[i + j] = (c[i + j] + da[i] * db[j]) % 3
    # theta^8 = 1 - theta^2 modulo theta^8 + theta^2 - 1.
    for i in range(14, 7, -1):
        t = c[i]
        c[i] = 0
        c[i - 8] = (c[i - 8] + t) % 3
        c[i - 6] = (c[i - 6] - t) % 3
    return sum(RADIX[i] * c[i] for i in range(8))


def fpow(a, exponent):
    out = 1
    while exponent:
        if exponent & 1:
            out = mul(out, a)
        a = mul(a, a)
        exponent >>= 1
    return out


def cube(a):
    return mul(mul(a, a), a)


def rank_over_q(matrix):
    """Exact rank over Q by elimination; entries are small integers."""
    a = [[Fraction(t) for t in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = 0
    for j in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][j]
        for i in range(r + 1, rows):
            if not a[i][j]:
                continue
            t = a[i][j] / v
            for k in range(j + 1, cols):
                a[i][k] -= t * a[r][k]
            a[i][j] = Fraction(0)
        r += 1
        if r == rows:
            break
    return r


def fano_lines(lam, gamma):
    theta = 3
    assert sub(add(fpow(theta, 8), fpow(theta, 2)), 1) == 0
    assert fpow(theta, Q - 1) == 1
    # Explicit degree-eight additive root spaces Vplus and Vminus.
    t0 = theta if lam == 1 else mul(gamma, theta)
    u0 = mul(gamma, theta) if lam == 1 else theta
    tv = [t0]
    uv = [u0]
    for _ in range(7):
        tv.append(cube(tv[-1]))
        uv.append(cube(uv[-1]))
    assert len(set(tv)) == len(set(uv)) == 8
    assert cube(tv[-1]) == tv[0]
    assert cube(uv[-1]) == uv[0]
    for t in tv:
        assert sub(add(fpow(t, 9), mul(lam, cube(t))), t) == 0
    for u in uv:
        assert sub(sub(fpow(u, 9), mul(lam, cube(u))), u) == 0
    pairing = lambda t, u: add(mul(t, cube(u)), mul(cube(t), u))
    symbol = tuple(pairing(tv[0], u) for u in uv)
    assert sorted(Counter(symbol).values()) == [2, 3, 3]
    for i in range(8):
        for j in range(8):
            assert pairing(tv[i], uv[j]) == symbol[(j - i) % 8]
    # Labels (family, b, frobenius_exponent). -1 means the root zero.
    labs = ([(g, b, j) for g in (0, 1) for b in range(3)
             for j in [-1] + list(range(8))]
            + [(2, b, -1) for b in range(3)] + [(3, 0, -1)])
    assert len(labs) == 58
    for g, b, j in labs:
        if g == 0:
            t = 0 if j == -1 else tv[j]
            d = add(cube(t), mul(lam, t))
            assert cube(d) == t
            assert cube(b) == b
        elif g == 1:
            u = 0 if j == -1 else uv[j]
            e = sub(mul(lam, u), cube(u))
            assert add(cube(e), u) == 0
            assert cube(b) == b
    return labs, symbol, tv, uv


def explicit_basis(label, lam, tv, uv):
    fam, b, j = label
    if fam == 0:
        t = 0 if j == -1 else tv[j]
        return ((1, 0, t, b), (0, 1, 0, add(cube(t), mul(lam, t))))
    if fam == 1:
        u = 0 if j == -1 else uv[j]
        return ((1, u, 0, b), (0, 0, 1, sub(mul(lam, u), cube(u))))
    if fam == 2:
        return ((0, 1, b, 0), (0, 0, 0, 1))
    return ((0, 0, 1, 0), (0, 0, 0, 1))


def quartic_value(v, lam):
    x0, x1, x2, x3 = v
    return sub(add(sub(mul(cube(x1), x2), mul(x1, cube(x2))),
                   sub(mul(cube(x0), x3), mul(x0, cube(x3)))),
               mul(lam, mul(mul(x0, x0), mul(x1, x2))))


def plucker(basis):
    a, b = basis
    return tuple(sub(mul(a[i], b[j]), mul(a[j], b[i]))
                 for i, j in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)))


def independent_intersection(p, q):
    # Wedge of the two bivectors in the top exterior power of k^4.
    return add(add(add(mul(p[0], q[5]), sub(0, mul(p[1], q[4]))),
                   add(mul(p[2], q[3]), mul(p[3], q[2]))),
               sub(mul(p[5], q[0]), mul(p[4], q[1]))) == 0


def verify_explicit_geometry(lam, labs, symbol, tv, uv):
    bases = [explicit_basis(label, lam, tv, uv) for label in labs]
    six = (0, 1, 2, 3, 4)
    for a, b in bases:
        for t in six:
            v = tuple(add(a[i], mul(t, b[i])) for i in range(4))
            assert quartic_value(v, lam) == 0
        assert quartic_value(b, lam) == 0
    # Vanishing at five affine points and infinity is an *identity* test
    # for a degree-four homogeneous polynomial on the projective line.
    pp = [plucker(basis) for basis in bases]
    for i in range(len(labs)):
        for j in range(i + 1, len(labs)):
            assert independent_intersection(pp[i], pp[j]) == is_incident(
                labs[i], labs[j], symbol), (lam, i, j)



def is_incident(x, y, symbol):
    if x == y:
        return False
    g, b, j = x
    h, c, k = y
    if g > h:
        return is_incident(y, x, symbol)
    if g == h == 0 or g == h == 1:
        return j == k and b != c
    if g == 0 and h == 1:
        w = 0 if j == -1 or k == -1 else symbol[(k - j) % 8]
        return w == (c - b) % 3
    if g == 0 and h == 2:
        return c == 0
    if g == 0 and h == 3:
        return False
    if g == 1 and h == 2:
        return False
    if g == 1 and h == 3:
        return True
    if g == h == 2 or g == 2 and h == 3:
        return True
    raise AssertionError((x, y))


def matrix_and_ranks(labs, sym):
    n = len(labs)
    adjacency = [[int(is_incident(labs[i], labs[j], sym))
                  for j in range(n)] for i in range(n)]
    assert all(adjacency[i][j] == adjacency[j][i] for i in range(n)
               for j in range(n))
    degrees = Counter(sum(row) for row in adjacency)
    assert degrees == Counter({3: 2, 12: 54, 30: 2}), degrees
    edges = sum(sum(row) for row in adjacency) // 2
    assert edges == 357
    # Intersection Gram matrix of smooth quartic K3 lines:
    # self-intersection -2, distinct intersecting lines intersection 1.
    gram = [[adjacency[i][j] if i != j else -2 for j in range(n)]
            for i in range(n)]
    assert rank_over_q(gram) == 22

    fixed_ranks = []
    for d in (1, 2, 4, 8):
        blocks = [[t * 27 + b * 9] for t in range(2) for b in range(3)]
        for t in range(2):
            for b in range(3):
                base = t * 27 + b * 9
                blocks += [[base + 1 + j for j in range(z, 8, d)]
                           for z in range(d)]
        blocks.extend([[i] for i in range(54, 58)])
        sums = [[sum(gram[i][j] for i in block1 for j in block2)
                 for block2 in blocks] for block1 in blocks]
        fixed_ranks.append(rank_over_q(sums))
    assert fixed_ranks == [8, 10, 14, 22], fixed_ranks
    assert sum(labs[i][2] == -1 for i in range(n)) == 10
    return edges, degrees, fixed_ranks


def point_count(lam, q):
    field = [x for x in range(Q) if fpow(x, q) == x]
    assert len(field) == q
    def surf(x):
        x0, x1, x2, x3 = x
        v = sub(mul(cube(x1), x2), mul(x1, cube(x2)))
        v = add(v, sub(mul(cube(x0), x3), mul(x0, cube(x3))))
        v = sub(v, mul(lam, mul(mul(x0, x0), mul(x1, x2))))
        return v == 0
    count = 1 if surf((0, 0, 0, 1)) else 0
    for u in field:
        count += surf((0, 0, 1, u))
        for v in field:
            count += surf((0, 1, u, v))
            for w in field:
                count += surf((1, u, v, w))
    return count


def main():
    gamma = next(x for x in range(1, Q) if mul(x, x) == 2)
    assert cube(gamma) == sub(0, gamma)
    results = []
    for lam in (1, 2):
        labs, symbol, tv, uv = fano_lines(lam, gamma)
        verify_explicit_geometry(lam, labs, symbol, tv, uv)
        edges, degrees, fixed_ranks = matrix_and_ranks(labs, symbol)
        counts = (point_count(lam, 3), point_count(lam, 9))
        assert counts == (28, 136)
        print(f'lambda={lam} pairing={symbol} edges={edges} '
              f'degrees={dict(degrees)} fixed_ranks={fixed_ranks} '
              f'points_F3_F9={counts}')
        results.append(fixed_ranks)
    assert results[0] == results[1]
    print('VERIFY_OK: 58 lines, Frobenius 1^10 8^6, Galois incidence; '
          'Gram ranks 22 and (8,10,14,22); NS charpoly '
          '(T-1)^6(T^8-1)^2; zeta for both nonzero prime-field fibers')


if __name__ == '__main__':
    main()
