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

# Reproducible checks and scope

Execute `python verify.py` with Python 3 and SymPy. It prints `PASS: 34 exact symbolic/rational assertions; generator, independent ordered-time integrals, onset and asymptotics.` when all checks complete.

The program uses two structurally different calculations of the stationary second and fourth active-position moments. The first recursively inverts the exact two-state stationary-generator blocks for all monomials of total degree up to four, keeping symbolic reversal rate and chirality. The second expands the convolution representation of position into ordered time integrations and integrates each interval using the inverse of a two-by-two Fourier-modulated Markov generator. The independent integrals are compared at three exact-rational parameter pairs, including a positive-cumulant witness and a negative-cumulant control.

It also confirms the polynomial factorization, the strict-convexity derivative, the negative discriminant needed at dimensionless chirality eight, the exact negative value at chirality nine and reversal rate three quarters, a positive-cumulant witness at chirality ten, and the leading high-chirality asymptotic polynomials. No random seeds or external data are needed.

The finite checks do **not** purport to prove positivity at all real parameters. The analytically demonstrated strict convexity, positive-parameter quadratic crossing, coercive threshold minimization, and root-asymptotic arguments prove those statements. No independent external audit or experimental validation has been performed.
