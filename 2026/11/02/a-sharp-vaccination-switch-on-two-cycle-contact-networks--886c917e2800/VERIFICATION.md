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

The finite-state checker in `verification/check.py` was executed using Python 3 with the standard library. It independently enumerated all bond configurations of the residual graphs for cycle lengths \(r=3,4,5\), rational transmissibilities \(q\in\{1/3,1/2,3/4,1\}\), and all one-vertex vaccination choices. Every direct pair-connectivity expectation matched the claimed exact formulas, and every nonportal had a strictly higher outbreak score than a portal. The script reported 231 successful checks, including numerical crossover-sign and large-cycle scale tests.

The numerical root checks and finite enumeration do not prove uniqueness of a crossover or the limiting scaling. The written proof uses the cycle's two edge-disjoint arcs, a graph-containment coupling, Descartes' rule, and uniform Taylor bounds. The original epidemiological article's full text was inaccessible; no independent publication-priority or mathematical validation is claimed.
