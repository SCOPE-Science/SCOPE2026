# Scientific review: monitoring edge-geodetic polynomials of unicyclic graphs

## Correctness — PASS

The precise domain is every finite simple connected unweighted graph having exactly one cycle. The proof establishes a necessary-and-sufficient classification of all monitoring sets: all degree-one vertices are compulsory, and the projections of selected vertices to the unique cycle must have every successive cyclic gap strictly shorter than half the circumference. The implication from an acceptable projected set to monitored bridge edges is proved by a selected leaf on the detached side of each bridge and a second selected vertex at another cycle root. The cycle-edge equivalence uses the unique hanging-tree paths and the two possible cycle arcs. This gives a bijective enumeration: free nonleaf/attachment-root selections contribute the binomial factor, and each mandatory cycle gap contributes a bounded-composition factor; with no attachments, a pointed cyclic-composition count gives the remaining polynomial. All boundary cases, including triangles, four-cycles, and a single attachment vertex, are treated explicitly.

The standalone exact-integer verifier recomputed shortest paths after every edge deletion and tested all 370,616 selected subsets in its deterministic finite graph suite, including every labeled unicyclic graph of order at most six. It additionally compared all 16,376 cyclic attachment patterns of circumferences three through thirteen against direct enumeration. These computations are corroboration rather than an infinite proof.

## Originality — PASS (bounded source comparison)

The 2022 introducing paper [1], Theorems 3.4 and 3.5, determines only the minimum size of a monitoring edge-geodetic set of cycles and unicyclic graphs. Its proof already describes leaves simulating attachment roots, which is explicitly credited; it does not state a full all-set equivalence, a generating polynomial, a composition product, a minimum-set multiplicity formula, or the branch-shape/gap-order invariance. The 2022 product paper [2], Theorem 1, supplies an exact sectional criterion for Cartesian products, not an enumeration on graphs formed by hanging rooted trees from one cycle. The 2024 bounds paper [3] concerns compulsory vertices and scalar structural bounds, while a relevant 2025 Nordhaus–Gaddum study concerns scalar extremal values. None of the inspected relevant statements dominates the all-cardinality theorem here. A previous derivation from the ideas in [1] might exist unindexed or be implicit; search non-detection is not a uniqueness proof. These limitations are retained as residual originality risks.

## Value — PASS

Network probes that must detect every single-edge failure are the motivating objects in [1]. The size of a smallest set does not tell how many placements are possible at that size or at each higher budget. The present formula determines **every** feasible deployment count on an arbitrary unicyclic network; it identifies exact minimum-set multiplicities; and it proves the mathematically nonobvious invariance under changes of every hanging-tree shape and under rearrangements of the cyclic attachment gaps. The classification and all-cardinality factorization supply structural information absent from the scalar theorem and do not rely on an arbitrary isolated finite example.

## Closest sources and limitations

[1] Dev, Dey, Foucaud, Narayanan, Ramasubramony Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774 (first publicly posted 2022-10-07), relevant full-text Definition 1.1, Lemmas 2.1–2.4, Theorems 3.1, 3.4–3.5.

[2] Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, arXiv:2210.08955 (first posted 2022-10-17), Section 2, Theorem 1 and its proof.

[3] Foucaud et al., *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs*, arXiv:2403.09122 (first posted 2024-03-14), mandatory-vertex characterization and scalar bounds.

[4] *Nordhaus–Gaddum-type results for monitoring edge-geodetic number of graphs*, Discrete Applied Mathematics (2025), DOI:10.1016/j.dam.2025.04.040; accessible article sections on unicyclic scalar extremal results. An independent literature audit has not been performed. Only connected unicyclic simple unweighted graphs are treated; new claims are not made about multicyclic graphs, edge weights, or algorithmic hardness.

Self-review: passed. Independent audit: not yet performed.
