# Scientific review of terminal reshuffling phase classification

## Correctness

**PASS.** Every component is a positive quadratic with the same Hessian. Its projection on an eigenvector evolves by an affine recursion with scalar multiplier \(q=1-\eta\lambda\). The RR and IID epoch noises are centered and independent between epochs; their second moments differ by precisely the finite-population cross-covariance \(-v/(n-1)\). The proof reconstructs both models' complete epoch-end second moments and cancels the identical deterministic initial-error contribution. The exact geometric factorization of \(A_n(q)^2-B_n(q)\) has sign \(q\) for every \(-1<q<1\). Pure-eigenmode center choices certify both directions of both data-uniform iff statements. The independent checker exhaustively enumerated 123 exact-rational cases, including negative multipliers and repeated epochs. Numerical or finite checks are not substituted for the symbolic argument.

## Originality

**PASS, subject to residual access and indexing risks.** Liu (2026, Theorem 1, Algorithm 1) compares a weighted average of within-epoch iterates through rate upper bounds, not the pointwise expected final objective on identical data. Ying (2018, Chapter 3, Lemma 3.1) explicitly obtains the covariance polynomial for **nonnegative** weights; this known identity is fully credited and is not offered as original. Its nonnegative-multiplier statement cannot establish the reversed ordering when \(-1<q<0\). The novelty assessed here is the exact finite-horizon signed spectral comparison, the sharp \(\eta\lambda=1\) transition, and the iff/mixed ordering classification. De Sa (2020, Section 2) establishes a different high-dimensional noncommuting matrix-product failure, not the present common-Hessian classification. Dewasurendra (Sections 1 and 5) studies an average and a small-step minimax bound, not terminal reversal. An equivalent unpublished or unindexed signed-weight argument remains a live risk, and no claim of global literature uniqueness or independent external validation is made.

## Value

**PASS.** The 2026 averaged-output superiority statement is susceptible to overgeneralization into terminal-iterate superiority. A sharp explicit two-sample counterexample and a complete spectrum-dependent phase classification show exactly why output selection and overshooting each curvature matter. The theorem supplies actionable, fully quantified guidance for terminal checkpoints of stochastic component descent: the scalar reciprocal-curvature threshold is independent of horizon and sample count, while mixed spectra forbid a universal winner without center-variance information. This is a motivated boundary, not a numerical micro-improvement or arbitrary parameter slice.

## Closest literature and scientific limits

The central precursors are Liu (arXiv:2606.32005; extended September 2026 full text), Ying (2018 dissertation, weighted covariance lemma), De Sa (NeurIPS 2020 counterexample), and Dewasurendra (all-inner average minimax analysis). The result assumes a shared positive Hessian, independent new permutations, uniform sampling, constant stable step, and complete epoch terminal outputs. The proof does not generalize to nonlinear components, varying Hessians, nonuniform sampling, or pathwise ordering. The 2018 nonnegative-weight covariance expression largely overlaps the elementary variance computation; the scientific distinction resides in the signed regime and the exact sample-uniform iff statement.

Self-review: passed. Independent audit: not yet performed.
