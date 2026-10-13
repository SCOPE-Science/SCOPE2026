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

`python3 restricted_gcd5_verify.py` checks all multiples of five between ten and twenty thousand against an independent binary digit dynamic program, and all admissible indices directly for rows through one thousand. The program also enumerates all minimal zero-sum residue multisets and tests existence of single-split witnesses in each ordinary class.

Recorded output: `VERIFY_OK minimal_zero_sum_types=14 entries=3999 brute_entries=199 level_three=3 first_level_three=[65, 1025, 16385]`.

The finite test is corroborative, not a proof for arbitrary row length. The formal argument uses Kummer's theorem, a complete size-at-most-five zero-sum case split, and explicit witnesses for all boundary classes. No independent audit or external certification is asserted.
