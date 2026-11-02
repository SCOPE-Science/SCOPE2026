---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

For the exact coefficient identities run `python verify_companion.py`. The script uses only Python's standard library. Its execution returned `EXACT_MONOMIAL_AND_SHIFT_CHECK_OK 8712` and `FINITE_PARTIAL_SUM_CHECK_OK`.

The exact rational checks cover 6 monomial degrees, 22 values of each input monomial exponent, and 3 pairs of rational contraction radii. All 8,712 cases passed. The independent factorial-norm-ratio and finite-product expressions agreed as rational numbers.

The script also computed six finite partial Schatten sums, two for each of three regimes, reporting scaled values alongside the limiting constants. Such truncated sums are only diagnostics; they do **not** certify the infinite-dimensional limits.

The analytic proof requires positivity and the orthogonality of distinct output monomials, a uniform factorial-ratio estimate for large second-coordinate degree, negligible fixed-degree contributions, comparison of a decreasing sum with an integral (error at most one), the three small-argument limits of the Laplace integral, and standard positive Riemann-sum convergence. Those steps are included in `RESULT.md`.

No separate independent mathematical audit was performed, and no claim of external certification is made.
