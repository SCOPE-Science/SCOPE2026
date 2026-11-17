---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The 15 vertices of L(KG(5,2)) and its 30 edges were reconstructed independently from disjoint Petersen 2-subsets. At r=3, the odd-threshold ball witness lemma yields the 30 distinct sets N[u]∪N[v] of cardinality seven. Direct independent enumerator found 2140 nonempty faces and f=(15,105,430,765,585,210,30). An independently coded free-face critical-facet algorithm produced 1059 pairs and critical vector one 0-cell plus 21 3-cells; oriented all 8955 Hasse incidences and topologically sorted the full graph. Forman then gives an integral wedge of 21 S^3, not just a mod-two homology claim. Pure 6-dimensional and H_3 nonzero gives non-shellability. The inspected verify.py additionally checks all 32768 ball-witness masks, reverse tie order and mod-two boundary ranks (14,91,339,405,180,30), not re-executed in this audit.

## originality

PASS

The value 21 is a graph-specific scale-three Čech homotopy classification and not a numerical specialization of the known scale-two line-graph collapse, the hypercube nerve theorem, or the once-subdivided line-graph scale-three result. The target graph has 15 vertices, whereas the latter object L(S(P)) has 30. Published Resultary Petersen Čech persistence applies to P (10 vertices), not L(P); Rips/clique complexes likewise differ. Searches include the exact object, parameter, nerve aliases and stronger class claims. Best-knowledge only; inaccessible or unindexed works could still cover.

## value

PASS

The line graph of the Petersen graph is a canonical small highly symmetric four-regular graph, not an arbitrary enumerative slice. Its first odd Čech scale beyond the known scale-two collapse exhibits a complete integral homotopy type with a six-to-three dimension drop and non-shellability. This gives an exact reproducible benchmark for graph metric topology; no family theorem is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
