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

The standalone checker `verify.py` compares an independently enumerated index-subsequence deck with an incremental subsequence dynamic program on every binary word of lengths one through nine. It checks all binary words of at most four runs through length nineteen, the run reconstruction identities on 4,096 four-run compositions, and 441 integer-parametrized reversal collisions. It explicitly confirms the two length-eight witness decks by both algorithms and exhaustively rules out nonreversal collisions at all shorter lengths. Expected successful result:

`VERIFY_OK brute_independent_decks=1022 low_run_words=10070 reversal_classes=40 four_run_parameters=4096 parametrized_reversals=441 first_nonreversal_length=8`

An exhaustive finite input domain certifies only the stated finite cutoff. The unbounded theorem is proved by direct symbolic identities in `RESULT.md`; code execution is not a general proof. The comparison risk from unavailable primary full texts remains; no independent mathematical audit or formal proof assistant was used.
