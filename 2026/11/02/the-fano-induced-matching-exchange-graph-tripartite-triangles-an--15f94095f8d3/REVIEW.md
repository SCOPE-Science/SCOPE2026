# Review of the Fano induced-matching exchange graph

## Correctness — PASS

The setting is the incidence graph of the unique order-two projective plane, with flags as graph edges. Two flags are compatible exactly when neither point is on the other's line. The four-point tangent-line obstruction bounds induced matchings by three. All 84 optimum three-flag systems arise from 28 noncollinear point triples (one tangent assignment) and seven collinear point triples (eight assignments). Every compatible two-flag pair has three completions, creating the asserted tripartite triangles; unique common two-flag pairs prove each exchange edge lies in exactly one triangle. The diameter, radius, distance profiles, and detours are finite statements established by two independent complete incidence constructions and exhaustive breadth-first search, not by sampling. All boundary counts, including all 5,985 four-flag subsets and all 3,486 unordered optimum pairs, were checked. The accompanying `verify_direct.py` and `verify_cyclic.py` programs both executed successfully.

## Originality — PASS, qualified

The maximum size three, the correspondence to strong representative systems, and the previously calculated 84 compatible triples are known and expressly excluded from the novel claim. The new statement concerns the exact graph whose configurations are individual three-edge induced matchings and whose moves replace one selected flag. An earlier seven-colour complete-partition trade graph is not equivalent: its vertices are complete partitions into seven classes, and its moves simultaneously change whole classes. The 1991 Illés–Szőnyi–Wettl study establishes strong representative systems and size bounds, while the 2013 Basavaraju–Heggernes–van 't Hof–Saei–Villanger paper develops general triangle-free maximum/maximal induced-matching bounds, without stating this exact exchange graph. Hibi et al. study dominating induced matchings; Dejter's different 84-vertex Fano-derived graph is four-regular. The inspected records and primary material do not entail the new tripartition and distances, but independent historical discovery under another name cannot be excluded. Some older source text had imperfect extraction.

## Value — PASS

The exact one-flag exchange graph is an intrinsic reconfiguration invariant of maximum strong representative systems of the smallest projective plane. Its three symmetry types, 84 uniquely associated triangles, nonuniform eccentricities, and sharp two-extra-exchange bound give the full shortest-path structure and the constraints on feasibility-preserving local moves, rather than an arbitrary slice or a restatement of the known extremal size. Although this is a fixed finite graph rather than an all-orders theorem, the solution supplies a natural complete classification of its optimum-set exchange geometry, with reusable explicit certificates.

## Source-specific limits

The nearest conceptual precedent is Illés, Szőnyi and Wettl (1991), *Blocking sets and maximal strong representative systems in finite projective planes*; the public author text was accessible but noisy. Basavaraju and collaborators (arXiv:1312.5180v1, 18 December 2013) provide an inspected full-text baseline on induced matchings in triangle-free graphs. Dejter (2009) studies a different Fano-derived graph; Hibi et al. (arXiv:1412.3881) discuss dominating induced matchings, a different condition. A complete historical search is impossible, so hidden equivalent formulations remain the residual originality risk. Independent external verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
