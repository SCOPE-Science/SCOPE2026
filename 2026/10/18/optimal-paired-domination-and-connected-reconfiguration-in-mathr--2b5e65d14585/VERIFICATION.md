---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The four-edge starting characterization was independently reconstructed: paired domination implies total domination and hence ground vertex-cover number at least three. A triangle whose fourth edge meets it gives a two-cover; a disjoint fourth edge gives a claw in the disjointness graph, which has no perfect matching. Four edges and no triangle imply bipartiteness, and König's theorem gives a matching of size three. Conversely such a triple dominates all vertices, and the fourth edge can be paired to one of the triple; two selected vertices never suffice and four do. The original census and matching multiplicities are correct, but are not claimed as the contribution of the repair. In the repair the cliques of states containing each matching triple cover the whole exchange graph. A change of one ground matching edge gives a common four-edge state; a two-edge flip ab,cd -> ac,bd with fixed ef links the cliques by exchanging cd for bd in states sharing ab,ac,ef. One-edge replacements align the six-label supports, and flips then insert desired pairs without undoing ones already installed. This also handles n=6, where no support changes are needed. Moves within each clique join the links and connect the given endpoints without leaving the optimum set space.

## originality

PASS

The original package's static minimum, full classification and exact census have demonstrable equivalent indexed coverage and do not pass originality as contributions. Both affected claim files now isolate the surviving all-n connectivity theorem. No examined statement gives that theorem for these feasible sets and moves. The conclusion distinguishes coverage from priority, which the catalogue dates do not settle.

## value

PASS

The repair answers a natural mobility question not determined by knowing or counting the optima: whether a single replacement can update solutions without ever losing feasibility or optimality. It gives an explicit lift from ground-matching operations to legal moves on four-edge states and includes the tight n=6 obstruction to moving supports. The proof works uniformly, rather than checking a finite sample or restating the covered census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
