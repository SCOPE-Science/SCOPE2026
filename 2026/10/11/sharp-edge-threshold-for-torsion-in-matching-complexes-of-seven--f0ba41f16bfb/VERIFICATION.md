---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For every simple graph with at most seven vertices, no matching has four edges, so its matching complex has dimension <=2 and all H1 torsion equals torsion of coker(boundary_2), as im(boundary_1) is free. Independently reconstructed every one of the 1,253 networkx Graph Atlas representatives (orders 0 through 7), enumerated all disjoint pairs/triples of graph edges, built the actual signed integer second boundary and ran exact SymPy Smith normal form on every matrix. Exactly 40 graphs have SNF nonunit invariants, each a single 3; histogram edges 13:1,14:3,15:9,16:10,17:8,18:5,19:2,20:1,21:1. The unique 13-edge G1105 has f=(13,42,30), SNF (1^29,3), and the original explicit integral certificate independently satisfies boundary_2(c)=3z. This census is exhaustive conditional on published Graph Atlas completeness; modular rank alone would not certify the integer torsion. Only up-to-7 graph order is proved.

## originality

PASS

The earliest underlying graph order and 13-edge threshold, unique sparse witness, and exact census of all forty seven-vertex torsion-bearing unlabeled graphs are additional to the known complete-graph K7 torsion and to flag complexes on at most twelve simplicial vertices. Reproducing a known K7 torsion value alone would not qualify; the sparse threshold and complete edge-distribution genuinely remain. No matching published exact census found in scoped searches, but unindexed catalogs remain possible.

## value

PASS

Finding the first graph order at which matching-complex 3-torsion occurs, sharp sparsest edge threshold, a unique sparse witness, and the complete finite classification are natural extremal/homological boundary questions. The 40-case integer torsion table is not a repetition of known K7 torsion and offers concrete data for edge-deletion phenomena. The 7-vertex cutoff is a complete finite invariant, not an arbitrary case slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
