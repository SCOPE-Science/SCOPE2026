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

A fresh exact set-based replay, without running either supplied checker, generated the two coordinate graphs, enumerated all k-subsets for k=1,…,6, tested induced reachability by closure and domination by neighborhood union, then bucketed eligible states by all their (k−1)-subsets. Joining all pairs in each bucket is exactly the one-replacement rule and introduces no false adjacency. BFS gave all components and every within-component eccentricity at k=5. At k=1,2,3 neither graph has a state (maximum connected coverage 7, 10, 13). At k=4,5,6 the triples (states,edges,component sizes) were Shrikhande (32,0,32 singletons), (672,5136,[672]), (4064,74304,[4064]); rook (8,0,8 singletons), (384,2112,[192,192]), (3744,63024,[3744]). The size-five degree and eccentricity histograms agree in full, with 48 eccentricity-six and 144 eccentricity-seven states per rook component. Direct degree/common-neighbor checks give A²=4I+2J, hence eigenvalues 6,2,−2 with multiplicities 1,6,9; local neighborhoods distinguish the graphs. The replay also matched all induced claws to the Shrikhande four-states and all rows/columns to the rook four-states. Structurally the rook states correspond to connected selected edge supports in K₄,₄ that cover one entire side. Five edges covering four rows require exactly two columns and form a tree with one bridge row. Switching the leaf assignments, moving the bridge by removing one of its incidences and adding a missing incidence at another row, and replacing the extra cell of a whole-column-plus-one support connect an orientation. An exchange across orientations would give a connected spanning union on eight vertices with at most six edges, which is impossible. Transposing the board exchanges the two components isomorphically. Together with the reproduced six-state connectivity this proves the first connected layers, without inference about later layers. The bounded replay recipe above reproduces the finite census; inspectable package verification paths are verify.py and verify_alt.cpp, both read but not executed.

## originality

PASS

The supported distinct claim is the different first connected fixed-cardinality one-replacement layers for these cospectral graphs, with their exact exchange structure and size-five metrics. Neither the common SRG parameters nor the rook minimum-size classification or state counts alone are credited as new.

## value

PASS

The canonical same-spectrum graph pair has the same minimum size but different first connected jump layers, so the spectrum cannot determine this reconfiguration threshold. The bipartite orientation barrier explains why rook k=5 is qualitatively different and why testing k=6 is meaningful. The exact components and within-component distances describe that obstruction and contrast, not an arbitrary list of subset counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
