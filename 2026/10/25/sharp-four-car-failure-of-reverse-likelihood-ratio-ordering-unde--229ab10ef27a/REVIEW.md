# Review of the sharp four-car reverse-TP2 obstruction

## Correctness
**PASS.** The joint random variables and conditional success event are explicit. The complete support argument proves reverse-TP2 at all sizes through three for arbitrary positive preference distributions, without numerical sampling. The four specified weighted cells are determined by complete independent preference-word enumeration and the displayed histogram multipliers. Their determinant is exactly \(1024>0\). All \(4^4\) words and small-size supports are checked by `verify.py`; the analytical scope does not exceed those finite cases.

## Originality
**PASS, with historical risk.** The relevant first-public 2005 Gessel–Seo paper enumerates lucky count alone. Stanley–Yin (2023) gives the joint luck/displacement enumerator for equally weighted parking functions, but not the nonuniform preference-label weight refinement needed for this counterexample. Kenyon–Yin's bivariate statistic is *critical left-to-right maxima* rather than lucky arrivals. Colmenarejo et al. (2024) analyze a restricted Stirling-permutation class with constant displacement. No directly covering result arose from semantic database searches for weighted parking, luck/displacement, reverse-TP2, or nonuniform preference laws. That is evidence against known coverage, not proof of global novelty; an unlocated general multivariate parking enumerator may exist.

## Mathematical value
**PASS.** Likelihood-ratio ordering is a strong and standard form of stochastic association. Since an extra unlucky car entails positive displacement, a general reverse-likelihood-ratio principle is a motivated candidate for biased linear probing. The example shows the exact first car count at which that universal principle fails, with only a factor-two difference in site preference weights, thus sharply limiting strong monotonicity theorems. It does not assert failure of weaker covariance or stochastic ordering.

## Limits
Independent historical-priority verification and external mathematical audit are not performed. No statement is made for all four-car probability profiles, or for uniform preferences beyond size three.

Self-review: passed. Independent audit: not yet performed.
