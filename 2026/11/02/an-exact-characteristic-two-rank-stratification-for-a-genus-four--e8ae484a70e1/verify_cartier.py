"""Exact finite-field checks for characteristic-two cyclic trigonal genus-four curves.

The unrestricted theorem is algebraic and is given in RESULT.md. This
program independently recomputes semilinear Cartier images and stabilised
image dimensions for all coefficient pairs in several finite fields. It also
checks sample zeta numerators via direct rational-point enumeration.
Only the Python standard library is used.
"""

IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011,
               5: 0b100101}


def multiply(x, y, m):
    polynomial = IRREDUCIBLE[m]
    mask = (1 << m) - 1
    result = 0
    while y:
        if y & 1:
            result ^= x
        y >>= 1
        x <<= 1
        if x & (1 << m):
            x ^= polynomial
    return result & mask


def power(x, n, m):
    result = 1
    while n:
        if n & 1:
            result = multiply(result, x, m)
        x = multiply(x, x, m)
        n >>= 1
    return result


def root2(x, m):
    return power(x, 1 << (m - 1), m)


def cartier(vector, a, b, m):
    # Ordered basis: dx/y, dx/y^2, x dx/y^2, x^2 dx/y^2.
    # C(e1)= e4+sqrt(a)e3+sqrt(b)e2; C(e3)=e1.
    v = [root2(c, m) for c in vector]
    return [v[2], multiply(v[0], root2(b, m), m),
            multiply(v[0], root2(a, m), m), v[0]]


def rank(columns, m):
    rows = [[col[r] for col in columns] for r in range(4)]
    pivotrow = 0
    for col in range(len(columns)):
        idx = next((r for r in range(pivotrow, 4) if rows[r][col]), None)
        if idx is None:
            continue
        rows[idx], rows[pivotrow] = rows[pivotrow], rows[idx]
        inv = power(rows[pivotrow][col], (1 << m) - 2, m)
        for j in range(col, len(columns)):
            rows[pivotrow][j] = multiply(rows[pivotrow][j], inv, m)
        for r in range(4):
            if r == pivotrow or rows[r][col] == 0:
                continue
            c = rows[r][col]
            for j in range(col, len(columns)):
                rows[r][j] ^= multiply(c, rows[pivotrow][j], m)
        pivotrow += 1
        if pivotrow == 4:
            break
    return pivotrow


def test_cartier():
    for m in range(1, 6):
        q = 1 << m
        for a in range(q):
            for b in range(q):
                vectors = [[int(i == j) for i in range(4)] for j in range(4)]
                ranks = []
                for _ in range(4):
                    vectors = [cartier(v, a, b, m) for v in vectors]
                    ranks.append(rank(vectors, m))
                expected = [2, 2, 2, 2] if a else [2, 1, 0, 0]
                assert ranks == expected, (m, a, b, ranks, expected)
        print(f"GF(2^{m}): verified {q*q} coefficient pairs")


def points(a, b, m):
    q = 1 << m
    cube_counts = [0] * q
    for y in range(q):
        cube_counts[power(y, 3, m)] += 1
    # The normalization has exactly one rational point above infinity.
    return 1 + sum(cube_counts[
        power(x, 5, m) ^ multiply(a, power(x, 3, m), m)
        ^ multiply(b, x, m) ^ 1] for x in range(q))


def test_zeta():
    # Newton's identities for the first four L-polynomial coefficients.
    reference = {
        (0, 0): [1, 0, 0, 0, -2, 0, 0, 0, 16],
        (0, 1): [1, 0, 2, 0, 6, 0, 8, 0, 16],
        (1, 0): [1, 0, 1, 0, 4, 0, 4, 0, 16],
        (1, 1): [1, 0, 3, 0, 4, 0, 12, 0, 16],
    }
    for (a, b), expected in reference.items():
        s = [0] + [(1 << m) + 1 - points(a, b, m) for m in range(1, 5)]
        L = [1]
        for n in range(1, 5):
            numerator = s[n] + sum(L[j] * s[n-j] for j in range(1, n))
            assert numerator % n == 0
            L.append(-numerator // n)
        L += [(1 << (j - 4)) * L[8-j] for j in range(5, 9)]
        assert L == expected, (a, b, L)
        assert max(j for j, v in enumerate(L) if v % 2) == (2 if a else 0)
    print('GF(2) zeta numerator coefficients and geometric 2-ranks verified')


if __name__ == '__main__':
    test_cartier()
    test_zeta()
    print('ODD_TRIGONAL_CHAR2_CARTIER_STABLE_RANK_AND_ZETA_OK')
