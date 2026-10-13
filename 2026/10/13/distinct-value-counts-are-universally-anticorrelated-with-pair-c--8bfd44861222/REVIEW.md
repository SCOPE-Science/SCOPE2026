# Review

## Correctness

PASS. The mixed covariance is reconstructed directly from indicator products. For each category and each sample pair, the joint event is split according to whether the matched pair uses that category or another one. This yields the exact summand in the theorem without approximation.

The strict sign does not rest on numerical evidence. After the algebraic rewrite, it is a weighted covariance between an increasing function of \(p_i\) and a decreasing function of \(p_i\). The weighted rearrangement inequality bounds the relevant tilted mean by \(q_2/(2-q_2)\), which is strictly below \(q_2\) for every nondegenerate law.

The birthday-scale \(L^2\) statement follows from the exact occupancy identity for the discrepancy and a second-moment bound on colliding triples. The correlation limit then follows because the uniform pair-collision variance tends to a positive finite limit.

The packaged checker independently reproduces the covariance by exhaustive rational enumeration for multiple nonuniform laws and verifies the uniform and asymptotic specializations.

## Originality

PASS, with a residual bibliographic risk from the size of the classical occupancy literature.

Camarri–Pitman and related unequal-birthday work study repeat times and repeat processes for arbitrary discrete laws, not the finite-sample covariance between distinct-count and pair-match statistics.

Chatterjee–Diaconis–Meckes explicitly compare multiple birthday collision counts and pair matches in the uniform case, including the role of triple occupancies. Their full text does not state the heterogeneous exact covariance or its universal sign.

Hwang–Janson treat the marginal number of occupied urns and local limit theory, not the pair-match joint law. Arratia–Garibaldi–Kilian define sequential collisions as repeat losses \(n-K_n\), not as matching pairs \(C_n\).

The nearest published occupancy finding located in the semantic record concerns pairwise-independent uniform allocations and reduces symmetric occupancy constraints to the mean pair-collision count. It neither covers arbitrary iid probability vectors nor determines the covariance with the occupied-count statistic.

## Value

PASS. The two quantities are canonical but genuinely different summaries of repeated sampling: \(K_n\) measures observed support, while \(C_n\) is the collision statistic underlying the birthday paradox, homozygosity estimation, hashing, and Poisson collision approximations.

The theorem supplies a distribution-free sign over arbitrary finite heterogeneity, where symmetry arguments no longer apply. The critical uniform limit adds structural content: pair matches and repeat losses differ only through triple and higher occupancies, and this discrepancy vanishes in \(L^2\), making their centered standardized fluctuations asymptotically opposites.

This is not a recomputation of a marginal occupancy formula; it is a joint law connecting two different classical statistics and clarifying exactly when their usual birthday approximations become interchangeable.

Self-review: passed. Independent audit: not yet performed.


Deterministic replay: `VERIFY_OK exhaustive_checks=25 weighted_sign_checks=25 uniform_checks=112 asymptotic_checks=9 enumerated_words=7882`.
