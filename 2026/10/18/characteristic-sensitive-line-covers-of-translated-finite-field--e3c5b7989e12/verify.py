"""Exact finite-field verification of explicit covering witnesses and the even-field construction."""

WITNESSES = {
    3: [(0, 1), (2, 0), ('v', 2)],
    5: [(0, 0), (2, 3), (4, 1), ('v', 1)],
    7: [(1, 0), (2, 1), (3, 5), (4, 5), ('v', 3)],
    11: [(1, 1), (2, 3), (2, 5), (3, 10), (7, 0), (8, 10), ('v', 1)],
    13: [(1, 0), (4, 6), (7, 1), (7, 8), (9, 12), (11, 3), (11, 9), ('v', 11)],
    17: [(0, 16), (1, 13), (2, 15), (5, 14), (7, 8), (10, 8), (12, 14), (15, 15), (16, 13), ('v', 0)],
    19: [(0, 5), (0, 6), (5, 6), (6, 15), (7, 7), (8, 10), (13, 16), (15, 1), (16, 0), (18, 2), ('v', 12)],
    23: [(0, 4), (0, 9), (3, 5), (3, 19), (10, 11), (14, 0), (15, 16), (16, 9), (19, 5), (20, 19), (21, 1), (22, 21), ('v', 5)],
}


def check_odd():
    for q, lines in WITNESSES.items():
        assert len(lines) == (q + 3) // 2
        assert sum(1 for slope, _ in lines if slope == 'v') == 1
        for x in range(q):
            for c in (0, 1):
                y = (x * x + c) % q
                assert any((slope == 'v' and x == b) or
                           (slope != 'v' and (y - slope * x - b) % q == 0)
                           for slope, b in lines), (q, x, c)
        print('ODD_WITNESS', q, len(lines))


def field_mul(a, b, q, defining_polynomial):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= defining_polynomial
    return z


def check_even():
    # Here bit vectors model F_2[T]/(the named irreducible polynomial).
    for q, polynomial in [(4, 0b111), (8, 0b1011), (16, 0b10011), (32, 0b100101)]:
        mul = lambda a, b: field_mul(a, b, q, polynomial)
        H = {mul(x, x) ^ x for x in range(q)}
        assert len(H) == q // 2
        candidates = []
        for m in range(1, q):
            B = {mul(x, x) ^ mul(m, x) for x in range(q)}
            if 1 in B and len(B) == q // 2:
                candidates.append((m, B))
        assert candidates, ('no suitable nonzero slope', q)
        m, B = candidates[0]
        lines = [(m, b) for b in sorted(B)] + [('v', 0)]
        assert len(lines) == q // 2 + 1
        for x in range(q):
            for c in (0, 1):
                y = mul(x, x) ^ c
                assert any((slope == 'v' and x == b) or
                           (slope != 'v' and y == (mul(slope, x) ^ b))
                           for slope, b in lines), (q, x, c)
        print('EVEN_WITNESS', q, 'slope', m, 'line_count', len(lines))
    # F_2: two vertical lines cover both entire parabolas and their point at infinity.
    print('EVEN_WITNESS', 2, 'two vertical lines')


if __name__ == '__main__':
    check_odd()
    check_even()
    print('VERIFY_OK')
