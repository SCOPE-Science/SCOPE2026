# Scientific review: endpoint alignment of bounded-noise gradient clipping

## Correctness

PASS. The pointwise affine minorant is proved by separate inside/outside-ball cases, with concavity on the exact admissible interval; centering eliminates its affine noise term. Monotonicity of Euclidean projection extends the result beyond unit gradient norm, and antipodal noise attains the claimed coefficient. The subthreshold interval gives exact zero conditional drift. Martingale convergence, Doob's inequality and a nondegenerate Gaussian component yield a positive-probability nonoptimal limit. The checker verified the new finite computations, but does not replace the analytic proof.

## Originality

PASS on the inspected record, with residual risk. The 2026 motivating Proposition 2 provides positive alignment only for clipping radius strictly larger than the bounded-noise radius, with a coefficient that collapses at the endpoint; its half-coefficient requires a radius at least twice the noise radius. The new result provides the sharp half-coefficient at the previously unresolved equality, for all centered noise distributions without symmetry. Chen, Wu and Hong (2020), Example 2, already gives an equivalent subthreshold zero-drift interval and is explicitly credited. Their symmetricity theorem does not imply a uniform bound over all asymmetric centered supported distributions. Koloskova, Hendrikx and Stich (2023) discuss uniform noise and thresholds but focus on bounded-variance bias without this sharp endpoint minorant. Qian et al. (2021) use additional component-gradient angle controls. Relevant mathematical search results include projection Lipschitz sensitivity and different clipping algorithms but none supplying this sharp endpoint implication. Equivalence in overlooked literature remains possible.

## Value

PASS. The motivating almost-sure convergence analysis currently assumes a strictly larger clipping radius than the bounded noise radius, and its stated descent coefficient vanishes as those parameters meet. A sharp, dimension-free positive coefficient at equality is a substantive structural improvement: it identifies the exact universal transition between guaranteed descent alignment and a failure regime. The pointwise affine minorant provides a reusable tool beyond the particular examples; the pathwise example makes clear why the lower side matters. This is not claimed as a new general convergence theory or as rediscovery of the 2020 dead-zone example.

## Limitations and risk

The hypothesis is an almost-sure bound on centered oracle error, not just bounded variance. There is no claim of a per-ratio optimal coefficient away from the endpoint or independent verification. Historical equivalents may remain unindexed or uninspected.

Self-review: passed. Independent audit: not yet performed.
