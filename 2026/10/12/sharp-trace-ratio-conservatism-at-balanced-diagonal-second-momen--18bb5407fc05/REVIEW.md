# Scientific review

## Correctness — PASS

Under the exact frozen-moment relation \(s_i=c p_i^2\), direct cancellation gives the arithmetic mean \(q=A\), and the stated feedback equation has precisely this balance as its fixed-point condition. The strict weighted Chebyshev comparison gives \(T\le A\). For the sharp upper bound, the objective \(\mathbb E[p]\,\mathbb E[p^{-2}]/\mathbb E[p^{-1}]\) attains a maximum over probability distributions on the spectral interval. Its first variation has an extremality function with strictly increasing derivative numerator, forcing support on interval endpoints. Exact one-variable differentiation yields the unique endpoint frequency and bound. Integer-square condition numbers give finite equality examples; rational proportions approximate the optimum for every other condition number. Exact-rational tests corroborate, but do not replace, those continuous arguments.

## Originality — PASS, with residual risks

The closest source is Yu--Chen--Feng, arXiv:2605.12878v1, Lemma 2.2 and Appendix C: its weighted Chebyshev proof covers \(q\ge T\), not the three-moment sharp upper bound on \(q/T\) under equilibrium second moments or the extremizing endpoint frequencies. Yu--Chen--Xu, arXiv:2604.08742v1, develops deterministic preconditioner analysis, but not the stochastic surrogate. Classical Lehmer-mean monotonicity recovers the lower inequality only; classical Kantorovich estimates concern the different product of first and inverse moments. No covering formulation appeared in the checked published mathematical records. A specialized generalized-mean inequality or unindexed equivalent argument remains a possible overlap; this review does not establish universal priority.

## Value — PASS

The bound answers a natural quantitative question left by the source's computable sufficient learning-rate surrogate. Perfect coordinate alignment and even exact frozen feedback balance do not prevent near-condition-number loss: the sharp ratio grows as \(\kappa-2\sqrt\kappa+O(1)\). It identifies both the spectrum and multiplicity pattern causing maximum conservatism, providing a concrete diagnostic boundary for choosing a trace-based certificate. It is not presented as a new algorithm, general convergence theorem, or performance guarantee.

## Scientific limitations

The idealized unsmoothed, frozen-moment setting differs from dynamically changing moments and positive numerical regularization. The sharp constant is dimension-free; finite dimensions with other endpoint proportions may have smaller optima. Generalized-mean literature may contain equivalent special cases, and no independent validation has been carried out.

Self-review: passed. Independent audit: not yet performed.
