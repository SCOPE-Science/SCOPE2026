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

The precise claim is the maximal-common-zero two-branch criterion, its all-dimensional finite-sum count, the sharp existence threshold, and exhaustively computed values through dimension five. The proof is in RESULT.md. Run the three accompanied programs as described there; expected outputs are embedded, from actual executions.

`count_diamond.c` enumerated monotone Boolean functions and valid ordered pairs exactly through five atoms. `count_diamond_orbits.c` independently executed a Burnside orbit fixed-point loop for every source coordinate permutation and both target permutations, verifying integer divisibility. `direct_check.py` independently enumerated every possible truth function through four atoms, then checked every possible target-upward-lifting clause directly rather than applying the local criterion; its separate Burnside implementation reproduced all overlapping counts. No beyond-five enumeration or external independent audit is asserted.
