# Review of the Möbius–Kantor magnitude-homology character

## Correctness
**PASS.** The graph, metric, chain groups and sign conventions are specified in the result. Complete enumeration yields \((16,1056,2592,1296)\) chains in bidegree length four. Surjectivity of the degree-two boundary and binary ranks \(1040\), \(1248\), together with the exact chain identities and \(48\) independent alternating four-cycles, force rational homology dimensions \((0,0,304,48)\). Exact exhaustive enumeration of all \(96\) distance-preserving permutations, chain-level fixed tuple traces and the fixed alternating cycles prove each character value. The signed chain-complex trace identity is applicable because all chain maps commute with the differential. All checks are reproduced by `magnitude_verify.py` against `character_table.csv`; no unresolved computational premise is needed for the rational claim.

## Originality
**PASS on accessible evidence, with residual priority risk.** The closest direct paper is Hepworth–Willerton arXiv:1505.04125, Appendix A.3.4: it tabulates the rank \(304\) and automorphism order \(96\), but not the representation character or three-dimensional invariant subspace. The same bidegree on Shrikhande, and graph configuration, independence, matching and Čech complexes on related graphs, have distinct chain complexes and do not imply the claim. Gu arXiv:1809.07240 and Asao–Hiraoka–Kanazawa arXiv:2101.09044 concern distinct generalizations and vanishings. Asao–Wakatsuki arXiv:2408.12147 is potentially strong but applies a geodetic basis theorem, inapplicable to the graph's two distinct geodesics from \(0\) to \(3\). Relevant full primary text and indexed mathematical records were inspected, not just title matches. An unindexed identical character computation cannot be categorically ruled out.

## Value
**PASS.** Hepworth and Willerton explicitly foreground the role of symmetry in the motivating classical cubic graphs. The new complete action on \(304\)-dimensional rational magnitude homology identifies three fixed directions and nonzero positive and negative traces on specified symmetry classes. Neither the earlier Betti number nor the magnitude Euler series alone determines these invariants. The answer concerns a canonical highly symmetric, non-geodetic example outside the reach of a later strong geodetic-basis theorem.

## Limits
The result is rational, one fixed bidegree and one graph only. It does not assert an integral representation decomposition or independently checked publication priority.

Self-review: passed. Independent audit: not yet performed.
