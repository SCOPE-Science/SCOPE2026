# Scientific review

## Correctness — PASS
The geometric-fixed-face rule follows by barycentric averaging on vertex orbits. Its Boolean-face test is proved for the actual total cut-facet definition. Alexander duality for a join gives a union of two cones, not merely a homology isomorphism; iterating yields the homotopy model. The weighted-threshold critical facets all attach to one contractible star along full boundaries, providing an integral sphere-wedge proof. The two-component mixed example and all polynomial degree shifts were explicitly checked. `verify.py` independently constructs the orbit faces and performs exact finite mod-two matrix reductions; exhaustive and seeded checks agree. Finite computations are not used as an all-parameter proof.

## Originality — PASS, with residual risks
Bayer et al. (arXiv:2304.13675, Section 7.1, Theorems 7.4, 7.8–7.9) establish strong **equivariant homotopy models** for the same graph family, and so imply all subgroup fixed-space homotopy types abstractly. This significant logical coverage is acknowledged. Their statements provide a poset product model, ambient ranks and representation decompositions, but not the direct orbit-weight full Betti polynomial, weighted-threshold sphere-wedge reduction, or mixed-dimensional geometric fixed-space instance. Those explicit computations require additional arguments and are not presented there. Carnero Bravo (arXiv:2602.21427) studies total cut complexes and duals, including some product graphs, but does not state this fixed-locus coefficient calculation. An equivalent unpublished computation or a derivation elsewhere from the published equivariant model remains possible.

## Value — PASS
The subgroup-invariant integral homotopy type is completely decidable from finite orbit-weight data without constructing the ambient cut complex or decomposing its rational symmetry representation. Different sphere dimensions can coexist in one fixed space although the ambient multipartite cut complex is a one-dimensional-degree sphere wedge. The \(K_{9,4}\), threshold-four example has two independent two-spheres and one three-sphere, a structural phenomenon invisible in ambient Betti numbers. The polynomial treats arbitrarily many parts, arbitrary orbit weights, and non-transitive or coupled within-part actions uniformly.

## Scope and limitations
The result does not cover part-permuting automorphisms. The ambient equivariant homotopy theorem is prior work, not attributed as new. The finite checks are mod-two only. Exact integral statements rest on the proof; unindexed equivalent literature and independent review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
