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

# Reproduction

Run `python3 maw_verify.py` from the directory containing this file. The checker independently constructs the recursive words by recursion and positional binary valuations, computes every contextual minimal absence directly for ranks 1 through 9, compares the complete sets and their spectra, and also checks every predicted absent word through rank 11.

Actual result: `VERIFY_OK exhaustive_all_MAWs_levels=1..9 explicit_candidates_levels=1..11`.

The computation is finite: it does not certify the statement for all ranks. The all-rank argument is given in `RESULT.md` and is independent of experiment. No independent external audit was conducted.
