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

# Reproducibility and limits

Run `python verify.py` in a standard Python 3 environment. The program constructs every vector subspace in reduced row-echelon form and tests its closure under multiplication on both sides by all basis elements of the given radical-square-zero path algebra. It compares its independently enumerated counts by quotient dimension against the closed Gaussian formula. The program reports `VERIFY_OK cases= 13` after checking thirteen finite prime-field configurations. Included are the three-vertex quiver with double and single arrows (predicted distribution `1,3,3,5,5,4,1` over the field of order two), loops, a directed cycle, parallel arrows, and disconnected quivers.

The finite checks do not establish the formula in arbitrary dimension, over extension fields, or in the large-field limit. Those claims rely on the normal-form and Gaussian-asymptotic proof given in `RESULT.md`. Independent validation has not been performed.
