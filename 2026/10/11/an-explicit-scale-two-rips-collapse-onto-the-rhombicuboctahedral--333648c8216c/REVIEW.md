# Same-model review: rhombicuboctahedral graph-metric Rips collapse

## Correctness — PASS
All 24 vertices and 48 graph edges are specified algebraically. The standard-library verifier rebuilds the shortest-path matrix and all 638 graph-square cliques, checks 252 distinct sequential free-face pairs of consecutive dimensions with unique cofaces, and confirms the exact remainder is a 24-vertex triangulation with 66 edges, 44 triangles, connected cyclic vertex links, and Euler characteristic 2. Thus the remainder is a 2-sphere. Scale-one clique triangles are eight vertex-disjoint triangles, removable to a graph with first Betti number 17. The proof is exhaustive for this finite graph, not an extrapolation from samples; no claims for scale three or other graphs.

The collapse certificate is checked pair by pair with the **actual generated files**: `verify_rhombicuboctahedron.py` and `collapse_certificate.json`. Finite exhaustive enumeration is conclusive here because this claim concerns precisely one specified finite graph and its complete finite complex. The supporting sphere identification is independently checked by vertex links and surface Euler characteristic; no unbounded extrapolation is claimed.

## Originality — PASS
Comparisons were by object, metric, threshold, homotopy conclusion and implication. Full primary text covers only Platonic 1-skeletons and explicitly proposes Archimedean generalizations. Closest published Euclidean cuboctahedron has 12 vertices; graph-metric truncated tetrahedron and truncated cube are different 1-skeletons. Targeted published-finding corpus and web queries for the 24-vertex rhombicuboctahedral graph-square Rips collapse found no equivalent theorem. Indexed search is not a guarantee of novelty, and specific residual literature risks are recorded.

The closest full published material read is *Vietoris–Rips complexes of Platonic solids* (arXiv:2302.14388), which discusses Archimedean solids as a future generalization. The published Euclidean cuboctahedron record (`2026/10/4/SCOPE-complete-vietoris-rips-filtration-of-the-euclidean-cuboctahedron--c10ad684de7e`) is a different 12-vertex metric object. The truncated tetrahedron and truncated cube records concern different graphs and cannot directly imply this 24-vertex collapse. Adamaszek’s general graph-power stability and universality theorems (arXiv:1104.0433) were examined: the target has girth three and nonstable scale-one/scale-two homotopy, while the universality theorem constructs a different graph. Both closest Archimedean published RESULT.md files were inspected in full; they concern different graphs and scales. Residual risk: alternate terminology, unindexed articles, unpublished arguments, or implicit general graph-square principles may cover the result. Absence in searches is not itself proof of global priority.

## Value — PASS
The rhombicuboctahedron is a natural 24-vertex Archimedean solid specifically within the published question of extending polyhedral Rips calculations beyond Platonic solids. A graph-square flag complex of dimension four collapses to the actual embedded boundary 2-sphere via 252 explicit elementary steps, which is stronger than a Betti computation and makes the simple-homotopy mechanism reproducible. Its scale-one 17-cycle topology and scale-two 2-dimensional fundamental class exhibit a substantive finite metric-space topology transition, not an arbitrary minor slice.

## Scope and limitations
The 252 steps are one explicit collapse witness, not a minimum. The conclusion is graph shortest-path metric only for thresholds one and two, not Euclidean chord distance or any threshold beyond two. Full independent scientific audit has not occurred.

Same-model review: passed. Independent audit: not yet performed.
