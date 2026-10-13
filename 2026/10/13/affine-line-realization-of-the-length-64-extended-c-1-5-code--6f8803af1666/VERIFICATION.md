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

# Exact checks

Run `python3 verify.py` using Python 3 standard library only. The field is specified by the irreducible primitive polynomial \(T^6+T+1\); all additions are bitwise XOR and products are exact polynomial reductions. The program builds each of the \(336\) affine \(\mathbb F_4\)-lines, checks unique incidence for every pair of distinct field points, derives the \(13\) binary parity-check rows from \(1,x,x^5\), and evaluates full binary ranks by Gaussian elimination. It also enumerates all weight-four zero-syndrome supports, via equal-syndrome pair partitions, and verifies they equal the affine lines.

The expected exact diagnostics are `PARITY_CHECK_RANK 13`, `AFFINE_LINES 336`, `WEIGHT_FOUR_SUPPORTS 336`, `LINE_SPAN_RANK 51`, `CODE_PARAMETERS [64,51,4]`, `AUT_GROUP_ORDER 23224320`, and `VERIFY_OK`. The group formula rests on the fundamental theorem of affine geometry and the line-spanning proof, not on exhaustive enumeration of all coordinate permutations. The prior literature already determines the classical geometric-code group. This is a complete finite-field calculation, not a generalization to other extension degrees, and does not substitute for independent audit.
