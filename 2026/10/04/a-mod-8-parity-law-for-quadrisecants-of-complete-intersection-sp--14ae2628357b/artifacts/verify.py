from fractions import Fraction

def cayley_from_degree_genus(a, b):
    d = a * b
    g = 1 + d * (a + b - 4) // 2
    assert d * (a + b - 4) % 2 == 0
    t1 = Fraction((d - 2) * (d - 3) ** 2 * (d - 4), 12)
    t2 = Fraction(g * (d * d - 7 * d + 13 - g), 2)
    q = t1 - t2
    assert q.denominator == 1
    return q.numerator

def specialized(a, b):
    p = a * b
    s = a + b
    num = p * (
        2 * p ** 3
        - 6 * p ** 2 * s
        + 3 * p * s ** 2
        + 18 * p * s
        - 26 * p
        - 66 * s
        + 144
    )
    assert num % 24 == 0
    return num // 24

def predicted_odd(a, b):
    if (a % 2) != (b % 2):
        even_degree = a if a % 2 == 0 else b
        return even_degree % 8 in (4, 6)
    if a % 2 == 1 and b % 2 == 1:
        return (a + b) % 8 in (0, 2)
    return False

checks = 0
for a in range(4, 81):
    for b in range(4, 81):
        q1 = cayley_from_degree_genus(a, b)
        q2 = specialized(a, b)
        assert q1 == q2
        assert (q2 & 1) == predicted_odd(a, b)
        assert (specialized(a + 8, b) - q2) % 2 == 0
        assert (specialized(a, b + 8) - q2) % 2 == 0
        checks += 1

odd_residues = []
for a in range(8):
    for b in range(8):
        aa = a if a else 8
        bb = b if b else 8
        actual = specialized(aa, bb) & 1
        predicted = predicted_odd(aa, bb)
        assert actual == predicted
        if actual:
            odd_residues.append((a, b))

assert len(odd_residues) == 24
assert specialized(4, 5) == 1275
assert specialized(5, 5) == 4775
assert specialized(6, 7) == 69825
assert specialized(4, 4) == 320
assert specialized(4, 6) == 3468
assert specialized(5, 7) == 27230

print("VERIFY_OK", checks, len(odd_residues))
print("ODD_RESIDUES", odd_residues)
