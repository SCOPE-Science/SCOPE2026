# Same-model review

## Correctness
PASS. The proof separates the infinite-looking endomorphism condition from the finite low-order classification. A fixed-simplex-free simplicial endomorphism of a sphere triangulation has a fixed-point-free realization; Lefschetz then forces degree \(-1\). A nonzero-degree simplicial self-map of the same closed triangulated surface must permute the triangles and hence is a simplicial automorphism. The sphere triangulations on four, five, and six vertices are classified from \(e=3v-6\) and the vertex-degree sum, after which explicit bad automorphisms rule out the tetrahedral boundary, triangular bipyramid, and octahedral boundary. The remaining six-vertex type has a four-element automorphism group, and each automorphism fixes a simplex. The standalone checker independently confirms all \(6{,}658\) simplicial self-maps of that complex have an invariant simplex.

## Originality
PASS with residual literature risk. The closest primary source is Barmak's 2013 paper, which explicitly states existence of fixed-simplex triangulations of \(\mathbb S^n\) for \(n\ge2\) after subdivision but gives no minimum vertex count for \(\mathbb S^2\). Idzik–Zapart treat retractable complexes, which does not subsume a sphere triangulation. Baclawski–Björner's finite poset model of \(\mathbb S^2\) concerns the order-theoretic fixed point property rather than this simplicial minimum problem. Exact-phrase and implication searches in the checked published-finding index and web literature did not produce the six-vertex cutoff or its uniqueness statement. An unindexed older appearance remains possible.

## Value
PASS. The minimum size is a natural complexity invariant for Barmak's existence phenomenon: dimension two is the first sphere dimension in which that construction applies, and the result closes the onset question exactly. The uniqueness of the minimum model and the explicit contrasting octahedral failure make the result a small but reusable benchmark for fixed-simplex algorithms and constructions.

## Closest literature and limitations
The closest statement is Barmak's existence theorem for fixed-simplex triangulations of spheres. The present result is narrower in dimension but strictly sharper in combinatorial size. It does not address larger triangulations or higher-dimensional minima. The finite checker certifies only the displayed low-order complexes and is not used as evidence for any unbounded classification.

Same-model review: passed. Independent audit: not yet performed.
