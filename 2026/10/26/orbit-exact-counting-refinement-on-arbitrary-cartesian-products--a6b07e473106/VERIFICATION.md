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

# Verification notes
Run `python check_star_products.py`. The program constructs Cartesian-star adjacency lists without graph-library dependencies, performs standard simultaneous refinement from one constant colour, computes the intrinsic orbit-profile partition independently from the coordinate data, and compares all classes and sizes. It also calculates walk coefficients directly by adjacency iteration and independently by truncated products of the single-star matrix exponential. Both methods use exact integers/rationals.

Executed output (`verification_output.txt`): 75 star-product parameter multisets tested (including five factors); exact Taylor walk coefficients verified for 344 vertices; all tests passed. This is evidence for finite sample instances, not a proof of an all-parameter assertion. The latter is the analytic and combinatorial proof in `RESULT.md`.

The exact values in the test log and the program text are embedded in the same record. Independent external audit has not been performed.
