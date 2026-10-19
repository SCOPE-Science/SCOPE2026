# Review: independent Gumbel cutoffs for two spectral-accuracy tiers

**Correctness — PASS.** The proof reconstructs the residual eigenvalues, validates the continuous-time Markov/exponential race mapping, derives an exact finite binomial–hypoexponential CDF, and proves the joint Gumbel limit by an explicit vanishing cross-exceedance estimate. The background count concentration and incomplete-block correction are both negligible at the \(\Theta(r)\) scale. Direct Schur complement and independent finite-state/integral checks support the algebra; asymptotic simulations are not used as infinite proofs.

**Originality — PASS, with residual bibliography risks.** The strongest inspected 2026 RPCholesky analysis establishes accuracy bounds and a diagonal coupon illustration, not the correlated two-tier spectral plateau, linked finite hitting law, or independence of the two thresholds. The 2022 algorithm and 2024 accelerated method give the sampling rule and performance estimates. Retrieved related stochastic pivot results use other operators or metrics. The abstract of Divan–Gilles 2026 reports broad convergence rates, but its full text was not accessible; generic two-stage coupon-collection literature is an additional residual coverage risk. A search failing to find a match is not a proof of originality.

**Value — PASS.** Numerical kernel approximation needs a principled distinction between moderate and strict spectral accuracy, especially under correlation. This nontrivial block family produces two different stopping-budget thresholds with exact finite strict-tier distribution and sharp limiting probabilities; asymptotic independence is a new qualitative property of one shared adaptive trajectory.

**Limitations.** Identical \(2\times2\) blocks, exact residual-diagonal sampling, fixed \(\rho,\beta\), background dimension at least order \(r\log r\), operator norm only. No general PSD or finite-sample uniform rate is claimed. Published overlap remains uncertain where full text was unavailable.

Self-review: passed. Independent audit: not yet performed.
