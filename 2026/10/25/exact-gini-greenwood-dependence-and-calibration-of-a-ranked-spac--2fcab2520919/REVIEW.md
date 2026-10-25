# Scientific review: Gini–Greenwood mixed moments and ranked-spacings calibration

## Correctness — PASS

The domain is the uniform \(m\)-spacing simplex, \(m\ge2\), including the degenerate pair-sum boundary at \(m=2\). Marginal moments follow from Dirichlet polynomial identities, while the decisive cross moment follows from the Dirichlet two-coordinate split: \(\mathbb E[|X_1-X_2|Q_m]=(2m+5)/(m(m+1)(m+2))\). The exact ranked-discrepancy identity is algebraic; combining three checked variances/covariances yields its stated variance. Standard Hoeffding/de-normalization calculations yield the two influence functions and the Gaussian limit with variance \(37/12\). All 230 exact-rational checks pass from the included source code. The infinite proof is analytic, not an extrapolation from those computations.

## Originality — PASS, with stated risk

The closest primary source, Jammalamadaka–Goria (2004), already introduces the ranked-spacing test, identifies it as a Gini–Greenwood combination, and states its distribution requires dependence analysis (Section 3, equations (10)–(11)). Those are prior facts. Tung–Jammalamadaka (2012), Theorem 4, supplies a general central limit theorem, which covers the existence of an asymptotic law for suitable linear combinations; the generic asymptotic method is also prior. The claimed new part is the explicitly evaluated exact finite-sample mixed covariance (and correlation) and resulting exact finite-sample variance, together with an explicit limiting variance specialization. Searches for both statistics and their equivalent ranked/Dirichlet formulations yielded no located covering formula. An unindexed earlier formula remains a material risk; search absence is not a proof of worldwide priority.

## Value — PASS

The exact covariance solves a specific finite-sample calibration gap for a published natural goodness-of-fit statistic: incorrectly setting the cross-covariance to zero would give leading variance \(49/12\), whereas the correct leading variance is \(37/12\). The sharp discrepancy is about 24.5% of the naive variance. The closed formula works at every admissible sample size and reveals persistent correlation even as each statistic concentrates. This is beyond a textbook marginal-moment exercise, although it is not a claim of a new general central limit theorem.

## Limitations and closest literature

The model is a fully specified continuous null and produces only moment/normal calibrations, not full exact quantiles or power. The 2004 work is a particularly plausible source of equivalent calculations, but its inspected relevant sections lack this covariance. The broader 2012 theorem covers asymptotic normality in principle; that coverage is acknowledged and not misrepresented as a new framework. Publication priority remains subject to independent literature review.

Self-review: passed. Independent audit: not yet performed.
