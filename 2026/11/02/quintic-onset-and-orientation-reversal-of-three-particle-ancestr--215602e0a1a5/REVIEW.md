# Scientific review

**Claim assessed.** On a unit-rate motion triangle with exactly three uniformly copying Fleming–Viot particles and killing rates \((1-\varepsilon,1,1+\varepsilon)\), the survival-weighted ancestral current satisfies \(\Delta_3=89\varepsilon^5/56010528+O(\varepsilon^7)\). This is the single new claim in the accompanying result.

## Correctness — PASS

The ten population-state and eighteen founder-state equations follow by first-step conditioning, including copying between coincident sites. At homogeneous killing, normalization removes the stationary and founder null directions, making the solution analytic in the perturbation. Exact-rational recursion gives zero degree-one and degree-three coefficients and the displayed positive degree-five coefficient; reflection eliminates all even terms. A standalone finite-matrix checker reproduces the coefficient and exactly matches the source's independent current at killing rates \((1,2,4)\). The theorem is a local asymptotic, not a numerical extrapolation or a claim about all killing contrasts.

## Originality — PASS, qualified

The closest work is Lin and Lu, arXiv:2610.12589v1, especially Section 5 and Appendices A–B. Its cubic law for \(N\ge4\) vanishes when formally evaluated at \(N=3\), and it gives a single exact nonperturbative three-particle witness, but not the exceptional fifth coefficient. Lin and Lu, arXiv:2610.18802v1, addresses a different Brownian current with a different perturbation profile. Cloez–Thai (arXiv:1603.04670) and Corujo (arXiv:2001.08000) concern uniform killing, which cannot supply the heterogeneous-killing fifth derivative. Actual parameter- and alias-based mathematical-record searches did not identify an equivalent full statement. A more general identity or an unlocated symbolic computation could still subsume this result; historical priority requires independent appraisal.

## Mathematical value — PASS

The missing response order at the minimum population supporting circulation is a natural and non-obvious structural question. The exact positive quintic coefficient demonstrates a change of **both onset order and direction** relative to the known negative cubic response for any fixed larger population. The conclusion is useful for interpreting the effect of weak spatial killing heterogeneity, without assuming a global current-sign theorem or broader applicability.

## Scope and limitations

Exactly three particles, three-site complete motion graph, symmetric unit jump rates, uniform copying, positive near-homogeneous killing, and survival-weighted founder transport. No global sign classification, alternative graphs, or nonuniform copying is established. The larger-population cubic coefficient belongs to the cited source.

Self-review: passed. Independent audit: not yet performed.
