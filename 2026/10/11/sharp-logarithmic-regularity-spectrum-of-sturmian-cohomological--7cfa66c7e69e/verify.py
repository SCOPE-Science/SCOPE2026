"""Exact rational spot checks for the finite circle-gap bounds.

The inputs are rational continuants with large denominators. The assertions
concern only the finite orbit segments tested here; the infinite theorem is
proved analytically in RESULT.md.
"""
from fractions import Fraction


def approximant_and_convergents(partials):
    # alpha=[0;a1,a2,...], convergents beginning 0/1.
    p0, p1, q0, q1 = 0, 1, 1, 0
    result = [(0, 1)]
    for a in partials:
        p0, p1 = p1, a*p1 + p0
        q0, q1 = q1, a*q1 + q0
        result.append((p1, q1))
    return Fraction(*result[-1]), result


def largest_circle_gap(alpha, n):
    assert n >= 1
    points = sorted((j * alpha) % 1 for j in range(n + 1))
    assert len(set(points)) == n + 1, "Rational approximation too short"
    return max([points[j+1] - points[j] for j in range(n)] +
               [1 + points[0] - points[-1]])


def check_case(partials, cap):
    alpha, conv = approximant_and_convergents(partials)
    assert alpha.denominator > cap
    checks = 0
    for n in range(1, cap + 1):
        M = largest_circle_gap(alpha, n)
        assert M >= Fraction(1, n + 1)
        q = max(d for _, d in conv[:-1] if d <= n + 1)
        assert M <= Fraction(3, q), (n, M, q)
        checks += 2
    for (_, q), (_, Q) in zip(conv[:-2], conv[1:-1]):
        if Q >= 8*q:
            n = Q // 4
            if 1 <= n <= cap:
                assert largest_circle_gap(alpha, n) >= Fraction(1, 2*q), (q, Q)
                checks += 1
    return checks


def main():
    cases = [
        ([1]*24, 260),
        ([2, 12, 1, 30, 1, 40, 1, 5, 2, 2, 2, 3, 2, 4, 2], 260),
        ([3, 1, 1, 17, 1, 12, 1, 24, 1, 6, 3, 2, 2, 3], 260),
    ]
    total = sum(check_case(digits, cap) for digits, cap in cases)
    print(f"PASS: {total} exact rational finite gap assertions across {len(cases)} continued fractions")


if __name__ == "__main__":
    main()
