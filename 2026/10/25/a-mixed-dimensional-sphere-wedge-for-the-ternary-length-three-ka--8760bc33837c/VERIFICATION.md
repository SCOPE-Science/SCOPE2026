---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Actual Kautz digraph has 12 admissible length-three words, 24 shifted arcs, indegree 2 at every vertex; exactly 3^12 incoming-edge assignments exhaust every face. Independent reconstruction enumerated 314,928 faces including the empty face and the 4,608 top and 132 next-to-top facets (24 root pairs, multiplicities 21 times five and three times nine). Independently recreated complete 157,439 nonempty face Morse pairs and checked a directed-Hasse topological sort of 314,927 nodes and 2,361,936 incidences, with critical dimensions (0:1,8:3,9:22,10:23). Recomputed the complete signed integral 3-by-22 and 22-by-23 Morse boundary matrices, their zero product, 3 and 11 integral unit cancellations, and zero residual boundary. The surviving 8 cells in degree 9 and 12 in degree 10 attach by null maps because π9(∨S9)=H9, establishing the integral wedge, not merely homology. The 384 spanning arborescences per root supply an independent determinant check. This establishes ONLY the specified finite digraph, not other Kautz parameters.

## originality

PASS

Best-of-knowledge exact finite homotopy classification is not implied by the full-text-checked directed-acyclic and doubly directed tree theorems; the Kautz line digraph has genuine directed cycles, no complete sink, and is not a bidirected tree. An unindexed classification or unpublished certificate of this exact digraph remains plausible.

## value

PASS

Directed-forest complexes are natural topological graph invariants and the ternary length-three Kautz network is a canonical finite shift network. Its large, nonpure face structure and exact mixed integral sphere-wedge type are not known to follow from spanning-tree counts; the 8/12 dimension split and lower facets offer a substantive reusable exact benchmark for cyclic digraph forest complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
