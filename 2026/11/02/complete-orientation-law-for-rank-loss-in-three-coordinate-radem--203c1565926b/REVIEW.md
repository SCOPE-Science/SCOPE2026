# Scientific review

## Correctness — PASS
The statement fixes the random object, all quantifiers, and the exact rangefinder output. The proof reduces each of the eight equally likely sign vectors to one of four equiprobable antipodal classes. The six projected-collinearity determinants are exactly the three pairs of signed coordinate equalities for a kernel normal. This gives four and only four admissible line-mass patterns, including the zero atom at a body diagonal. Inclusion–exclusion supplies the exact finite-width probabilities. The loss relation for row coisometries follows from \(\operatorname{tr}((I-P)AA^{\mathsf T})=2-\operatorname{rank}P\). No infinite-dimensional conclusion follows from the finite checks. The independently replayable integer verifier exhausts 372 finite normal-width cases, while the algebraic proof covers all nonzero real normals and all widths \(L\ge2\).

## Originality — PASS under accessible evidence
The recent motivating preprint (arXiv:2610.31333v1) specifically says in Remark 2.21 that discrete Rademacher projections may lose rank and points to general sub-Gaussian probability bounds, but its relevant theorems and numerical discussion do not state an exact kernel-orientation four-class law. Saibaba–Międlar (arXiv:2308.05814) provides general non-Gaussian bounds without this exact finite support classification. The standard Halko–Martinsson–Tropp Gaussian rangefinder result gives an almost-sure full-rank contrast, not this Rademacher formula. Searches of relevant published mathematical records for rank loss, Rademacher sketch geometry, three-coordinate kernels, and equivalent antipodal/projective formulations found no directly covering record. The formulas are an elementary consequence of projective cube support once the right quotient is chosen; residual historical-priority risk remains, especially from specialized small-sample discrete-sketch calculations.

## Mathematical value — PASS
This exhaustively solves the first input dimension in which rank-two subspace orientation can vary for an entrywise sign sketch. It supplies sharp exact success probabilities and attainable equal-singular-value counterexamples to a covariance/singular-value-only prediction of recovery. The exponential orientation spread under increasing oversampling is an operational quantitative distinction, rather than a trivial positivity check or an arbitrary parameter slice. The result is restricted to three input coordinates; no higher-dimensional sharp law is asserted.

## Remaining limitations
Exact arithmetic, iid fair signs, rank two, three input coordinates, and range projection are essential. General probabilistic sketch bounds are not contradicted. No conclusion about numerical conditioning, alternative output truncation, or generic matrix dimensions is claimed. Independent expert audit and complete historical-priority certification have not occurred.

Self-review: passed. Independent audit: not yet performed.
