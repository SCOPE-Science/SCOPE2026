#!/usr/bin/env python3
"""Reproducible finite checks for the rational n+log(n) correlation formula.
Python 3 standard library only. Finite checks corroborate, not prove, the limit.
"""
import math
from fractions import Fraction


def limit_profile(a, s):
    if s == 0:
        return 0.0
    c = 2 * s / (a * math.expm1(1 / a))
    return c + 2 * sum(max(0, 1 - a * h / s)
                       for h in range(1, int(s / a) + 2))


def direct_count(a, b, N, s):
    p = [(a / b) * (n + math.log(n)) for n in range(1, N + 1)]
    pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if abs(math.remainder(p[j] - p[i], 1.0)) <= s / N:
                pairs += 1
    return pairs * 2


def resonance_count(a, b, N, s):
    """Independent root-window enumeration, no quadratic pair loop."""
    if s == 0:
        return 0
    delta = b * s / (a * N)
    assert delta < 1 / (2 * a), 'choose larger N'
    count = 0  # unordered pairs
    for h in range(1, int(s / a) + 3):
        distance = b * h / math.expm1(delta)
        m_min = max(1, math.ceil(distance))
        # numerical boundary guard: direct formula at adjacent integers
        while m_min > 1 and math.log1p(b * h / (m_min - 1)) <= delta:
            m_min -= 1
        while m_min <= N - b * h and math.log1p(b * h / m_min) > delta:
            m_min += 1
        count += max(0, N - b * h - m_min + 1)
    jmax = int(a * (math.log(N) + delta)) + 1
    for j in range(1, jmax + 1):
        c = math.exp(j / a)
        r = (-j * pow(a, -1, b)) % b if b > 1 else 0
        lo = c * math.exp(-delta)
        hi = c * math.exp(delta)
        for m in range(1, min(N, int(N / lo)) + 1):
            low = max(m + 1, math.ceil(lo * m))
            high = min(N, math.floor(hi * m))
            first = low + (m + r - low) % b
            if first <= high:
                count += 1 + (high - first) // b
    return 2 * count


def main():
    direct_tests = 0
    for a, b in [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 2)]:
        assert math.gcd(a, b) == 1
        for N in (131, 397, 701):
            for s in (0.4, 1.25, 2.75, 4.1):
                x = direct_count(a, b, N, s)
                y = resonance_count(a, b, N, s)
                assert x == y, (a, b, N, s, x, y)
                direct_tests += 1
    # Check predicted limits and the independence from the denominator.
    asymptotic_tests = 0
    for a, b in [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 2)]:
        for s in (0.5, 1.5, 3.5):
            N = 50000
            measured = resonance_count(a, b, N, s) / N
            expected = limit_profile(a, s)
            assert abs(measured - expected) < 0.055, (a, b, s, measured, expected)
            asymptotic_tests += 1
    for a in (1, 2, 3, 5):
        assert limit_profile(a, a / 2) < a  # below 2s in first segment
    print(f'CERTIFICATE_OK direct_root_agreements={direct_tests} '
          f'large_cutoff_agreements={asymptotic_tests} denominator_universality=checked')


if __name__ == '__main__':
    main()
