# Scientific review: sharp all-prefix block-reshuffling risk

## Correctness — PASS

The result fixes a finite vector array, a uniform permutation of equal-size labeled blocks, a deterministic internal order, and a matched number of individual vector evaluations. Equation (1) is reconstructed from the finite-population covariance and the conditional law of the block immediately following the first \(q\) blocks. The bias term remains present for incomplete prefixes. The scalar quadratic form decomposes into the constant-across-blocks mode and the \(K-1\) block-contrast modes; its two-dimensional matrix (5) has the claimed top eigenvalue. The determinant calculation and strict convexity of \(\mathcal H(r)\) give a strict matrix inequality whenever \(0<r<b\). At \(r=0\), block-constant nonzero contrasts give equality. Exact rational exhaustive short-permutation checks and algebraic integer-parameter checks passed, but do not replace this proof.

## Originality — PASS (best-knowledge comparison, with residual risk)

The 2026 source gives the block-level and individual-level sampling formulas, not a per-individual-budget spectrum over *all* prefixes; its calculations are building blocks for the complete-block case. The 2020 source gives the standard finite-population lemma and does not analyze fixed-order block permutations. Classical whole-cluster sampling already covers the general phenomenon of design-effect inflation at complete blocks; that part is excluded from the novelty assertion. The additional result is a closed, attained sharp comparison for every incomplete prefix and its exact order bias, with a rigorous strict global-envelope gap. No equivalent exact partial-prefix statement was identified in the searches and inspected materials. Earlier survey-sampling analyses of partially observed clusters remain a substantive bibliographic overlap risk.

## Value — PASS

Block reshuffling is proposed as a way to improve gradient-prefix variance constants, but actual epoch prefixes consume individual gradients. The exact per-sample profile distinguishes the full-block and partial-block regimes, quantifies the maximum variance amplification (which can grow approximately linearly with block size), and provides a sharp grouping criterion for improvement at block boundaries. The nontrivial arbitrary-prefix classification, rather than the basic variance-decomposition identity, is the mathematically useful contribution. It is a reusable, dimension-free benchmark for evaluating structured shuffles, not a claim of improved convergence or runtime.

## Sources and limitations

- Nguyen, Phan, Kalagnanam (2026), arXiv:2604.00260v1: Sections 2.2, 3.1 and Appendix A.1--A.3 materially compared.
- Mishchenko, Khaled, Richtárik (2020), arXiv:2006.05988: Section 7 and methodological context materially compared.
- Classical cluster sampling design effects: verified as a closely related full-block precedent, not as a source for an exact partial-prefix theorem.

The result assumes uniform block permutation, equal-size blocks, fixed internal order and a fixed deterministic vector array. It does not prove algorithmic convergence. Bibliographic originality remains subject to independent literature review.

Self-review: passed. Independent audit: not yet performed.
