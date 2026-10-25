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

Run `python3 verify.py` in the folder containing this document. The program uses only the Python 3 standard library and prints `VERIFY_OK matrix_permutation_cases= 49660` if all comparisons pass.

The checker constructs the cyclic-neighbor XOR transformation as bit-vector maps, applies each chosen permutation directly, and computes the ranks of the first and second iterates using exact elimination over the binary field. It checks all 46,230 permutations with sizes three through eight (the odd cases are controls), one hundred deterministic pseudorandom wirings for each size nine through 36, and every prefix-rotation wiring for those larger sizes. No floating-point equality or external files are involved. The result was replayed successfully from the standalone script prior to packaging.

The enumerations verify boundaries and implementation only. They do not certify all infinitely many lengths or all permutations for larger sizes. Those conclusions follow from the two-dimensional kernel/image pairing proof in `RESULT.md`. The source-study comparison was completed at the level described in `REVIEW.md`; no independent audit or external certification has been performed.
