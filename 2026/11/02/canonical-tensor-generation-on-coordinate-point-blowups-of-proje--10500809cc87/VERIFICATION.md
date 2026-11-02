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

The finite checker `verify_coordinate_blowups.py`, invoked with `python3 verify_coordinate_blowups.py`, enumerates exponent-vector lattice points of every orbit-subspace restricted anticanonical polytope for dimension parameters \(2\le n\le8\), every center count, every subspace dimension, and every realizable intersection count. It independently computes affine dimensions of the lattice sets and compares them with the inequality in the mathematical proof; for invariant lines, it checks the actual line degree and its sign. It then checks the final tensor-generation cases. The original execution printed:

`VERIFY_OK: 567 orbit-subspace tests; all n=2..8, all t`

The check cannot establish the formula for arbitrarily large dimension and does not verify the general external toric criterion. The infinite mathematical argument is in `RESULT.md`. The examples are sufficient to expose many off-by-one errors around the dimension-three, dimension-four, and dimension-five transitions. Independent mathematical validation remains unperformed.
