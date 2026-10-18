"""Independent numerical stress checks of the explicit harmonic quadrature formulas.

Runs with Python's standard library. The universal result is proved analytically
in RESULT.md; floating-point checks alone do not establish it.
"""
import cmath
import math
from fractions import Fraction


def weights(N):
    assert N >= 4
    if N % 2 == 0:
        return N // 2, {0: 0.5, N // 2: 0.5}
    D = (N + 3) // 2
    a = math.sin(math.pi / (2 * N))
    b = math.sin(3 * math.pi / (2 * N))
    c = math.sin(5 * math.pi / (2 * N))
    A = c * (c * c - b * b)
    B = a * (b * b - a * a)
    C = a * c * (c * c - a * a) / b
    total = A + B + C
    result = {}
    for pair, mass in [((1, D - 1), A), ((2, D - 2), B), ((0, D), C)]:
        for j in pair:
            result[j] = result.get(j, 0.0) + mass / (2 * total)
    return D, result


def verify():
    tested = 0
    for N in range(4, 1001):
        D, ws = weights(N)
        assert D == (N // 2 if N % 2 == 0 else (N + 3) // 2)
        assert min(ws) == 0 and max(ws) == D
        assert 0 < min(ws.values())
        assert len(ws) <= 6
        assert abs(sum(ws.values()) - 1) < 1e-10
        for k in (1, 3):
            moment = sum(w * cmath.exp(2j * math.pi * k * j / N)
                         for j, w in ws.items())
            assert abs(moment) < 1e-10, (N, k, moment)
        if N % 2:
            Dlow = (N + 1) // 2
            a = math.sin(math.pi / (2 * N))
            phi = math.pi * Dlow / N
            vals = [math.cos(2 * math.pi * j / N - phi)
                    for j in range(Dlow + 1)]
            assert all(x * (x * x - a * a) > 1e-13
                       for x in vals[1:-1]), (N, vals)
            assert abs(vals[0] + a) < 1e-12
            assert abs(vals[-1] + a) < 1e-12
        tested += 1
    # Exact rational identities behind the three-level positivity construction.
    identities = 0
    for a, b, c in [(Fraction(1), Fraction(2), Fraction(3)),
                    (Fraction(1, 5), Fraction(3, 7), Fraction(9, 10)),
                    (Fraction(2, 9), Fraction(4, 9), Fraction(7, 9))]:
        A = c * (c*c - b*b)
        B = a * (b*b - a*a)
        C = a*c*(c*c - a*a)/b
        assert A > 0 and B > 0 and C > 0
        assert A*a + B*c == C*b
        assert A*a**3 + B*c**3 == C*b**3
        identities += 2
    print(f"VERIFY_OK {tested} cyclic orders, {2*tested} complex moments, "
          f"{identities} exact rational cancellation identities")


if __name__ == '__main__':
    verify()
