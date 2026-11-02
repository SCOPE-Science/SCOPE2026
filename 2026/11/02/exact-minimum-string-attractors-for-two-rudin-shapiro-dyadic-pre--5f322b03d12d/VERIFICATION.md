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

# Exact computational checks

Execute `python3 artifacts/verify_attractors.py`. This regenerates the standard Rudin–Shapiro prefixes and *every* nonempty distinct factor, checks every displayed attractor against all factor masks, verifies that each mask deleted in reduction is implied by a retained mask, and runs complete recursive hitting-set refutations for targets smaller by one. The verifier uses only the standard library and contains all necessary code and input data.

Expected complete results:

| Prefix length | Distinct factors | Retained masks | Optimal attractor size | Failed smaller-budget search nodes |
|---:|---:|---:|---:|---:|
| 128 | 7008 | 48 | 10 | 243 |
| 256 | 28128 | 64 | 11 | 3703 |

The output was reproduced in the scientific package before this review. The input word is computed from the parity of consecutive `11` occurrences in base-2 representations. The algorithm is exhaustive for these two finite words, not a proof for any other length. Mathematical and literature-priority confirmation by an independent party is not performed.
