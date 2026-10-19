# Scientific review

## Correctness — PASS
The claimed rank formula is proven for all subsets, not inferred from sampling a few erasures. Exact algebra over \(\mathbb Q(\sqrt5)\) gives an odd interpolation determinant of \(1024\), a nonzero six-by-six even interpolation minor of \(32\), the Petersen adjacency relation and its \((-2)\)-eigenspace projector, and a centered unsigned-incidence Gram identity. The incidence-rank lemma then proves the all-erasure formula; an exact checker independently verifies every one of the 1024 possible touched-pair sets and all 4845 four-point erasures. Risk: the theorem applies only to the specified normalized vertex geometry and degree bound.

## Originality — PASS, with residual risk
The closest general interpolation paper by zu Castell, Laín Fernández and Xu (arXiv:math/0407448v1) constructs poised spherical node sets through factorization, without determining the fixed dodecahedron's deletion matroid. Dette, Melas and Pepelyshev (arXiv:math/0603075v1) study optimal spherical-harmonic design and discrete quadrature; their statements do not produce exact dodecahedral deletion ranks. Dell’Accio and collaborators (arXiv:2605.13124v1) analyze antipodal parity splitting and rank-guided interpolation subset selection, but not the precise \(K_5\)-incidence characterization or the 2960 count. An equivalent older Petersen eigenspace-matroid computation, or an unindexed dodecahedral interpolation table, remains a residual originality risk.

## Mathematical value — PASS
This classifies the complete reconstruction matroid of a canonical twenty-site cubic spherical-harmonic grid through a five-vertex graph, rather than merely displaying a feasible interpolation set or checking one determinant. The 2960 exact robust four-erasure patterns and the two explicit forbidden graphic types expose nonobvious combinatorial structure, permitting instant symbolic decisions about any of the million-plus erasure subsets.

## Limits and status
Computational evidence uses exact arithmetic and is not needed as a surrogate for a missing proof. No numerical stability or perturbed-coordinate theorem is claimed. Independent specialist validation and literature audit remain to be performed.

Self-review: passed. Independent audit: not yet performed.
