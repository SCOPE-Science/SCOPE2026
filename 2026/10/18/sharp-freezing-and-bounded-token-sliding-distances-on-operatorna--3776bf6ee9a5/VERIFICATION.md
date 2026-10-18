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

# Reproducibility

The command `python3 verify.py` (Python standard library only) regenerates the exact finite state graphs from the disjointness definition of \(\operatorname{KG}(n,2)\), enumerates all legal slides, and runs breadth-first search from every state. The recorded stdout from the actual execution is `CHECKS.txt`, terminating `ALL_CHECKS_PASSED`.

The checks cover \(n=5,6,7,8,9\) for two- and three-token states and every ordered pair's distance in the three-token graph; the state-level checks are not assumed to prove a statement for unbounded \(n\). They cover every occupancy at least four for \(n=5,6,7\). The infinite dimension step for two tokens is a six-label reduction and an exhaustive orbit table. The infinite dimension step for three tokens and the frozen range is a combinatorial proof in `RESULT.md`.

No external independent audit or validation has been performed.
