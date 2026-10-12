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

# Verification notes
Run `python3 verify.py` in a standard Python 3 environment. The self-contained verifier has no nonstandard dependencies. It performs forward subset-BFS for all \(2\le n\le12\), all \(1\le h<n\), checking both finite formula and infinite/non-synchronizing prediction; 66 parameter pairs are exhaustively checked at these sizes. It separately enumerates 3,448 instances of inverse cyclic intervals to test interval preservation, and constructs and replays the proposed word for all coprime parameters up to \(n=100\). Expected output:

`VERIFY_OK exhaustive_BFS_n=2..12 cases=66 inverse_intervals=3448 constructive_witness_n=2..100`

The BFS explores all reachable subsets for those finite sizes, so its minimum is exact within that finite domain. No finite test on bounded state counts establishes the theorem for all \(n\); the independent symbolic proof in RESULT.md does. Literature checks are qualified by the unresolved availability of the complete 2000 and 2022 simple-idempotent papers.
