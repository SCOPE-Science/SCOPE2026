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

# Reproducibility and scope

Invoke `python3 verify.py` in the same directory as this document. It checks the pair-transition recurrences, complete shortest-distance spectrum, explicit merging words, and positive-cost minimum uniqueness using independently computed reverse-graph distances for five weight pairs.

The successful output is `VERIFY_OK`. The finite checks range over \(2\le n\le50\), while reverse Dijkstra tests range over \(2\le n\le17\). The proof for every integer \(n\ge2\) is in `RESULT.md`; finite tests are cross-checks and cannot establish the infinite statement. No external validation or independent audit has been performed.
