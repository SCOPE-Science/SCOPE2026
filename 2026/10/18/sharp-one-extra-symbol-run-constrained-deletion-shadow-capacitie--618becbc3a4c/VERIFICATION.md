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

# Verification and scope

Run `python3 verify.py` from the directory containing this file. The verifier constructs deletion-output sets directly and uses no third-party packages or proof logs. Expected terminal lines:

`CANONICAL_OK 540`

`GLOBAL_EXHAUSTIVE_OK 40680`

It covers all canonical duplication positions in 540 cases for \(2\le q\le7\) and \(q\le r\le\min(q+9,16)\), and all 40,680 words of length \(r+1\) with \(r\) runs for \((q,r)\) in \(q=2,2\le r\le10\), \(q=3,3\le r\le9\), and \(q=4,4\le r\le7\), for \(0\le t\le q\). It asserts each exact coefficient and global extremum against the formulas.

The infinite theorem is proved from the distinct-subsequence recurrence, explicit modular-polynomial coefficient extraction and the already published cyclic-operation lemma; finite enumeration does **not** substitute for that general proof. The theorem covers only \(n=r+1\) and \(0\le t\le q\). An earlier indexed or unindexed equivalent theorem may exist; one relevant older article's full text was unavailable. This file does not assert independent certification.
