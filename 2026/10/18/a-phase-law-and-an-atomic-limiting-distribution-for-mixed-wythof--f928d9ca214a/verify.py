"""Exact finite checks for the mixed Wythoff phase-law theorem.

Run with Python 3.10 or later. The theorem's infinite bounds are proved
analytically; this program checks only the explicitly indicated finite range.
"""

from math import isqrt, log, sqrt


def floor_m_alpha(m: int) -> int:
    """Exact floor(m / golden_ratio), avoiding floating-point arithmetic."""
    return (isqrt(5 * m * m) - m) // 2


def floor_m_phi(m: int) -> int:
    """Exact floor(m * golden_ratio)."""
    return (isqrt(5 * m * m) + m) // 2


def run():
    cap = 8192
    # Compute the complementary Beatty indicator in exact integer arithmetic.
    lower = [0] * (cap + 1)
    for m in range(1, cap + 1):
        lower[m] = floor_m_alpha(m + 1) - floor_m_alpha(m)
        assert lower[m] in (0, 1)

    # Count lower-plus-upper decompositions by exact indicator convolution.
    counts = [0] * (cap + 1)
    for m in range(1, cap):
        if lower[m]:
            for k in range(1, cap - m + 1):
                if not lower[k]:
                    counts[m + k] += 1

    # Independently enumerate literal Beatty-pair representations.
    check_cap = 2048
    independent = [0] * (check_cap + 1)
    for h in range(1, check_cap + 1):
        a = floor_m_phi(h)
        if a > check_cap:
            break
        for k in range(1, check_cap + 1):
            b = floor_m_phi(k) + k
            if a + b > check_cap:
                break
            independent[a + b] += 1
    assert counts[: check_cap + 1] == independent

    # Compare the phase formula with exact integer counts (supportive finite test).
    alpha = (sqrt(5) - 1) / 2
    beta = 1 - alpha
    errors = []
    for n in range(2, cap + 1):
        theta = (n * alpha) % 1
        phase = (beta - theta if theta < beta else
                 theta - beta if theta < 2 * beta else beta)
        error = counts[n] - (n - 1) * phase
        errors.append(error)
        assert abs(error) <= 12 * (1 + log(n + 1))

    # The empirical first moment agrees to increasing accuracy with the law.
    finite_mean = sum(counts[n] / n for n in range(2, cap + 1)) / (cap - 1)
    limiting_mean = beta * (1 - beta)
    assert abs(finite_mean - limiting_mean) < 0.005

    # OEIS A259598 begins at n=1; check its first 11 terms exactly.
    assert counts[1:12] == [0, 0, 1, 0, 1, 2, 0, 3, 1, 2, 4]
    print(
        'VERIFY_OK',
        f'exact_convolution_to={cap}',
        f'pair_enumeration_to={check_cap}',
        f'min_phase_error={min(errors):.6f}',
        f'max_phase_error={max(errors):.6f}',
        f'finite_mean={finite_mean:.9f}',
        f'limit_mean={limiting_mean:.9f}',
    )


if __name__ == '__main__':
    run()
