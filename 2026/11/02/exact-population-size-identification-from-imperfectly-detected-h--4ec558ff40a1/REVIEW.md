# Scientific review: exact population-size identification from imperfectly detected herding dynamics

## Correctness — PASS

The finite irreducible birth–death chain has exact drift \(Na-(a+b)k\), giving stationary mean \(Nr\) and positive-lag covariance \(V e^{-(a+b)t}\). The second-moment generator gives \(V=Nr(1-r)(A+Nh)/(A+h)\). Fresh binomial detection rescales cross-lag covariance by \(p^2\) and contributes \(m(1-p)\) only to same-time variance. Consequently the two positive lags identify \(A\) and \(s=p^2V\), and the same-time variance identifies \(p\). Reconstructing positive \(a,b,h\) for each integer \(N\) is equivalent to the strict inequalities \(L<N<U\). Both directions of the equivalence are proved in RESULT.md; finite checks only corroborate it. The standalone check.py separately evaluates 1,100 exact stationary detailed-balance laws and two boundary examples. The result is an exact-moment theorem, not finite-sample statistical consistency.

## Originality — PASS within material inspected; historical priority remains provisional

Kirman (1993) introduced the recruitment model; Moran et al. (2020) and Holehouse–Moran (2022) supply stationary-law and relaxation machinery. Carro–Toral–San Miguel (2016) analyze noisy-voter correlations. Royle (2004), Dennis–Morgan–Ridout (2015), and the published closed binomial N-mixture identifiability result address related detection/abundance questions, but different latent dynamics or information classes. The present precise claim is the complete integer inverse fiber of four stationary mean/variance/two-lag covariance summaries under unknown freshly redrawn detection, including singleton, bounded and unbounded fibers. Those features were not established in inspected material. The original 1993 technical full text was not accessible, and wider detection/inference literature could contain a stronger theorem; failed searches do not establish universal novelty.

## Value — PASS

Unknown detection, unknown group size, and imitation confound behavioral recruitment inference. An exact open integer interval provides a rigorous feasibility diagnostic, a precise possible-identification case (a singleton) and a nonidentifiability boundary (unboundedly many compatible group sizes). It also proves the intrinsic inability of *any number* of additional second-order lags to resolve this ambiguity, motivating designs that collect higher-order or intervention information. Its scope is a natural calibrated observational problem rather than an arbitrary algebraic restriction.

## Limitations and closest work

All parameter rates must be strictly positive, the latent process stationary, and binomial indicators independently redrawn at each census. The result identifies population size only if its open interval contains a single integer. There is no estimate of robustness under measurement noise. Sources: https://doi.org/10.2307/2118498; https://arxiv.org/abs/2004.06667; https://arxiv.org/abs/2201.09573; https://doi.org/10.1038/srep24775; https://doi.org/10.1111/j.0006-341X.2004.00142.x; https://doi.org/10.1111/biom.12246.

Self-review: passed. Independent audit: not yet performed.
