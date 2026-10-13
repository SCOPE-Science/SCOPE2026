# Scientific review: exact singleton-rarefaction envelope and dominant-species staircase

## Correctness — PASS

The random-subsample indicator identity gives the exact integer objective. The first and second forward differences are explicit binomial identities, with a decreasing-then-increasing first-difference profile, including the terminal zero plateau. Pairwise mass transfers never decrease the objective: the convex upper branch can be concentrated into one abundance, and the concave lower branch can be balanced. The resulting one-parameter family is exhaustive for *at least one* maximum. In the fixed-richness macroscopic-sampling limit, an exact hypergeometric identity yields a uniformly exponentially small tail, establishing uniform convergence to \(a\rho(1-\rho)^{a-1}\); its strict discrete maximum away from reciprocal sampling fractions implies eventual uniqueness. All endpoint cases \(2\le k\le N\) are addressed. Finite exact enumeration and direct sampling checks supplement, but do not replace, the general proof.

## Originality — PASS, with residual risks

Heck, van Belle, and Simberloff (1975) give ordinary rarefaction richness moments; Coddington et al. (2009) investigate observed singleton biases; Chao and Jost (2012) develop coverage-based richness comparisons; and Locey and White (2013) analyze abundance-vector feasible sets. None of the inspected accessible primary material establishes the maximum expected **number of sample singletons**, its all-integer abundance reduction, or its eventual sampling-fraction staircase. A 2023 continuous symmetric resource-allocation theorem contains an analogous one-exception/equal-tail motif, but concerns nonincreasing cost functions and nonnegative real allocations, not this discrete nonmonotone hypergeometric objective or its limiting classification. Unavailable complete texts, especially the 1975 rarity paper and 2013 feasible-set paper, leave a genuine prior-coverage risk. Search absence is not treated as proof of originality.

## Value — PASS

The expected count of singletons influences sample coverage, extrapolation, and apparent biodiversity. Conditioning on both true species richness and census abundance gives a natural finite null-envelope problem. Its exact solution reduces all positive integer partitions to linear-sized evaluation, and its asymptotic staircase identifies the specific rare abundance scale maximizing singleton detections at a fixed sampling fraction. The theorem is a structural ecological sampling benchmark, not a claim about naturally selected abundances, estimation precision, or sampling with replacement.

## Limitations and reproducibility

Only existence of a canonical finite maximizer is proved, not classification of all ties. The asymptotic uniqueness excludes reciprocal limiting fractions and growing species richness. The proof is self-contained and the companion checker uses Python's standard library. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
