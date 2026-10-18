# Scientific review

## Correctness — PASS

The two states counting distinct nonempty subsequences by their final letter form an exact three-dimensional affine transfer, including the empty-word boundary. Both formal generating functions follow from matrix geometric series. The key nine-dimensional rational identity has an explicitly exhibited polynomial-vector certificate, checked by direct exact polynomial multiplication; no unverified infinite extrapolation is needed. The iid formula follows by substitution and partial fractions, with the empty-word and constant-word cases covered. The standalone checker verifies the certificate and independently enumerates all binary words through length 11 by composition; lengths through 9 are checked by constructing actual subsequence sets. Risks: no mathematical gap found in the stated matrix and ring assumptions; exact calculations are confined to integer coefficients.

## Originality — PASS on inspected sources

Primary full-text comparison included Flaxman–Harrow–Sorkin (2004), which evaluates extremal counts and random-string benchmarks but does not supply a binary fixed-composition second-moment function, and Collins (2013), which derives first moments. The Biers-Ariel–Godbole–Kelley first-moment extension (2017/2018) was also inspected and is not a second-moment theorem. Published searchable comparisons for random subsequences, conditional compositions, equivalent second-moment transforms and deletion-ball diversity did not identify an equivalent claim. The closest indexed findings involve *contiguous substrings*, exactly-two-deletion balls, and subsequence *universality*, different observables that do not imply the present full-length scattered-subsequence variance. The standard transfer-matrix method and all previously established expectations are acknowledged rather than claimed as new. Risk: specialized unindexed formulas or implicit equivalent evaluations in a broader treatise remain possible; search failure is not a uniqueness proof.

## Mathematical value — PASS

The rational bivariate second-moment function simultaneously resolves every fixed-composition variance for the natural diversity statistic measuring all deletion outcomes. Its uniform-source specialization uncovers an exponential variance scale and a strictly growing squared coefficient of variation, information not implied by any known first-moment formula. This is an infinite-domain closed evaluation with an exact finite symbolic certificate; the first-moment calculation alone would not meet the same value threshold. Limitations include the lack of a distributional limit, sharp tails, and general-alphabet variance formulas.

Self-review: passed. Independent audit: not yet performed.
