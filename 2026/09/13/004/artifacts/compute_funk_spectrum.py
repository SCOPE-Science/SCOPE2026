"""Verify Funk-Radon eigenvalues P_{2k}(0) on S^2: nonvanishing + decay ~ 1/sqrt(pi k).

For the round metric on RP^2, I^*I has eigenvalues mu_k = c * lam_k^2 with
lam_k = L * P_{2k}(0), L = great-circle length factor (nonzero constant).
We check: lam_k != 0 for all k (injectivity), and mu_k ~ const/k -> 0
(order -1 smoothing), so the inverse grows like k and cannot be differential
(see DRAFT.md for the symbol/parity contradiction).

Uses only the Python standard library.
"""
import math

def P_even_zero(k):
    # P_{2k}(0) = (-1)^k * C(2k,k) / 4^k
    return ((-1) ** k) * math.comb(2 * k, k) / (4 ** k)

def main():
    print(f"{'k':>4} {'P_{2k}(0)':>22} {'|P|*sqrt(pi*k)':>16} {'mu_k*k (up to c)':>18}")
    worst = 0.0
    for k in range(1, 61):
        p = P_even_zero(k)
        assert p != 0.0, f"vanishing eigenvalue at k={k}"
        asym = abs(p) * math.sqrt(math.pi * k)
        mu_k_times_k = p * p * k  # proportional to true mu_k * k
        worst = max(worst, abs(asym - 1.0))
        if k <= 12 or k % 10 == 0:
            print(f"{k:>4} {p:>22.15f} {asym:>16.10f} {mu_k_times_k:>18.10f}")
    # asymptotic constant check: |P|*sqrt(pi k) -> 1
    # asymptotic constant check: |P|*sqrt(pi k) -> 1 (Wallis product rate 1-1/(8k))
    # use stable recurrence p_{k+1} = -p_k*(2k+1)/(2k+2) for large k
    p = 1.0
    for j in range(0, 600):
        p = -p * (2 * j + 1) / (2 * j + 2) if j > 0 else -0.5
    # p is now P_{1200}(0)
    ratio600 = abs(p) * math.sqrt(math.pi * 600)
    print(f"asymptotic ratio at k=600 (recurrence): {ratio600:.10f} (expect -> 1)")
    assert abs(ratio600 - 1.0) < 0.002
    # injectivity: no zero eigenvalue among first 2000 modes
    for k in range(0, 2000):
        assert P_even_zero(k) != 0
    print("OK: all even eigenvalues nonzero for k<2000; mu_k = c*lam_k^2 ~ const/k -> 0.")

if __name__ == "__main__":
    main()
