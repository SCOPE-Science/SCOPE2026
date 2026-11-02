---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Ind_2(G disjoint H) is exactly the simplicial join of the parent complexes because connected components stay in their part. Ind_2(G join H) has every pure parent face but its only mixed faces are individual bipartite cross edges: a mixed triple is connected and forbidden. The parent complexes are connected since all vertex pairs form faces, so attaching ab cross edges to two connected CW spaces gives the wedge of the parent spaces with ab-1 independent S1 loops; no higher mixed attaching maps. Join of sphere wedges gives t P_G P_H (or contractible if a factor is contractible). Induction on any finite binary disjoint-union/graph-join cotree yields integral wedge and no torsion; base K1 is a point, ab=1 boundary addressed. Independent face-based F2 homology of 90 random cographs up to nine vertices and the mixed S3∨18S1 nine-vertex example matches; finite tests do not establish general theorem.

## originality

PASS

Best-of-knowledge PASS: 2020 Deshpande–Singh Theorem 3.5 classifies complete multipartite graphs, not arbitrary cographs with nested union and join. The full 2025 Deshpande–Roy–Sawant Theorem 4.7 applies to Alexander dual and conditional vertex decomposability/shellability, not the direct integral homotopy type; its index Ind_3 represents the same component-size-two condition under shifted conventions. Mamun–Nalikka–Ramos 2026 covers finite generation of homology of graph complexes on cographs rather than explicit cotree wedge ranks, but complete primary full text was inaccessible this run, leaving priority uncertainty. Exact and alias searches found no dominating all-cograph recurrence.

## value

PASS

A cotree is the canonical structural decomposition of the major P4-free hereditary graph class. The recurrence computes a genuine complete integral homotopy type and graded Betti multiplicities without building a simplicial complex; it explains separated-dimensional homology, e.g. S3∨18S1, beyond the known equidimensional complete multipartite case. The bound two is structural because it turns mixed graph-join simplices into edges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
