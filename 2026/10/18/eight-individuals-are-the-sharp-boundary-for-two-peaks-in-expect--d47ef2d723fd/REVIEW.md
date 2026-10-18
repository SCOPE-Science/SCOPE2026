# Scientific review: two peaks in expected sample singleton counts

## Correctness — PASS

Every possible positive census abundance multiset with total at most eight is a positive-integer partition. The nonincreasing recursion enumerates 66 such profiles without duplication; an independent all-compositions construction checks the completeness, one census size at a time. For each profile, the hypergeometric probability that a species occurs exactly once is its abundance times a binomial coefficient divided by the total sample count. The embedded program independently enumerates every labeled-individual subset and recovers the same rational expected singleton count for every profile and sample size. Exact comparisons show no profile with two strict interior peaks below eight and the sole eight-individual profile \((5,2,1)\), with peaks at \(2\) and \(6\). The two all-size exceptions (uniform abundance and abundances at most two) have separate elementary algebraic proofs. Finite enumeration is not used as proof for any claim about censuses larger than eight.

## Originality — PASS, conditional on the documented literature-access limits

The classical hypergeometric formula is not original. Coddington et al. (2009), DOI `10.1111/j.1365-2656.2009.01525.x`, discusses observed singletons and undersampling; Colwell et al. (2012), DOI `10.1093/jpe/rtr044`, develops finite-population rarefaction and frequency-of-frequency methods; Chao and Jost (2012), DOI `10.1890/11-1952.1`, develops sample completeness and rarefaction from frequency counts. Inspected article sections and methods do not supply the sharp minimum, exact first-layer classification, or the two structural contrasts as the same mathematical result. Closest adjacent research-index records concern covariance of richness with frequency counts, covariance of successive discoveries, and pairwise comparison of expected singleton curves under abundance transfers; none logically determines the number of maxima in one fixed finite-population curve. A covering theorem under occupancy/urn terminology, or in uninspected appendices/older literature, remains a nonzero bibliographic risk; this status is a self-review, not independent originality certification.

## Mathematical value — PASS

Singletons are a natural ecological diagnostic of undersampling, and the expected number observed at increasing sampling effort is a natural rarefaction profile. The first possible double peak at only eight individuals demonstrates concretely that a single-peak assumption fails in the smallest heterogeneous examples. The unique abundance profile at the sharp threshold and the two all-size no-double-peak structural classes isolate when this behavior needs genuinely different abundance scales. These are finite exact structural facts with interpretive value for sampling design; the proof does not claim empirical prevalence or a larger-scale classification.

## Closest prior work and unresolved limits

The cited literature supplies the ecological motivation and hypergeometric setup, not demonstrated exact coverage of the new threshold. Earlier work about comparing two curves is not equivalent to classifying peaks within a curve. There remains a risk of older equivalent occupancy-language results; independent bibliographic checking is necessary before publication. The scope is fixed finite abundances, perfect detection, one random sample at each size and unconditional expected singleton count, not variance, replacement sampling or estimated abundance.

Self-review: passed. Independent audit: not yet performed.
