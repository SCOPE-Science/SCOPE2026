# Self-review

## Correctness — PASS

The proof reconstructs the incidence map from independent cactus cycle relations, giving an invertible linear transformation from a direct sum of zero-sum cycle spaces and bridge lines. The polar is a direct product of cycle cube sections and intervals. Every vertex of an even-cycle section has squared norm equal to the cycle length; every vertex of an odd-cycle section has squared norm one less. Componentwise sign and permutation symmetries force canonical shape matrices to be block scalar. The maximal determinant John problem reduces to one linear budget constraint and a strictly concave log-determinant optimization; its Lagrange solution is the stated parity-weighted Laplacian. The Löwner problem reduces to independent exact lower bounds on the block scalar variances and attains all of them. The common invertible transformation correctly transports both matrices, and block determinant ratios plus weighted spanning-tree identities yield the volumes. The homothety criterion follows from matching all block-variance ratios.

The exact-rational implementation checks 61 concrete cactus graphs, 26,006 polar facet contacts and 998 signed vertex contacts. Finite enumeration serves only as a consistency check; the proof is for the entire stated infinite class. Critical boundary cases include a single bridge, all-even-cycle cacti, and multiple odd cycles of different lengths. No theorem is asserted for graphs with overlapping cycles.

## Originality — PASS, with priority risk

The principal regular-matroid symmetric-edge-polytope source (D’Alì–Juhnke-Kubitzke–Koch, arXiv:2307.04933v1, 2023) gives polytope and polar/facet structure, not an explicit John or Löwner formula. D’Alì–Delucchi–Michałek, *Many faces of symmetric edge polytopes* (2019 preprint/2022 publication), gives combinatorial structure and facet counts. Chen–Davis–Korchevskaia, arXiv:2107.12315, treats facets via subgraphs. Ivanov, arXiv:1707.04442, treats general extremal-ellipsoid questions but no cactus parity classification. The closest semantically retrieved published records concerned oriented cycle root-polytope Ehrhart theory or a numerical index for Lipschitz-free spaces over cycles; neither implies an equality of John and Löwner shape operators for undirected symmetric cactus root polytopes. Euclidean inradius and directed root-polytope Minkowski asymmetry are mathematically different invariants; neither type of result implies the pair of extremal ellipsoid matrices here.

The exact theorem, complete facet/vertex contact statements and mixed-cycle homothety dichotomy were compared, rather than searching for matching words alone. No decisive covering statement was found, but a general optimal-design or cube-section formulation could preexist. This is a self-review, not a universal or independent priority certification.

## Value — PASS

The result completely classifies two natural canonical geometric invariants on all connected cactus symmetric edge polytopes. Its coefficients distinguish odd from even cycles and detect whether the two canonical ellipsoids are homothetic; the condition is sensitive to bridges and differing odd cycle lengths. The all-facet and all-vertex tangency statements give structural extremal certificates without exponential face enumeration, while weighted matrix-tree formulas give individual absolute Euclidean volumes. This is stronger and geometrically different from an inradius formula, pure facet enumeration, or a routine parameter substitution.

## Residual limitations

The cactus assumption is essential to the direct-product polar reduction; extension to arbitrary graphs is not established. Possible independently published equivalent ellipsoid formulas under other terminology are not excluded. The reproduced finite arithmetic checks do not constitute independent review.

Self-review: passed. Independent audit: not yet performed.
