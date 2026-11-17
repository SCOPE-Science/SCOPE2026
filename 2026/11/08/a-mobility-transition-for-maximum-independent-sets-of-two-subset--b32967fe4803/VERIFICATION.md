---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Every intersecting edge family with at least four 2-subsets is a unique star (otherwise only triangle). For n>=6 optimum ordered layer pair is full star at i and opposite partial star at j avoiding ij, count 2n(n-1), and one legal move swaps orientation of pair (i,j), forming n(n-1) disjoint edges. At n=5 three-set triangle exception yields 80 states and connected graph (140 edges, degrees 3/4, diameter9); n=3 gives Q3 and n=4 gives 8 isolates. Read RESULT.md and prism_direct.py; independently generated all bitmask maximum stable sets for n=3,4,5, checked counts, graph metrics and all-pairs BFS diameter9. Maximal-independent-set domination forces any jump to be a slide.

## originality

PASS

EKR determines star extremizers in a single Kneser graph, not the disjoint two-layer optimum space or sharp prism mobility n=5 versus n>=6. Bonsma--Kaminski--Wrochna 2014 established general maximal independent set move models, which are explicitly credited. Resultary semantic search showed same title plus distinct optimum reconfiguration results on other graphs; no stronger prism theorem found.

## value

PASS

The n=5 to n>=6 change from one connected eighty-state component to n(n-1) disjoint edges is a nonroutine exact reconfiguration transition for a classical Kneser construction, with self-contained combinatorial classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
