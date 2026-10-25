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

# Reproducibility and verification

The theorem is proved symbolically and analytically in `RESULT.md`. The standalone Python 3 program `CHECK.py` uses only the standard library, runs without internet access, and prints `CHECK_OK` if its tests pass. It verifies that the exact Gamma-factor monomial weights have the asserted asymptotic leading coefficient at four distinct parameter sets, including noninteger ellipsoid exponents. It also reconstructs finite-degree optimal coefficients and checks the equality of the calculated residual norm and the inverse partial-weight sum, and tests the normalization and phase constraint of sample boundary-circle points.

Observed output: `CHECK_OK`.

**Analytic checks:** The phase-group annihilator is taken for the *full* kernel of \((\eta_1,\eta_2)\mapsto\eta_1^a\eta_2^b\), including all components when \(\gcd(a,b)>1\). Weighted Cauchy–Schwarz gives the exact unrestricted finite-dimensional optimum. Haar character orthogonality both supplies the energy minimizer and proves that every competitor has at least the same energy. Stirling and series comparison prove the limit laws for all fixed admissible parameters.

**Limits:** Numerical samples do not prove infinite-dimensional optimality, the asymptotics, or historical novelty. The proof assumes the specified normalized Poletsky–Stessin coefficient norm and classifies only the stated monomial family. No independent audit has been performed.
