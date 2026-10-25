# Review of the four-by-four Sudoku placement complex

## Correctness — PASS

The exact recurrence enumerates every subset of the sixteen cells and finds face vector \((16,64,64,16)\). The 32 specified free-face pairs, recomputed and checked against remaining strict cofaces, collapse the complex to a two-dimensional complex with vector \((16,48,32)\). Every edge has precisely two incident triangles; every vertex link is one cycle; the one-skeleton is connected; triangle orientations can be chosen consistently. A closed connected orientable surface of Euler characteristic zero is a torus. The integer homology, fundamental group, and cup-product conclusions follow from a strong deformation retract, not from matching homology ranks alone.

## Originality — PASS

Sander's fully inspected seven-page graph paper (2009, doi:10.37236/263) defines the same Sudoku graph but proves its spectral integrality, not a homotopy classification. Jones, Perkins and Roach (2012, doi:10.1155/2012/760310) count 288 complete Sudoku colorings, a different object. Goyal, Shukla and Singh (arXiv:1905.06926) prove a product-graph wedge-of-circles theorem for categorical products of two complete graphs; Sud(2) is a different four-factor NEPS. The published four-by-four rook independence complex is an ambient sphere wedge, and its type does not determine this proper subcomplex. Multiple exact-object, alias, and theorem-implication searches located no direct coverage. An unindexed equivalent theorem remains possible.

## Value — PASS

The first nontrivial Sudoku board produces a torus after elementary collapses of its single-symbol placement complex. This distinguishes the invariant from complete-coloring counts and from the ordinary chessboard complex; importantly the nonzero first-cohomology cup product rules out replacing it with a wedge of spheres. The result establishes a full integral homotopy type for a natural named graph without asserting an arbitrary generalization.

## Limits

The proof and checker concern only the sixteen-cell standard four-by-four Sudoku graph, and no full-grid colorings are represented by the complex's simplices. Independent validation has not been performed; unknown equivalent literature remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
