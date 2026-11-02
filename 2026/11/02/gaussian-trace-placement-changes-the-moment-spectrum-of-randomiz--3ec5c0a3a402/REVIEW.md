# Scientific review

## Correctness: PASS

The Gaussian direct denominator is a positive weighted chi-square variable over exactly \(mn\) independent Gaussian coordinates; the small-ellipsoid probability includes the determinant factor \(\det(R)^{-m/2}\). The complementary denominator crosses zero at a strictly interior point of a weighted gamma density because \(H\) has at least one positive eigenvalue. Its smooth positive density there yields the two-sided local probability \(2\varepsilon f_H(n)\). These facts prove both complete tail and positive-moment spectra, including threshold equality. The fixed-norm identity and deterministic lower bound prove the Rademacher contrast. The worked chi-square example and 836 finite code checks support the algebra but are not substitutes for the proofs. Assumptions explicitly exclude singular \(R\), trivial \(H=0\), random numerators, and probe-dependent smoothers.

## Originality: PASS (qualified)

The complete 2020 Gazzola–Sabaté Landman open-access paper establishes the GCV and randomized trace-estimation context; it does not, in the inspected GCV passage, provide the stated inverse-moment dichotomy. The 2021 Chung–Gazzola survey concerns large-scale regularization and is not evidence for the new thresholds; its full paper was not inspected. The Girard–Hutchinson notes cover unbiased Gaussian/Rademacher quadratic traces and their variance, not the reciprocal-squared nonlinear score. published-finding corpus searches using generalized cross-validation, complement subtraction, moment thresholds, chi-square poles, and fixed-norm aliases returned nearby probabilistic and inverse-problem results but no statement implying the full theorem. No searched database or primary table of this exact statistic was identified. Classical facts about inverse chi-square moments and weighted gamma densities are credited as proof tools. A specialized pre-existing noisy-GCV pole analysis remains a residual priority risk; there is no claim of exhaustive literature coverage or independent novelty verification.

## Value: PASS

GCV is a standard regularization-parameter selection objective. The finding shows that mathematically equivalent and individually unbiased Monte Carlo forms of its denominator can have different, *exact* integrability classes, making finite means impossible for one natural Gaussian placement at every finite sample size. It also supplies a simple, samplewise fixed-norm alternative and an exact finite-moment budget for the direct placement. These observations concern estimator reliability beyond the familiar variance of a trace estimator, and they distinguish moment failure from merely increased numerical error.

## Closest literature and limits

Gazzola–Sabaté Landman (2020), DOI:10.1002/gamm.202000017: inspected relevant full-text GCV and stochastic trace-estimation discussion. Chung–Gazzola (2021 preprint, 2024 journal), arXiv:2105.07221 / DOI:10.1137/21M1441420: inspected abstract and metadata; full text unavailable. Girard–Hutchinson estimator notes: inspected Gaussian and Rademacher trace laws. Classical Hutchinson (1990) trace estimator: bibliographic comparison. The claim is conditional on a fixed positive-contraction smoother; adaptive tuning, other probe families, score clipping, and alternative GCV normalizations involving random numerators are not analyzed. Independent literature priority assessment remains necessary.

Self-review: passed. Independent audit: not yet performed.
