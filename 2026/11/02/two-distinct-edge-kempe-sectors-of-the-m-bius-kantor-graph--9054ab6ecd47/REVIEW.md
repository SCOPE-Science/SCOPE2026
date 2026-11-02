# Review of the Möbius–Kantor edge-Kempe classification

## Correctness: PASS

The domain is exactly the graph \(GP(8,3)\) with 16 vertices and 24 edges, and every proper named three-edge-colouring is an ordered triple of perfect matchings. Choosing the least uncovered vertex gives an exhaustive, nonduplicating recursion, yielding 33 perfect matchings and 120 colourings. Every two-colour union is an even spanning two-factor, and its complete cycles constitute exactly the allowed moves. The exhaustive relation yields two components of sizes 24 and 96 with 54 and 288 edges. Every-root breadth-first search verifies the sphere profiles and diameters; two-colouring checks establish the contrasting parity, with a five-cycle certificate for the small component. A separate edge-colour recursion verifies the counts and graph independently. The explicit graph automorphisms generate a 96-element group whose action on the larger component is regular, proving its Cayley interpretation. Nothing infinite is inferred from the finite search.

## Originality: PASS, with residual historical risk

The 2012 Belcastro–Haas paper studies Kempe classes of cubic edge-colourings and provides the correct historical setting. The 2017 Belcastro–Haas paper studies reconfiguration graphs, but its explicitly worked crossed-prism graph is not \(GP(8,3)\). Goedgebeur–Östergård's 2021 exhaustive census includes all cubic graphs on 16 vertices in aggregate; its tables cover broad component-count computations, not this complete graph's unequal sector sizes, Cayley transitivity, bipartiteness contrast, factor-cycle profiles, or exact metrics. The bare count of two Kempe classes is not claimed as independent novelty. Alternative names such as Möbius–Kantor, \(GP(8,3)\), Levi graph of the \((8_3)\)-configuration, Tait-colouring switches and one-factorization exchanges were searched. Similar exact calculations on Desargues and Pappus graphs have different objects and do not imply this result. Unindexed specialised enumerations remain a nonzero priority risk.

## Value: PASS

This is a complete, natural edge-colouring reconfiguration benchmark for a classical arc-transitive, nonplanar, cubic bipartite incidence graph. Its two disconnected Kempe sectors are structurally different: one is a homogeneous bipartite Cayley graph, while the other is irregular with odd cycles. The bichromatic factor types provide an intrinsic geometric way to distinguish the two sectors. The precise obstruction, together with all shortest-path profiles, is relevant to determining reachability of optimal Tait colourings and to evaluating local-exchange sampling rules. Its value does not rely on a large-parameter generalisation or an unproven application.

## Limitations

The claim is specific to the named-colour, complete-alternating-cycle move definition. No mixing-time, universal nonplanarity theorem, or exact independent publication priority is claimed. General cubic-graph computational enumeration predates this calculation. The two ordinary programs are independent constructions, not an independent scientific review.

Self-review: passed. Independent audit: not yet performed.
