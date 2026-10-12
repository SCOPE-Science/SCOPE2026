# Review
## Correctness
PASS. Conditional on a fixed support of size \(k\), the ordered bootstrap labels are uniform over surjections. Identifying two draw positions gives the same-label probability
\[
\frac{\left\{\begin{matrix}n-1\\k\end{matrix}\right\}}
{\left\{\begin{matrix}n\\k\end{matrix}\right\}}.
\]
Combining this with the exact expected-variance identity for exchangeable draws and then averaging over a uniform \(k\)-subset proves the regression. An independent multiplicity calculation gives the covariance. Exact exhaustive resampling checks agree through \(n=6\) for multiple fixed data profiles.

## Originality
PASS, with an older-occupancy-literature risk. The closest classical full text explicitly studies the random number of distinct observations in ordinary bootstrap samples and uses it to motivate sequential resampling, but it does not state the conditional sample-variance regression, the adjacent-Stirling factor, or the resulting covariance. A later fixed-support bootstrap paper studies empirical-process consistency rather than this finite mixed statistic. Targeted alias and exact-form searches located no equivalent statement.

## Value
PASS. Random support size is the classical “information content” issue behind sequential bootstrap variants, while sample variance is a basic resampling statistic. The theorem makes that concern quantitative at finite \(n\): for every fixed dataset, support size determines the conditional expected resample variance through one universal coefficient, and the normalized covariance is completely data-free.

## Closest literature and limitations
The result is restricted to the equal-weight ordinary bootstrap with resample size \(n\). It does not give a conditional distribution or stochastic ordering. Unequal-weight, \(m\)-out-of-\(n\), Bayesian, and sequential bootstraps have different occupancy structures. Older survey-sampling literature under another encoding remains the principal originality risk.

Self-review: passed. Independent audit: not yet performed.
