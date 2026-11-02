#!/usr/bin/env python3
"""Exact finite-field checks for rational secants and elliptic resolvents.

All arithmetic is in GF(2^r), represented by polynomial residue classes.
These computations test the formulas through degree 7; the universal result
is established by the accompanying algebraic proof, not by enumeration.
"""

IRREDUCIBLE = {2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101,
               6: 0b1000011, 7: 0b10001001}


def multiply(a, b, q, polynomial):
    value = 0
    while b:
        if b & 1:
            value ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= polynomial
    return value


def power(a, exponent, q, polynomial):
    value = 1
    while exponent:
        if exponent & 1:
            value = multiply(value, a, q, polynomial)
        a = multiply(a, a, q, polynomial)
        exponent >>= 1
    return value


def test_degree(r):
    q = 1 << r
    polynomial = IRREDUCIBLE[r]
    mul = lambda a, b: multiply(a, b, q, polynomial)
    pw = lambda a, n: power(a, n, q, polynomial)
    for a in range(1, q):
        assert mul(a, pw(a, q - 2)) == 1

    def trace(x):
        total, current = 0, x
        for _ in range(r):
            total ^= current
            current = mul(current, current)
        assert total in (0, 1)
        return total

    for t in range(1, q):
        alpha = next(a for a in range(1, q) if pw(a, 8) == t)
        delta = 1 ^ pw(alpha, 3)
        points = set()
        for w in range(q):
            w2 = pw(w, 2)
            w4 = pw(w, 4)
            y = w4 ^ mul(alpha, w2) ^ w
            z = mul(pw(alpha, 2), w4) ^ w2
            points.add((y, z))
            lhs = pw(z, 4) ^ pw(y, 2) ^ z
            rhs = mul(t, pw(y, 4) ^ pw(z, 2))
            assert lhs ^ rhs == 0
        assert len(points) == q

        # Lines through (0,0) represent the q+1 affine directions.
        weights = {}
        for y, z in points:
            if y == z == 0:
                continue
            slope = q if z == 0 else mul(y, pw(z, q - 2))
            weights[slope] = weights.get(slope, 0) + 1
        assert set(weights.values()) <= {1, 3}
        s4 = sum(weight == 3 for weight in weights.values())
        s2 = sum(weight == 1 for weight in weights.values())
        s0 = q + 1 - s4 - s2
        assert s2 == q - 1 - 3 * s4
        assert s0 == 2 + 2 * s4
        assert weights.get(q) == 1

        if delta:
            delta3 = pw(delta, 3)
            alpha3_inverse = pw(alpha, q - 4) if q > 4 else pw(pw(alpha, 3), q - 2)
            # Avoid relying on signed exponent conventions.
            alpha3_inverse = pw(pw(alpha, 3), q - 2)
            e = mul(delta, pw(pw(alpha, 4), q - 2))
            e3 = pw(e, 3)
            count = 1  # Point at infinity on the smooth elliptic cubic.
            for x in range(q):
                rhs = pw(x, 3) ^ mul(alpha3_inverse, pw(x, 2)) ^ mul(e3, x)
                for yy in range(q):
                    if pw(yy, 2) ^ mul(x, yy) == rhs:
                        count += 1
            assert count == 6 + 6 * s4, (q, t, s4, count)
            assert abs(count - (q + 1)) <= 2 * q ** 0.5 + 1e-10
        else:
            predicted = (q - 2) // 6 if r % 2 else (q - 4) // 6
            assert s4 == predicted, (q, t, s4, predicted)

        # A projective line is characterized by an affine direction and
        # intercept; each nonempty intersection is a coset of a kernel.
        n4 = q * s4 // 4
        n2 = (q // 2) * s2
        n1 = q * s0
        n0 = 1 + (q * (q - 1)) // 2 - (3 * q * s4) // 4
        assert n0 + n1 + n2 + n4 == q * q + q + 1
        assert n1 + 2 * n2 + 4 * n4 == q * (q + 1)

    print(f"GF(2^{r}): {q - 1} parameters checked")


if __name__ == '__main__':
    for degree in range(2, 8):
        test_degree(degree)
    print('QUARTIC_FOUR_SECANTS_ELLIPTIC_RESOLVENT_PASS')
