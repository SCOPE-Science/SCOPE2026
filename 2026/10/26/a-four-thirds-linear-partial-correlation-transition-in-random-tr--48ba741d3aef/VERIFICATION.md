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

# Reproducible verification

Execute `python3 verify_precision.py` with Python 3 (standard library only). It exhaustively enumerates the graph law for parameter pairs `(5,2)`, `(5,3)`, and `(6,2)`, computes the exact rational covariance from graph realizations, inverts it without using the spectral formula, and compares every covariance and precision entry to the theorem. It also checks exact signs and spectral positivity at finite parameters and tests asymptotic-convergence trends with high precision.

Observed execution: `PASS: 3332 exact assertions plus high-precision asymptotic diagnostics`. These checks validate finite instances only and are not a proof of the infinite-parameter claims. The proof in `RESULT.md` establishes the infinite results by analytic diagonalization and uniform asymptotic expansion. The identity `-Q_{ef}/sqrt(Q_{ee}Q_{ff})` is a *linear* partial correlation and is not evidence of nonlinear conditional independence.
