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

The analytical proof is in RESULT.md. Run `python verify.py` with Python 3.10+ (standard library only). The code checks exact power-series recovery of the squared-axis polynomial for dimensions two, three and four, monotonicity and numerical inversion of the last elementary symmetric coefficient, and an independently computed spherical integral for dimension three. In the test with squared axes `(1,4,9)`, relative discrepancies in three moment ratios are below `3e-14`.

The high-dimensional uniqueness argument rests on Gaussian polar integration and the strict sign of a convergent integral derivative; numerical checks are not an infinite-dimensional or all-parameter proof. Moment estimation from finite samples and stability for nearly repeated roots are not certified.
