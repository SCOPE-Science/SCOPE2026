# Scientific review

## Correctness: PASS

The stationary Poisson-reset process has an exact positive normalized renewal resolvent. On the positive half-line its Fokker--Planck equation reduces, after an exact ground-state transform, to \(\psi''=Q\psi\). The explicit \(Q\), \(Q'\), and \(Q''\) expansions show a positive asymptotic spectral gap and an integrable Liouville--Green error; nonintegrability rules out the growing solution. The resulting **multiplicative** WKB asymptotic yields an integrable correction below \(\alpha=1/2\), an exact logarithmic coefficient at equality, and an \(x^{2\alpha-1}\) correction above it. Every quantifier fixes \(D,r,\lambda,\alpha\) before \(x\to\infty\). A standalone Riccati/eikonal diagnostic reports 106 passing finite assertions, but the infinite-distance claim is grounded in the analytical proof, not extrapolation from numerics.

## Originality: PASS (qualified)

The nearest **same potential** literature is Defaveri--Barkai--Kessler (arXiv:2309.13126), which studies nonreset long-time relaxation and an equilibrium Boltzmann profile; this does not imply the stationary *Poisson-resolvent* tail coefficient or the exponent-\(1/2\) threshold. Capała--Dybiec (arXiv:2305.14832) considers the same power-well/reset ingredients but only first-passage escape with an absorbing boundary. Pal (arXiv:1408.1230) supplies the older arbitrary-potential framework, not a verified statement of the three-way subleading asymptotic. Singh--Metzler--Sandev treat the marginal linear trap. The later 2026 de Mauro--Majumdar--Schehr paper covers a resetting gas and leading extreme-value scaling, not the asserted subleading stationary tail. The residual possibility of a more general published resolvent-asymptotic theorem covering this special model is a real priority risk; Pal's full text was unavailable in this review.

## Mathematical value: PASS

The exponent \(1/2\) is not an arbitrary chosen parameter: it is precisely the integrability threshold for the **squared confining force** after the universal reset exponential and half-Boltzmann factor are removed. It distinguishes a finite normalized tail amplitude from a nontrivial algebraic correction and a second stretched-exponential suppression. The crossover affects rare excursions and finite-size tail approximations under soft confinement, and makes the usually neglected squared-force term quantitatively consequential. It is a structural boundary in a physically motivated weak-potential family, rather than a recomputation of a known exact table.

## Limitations and priority risks

The result is for fixed positive reset rate, one dimension, smooth sublinear power wells, and far-distance stationary tails only. It makes no uniform claim near \(\alpha=1/2\) or as the reset rate tends to zero. The review is based on literature comparisons and direct mathematical verification of the submitted proof, not an independent external assessment.

Self-review: passed. Independent audit: not yet performed.
