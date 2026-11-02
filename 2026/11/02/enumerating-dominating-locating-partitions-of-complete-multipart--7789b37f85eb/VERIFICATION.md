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

The proof reduces locating signatures and domination to necessary and sufficient class-occupancy conditions; the resulting polynomial identities are valid for arbitrary integer part sizes in their stated ranges.

`VERIFY.py` implements a direct bitmask test for each candidate bipartition. It checks both directed domination conditions and all pairwise off-code neighbourhood signatures without using the classification theorem, then compares the complete predicted coefficient dictionaries.

Executed command: `python3 VERIFY.py`

Observed result: `VERIFY_OK profiles=147 subsets=209812 both_complete_weight_enumerators=true`

This finite exhaustive check is not an infinite proof. The proof in `RESULT.md` handles arbitrary numbers and sizes of parts. No independent mathematical audit has been performed.
