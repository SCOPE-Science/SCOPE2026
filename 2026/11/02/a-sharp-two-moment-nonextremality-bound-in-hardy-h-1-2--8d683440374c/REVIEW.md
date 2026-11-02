# Scientific review: a sharp two-moment nonextremality bound

## Correctness: PASS

The exact two-term decomposition is algebraic. The Hardy \(H^{1/2}\) quasi-norm converts the two pieces into squared weighted means of \(\sqrt{1\pm X}\). An exact pairwise variance identity followed by Cauchy–Schwarz yields the \(1/4\) variance deficit. Maximizing the variance over phases yields the stated \(1/8\) first-two-moment coefficient. The sharpness sequence uses boundary Poisson mixtures and genuine nonzero outer functions; no atomic function is falsely regarded as an outer function. A standalone standard-library numerical checker provides finite consistency tests, not proof of the infinite claim. Constant-inner and degeneracy cases follow from the same identities.

## Originality: PASS under evidence examined

The closest inspected primary source is Brevig–Søvik, arXiv:2610.21788v1, Theorem 1 and Corollary 2, which gives the qualitative strictness for every \(0<p<1\) but no quantitative two-moment defect, phase optimization, or exact \(1/8\) envelope sharpness. De Leeuw–Rudin (1958), Section 2.2, supplies the ancestor decomposition for \(H^1\) but not the new moment inequality. The relevant published mathematical-record queries primarily retrieve harmonic Hardy coefficient stability and unrelated power-mean phenomena, not a dominating theorem. Classical reverse-Hölder/Hellinger inequalities can support the argument but a precise previously published all-hypotheses equivalent statement remains a residual risk; negative searches are not proof of novelty. The coefficient is claimed sharp only for the explicitly defined envelope.

## Value: PASS

The recent sharp outer-extremizer theorem motivates a numerical diagnostic for near-extremality. Here only two computable complex moments of the inner factor (with natural outer boundary weighting) suffice to control the entire dual defect. The sharp constant and the explicit concentration construction show the estimate is a substantive, exact stability law, not a small numerical improvement or an arbitrary finite slice. It gives a quantitative obstruction to nontrivial inner factors even without norm attainment.

## Limits and checks

This review has not independently audited the theorem. Its correctness depends on the explicit equality identities and limiting sharpness sequence as stated. It does not assert a sharp dual-functional constant nor treat \(p\ne1/2\). Highly relevant original works were inspected; broad historical overlap remains a research risk.

Self-review: passed. Independent audit: not yet performed.
