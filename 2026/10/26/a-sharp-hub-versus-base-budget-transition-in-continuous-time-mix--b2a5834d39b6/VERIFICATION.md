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

Direct checks: run `python cone_verify.py` in a Python environment with NumPy installed. Cases include cycles of length 3 to 14; hypercubes of dimension 2 to 6; and the complete graph on 8 base vertices. The script checks rate-budget equality, the computed Laplacian second eigenvalue against the closed formula at tolerance 1e-9, and a finite grid of 1001 symmetric budget allocations. The critical dimension cases are included. These are numerical cross-checks only: global optimality, the strict support implication for all optimizers, and integer-family thresholds are proved analytically in RESULT.md. Independent audit or validation has not been performed.
