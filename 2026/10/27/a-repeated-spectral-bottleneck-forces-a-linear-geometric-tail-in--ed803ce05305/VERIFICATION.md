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

Run `python3 verify.py` beside this document. Only Python's standard library is needed. The code independently enumerates one-round permutations through seven cards, computes all exact transition probabilities through 20 states, verifies two- and three-card exact laws to 45 rounds, and calculates leading double-pole constants recursively. The checker reports 221 successful exact assertions. The all-size double-pole asymptotic is proved in `RESULT.md`; no finite check can certify asymptotics for every fixed integer initial state.

The literature comparison is limited by inaccessible full text of the 2016 originating paper. The result is self-reviewed, not independently audited.
