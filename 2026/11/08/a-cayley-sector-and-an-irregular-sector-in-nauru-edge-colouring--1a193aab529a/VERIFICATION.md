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

Inspected two complete standard-library source scripts. Independent exhaustive perfect-matching enumeration found exactly 120 matchings, feasible even complementary factors yield 504 distinct NAMED colorings. Enumerated every bichromatic cycle switch and verified reciprocity, 1674 undirected switching edges and exactly 144/360 components. All-source BFS recomputed small-sector shells (1,6,27,66,44), edge count432, diameter4 and large-sector degree counts 6:210,8:144,12:6, distances (1242,5904,18981,31401,6732,360), ecc 5:330 and 6:30; cycle-type 10+14 exactly small sector. Verified explicit shift/reflection/alpha preserve base graph, generated 144-element group, regular 144-colouring orbit and all six neighbouring generators are involutions. Exact finite exploration exhausts the defined graph, not an infinite family.

## originality

PASS

The 2021 Goedgebeur–Östergård full paper gives aggregate numbers of edge-Kempe classes across cubic graph censuses, not this entire 504-state adjacency/metric classification. Earlier belcastro–Haas develops equivalence theory; Eppstein treats Nauru itself and its 144 automorphisms, not their free and transitive action on a Kempe component. Same-graph Nauru anti-forcing spectrum is a different invariant. The uninspected 1969 Watkins full text and underlying graph-census raw dataset are specific priority risks.

## value

PASS

A complete metric and group-action classification of a natural 24-vertex symmetric cubic graph’s edge-Kempe state space reveals a sharp Cayley-versus-irregular sector dichotomy, marked by an invariant bichromatic 10-cycle and different girth/eccentricity. These structural invariants can serve exact reconfiguration benchmarks beyond the previously tabulated class count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
