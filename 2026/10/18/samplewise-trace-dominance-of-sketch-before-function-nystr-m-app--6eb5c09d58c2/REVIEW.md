# Self-review

## Correctness — PASS

The claim has explicit quantifiers: arbitrary real finite positive-semidefinite input, arbitrary sketch including rank deficiencies, nonzero continuous operator-monotone \(f\) with \(f(0)=0\), the exact same sketch, and untruncated Nyström. The proof reconstructs (i) Nyström as an orthogonal projection sandwiched by the square root, (ii) the operator Jensen compression step, and (iii) the novel monotone projector-homotopy derivative. The derivative is a nonnegative pairwise covariance sum because both \(f(\lambda)\) and \((\lambda/f(\lambda)-1)/(1-t+t\lambda/f(\lambda))\) preserve eigenvalue order. Zero eigenvalues are removed by a common-support reduction. Each error residual is positive semidefinite, making nuclear norm exactly trace. The exact two-dimensional witness verifies strict trace ordering without Löwner ordering. The verifier completed 38,400 finite consistency checks, but the infinite theorem rests on the analytic argument, not sampling.

## Originality — PASS, with residual priority risk

The original funNyström paper (Persson–Kressner, arXiv:2209.11023, §§3–5) establishes probabilistic guarantees and reports numerical comparisons between processing before/after the function. Section 4.3 observes no worse error in its tests, but does not give a samplewise all-rank nuclear comparison. The algorithm-agnostic extension (Persson–Meyer–Musco, arXiv:2311.14023, Theorem 1.1 and §2) transfers near-optimal low-rank error bounds, not pairwise ordering of two coupled Nyström algorithms. The 2024 doctoral treatment contains the same broad transfer and numerical comparison themes. Relevant published research comparisons did not show an equivalent universal same-sketch trace theorem, and previously recorded planar asymptotic examples do not logically imply this all-ranks statement. Residual risk: the monotone reweighting lemma may be known under a different matrix-analysis formulation; novelty has not been independently certified.

## Value — PASS

The theorem resolves a concrete, published practical comparison in the nuclear-error metric: for a common sketch, computing the matrix function after Nyström cannot be worse than directly Nyström-sketching the matrix function, *for any sketch rank*. The result is deterministic, requires no oversampling or spectral assumptions, and simultaneously gives a useful methodological boundary: trace/nuclear order does not imply Löwner order or any claimed Frobenius/independent-sketch order. This is a general structural decision theorem, not a dimension-specific numeric recomputation.

Self-review: passed. Independent audit: not yet performed.
