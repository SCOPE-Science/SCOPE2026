# Scientific review: lucky cars and preference richness

## Correctness (PASS)

The Pollak circular representation preserves lucky-car indicators and preference richness, not just their individual marginals. Conditional on past richness \(m\), the three transition weights count vacant spots, occupied never-preferred spots and previously preferred spots. The lucky Bernoulli variables have deterministic success probabilities and therefore are independent. Conditional richness transitions, given lucky indicators, are monotone in previous richness and the current lucky bit. Independent-Bernoulli association, with strictness in the last bit, proves covariance positivity for every pair of strictly increasing recodings. The local exact covariances follow from occupancy martingale conditioning; summation and explicit variance formulas give the constants. The standalone checker passed 3048 assertions using exhaustive parking-function enumeration through size seven and exact rational arithmetic. No finite test is used as a substitute for the infinite-size proof.

## Originality (PASS, qualified)

Gessel and Seo (arXiv:math/0507497, 2005) provide the one-variable lucky enumerator. Shin (arXiv:0810.0427, 2008) relates lucky cars to rooted forests. Diaconis and Hicks (arXiv:1611.09821, 2016) study the marginal lucky and distinct-preference distributions separately. Butler et al. (arXiv:2412.07873, 2024) and Harris and Martinez (arXiv:2410.08057, 2024) refine lucky-car and lucky-spot events but do not present the full luck/richness Markov law or the increasing-transform covariance theorem. FindStat St000135 records the lucky marginal, not the bivariate table. These results cannot directly imply the signed dependence or arrival-resolved covariance solely from their stated marginals. An as-yet-unlocated older multivariate enumeration could imply the bivariate recursion, which is a residual historical-priority risk. Independent novelty certification has not been performed.

## Mathematical value (PASS)

Classical parking functions are a standard finite probability model. Luck is an arrival statistic depending on occupied *parking spots*, while preference richness is an occupancy statistic depending on *requested spots*. Their exact finite conditional coupling clarifies a dependence not determined by either familiar marginal, proves robustness under arbitrary strictly increasing transformations, and locates the peak dependence at a nontrivial arrival fraction \(W(1)\). This is a structural finite-size theorem, not an arbitrary isolated numerical statistic.

## Scientific limitations

The claim is restricted to uniform classical parking functions. It gives a bivariate finite distribution and covariance/asymptotic limits, not an infinite-dimensional functional limit or a nonuniform-preference theorem. Existing stronger general multivariate parking results may require an additional historical comparison.

Self-review: passed. Independent audit: not yet performed.
