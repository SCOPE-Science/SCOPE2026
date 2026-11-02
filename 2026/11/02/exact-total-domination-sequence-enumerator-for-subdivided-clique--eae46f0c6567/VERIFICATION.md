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

Run `python verify_sequences.py` using Python 3 (standard library only). The verifier constructs the original incidence-graph adjacency and counts distinct completed legal vertex sequences via memoized graph-vertex masks, independently of the recurrence. It compares the full coefficient map with the recurrence plus shuffle enumeration for \(n=2,3,4,5\), and checks the exact support and minimum/maximum coefficient identities.

Observed outputs: \(n=2\): 4 sequences at length 2; \(n=3\): 216 at length 4; \(n=4\): 1440 at length 5 and 34560 at length 6; \(n=5\): 756000 at length 7 and 12096000 at length 8. Each comparison passed. These finite tests do not certify every \(n\); the proof supplies the universal conclusion. There has been no independent mathematical audit.
