# Review of rank-one positivity defect

## Correctness — PASS

The proof reconstructs the exact rank-two compression of the Moore–Penrose inverse, diagonalizes the Hermitian rank-two Jordan expression, checks the orthogonal and coincident endpoints separately, and optimizes the entire overlap interval by a single strictly increasing cubic. A direct exact real symmetric witness and the sharp translation-covariant positivity threshold are included. The standalone SymPy/NumPy checker passed exact symbolic identities and 900 deterministic random tests; the theorem itself follows from analytic algebra, not those finite samples.

## Originality — PASS

Jiao–Luo–Wu, arXiv:2610.21445v1, Section 3, introduces the identical operation and proves permutation symmetry and trace-class norm bounds, not its complete rank-one eigenvalues or sharp cone regularization. Nakagawa's arXiv:2602.14007v2 defines a different Riemannian metric median. Bounded published research comparisons on rank-one positivity, mixing maps and an exact threshold returned Schur truncations, crossed-Heinz maps and other distinct constructions; their statements do not entail this formula. Possible earlier Jordan-product simplifications and incompletely indexed matrix-mean literature remain priority risks.

## Mathematical value — PASS

A recent trace-class mixing construction is evaluated against the essential positive-matrix cone. The result establishes not only an explicit positive-definite failure but the exact universal boundary where scalar regularization restores cone preservation for all rank-one projection triples, independently of dimension. It is a natural complete spectral classification for an important input family, not a purported classification for unrestricted matrices.

## Limitations

The optimal threshold applies to equal-amplitude rank-one projections, not general positive matrices. Independent historical priority and scientific audit remain open.

Self-review: passed. Independent audit: not yet performed.
