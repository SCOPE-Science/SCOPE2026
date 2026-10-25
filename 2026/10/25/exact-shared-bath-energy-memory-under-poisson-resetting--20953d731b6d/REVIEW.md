# Review of exact shared-bath energy memory

## Correctness
**PASS.** The complete Poisson-reset process is well posed, and its unique regenerative stationary law possesses the required fourth moments. Polynomial generator identities determine the exact stationary cross-moments. The centered pair of observables has an exact Jordan-block semigroup, yielding the full lag covariance; integrating the exponentially decaying kernel rigorously yields the Green–Kubo coefficient. These identities are reproduced by the included executable with symbolic stationarity checks, an independent Brownian-functional moment route and 15 numerical quadrature comparisons. The dimension limit is deliberately taken after the long-time variance coefficient.

## Originality
**PASS, subject to scholarly priority uncertainty.** The closest directly examined primary article is Santra–Basu–Sabhapandit (arXiv:2205.00549v1), which derives the specific common-diffusivity/common-reset process and stationary one-time position laws, but not its time-lagged energy covariance or long-time energy-measurement variance. Mesquita–Majumdar–Sabhapandit (arXiv:2506.20859v2) evaluates equal-time squared-coordinate correlations in the unreset, nonstationary shared-bath model; the presence of a joint reset and the lagged stationary functional are materially different. Other general Markov-renewal results can simplify the derivation but were not found to furnish the evaluated coefficients. Primary literature was searched by source, aliases, parameters and implications; no equivalent claim was recovered. The possibility of an unlocated general specialization remains a residual risk and no priority certification is claimed.

## Scientific value
**PASS.** The normalized total squared position is a natural energy/spatial-spread observable for a particle with shared stochastic temperature. Its temporal-average error remains order one in dimension despite independently driven coordinates, in direct contrast to averaging independent baths and reset histories. The exact \(38/r\) limit and positive rank-one bath contribution quantify an experimentally interpretable failure of spatial self-averaging, beyond a one-time covariance calculation or simple normalization exercise.

## Limitations
This theorem assumes fully coordinated resets of the positions and diffusivity, a squared-Brownian environment, stationary initialization, positive rate and amplitude, and the sequential limit of large time before large dimension. The proposed observable is the squared radial displacement, not a thermodynamic kinetic energy with separately modeled momenta. Full prior-art exhaustiveness and independent validation have not been established.

Self-review: passed. Independent audit: not yet performed.
