# Scientific review: Benford limits under heterogeneous cuts

## Correctness — PASS

The proof identifies the exact domain (fixed dimension, independent stationary-within-coordinate cuts, common finite logarithmic mean and positive variance, and integer-frequency nonresonance). An independent-coordinate multivariate CLT gives a rank gap of order \(\sqrt n\) in probability and uniform limiting winner labels. A final block of length \(\lfloor\sqrt n\rfloor\) has centered fluctuations smaller than the prefix rank gap with probability tending to one, while its integer-frequency Fourier character decays exponentially. The joint label–phase limit follows from Fourier uniqueness. The deterministic competing-face bound and the rank-gap divergence transfer it to total frame volume. Every boundary, including \(m=1\) and \(d=m\), is handled separately. The included verifier passed 8,063 exact finite subset-product comparisons. These tests do not prove the asymptotic statements; the full analytic argument does.

## Originality — PASS, with stated priority risk

Betti et al., arXiv:2304.08335v1, explicitly formulated the all-dimensional maximal-face conjecture but did not prove the general heterogeneous case. Importantly, Fang and Miller, arXiv:2508.12915v4, **already proved all-dimensional strong Benford behavior** under globally iid logarithmic cuts with all centered moments, bounded density and bounded density derivative. Their Section 3.1 identifies the non-identical-coordinate generalization as future work. The final theorem covers those prior smooth-iid cases, but its distinct contributions are the weak second-moment assumptions, heterogeneous coordinate cut distributions, and explicit joint independent winner-label/leading-digit limit; these are not consequences of the inspected earlier theorems. Searches of primary literature, equivalent order-statistic formulations, and an indexed published-results collection gave no dominating statement. These searches do not establish absolute novelty, and an unknown equivalent earlier mixing theorem is a residual risk.

## Value — PASS

This is a natural open problem of geometric probability and Benford behavior explicitly posed in the 2023 article and partially addressed in 2025. The weak assumptions permit non-smooth and coordinate-heterogeneous fragmentation mechanisms excluded by the strongest inspected theorem. Joint convergence identifies the law of the dominant face and its relation to the frame-volume digits, a more informative probabilistic invariant than either Benford marginal alone. The statement is not a rate, pathwise equidistribution, or a theorem under arbitrary dependencies.

Self-review: passed. Independent audit: not yet performed.
