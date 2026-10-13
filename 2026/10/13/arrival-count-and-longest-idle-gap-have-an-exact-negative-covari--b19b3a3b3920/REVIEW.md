# Review
## Correctness
PASS. Conditional on the count, the arrival epochs are uniform order statistics and the normalized gap vector is exactly Dirichlet with all parameters one. Inclusion-exclusion gives the largest-gap mean \(H_m/m\). Poisson mixing gives \(t\operatorname{Ein}(\mu)/\mu\), and differentiating a Poisson expectation gives the exact covariance. The sign and both asymptotic regimes follow from elementary identities with explicit boundary handling.

## Originality
PASS, with an older random-division literature risk. The full simplex source gives the largest-spacing first moment but not a random-count covariance. The full Poisson longest-gap source studies the same gap statistic and its Poissonized-spacing representation, but its stated results concern distributions, transforms, and large deviations rather than dependence on the realized count. Claim-specific searches found no equivalent mixed moment.

## Value
PASS. The number of arrivals and the longest idle interval are two basic, operationally distinct summaries of the same Poisson window. The exact negative covariance quantifies their dependence for every intensity and observation horizon, while the conditional harmonic regression and dense/sparse asymptotics explain the mechanism and scaling.

## Closest literature and limitations
The closest fixed-dimension precursor is the exact mean of the largest uniform spacing. The closest same-process precursor is the homogeneous-Poisson longest-gap literature. The theorem includes both boundary gaps and assumes homogeneous intensity. Older bivariate random-division or maximal-spacing work remains the main residual originality risk.

Self-review: passed. Independent audit: not yet performed.
