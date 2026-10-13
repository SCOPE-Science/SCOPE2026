# Self-review

## Correctness
PASS. The support reduction is exact. The global asymptotic argument separates edge localization from the central expansion, uses a uniform Stirling remainder on the localized compact region, and derives the square-root scale from an exact quartic loss versus a quadratic \(1/N\) correction. The limiting profile has only the two claimed maximizers. Finite computations are used only as regression checks.

## Originality
PASS. The closest full-text source, Harremoës–Matúš, studies the same divergence and provides general bounds plus an asymptotic indexed by the unsampled fraction, but the inspected text does not state the leave-one-out two-point identity as an optimization tool, the square-root displacement of the maximizing composition, or the \(1/(6N^2)\) gain. Targeted searches over equivalent hypergeometric/binomial and entropy formulations found no covering statement. A prior leave-one-out maximal-density-ratio result is not an implication because that different discrepancy is maximized near one-quarter rather than near one-half.

## Value
PASS. Leave-one-out sampling is a canonical finite-population endpoint, and the square-root displacement explains a subtle failure of exact balance to be asymptotically worst at the first composition-sensitive correction. The result gives a complete asymptotic location for all global maximizers and a sharp expansion of the maximum.

## Closest literature and limitations
Harremoës–Matúš (arXiv:2002.03002v1; DOI: 10.14736/kyb-2020-6-1111) is the closest source and was inspected in full where relevant. Dümbgen–Samworth–Wellner (arXiv:1905.03009v1) concerns maximal density ratio rather than KL divergence. The present theorem is limited to binary leave-one-out sampling and does not provide a closed finite-\(N\) rounding formula for the maximizing integer. An older equivalent formulation remains a residual literature risk.

Self-review: passed. Independent audit: not yet performed.
