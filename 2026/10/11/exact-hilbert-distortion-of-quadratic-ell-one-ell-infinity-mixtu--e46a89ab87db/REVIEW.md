# Same-model scientific review

## Correctness — PASS
The claimed norm is a norm for every positive parameter. For any positive definite Euclidean pullback matrix, averaging its quadratic form under signed coordinate permutations retains both norm-comparison bounds and reduces it to a scalar matrix, so an arbitrary change of basis cannot beat Euclidean coordinates. The upper Euclidean-sphere norm squared is the larger eigenvalue of a rank-two matrix, with trace \(1+nt\) and nonzero eigenvalue product \(t(n-1)\). The lower value follows from a mass-transfer majorization lemma and an interval derivative with exactly one interior maximum. Both bounds have explicit actual extremizers, yielding the exact multiplicative distortion. The asymptotic lower bound holds for every parameter and matches the explicit choice \(t=1/n\). A reproducible finite checker passed all cases, but the proof does not rely on sampling.

## Originality — PASS, with residual risk
The motivating 2022 paper studies exact Banach--Mazur distances to cubes for usual \(\ell_p\) norms. A 2015 paper studies **linear**, polyhedral \(\ell_1\)/\(\ell_\infty\) mixtures rather than this quadratic norm, and the 2020 cube--cross-polytope paper studies a max-norm/intersection-body family. The closest publicly indexed two-dimensional mixed-norm result is restricted to same-side exponents, not the opposite-side \(\ell_1\)/\(\ell_\infty\) pair, and cannot imply the quantified \(n\ge3\) formula or high-dimensional asymptotic. Search by object, eigenvalue, sparsity, and equivalent norm expression did not identify a covering published theorem. The full 2015 article was inaccessible; equivalently formulated older material remains a named bibliographic risk, and a failed search alone is not a novelty proof.

## Mathematical value — PASS
This is a natural quadratic interpolation between the two classical endpoint norms. The exact norm geometry has two genuinely different extremal mechanisms: a one-spike-plus-plateau eigenvector and a sparse, equal-support minimum with a complete support-transition law. Consequently, one can compute the *unrestricted* Euclidean Banach--Mazur profile in every real dimension and prove the sharp optimal asymptotic constant \(1/\sqrt2\), not merely an example or a numerical estimate. The statement is a complete family-level classification with a nontrivial dimensional optimization rather than an arbitrary isolated constant.

## Sources and limits
Sources: Zhang--Meng--Wu, arXiv:2207.05499v1 (full text); Gotoh--Uryasev, DOI 10.1007/s10107-015-0899-9 (abstract and defining excerpt only); Deza--Hiriart-Urruty--Pournin, arXiv:2011.05607 (full text); published two-dimensional quadratic mixed-norm distance result (full text). No claim about complex scalars, exact finite-dimensional best parameter, or independent review.

Same-model review: passed. Independent audit: not yet performed.
