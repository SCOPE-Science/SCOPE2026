# Same-model review

## Correctness
PASS. The proof starts from the published edge-segment realization and acyclic-orientation vertex model. The symmetry center is half the degree vector. At an orientation vertex, the centered coordinate is half of indegree minus outdegree, so the squared norm is a fixed degree-square term minus the number of directed two-edge paths. In a complete multipartite graph, triples from three distinct parts contribute a fixed amount; the only variable contribution comes from a singleton vertex interleaving two vertices of one part. Hence the maximum occurs exactly when all parts are contiguous blocks, equivalently when every pair of parts is uniformly oriented. The exact cubic-moment formula follows by elementary symmetric-polynomial simplification. Central symmetry proves both uniqueness of the circumcenter and the diameter formula.

## Originality
PASS. The exact graphical-zonotope source and the highly relevant shuffle/join source were inspected in full. They supply the standard realization, acyclic-orientation vertices, and the complete-multipartite join construction, but no Euclidean circumradius or diameter statement. Direct published-result and literature searches under graphical-zonotope, complete-multipartite, acyclic-orientation imbalance, farthest-vertex, and complete-bipartite formulations found no covering theorem. Own current and prior ledgers contain graphical-zonotope inradius results but no complete-multipartite circumradius result.

## Value
PASS. Complete multipartite graphical zonotopes are a canonical iterated-join family in recent generalized-permutahedron work. The result computes their exact circumspheres for arbitrary part sizes and identifies all extremal acyclic orientations. The formula
\[
R^2=\frac{N^3-\sum_i n_i^3}{12}
\]
shows that the entire outer Euclidean size is encoded by the cubic moment of the part-size distribution, while the equality class has the transparent interpretation of total orders on the parts.

## Closest literature and limitations
The closest literature gives complete combinatorial and deformation descriptions but does not optimize Euclidean orientation norms. The own weighted graphical-zonotope result concerns inradius and cut expansion, a different metric problem. A residual risk remains for an equivalent theorem in orientation-imbalance terminology. The claim is restricted to unweighted complete multipartite graphical zonotopes.

Same-model review: passed. Independent audit: not yet performed.
