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
# Verification and limits

The analytical proof supplies both bounds: contractive multipliers give coefficient estimates through action on the constant vector, and each normalized monomial is contractive by the exact multivariate Vandermonde weighted-shift formula. The diagonal multiplier simultaneously saturates all coefficients. These steps prove the infinite-dimensional theorem; finite experiments alone do not.

Run `python CHECKER.py` with Python 3.9 or later. A direct execution passed 52,012 finite assertions involving exact rational weights over tested multiindices, the disk `diag(w,w**2)` counterexample at radius `2/3`, finite pointwise comparisons, and dimension-collapse examples. There are no external dependencies.

The check does not enumerate all multiindices in arbitrary degrees or independently certify the literature-priority assessment. Full independent audit and external validation have not been performed.
