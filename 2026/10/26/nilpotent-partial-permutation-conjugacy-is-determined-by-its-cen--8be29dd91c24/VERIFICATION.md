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

The proof reduces all centralizer elements to weighted matchings, then uses the degree-\(j\) coefficient difference to reconstruct the number of chains of length at least \(j\). Running `python3 verify.py` independently enumerates all partial injections for every partition through six vertices, and checks reconstruction on all partitions through seven vertices. Observed: `ALL_NILPOTENT_CENTRALIZER_RANK_CHECKS_PASSED 18348`. No claim of independent audit or exhaustive testing beyond these ranges is made.
