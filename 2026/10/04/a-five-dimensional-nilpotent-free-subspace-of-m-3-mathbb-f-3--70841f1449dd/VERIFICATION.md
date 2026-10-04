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

The file `verify_f3_five_space.py` performs a complete exact check over all 243 parameter tuples in the displayed five-dimensional family. It first computes rank 5 for the coefficient matrices over the field with three elements. For every matrix it then checks both that nilpotency is equivalent to a zero cube and that the three non-leading characteristic-polynomial coefficients vanish. The two predicates agree on every tuple and identify only the zero tuple.

The archived output is `VERIFY_OK total=243 nonzero=242 nilpotent_total=1 nilpotent_nonzero=0 zero_charpoly=1 basis_rank=5`.

This verifies only the stated five-dimensional construction. It does not search all six-dimensional subspaces and gives no upper bound on the maximum dimension.
