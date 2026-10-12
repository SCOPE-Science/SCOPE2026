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

# Verification

The accompanying `verify_cross_base.py` was run directly and returned `EXACT_CHECKS_OK`. Its exact rational compatibility cases cover \((b,m,n)=(2,1,3),(2,2,3),(2,3,4),(3,2,3),(4,2,3)\), involving 8, 64, 4096, 729, and 4096 common-base symbols, respectively. For each case it checks every common-base cylinder weight. It also checks incompatible all-zero-cylinder weights and the exact rank 10 of the 64-by-12 logarithmic compatibility matrix for bases four and eight.

The analytic proof establishes all infinite-dimensional measure claims: common-base iid regrouping; strong-law separation of unequal common-base digit laws; coprime boundary splitting of each primitive block; Chinese-remainder rigidity of coordinate marginals; and full support from positive cylinders. Exact finite tests are not presented as exhaustive proof of this theorem. Numeric approximations are not required. Historical source priority and external mathematical validation remain unperformed.
