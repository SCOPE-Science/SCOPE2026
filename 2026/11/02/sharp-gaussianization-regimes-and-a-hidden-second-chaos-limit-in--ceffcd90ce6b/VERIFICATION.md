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

# Mathematical verification

The accompanying `verify.py` can be run with Python 3 and SciPy. It independently evaluates the normalized diffusivity covariance integral in two ways: the incomplete-beta reduction of the triangular double integral, and a nested beta-weighted quadrature in independent triangular coordinates. Nine pairs of evaluations agree within a relative tolerance of \(2\times10^{-7}\). Three large-time evaluations corroborate the asymptotic amplitudes in the three regimes, and a final identity confirms the coefficient of the second-chaos fluctuation variance. The reproducibility program prints `PASS 13` after all assertions succeed.

The proof, rather than the numerical checks, establishes the asymptotic limits for all admissible parameters. Numerical comparisons with a single large-time value do not establish the limiting rates or exclusion of other parameter regimes; those facts use dominated/monotone convergence and explicit beta integrals in `RESULT.md`.

The stationary Gaussian process with covariance \((1+|h|)^{-\eta/2}\) has a positive covariance kernel by its Laplace-mixture representation. The convergence in \(L^2\) of the improper quadratic integral follows from a finite weighted covariance double integral in the strict subcritical regime. The non-Gaussian conclusion follows from its nonzero second-chaos fourth cumulant, not a simulation.

The external literature comparison is best-knowledge and is not independent publication-priority verification.
