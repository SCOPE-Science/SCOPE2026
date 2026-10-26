# Scientific assessment

## Correctness — PASS

The independent-pool Bernoulli calculation reduces the assay-count variance to four times a matching objective with edge weight \(f(q_iq_j)=q_iq_j(1-q_iq_j)\). Both four-point factorization identities are exact. Their ordered relation proves that a crossing pair is never strictly better than both uncrossings. A two-level index-span tie-break proves existence of a noncrossing global optimum without assuming a fixed sign for the mixed derivative. The interval recurrence enumerates all noncrossing perfect matchings exactly. The certified exhaustive six-person example is uniquely optimized by the stated noncanonical pairing. The standalone exact-rational checks reproduce the finite assertions; they do not purport to prove the universal result.

## Originality — PASS with residual uncertainty

The source comparison separates risk-ordered methods targeting expected assay count (McMahan, Tebbs and Bilder, 2011; Bilder and Tebbs, 2012) and estimator-variance or information criteria (Warasi and Das, 2024) from minimum variance of the *total number of retests* for a fixed two-person pairing. General matching methods are broader algorithmically, but do not by themselves assert the special noncrossing form for this non-Monge cost. Earlier one-sided prevalence optimal-pairing laws do not imply the mixed-risk theorem, as the six-person exact optimum lies outside either canonical pairing. Full-text access to one plausible older article was incomplete; an unnoticed equivalent formulation is possible. No independent literature audit has occurred.

## Value — PASS

Variability in second-stage assay demand is an operationally meaningful property of fixed pooled-screening designs, distinct from their expected consumption. The finding gives a complete structural reduction for all heterogeneous infection-risk profiles, including the mixed regime where neither sorting-and-pairing-adjacently nor opposite-extreme pairing is always optimal. The resulting interval optimization is elementary to implement without a general matching solver. The example demonstrates that the mixed regime produces genuinely new optimal structures. Value is conditional on mandatory size-two pooling; unrestricted single tests remove the variance optimization problem, and no clinical testing recommendation or advantage in all prevalence regimes follows.

## Closest literature and limitations

The closest primary article is McMahan, Tebbs and Bilder, *Informative Dorfman Screening*, first published 15 July 2011, DOI `10.1111/j.1541-0420.2011.01644.x`, whose inspected indexed method sections optimize expectations, pool sizes and error-aware accuracy. The related 2012 article by Bilder and Tebbs, DOI `10.1002/sim.5334`, addresses heterogeneous pooling but was incompletely accessible for full-document comparison. Warasi and Das, DOI `10.1007/s13253-024-00646-6`, explicitly optimize expected testing and the variance of a prevalence estimator, not the variance of total test count. Generic ordered-matching theorems may still subsume part of the structure. The mathematics assumes independent statuses, perfect tests, forced equal-size two-person pools, and no dilution.

Self-review: passed. Independent audit: not yet performed.
