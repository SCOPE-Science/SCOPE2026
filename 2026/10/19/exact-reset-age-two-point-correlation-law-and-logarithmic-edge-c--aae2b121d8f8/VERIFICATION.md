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

For the exact analytic claim, the governing Glauber flip generator closes on the two-point recurrence, the Bessel kernel is the Dirichlet semigroup on positive separations, and positivity of \(I_n(z)\) gives the inverse function. The large-time Bessel expansion gives a \(t^{-3/2}\) decay prefactor and makes the logarithmic factor at the critical reset rate indispensable. The near-zero Bessel series yields the distance-dependent exponent. The stationary mean follows from the Laplace-transformed half-line recurrence.

`verification.py` independently constructs the 256-state generator of an eight-spin periodic Glauber system and compares its transient and reset-age mean correlations against the infinite-chain formula. It also checks Bessel integral normalization and Laplace transforms at multiple parameters, short-time power laws, and rescaled long-time tail behavior. Execution on the included file returned `PASS 108 tests` with maximal absolute raw discrepancy about \(0.0056112\). Differences in finite-ring checks are not exact-math errors and have explicit comparison tolerances. Finite numerical tests do not certify infinite-dimensional results; numerical quadrature is not accompanied by rigorous rounding interval bounds.

Reproduce with `python verification.py` in a Python environment with NumPy and SciPy. No third-party data files or network requests are needed.
