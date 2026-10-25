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

# Verification record

The standalone program `check_kneser_orientations.py` was run using Python 3 in the package working directory. The completion marker was:

`KNESER_CROSSPOLYTOPE_ORIENTATION_CHECKS_OK 3318`

Checks include exact maximal-facet tests for all supports and all possible extra vertices in the parameter pairs (3,6), (3,7), (3,8), (4,8), (4,9), and (5,10), plus direct permutation-sign calculations on complement-pair axes for n=3 through 6 and integer-valued small-cycle character tests.

The mathematically essential infinite steps are proved in `RESULT.md`: construction of maximal facets for arbitrary n and m, integral dual cocycles, determinant of the complement-pair representation, and the exact binary valuation. No finite test is presented as an infinite proof. The quoted full rational rank in the triple case is a published mathematical theorem, not a computer extrapolation. Other integral torsion and unclassified homology degrees remain open.
