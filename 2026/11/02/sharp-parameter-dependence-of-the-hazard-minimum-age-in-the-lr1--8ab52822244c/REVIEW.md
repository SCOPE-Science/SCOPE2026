# Scientific review: LR1 hazard-minimum age

## Correctness

PASS. The hazard is derived from the LR1 exponential/Gamma mixture; the exact derivative numerator and a positive-coefficient polynomial prove unique minimization and strict monotonicity of the minimum age over the full positive parameter domain. Endpoint expansion is obtained from the explicit strictly monotone inverse, not from finite numerical sampling. Symbolic identities, expansions, and bracketed numerical roots were reproduced from the packaged checker. The fixed-time-unit convention and endpoint remainders are explicit.

## Originality

PASS with historical-priority qualification. Singh and Patawa give the source model and endpoint hazard signs. Block et al. (2010), Theorem 2.1, already provide a broad **qualitative bathtub classification**, and Block, Langberg and Savits (2012) classify shapes for exponential/Gamma mixtures; uniqueness of a minimum is therefore not claimed as an independent innovation. The nontrivial evaluated addition is the exact coupling of LR1's changing mixing weight and rates to the globally decreasing minimum-age map, the small-parameter finite limit with first correction, and the large-parameter log/log-log expansion and comparison to mean lifetime. Targeted mathematical-record and literature searches did not identify these quantitative statements. The 2012 full text could not be inspected and is an explicit residual risk.

## Mathematical value

PASS. The minimum-age of a nonmonotone failure hazard is a natural reliability invariant. Its strict parameter dependence and two unlike scaling regimes quantify when the lowest-risk age occurs in absolute and mean-normalized units. The logarithmically diverging normalized age is a structural consequence of the coupled-rate/mixing-weight restriction, not a renaming of the known shape classification. No cost-optimal screening policy is inferred.

## Closest literature and limits

- Singh and Patawa, arXiv:2610.24575v1 (2026), Sections 2 and 3, supply the LR1 distribution, hazard and endpoint analysis.
- Block et al., *Journal of Applied Probability* 47 (2010), Theorem 2.1(iii), proves a broader bathtub-shape property that covers the qualitative element here.
- Block, Langberg and Savits, *Journal of Applied Probability* 49 (2012), abstract and scope, announce a general shape classification. Only the abstract was accessible; a full-text comparison of the quantitative minimum-age laws remains outstanding.

Self-review: passed. Independent audit: not yet performed.
