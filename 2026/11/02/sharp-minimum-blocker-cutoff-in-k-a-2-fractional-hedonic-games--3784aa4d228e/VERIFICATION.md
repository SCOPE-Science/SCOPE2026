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

# Verification of the claim

The included `verify.py` has no external dependencies. Running `python verify.py` enumerates every labeled set partition with \(a\) ordinary agents and two special agents for \(2\le a\le6\). It then tests each possible mixed subset as a prospective core-blocking coalition using integer arithmetic and checks the complete predicted phase diagram and minimum size. It also checks the maximum over all unstable partitions and enumerates all blockers in the extremal construction.

Actual replay: 5,287 labeled partitions; 217,392 strictly blocking coalitions; every assertion passed. The general theorem is established by a case-complete symbolic proof in RESULT.md. The finite computation does **not** serve as a certificate for arbitrary \(a\). No external independent audit is claimed.
