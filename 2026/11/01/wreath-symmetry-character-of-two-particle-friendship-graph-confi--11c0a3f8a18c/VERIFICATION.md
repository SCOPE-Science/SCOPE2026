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
The accompanying source file `verify_friendship.py` reconstructs the complete signed cellular incidence and group actions for petal counts 2 through 5. It checks the boundary composition, the full-rank signed-unit triangular minor, connectedness, and the exterior-square/tensor-product character prediction for every group element. The included `checks.txt` is the resulting execution output; the proof of all parameter values is in `RESULT.md`, independent of numerical extrapolation. The `checks.txt` output is not a certificate of independent peer verification.
