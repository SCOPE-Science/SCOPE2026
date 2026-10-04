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

The proof diagonalizes the SPD Hessian and reduces the published Hessian-corrected heavy-ball update to one scalar two-step recurrence per eigenvalue. Necessary-and-sufficient Jury conditions give the exact stability region, while characteristic-root products and discriminants give the rate optimum.

`artifacts/verify_hessian_corrected_hb.py` checks the modal reduction, the exact stability-budget equivalence, the optimal-root formulas for positive and negative effective momentum, and the matched-curvature one-update cancellation.

The finite replay is a consistency check only. Nonnormal, nonquadratic, adaptive, stochastic, and inexact settings are outside the claim.
