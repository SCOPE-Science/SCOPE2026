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

Exact verification uses the standalone `check.py` with Python's standard library. The program enumerates the two-state transition matrix over four observations and checks the simplified no-detection polynomial on 750 rational configurations, then checks exact sample solutions and transition-boundary identities. The proof is an algebraic identity and a convexity argument, rather than a finite experiment. No independent audit has been performed.
