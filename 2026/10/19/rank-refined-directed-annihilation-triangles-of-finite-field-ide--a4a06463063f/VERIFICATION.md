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
# Reproducibility and proof boundary

Run `python check_triangles.py` using standard-library Python. It enumerates actual matrices, calculates multiplication and Gaussian-rank counts independently, and checks all rank-refined directed triples for the seven finite (dimension, field-order) cases (1,2), (2,2), (2,3), (2,4), (3,2), (3,3), and (4,2). The field of order four is represented explicitly by a quadratic polynomial over the two-element field. It additionally checks cyclic symmetry and support from the formula for (5,2), (6,2), (5,3), and (4,4). The expected final line is `ALL_EXACT_CHECKS_PASSED`.

The universal count is established by the constructive block, complement, and subspace-lifting arguments in RESULT.md. Finite experiments are checks, not substitutes for those proof steps. No external or independent audit has been performed.
