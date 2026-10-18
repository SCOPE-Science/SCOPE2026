"""Numerical corroboration of the two-site cyclic Gabor operator-band theorem.

Requires Python 3 and NumPy. This is a finite-dimensional test, not a proof
for all cyclic orders.
"""
import math
import numpy as np


def step_order(n, a):
    return n // math.gcd(n, a)


def half_angle_sine_squared(L):
    return 0.0 if L % 2 == 0 else math.sin(math.pi / (2 * L)) ** 2


def optimal_ratio_squared(L):
    s = half_angle_sine_squared(L)
    m = 3.0 - 4.0 * s
    return (m + math.sqrt(max(0.0, m * m - 4.0))) / 2.0


def claimed_nonzero_singulars(n, a, r):
    L = step_order(n, a)
    x = r * r
    roots = np.exp(2j * np.pi * np.arange(n) * a / n)
    values = np.r_[np.abs(1 + x * roots), np.full(2*n, r)]
    values *= math.sqrt(n) / (1+x)
    return np.sort(values[values > 1e-8])


def actual_nonzero_singulars(n, a, r):
    g = np.zeros(n, dtype=complex)
    g[0], g[a] = 1, r
    g /= np.linalg.norm(g)
    jj = np.arange(n)
    measurements = []
    for shift in range(n):
        for mod in range(n):
            v = np.roll(g, shift) * np.exp(2j*np.pi*mod*jj/n)
            measurements.append(np.outer(v.conj(), v).reshape(n*n))
    S = np.linalg.svd(np.asarray(measurements), compute_uv=False)
    return np.sort(S[S > 1e-8])


def optimize_exact(L):
    x = optimal_ratio_squared(L)
    s = half_angle_sine_squared(L)
    k = math.sqrt(5 - 4*s)
    assert abs((1+x)/math.sqrt(x) - k) < 1e-12
    if x > 1.000001:
        for factor in (0.4, 0.7, 0.91, 1.1, 1.5, 2.5):
            z = x * factor
            d = math.sqrt((1-z)**2 + 4*z*s)
            cond = (1+z)/min(math.sqrt(z), d)
            assert cond >= k - 1e-10
    return k


def main():
    cases = 0
    spectrum_checks = 0
    exceptional_cases = 0
    largest_error = 0.0
    for n in range(3, 12):
        for a in range(1, n):
            L = step_order(n, a)
            if L < 3:
                continue
            optimize_exact(L)
            for r in (0.55, 1.0, math.sqrt(optimal_ratio_squared(L)), 1.9):
                observed = actual_nonzero_singulars(n, a, r)
                predicted = claimed_nonzero_singulars(n, a, r)
                assert len(observed) == len(predicted), (n, a, r, len(observed), len(predicted))
                if L % 2 == 0 and r == 1:
                    expected_rank = 3*n - n//L
                    exceptional_cases += 1
                else:
                    expected_rank = 3*n
                assert len(observed) == expected_rank, (n, a, r, len(observed), expected_rank)
                error = float(np.max(np.abs(observed - predicted)))
                largest_error = max(largest_error, error)
                assert error < 1e-10, (n, a, r, error)
                spectrum_checks += 1
            cases += 1
    print(f"VERIFIED: {cases} cyclic geometry cases, {spectrum_checks} direct complex SVD comparisons; ")
    print(f"{exceptional_cases} rank-defect cases; maximum singular-value error {largest_error:.2e}.")
    for n in range(3, 17):
        Ls = [step_order(n,a) for a in range(1,n) if step_order(n,a)>=3]
        kbest = min(optimize_exact(L) for L in Ls)
        odddiv = next((p for p in range(3,n+1,2) if n%p == 0 and all(p%d for d in range(3, int(p**0.5)+1, 2))), None)
        expected = math.sqrt(5 - 4*math.sin(math.pi/(2*odddiv))**2) if odddiv else math.sqrt(5)
        assert abs(kbest-expected)<1e-12
    print("VERIFIED: global step-order optimum for 3 <= n <= 16.")

if __name__ == "__main__":
    main()
