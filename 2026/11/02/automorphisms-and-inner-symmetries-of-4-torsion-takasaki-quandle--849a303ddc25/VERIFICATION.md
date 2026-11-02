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
# Reproducibility and verification

The abstract classification for all positive dimensions is established symbolically in `RESULT.md`; finite enumeration cannot replace that proof. Running `python3 check.py` in any Python 3 interpreter with the standard library prints `VERIFY_OK` on success.

The checker independently computes the right-translation fiber functions and their binary linear ranks for dimensions one through four. For dimensions one and two, it enumerates every permutation of the intrinsic orbit set and every choice of image for each orbit representative, reconstructs the only operation-compatible candidate map, and evaluates every binary quandle equation on every pair of elements. Dimension two yields exactly 6144 automorphisms. In dimension three it examines all 40320 permutations of the eight orbits for affine linearity and spot-checks the operation equations for 24 maps; these samples are not exhaustive automorphism classification.

The reported group orders, normal forms and quotient index can be recomputed directly from the proof. The previous 2017 published inner-group count is contradicted by the explicit right-translation relations, not by a numerical timeout or unbounded search.

Self-review passed. Independent audit not performed.
