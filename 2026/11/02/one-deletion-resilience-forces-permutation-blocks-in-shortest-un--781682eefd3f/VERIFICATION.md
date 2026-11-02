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
# Reproduction and limits

Run `python3 verify_deletion_robust.py` with Python 3. The checker enumerates exact-multiplicity candidate hosts; for each host it deletes every possible position and checks all patterns of the target length using a literal subsequence scan. It does not use the ordering argument from the proof.

Verified parameter pairs: \((q,k)=(2,1),\ldots,(2,6),(3,1),(3,2),(3,3),(4,1),(4,2)\). Exact total: 413,244 candidate words. Exact acceptance counts, in that order: 6, 8, 16, 32, 64, 128, 90, 216, 1296, 2520, 13824. The last printed line is `VERIFY_OK parameter_cases=11 multiset_words=413244`.

These are finite regression checks. The lower bound and all-parameter classification follow from the proof in `RESULT.md`; no independent mathematical audit or proof-assistant verification is claimed.
