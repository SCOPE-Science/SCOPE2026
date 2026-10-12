# Scientific review

## Correctness — PASS

The proof uses exact determinant and rank-one residual identities to reduce the conditional estimator error to \(Z(\chi_1^2-1)\). Its unconditional risk is then computed from an absolutely convergent Fourier series and Parseval's identity. The strict ideal-preconditioning comparison uses \(\operatorname{tr}\widehat A\le a\), including equality conditions. The asymptotic coefficient follows from a Cauchy-variable representation and dominated convergence with explicitly evaluated integrals. The included verification program independently compares formulas against angular quadrature, direct matrix reconstruction, exact two-step Lanczos and four high-contrast scales. Its finite experiments are corroboration, not an infinite proof.

## Originality — PASS, with a specified residual literature risk

Cortinovis–Toni, arXiv:2601.05778 (2026), is the most directly relevant antecedent. Its conditional Gaussian trace-variance principle and Nyström construction are credited; its published Nyström theorem provides general bounds under an oversampling condition and does not give a closed two-dimensional unconditional variance or the square-root spectral-gap coefficient. Saibaba–Alexanderian–Ipsen (2017), Theorem 7, instead bounds a compressed log-determinant estimator based on subspace iteration. Persson–Kressner (2023) analyze approximation of matrix functions and do not establish this preconditioned independent-probe risk. The source-comparison record distinguishes source formulas that can be specialized from the further nontrivial integration and asymptotic conclusion. No equivalent result was returned by targeted mathematical-finding and literature searches. This does not prove exhaustive uniqueness; an older angular-moment formulation could be equivalent.

## Value — PASS

A new low-rank-preconditioned stochastic log-determinant method raises a natural quantitative question about the extra variance from random preconditioner construction. The exact natural minimal benchmark identifies a previously unquantified spectral-gap mechanism: exceptional Gaussian sketch directions make the excess decrease as only the inverse square root of contrast. The result is an attained exact risk characterization for all positive two-eigenvalue inputs, not an arbitrary coefficient fit; it supplies a precise calibration against ideal spectral preconditioning. The result does not claim general-dimensional performance or a computational speedup.

## Boundaries and sources

The two-dimensional exact-arithmetic assumptions, independent standard Gaussian vectors, identity regularization and fixed-small-eigenvalue limit are essential. Relevant sources are Cortinovis–Toni (arXiv:2601.05778, Section 3); Saibaba–Alexanderian–Ipsen (arXiv:1605.04893, Theorem 7); and Persson–Kressner (arXiv:2209.11023). Higher-dimensional transfer remains open within this statement.

Self-review: passed. Independent audit: not yet performed.
