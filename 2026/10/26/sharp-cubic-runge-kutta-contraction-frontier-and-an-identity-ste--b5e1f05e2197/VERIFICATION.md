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

# Reproducibility

Run `python verify.py` with SymPy. The script was run successfully after writing and before packaging. It verifies the exact expansion coefficients and exact rational equal-rate and reentrant identities via symbolic assertions. The universal small-step conclusions additionally use a leading-polynomial-coefficient argument and the trace/determinant definiteness criterion, fully written in RESULT.md. The all-step equal-rate conclusion follows from the factored signs for the entire interval. The long-step claim follows from the nonsingular leading cubic matrix coefficient; finite evaluations alone are not claimed as an infinite proof. No external independent audit has been performed.
