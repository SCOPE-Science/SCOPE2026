# Scientific review

## Correctness

**PASS.** For all integer \(p,q\ge2\) and \(a,b\ge1\), group averaging is feasible and cannot increase the centered spectral norm. The three edge-orbit probabilities have exactly two independent row-sum constraints, producing one parameter. A full four-class eigenvalue decomposition, with exact multiplicities, proves the stated SLEM formula. Two affine intersections and the interval caps give all four closed-form regimes, including equality boundaries and strict uniqueness within the symmetry-invariant family. The separate standard-library rational checker builds transition matrices and checks eigenvector identities; its 576,512 successful assertions corroborate but do not replace the all-parameter proof.

## Originality

**PASS on checked evidence, with residual historical risk.** Boyd–Diaconis–Xiao (2004) provide the general fastest-mixing convex framework with holding allowed. Boyd–Diaconis–Parrilo–Xiao (2007), Section 5.3.2, give the general complete-multipartite representation and block reduction, but do not solve the present loopless two-size problem or state its four phases. Jafarizadeh (2010) addresses equal-sized neighboring-layer multipartite networks, not the complete multipartite graph here. Related results for zero-holding cyclic prisms and three-class chains with holding do not imply the present family. The novelty is the explicit all-parameter loopless solution and its two sharp support-deletion thresholds, **not** the already-known group-averaging or multipartite block-diagonalization methods. Unindexed or inaccessible prior studies may have equivalent formulas.

## Value

**PASS.** Zero holding is a natural constraint when an update must move at each step. The result replaces a general convex spectral optimization with an explicit allocation for every two-size multipartite instance with both multiplicities at least two. Its sharp edge-support transitions at \(pa=b\) and \(a=qb\), its switch in the active spectral obstruction at \(a=b\), and its exact balance-optimal mixing value are structural information rather than a numerical fit or an isolated small case. The scale-invariant optimum permits immediate transfer across network blow-ups.

## Scope and risk

Zero probabilities on allowable edges are permitted, and the outer-phase optima may not be attainable with strictly positive edge constraints. The theorem does not optimize nonreversible walks or assert that every global optimizer is symmetry-invariant. Broad-spectrum uniqueness and all historical priority claims are deliberately not made. A separate independent mathematical validation has not been completed.

Self-review: passed. Independent audit: not yet performed.
