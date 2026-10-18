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

The theorem and the complete case analysis are in `RESULT.md`. Run `python3 verify_circular_parikh.py` with Python 3 and only the standard library. It explicitly materializes each circular word, enumerates all `n` rotations, and independently counts three scattered-subsequence statistics before grouping by the complete circular Parikh matrix. It checks all 8436 anchored two-`a` necklaces with `h` from 0 through 35, the full size-one/size-two classification, exact class counts, and the one-`a` boundary up to 35.

Expected exact terminal line:

`CIRCULAR_PARIKH_CLASSIFICATION_PASS two_a_c_range=0..35 anchored_necklaces=8436 one_a_boundary_c_range=0..35`

The unbounded parameter statement is established symbolically by cyclic cut counting and a positive-integer gap equality; verification of finite cases alone does not extend beyond those cases. An independent audit has not been performed.
