# Scientific review: D-optimal parallel-path shortcut

## Correctness — PASS
The finite simple-graph Laplacian map is injective in individual edge weights, hence the log determinant is strictly concave wherever the graph stays connected. A direct weighted spanning-tree enumeration is symmetric under intra-path edge permutations, forcing the unique optimizer to equalize each path. The resulting strictly concave budget problem has explicitly solved KKT equations, including the boundary derivative. The sum \(S=\sum_i(\ell_i+1)^{-1}\) is exactly the boundary KKT test; at equality the two formula branches agree. Exact-rational determinant tests, permutation invariance, and full-dimensional numerical optimizations provide standalone finite checks, not an infinite proof.

## Originality — PASS with stated residual risk
The closest inspected primary research is Cheng's 1981 D-optimality connection, Boyd's 2006 convex graph-Laplacian framework, and Khosoussi et al.'s original 2016 weighted tree-connectivity and edge-selection study. Those works respectively optimize discrete graph topology, describe general spectral convex optimization, and develop selection/relaxation methods with fixed base weights. None of the materially inspected statements gives the present unique unrestricted edge-by-edge allocation on arbitrary parallel-path networks or the reciprocal-path-length deletion law. Broader general optimization frameworks do encompass the problem but do not analytically settle the specified support. An equivalent formula in specialized network-design or design-theory literature remains possible.

## Value — PASS
This is a natural exact D-optimal network-design question: with a fixed budget, should a physically available one-edge shortcut be funded or discarded? The answer is a sharp, parameter-free combinatorial threshold involving only path lengths. It applies to any finite number of unequal-length parallel routes, classifies a nontrivial support phase change, and identifies the unique optimal conductance on every individual edge. Unlike a single computed example, the law directly identifies which infrastructure edge receives no resources for whole families of networks.

## Scientific limits
Unit cost per conductance on each edge, no cross-links, no edge caps, and just one direct terminal shortcut are essential. Numerical checks are finite; the theorem is analytic. Specialized older coverage is not excluded categorically.

Self-review: passed. Independent audit: not yet performed.
