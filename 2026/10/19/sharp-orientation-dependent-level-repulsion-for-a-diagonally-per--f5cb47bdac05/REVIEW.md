# Scientific review

## Correctness — PASS

The exact random object is a two-dimensional compression of three independently uniform diagonal variables. Its squared eigenvalue separation is an explicit ellipse quadratic form; the transformed density is exactly the truncated range density, so ellipse area and first-absolute-moment integrals establish the probability polynomial without asymptotic heuristics. Boundary orientations reduce to a convolution of weighted uniforms, and the inverse-moment classification follows by layer cake. The Schur-complement argument establishes samplewise first-order transfer to the perturbed rank-one projector, with a uniform error bound. Symbolic and numerical scripts reproduce the algebra and sample checks; simulation does not establish the analytical continuum statements.

## Originality — PASS (self-review)

The closest methodological source is Kressner and Shao, *On a randomized small-block Lanczos method for large-scale null space computations*, arXiv:2407.04634 (originally July 5, 2024). Its Section 2.1, Proposition 3, and Theorem 4 treat eigenvalue repulsion under independent uniform diagonal perturbations; its finite-strength high-probability bound does not compute the orientation-dependent first-order CDF, exact cubic term, sharp local radius, or boundary inverse-moment threshold. The closest general spectral-statistics source inspected is Kumar and Ahmed, *New Spectral Statistics for Ensembles of 2x2 Real Symmetric Random Matrices*, Acta Polytechnica 57 (2017), Section 2, which computes spacing laws for two different unconstrained matrix-entry ensembles. Their polynomial-shaped local spacing law is acknowledged; the constrained 3x3 compression with arbitrary prescribed nullspace coordinates is not a corollary of their formulas.

Targeted mathematical-record queries used aliases for compressed diagonal disorder, degenerate eigenvalue splitting, null-space repulsion, and inverse-gap moments. No covering result was identified. That absence alone is not a uniqueness proof. Older exact random-compression treatments remain a novelty risk.

## Value — PASS

The classification resolves a concrete risk left implicit in randomized diagonal-perturbation null-space algorithms: near collision of the two formerly zero eigenvalues. It identifies a sharp geometry-dependent transition in small-gap likelihood and in the existence of expected inverse gaps, whose reciprocal appears in Krylov convergence estimates. This is a natural complete minimal case, not an arbitrary slice of a broader computation. The theorem does not claim a new high-dimensional convergence rate, practical solver runtime gain, or novelty for generic Wigner level repulsion itself.

## Limitations and literature

The probability polynomials apply to the perturbative first-order compression, not to an arbitrary finite perturbation. The results assume three real coordinates, a rank-one orthogonal projector, and independent uniform diagonal noise. Relevant primary sources: Kressner–Shao, arXiv:2407.04634, Theorem 4; Kumar–Ahmed, DOI:10.14311/AP.2017.57.0418, Section 2. No independent audit or full historical originality certification has been performed.

Self-review: passed. Independent audit: not yet performed.
