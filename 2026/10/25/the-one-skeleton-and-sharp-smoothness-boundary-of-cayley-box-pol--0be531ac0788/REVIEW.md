# Review of the Cayley box polytope graph and smoothness classification

## Correctness — PASS
The result applies to a nonnegative no-zero-row matrix and explicitly uses the standard lattice for smoothness. An integral shear of every vertex cone produces independent orthant rays plus the homogenized box-Cayley cone over the remaining base columns. Its ray count establishes the cross-layer adjacency criterion, exact degrees and edge totals. The inequalities \(2^r-1\geq r\) and the no-zero-row hypothesis then give an if-and-only-if simplicity criterion. The remaining primitive rays form one-dimensional blocks or blocks with determinant equal to a singleton coefficient, proving the if-and-only-if smoothness criterion. The simplex–cube combinatorial type follows from removing and restoring strictly positive full-support rows. Exact standard-library tests reproduce the graph and determinant properties for 1686 matrices. The proof, not finite enumeration, covers every dimension.

## Originality — PASS under inspected literature
The closest source is Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513v1. Proposition 2.1 already gives the vertices; Proposition 2.3 shows smoothness when the matrix is strictly positive. Neither provides the graph across degenerate layers or the necessary-and-sufficient criterion when zeros occur. Curtis–Le–Lowen, *On Smooth Combinatorial Products of Simplices*, arXiv:2609.25181, give a broader Cayley-tower and Nakajima structure theory, but do not state the support-pattern graph or exact smoothness equivalence for this matrix family. Tsuchiya, arXiv:1804.10538, treats Cayley-sum IDP, not vertex degrees or Delzant cones. Targeted semantic research-record and literature queries found no stronger covering claim. Residual risk: an equivalent older formulation may exist in toric/chimney terminology; a negative search is not a priority proof.

## Mathematical value — PASS
The new classification resolves a natural missing boundary in a 2026 construction used to disprove longstanding Ehrhart conjectures. It computes the entire graph uniformly over matrix magnitudes, identifies every nonsimple layer, proves that every simple member is a simplex–cube combinatorial product, and distinguishes that property from the arithmetic obstruction to smoothness. The motivating matrix \(A_{\alpha,\beta}\) has exactly \(2d\) nonsimple vertices of degree \(2^{d-1}+2d-1\) amid \(2^d\) simple vertices, a sharp and structurally informative consequence rather than an arbitrary finite slice.

## Limits
No analogous statement is asserted for signed, non-box, or arbitrary Nakajima data. The checker validates a finite sample and the source-family symbolic identities; it is not a machine proof of universal quantifiers. Originality is conditional on inspected sources and remains open to independent historical verification.

Self-review: passed. Independent audit: not yet performed.
