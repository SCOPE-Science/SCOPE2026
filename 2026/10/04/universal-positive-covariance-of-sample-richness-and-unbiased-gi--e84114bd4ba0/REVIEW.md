# Review

## Correctness

PASS. Pair exchangeability reduces the covariance with the full Simpson \(U\)-statistic to the covariance with one collision indicator. For each category, the joint event “category observed and the selected pair collides” has an exact two-case decomposition, yielding the displayed covariance formula after summation.

The sign argument is independent of finite enumeration. Under the size-biased category law, \(P\) has mean \(s_2\), while \((1-P)^{n-2}\) is nonincreasing. The standard two-copy antitonic identity gives \(B_n\le s_2A_n\), which immediately yields the positive lower bound. Equality conditions follow from strict monotonicity when \(n>2\).

## Originality

PASS, with an explicit residual risk from older occupancy and ecological-diversity literature. Barbour's full arXiv treatment was inspected at its arbitrary-probability occupancy setup and its definitions of the number of occupied boxes and frequency counts. It studies distributional approximation of those occupancy summaries, not covariance with Simpson concentration.

Källberg--Leonenko--Seleznjev's full arXiv treatment was inspected at the discrete exact-coincidence section and generalized \(U\)-statistic construction. It covers coincidence-probability estimation and asymptotic normality, but not the exact finite-sample richness/collision covariance.

Targeted searches for species richness, occupied-box counts, collision pairs, Simpson concentration, Gini--Simpson diversity, and covariance did not locate the exact identity, lower bound, or equality characterization.

## Value

PASS. Observed richness and Gini--Simpson diversity are two standard but differently weighted summaries of categorical diversity. The theorem gives a distribution-free sign relationship between their unbiased sample versions for every sample size and every nondegenerate finite category law, together with a quantitative lower bound and exact equality cases.

The result is structurally informative rather than a numerical example: it explains why a richness statistic sensitive to rare categories and a pairwise diversity statistic sensitive to common categories nevertheless fluctuate in the same covariance direction under arbitrary heterogeneity.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK enumeration_checks=19 formula_checks=24038 lower_bound_checks=24038 equality_checks=1037 strict_checks=11486`.
