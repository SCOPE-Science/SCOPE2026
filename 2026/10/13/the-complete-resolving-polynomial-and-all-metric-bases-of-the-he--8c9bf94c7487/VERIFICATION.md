---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a same-type pair, five of its own part and three of the opposite part are equidistant; the 42 sets are distinct by the omitted pair and the sizes in each part. Bipartite parity handles opposite-type pairs, and the empty selection is also excluded by the same-type obstructions. With two chosen lines, the three two-point signature classes each require one chosen point. Three noncollinear points give distinct signatures for all lines; collinear points give three duplicate pairs, which two chosen lines cannot eliminate. Choosing a,b on the two lines away from their intersection leaves exactly one noncollinear choice of c outside their union. Thus the classification gives 84 bases and 84 duals. In the vector model, x,a,b are a vector basis and the eligible c is x+a+b, giving transitivity of GL(3,2) on the first type; polarity exchanges the two types. The connected bipartition shows that the 168 collineations and their 168 duals exhaust the automorphisms. A separate vector/kernel-line construction with BFS and distance-signature enumeration tested every one of the 16384 subsets. It gave 11588 resolving sets, precisely the stated rank counts, and 4796 nonresolving subsets, exactly the union of the 42 obstruction subcubes. The orbit and geometric classification also matched independently. Replay: /workspace/branches/753da2d3-ada6-41f4-998e-1b0133646dad/independent_check.py. No frozen script was executed.

## originality

PASS

Distinct contribution supported: the full cardinality polynomial for ordinary vertex resolving sets of the fixed Heawood graph, the corresponding equal-distance blocker census, and the complete base geometry and orbit in this setting. Neither the known metric dimension nor the general resolving-set criterion is new. A catalogue result with matching minimum geometric configurations resolves edges and does not give the vertex census. This is a bounded best-of-knowledge comparison.

## value

PASS

The Fano incidence graph is the exceptional smallest projective-plane case of an established resolving-set problem. Its exact rank counts answer how many labelled sensor placements of each size work, rather than only giving the minimum size. The 42 equal-distance obstructions explain why every placement of size at least nine works, and the 84+84 geometric classification and single orbit give a concise description of the optimal placements. This is a complete natural finite invariant with a checkable structural interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
