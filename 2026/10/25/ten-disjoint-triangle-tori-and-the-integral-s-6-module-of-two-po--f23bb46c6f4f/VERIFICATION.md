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

# Reproducibility certificate

Run `python3 verify.py` with the Python standard library. The verifier generates all \(15\) zero-cells, \(60\) one-cells and \(45\) two-cells, checks signed cellular boundaries and the rank of the second boundary over \(\mathbb F_{101}\). It generates the ten complementary-triple product torus cycles, verifies their boundary is zero and their primitive relation, and checks a fixed integral determinant and all \(720\) signed vertex-permutation actions. Expected leading marker:

`VERIFY_OK_K6_TEN_TRIANGLE_TORI_PRIMITIVE_ALTERNATING_RELATION`

The observed unit certificate uses rows `0,1,3,6,7,9,12,13,18` in the generated square-coordinate order and columns `0..8` in lexicographic triangle-pair order; determinant is `1`. Rank modulo `101` of the second boundary is `36`; rank modulo `2` is `35`, and the latter is not used to infer a rational or integral rank. This is a finite exact computation for the specified graph; it does not assess other graphs or furnish an external mathematical review.
