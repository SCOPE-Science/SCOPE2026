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

# Reproducibility checks

Run `python verify.py` with Python 3 and NumPy. The program implements the tangent projector, full symmetric eigendecomposition and signed truncated-SVD reconstruction, then compares eigenvalues, critical steps, positivity, exact-flow semidefiniteness and residual costs with the analytic expressions. It exercises the strictly damped counterexample and rank extensions as well as rank-one controls. The final assertion count is printed when the test finishes.

The universal rank-one and sharp rank-two statements are proved in `RESULT.md`; finite test cases are supplementary checks only. The exact threshold has nonunique best rank-two truncations: the verifier deliberately tests parameters strictly on either side rather than inferring a unique matrix at equality. No numerical comparison can establish novelty, and no independent validation was performed.
