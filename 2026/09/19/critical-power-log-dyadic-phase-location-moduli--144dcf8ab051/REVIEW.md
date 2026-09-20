# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The critical family is symmetric and log-concave by a direct second-derivative calculation. Its endpoint density is asymptotic to a positive constant times `s log(1/s)^(-kappa)`, so the score-squared integral is equivalent to `1/[s log(1/s)^kappa]`, giving the Fisher threshold exactly at kappa=1.

With the standard convention `H^2=(1/2) integral (sqrt(f)-sqrt(g))^2`, the square-root density has endpoint derivative energy asymptotic to `a_kappa/[4s log(1/s)^kappa]`. Two support endpoints and a translation of size `2r` produce the displayed constants. Boundary strips of width comparable to the shift are lower order for kappa<=1, while for kappa>1 ordinary L2 translation differentiability applies. The asymptotic inversions were checked with the factor `log(1/r) ~ (1/2)log(1/t)` retained, which is responsible for the factor `2^(1-kappa)`.

The endpoint CDF is asymptotic to `(a_kappa/2)s^2 log(1/s)^(-kappa)`. Its inverse therefore has regular-variation index one half, giving the dyadic quantile-gap factor `sqrt(2)-1`. Summation of the resulting dyadic energy gives a power of `log(1/p)` for kappa<1 and `log log(1/p)` at kappa=1. These constants cancel against the inverse-Hellinger constants to the common ratio `(sqrt(2)-1)sqrt(log 2)`.

For kappa>1, reversing the exact finite dyadic sum yields a summable series indexed from the coarsest retained quantile scale. This proves the subsequential phase-profile formula. The Laplace example is exact: all relevant lower-tail dyadic quantile gaps equal `log 2`, and direct integration gives Hellinger affinity `(1+r)e^{-r}` for a location separation `2r`. The resulting subsequential intervals follow algebraically. Numerical integration and quantile inversion in the verification artifact support the critical-family asymptotics and exact Laplace constants; they are supplementary to the analytic proof.

## Originality

**PASS, to the best of our knowledge.** Wang--Gao (2026) introduce the dyadic functional and prove only universal constant-factor comparison to the inverse Hellinger modulus. Their power-log example assumes `0<alpha<1`, while their triangle and Epanechnikov examples already identify the critical linear-boundary order `(n log n)^(-1/2)`.

The latter phenomenon is prior art. Beckert--McFadden (2007) explicitly state `(n log n)^(-1/2)` best rates for triangular and quadratic compact-support location models and develop general Hellinger-rate machinery. Smith (1985) treats power-law endpoint densities and identifies the linear-density boundary as a critical nonregular case, while noting that single-location results predated that paper. No novelty is claimed for those facts or for general Hellinger methods in nonregular location estimation.

Searches covered the exact 2026 source, critical endpoint and slowly varying variants, Hellinger location rates, power-log and log-log formulations, dyadic quantile gaps, and the older nonregular-location literature surfaced by Beckert--McFadden. No prior statement was found of the explicit kappa-dependent critical power-log trichotomy, the sharp asymptotic constants for the 2026 dyadic functional on that family, its universal ratio to the inverse Hellinger modulus, or the exact Laplace dyadic-phase interval.

The full text of Smith (1985) was not directly inspected; its abstract and later full-text literature discussing the same nonregular regime were inspected. Smith and the older location literature it cites are the principal residual risk for the slowly varying Hellinger refinement. They cannot cover the claims involving Wang--Gao's dyadic functional, which was introduced in 2026.

## Value

**PASS.** The result resolves a natural missing endpoint of a new power-log example and reveals a finer statistical phase transition inside the classical critical boundary. It also turns a constant-factor Hellinger--quantile equivalence into an exact asymptotic identity on a nontrivial infinite-information family. The Laplace calculation supplies a complementary obstruction: a fixed dyadic discretization can preserve order-one phase oscillations even in a regular model, so a single universal asymptotic efficiency constant for the functional is impossible without modifying or averaging the grid.

## Limitations

The power-log statements are local and no remainder uniform in kappa is established. The phase-profile theorem for kappa>1 does not claim nonconstancy for every member of the compact-support family; nonconstancy is proved exactly for Laplace. The phase-averaging identity is structural only and is not presented as a new estimator. Independent audit has not been performed.
