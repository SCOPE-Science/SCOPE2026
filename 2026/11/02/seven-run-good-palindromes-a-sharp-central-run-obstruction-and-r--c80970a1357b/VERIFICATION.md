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

# Reproducibility and limits

Run `python3 verify.py` with the included standalone standard-library script. The actual execution yielded:

`VERIFY_OK quadruples=6561 full_palindrome_lengths=26 coefficient_lengths=60`

`LENGTH_COUNTS [(9, 2), (10, 2), (11, 6), (12, 2), (13, 12), (14, 6), (15, 16), (16, 8), (17, 22), (18, 12), (19, 26), (20, 14), (21, 32)]`

The script's literal factor scan tests *every* possible contiguous even-length block in each enumerated palindrome; it is independent of the stated structural inequalities. The infinite result rests on the proof, especially the published exhaustive minimal-forbidden-factor theorem. No computational test certifies unbounded parameters.
