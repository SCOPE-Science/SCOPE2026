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

# Verification and limits
The self-contained `verify.py` independently enumerates possible products in the normal-form group via dynamic programming on exact letter counts and compares them with the stated Parikh-membership rule, including the zero-count boundary. It then uses the claimed canonical state labels and checks all tested representative signatures and pairwise distinguishing suffixes for each integer parameter 2 through 10. The output is `VERIFY_OK`.

Run with `python3 verify.py` from the extracted files; the implementation uses only the Python standard library. The script is a bounded consistency and reproducibility check. The proof of the family-wide result is mathematical, and no independent audit has been performed.
