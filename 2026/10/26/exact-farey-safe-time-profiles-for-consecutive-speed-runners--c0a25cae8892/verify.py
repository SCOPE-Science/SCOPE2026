"""Exact finite checks for the consecutive-speed safe-time profile."""
from fractions import Fraction
from math import gcd


def safe_measure_by_intervals(n, delta):
    """Independent union calculation using every unreduced speed center."""
    arcs = []
    for v in range(1, n + 1):
        radius = delta / v
        for j in range(v):
            center = Fraction(j, v)
            a, b = center - radius, center + radius
            for shift in (-1, 0, 1):
                left = max(Fraction(0), a + shift)
                right = min(Fraction(1), b + shift)
                if left < right:
                    arcs.append((left, right))
    arcs.sort()
    covered = Fraction(0)
    end = Fraction(0)
    for a, b in arcs:
        if b > end:
            covered += b - max(end, a)
            end = b
    return 1 - covered


def farey_profile(n, delta):
    ans = Fraction(0)
    for q in range(1, n + 1):
        for r in range(1, n + 1):
            if gcd(q, r) == 1 and q + r > n:
                ans += max(Fraction(0), 1 - delta * (q + r)) / (q * r)
    return ans


def kink_set(n):
    return {q + r for q in range(1, n + 1) for r in range(1, n + 1)
            if gcd(q, r) == 1 and q + r > n}


def predicted_kink_set(n):
    result = set(range(n + 1, 2 * n))
    if n % 2 == 0:
        result.discard(2 * n - 2)
    return result


def main():
    tested = 0
    for n in range(2, 22):
        assert kink_set(n) == predicted_kink_set(n), n
        samples = {Fraction(0), Fraction(1, 2 * n), Fraction(1, n + 1),
                   Fraction(1, 2), Fraction(1, 3 * n)}
        for s in range(n + 1, 2 * n):
            samples.add(Fraction(1, s))
            if s < 2 * n - 1:
                samples.add((Fraction(1, s) + Fraction(1, s + 1)) / 2)
        for delta in samples:
            exact = safe_measure_by_intervals(n, delta)
            predicted = farey_profile(n, delta)
            assert exact == predicted, (n, delta, exact, predicted)
            tested += 1
        near = Fraction(1, 2) * (Fraction(1, n + 1) + Fraction(1, n + 2))
        m = n + 1
        pair_weight = sum((Fraction(1, q * (m - q))
                           for q in range(1, m) if gcd(q, m) == 1), Fraction(0))
        assert farey_profile(n, near) == (1 - m * near) * pair_weight
        assert pair_weight == Fraction(2, m) * sum(
            (Fraction(1, q) for q in range(1, m) if gcd(q, m) == 1), Fraction(0))
        mass_at_union_bound = 1 - Fraction(1, n) * sum(
            (Fraction(sum(gcd(j, q) == 1 for j in range(q)), q)
             for q in range(1, n + 1)), Fraction(0))
        assert farey_profile(n, Fraction(1, 2 * n)) == mass_at_union_bound
    print(f'CERTIFICATE_OK sizes=20 exact_profile_points={tested} kink_classifications=20')


if __name__ == '__main__':
    main()
