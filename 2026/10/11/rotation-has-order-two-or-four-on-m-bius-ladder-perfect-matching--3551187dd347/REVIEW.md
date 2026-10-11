# Scientific review: cyclic rotation on perfect-matching homology

## Correctness — PASS
The claim specifies the even graph parameter, graph-edge and simplicial-complex conventions, homology coefficients, and action. Agarwal and Basak's Theorem 21 proves the required concentration of rational reduced homology in one two-dimensional group. The proof classifies every rotation-fixed simplex by all permutation orbits of graph edges, including the empty augmented simplex, and computes orientation signs directly. The finite-order and unit-circle argument turns the two traces into the claimed operator identity, including both congruence classes. The standalone program verifies complete fixed-face lists for four even parameters and exact mod-two homology for three of them, without treating that finite evidence as the infinite proof.

## Originality — PASS, qualified
The closest source, Agarwal and Basak (arXiv:2608.30601, full relevant section read), gives the underlying wedge-of-two-spheres homotopy type but not the induced automorphism action. Li (arXiv:2202.08828, introduction, theorem and equivariance argument read) concerns graded matching permutation modules and equivariant log-concavity, not reduced homology of perfect-matching-generated complexes. Bate and coauthors (arXiv:2312.13750, introductory theorem setting read) treat representations for different matching complexes of complete hypergraphs. Searches for rotation traces, equivariant formulations, and equivalent eigenspace decompositions yielded no identified prior implication. No search proves uniqueness: unindexed and unpublished analyses remain possible.

## Value — PASS
The graph family was recently classified nonequivariantly, but that two-sphere wedge alone cannot resolve the natural cyclic symmetry action. The exact rational representation for every even parameter shows that a geometric rotation of order increasing with the graph size acts on top homology with bounded exact order two or four, changing at the intrinsic congruence boundary. This is a natural topological invariant of the symmetry, not a renamed dimension count. It does not solve integral or full equivariant topology.

Same-model review: passed. Independent audit: not yet performed.
