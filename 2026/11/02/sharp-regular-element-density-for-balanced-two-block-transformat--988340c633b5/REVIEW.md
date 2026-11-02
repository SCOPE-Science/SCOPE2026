# Scientific review: balanced two-block regular-element density

## Correctness — PASS

The claim quantifies over every positive integer \(m\) and counts all total partition-preserving transformations. There are exactly four block characters, each supporting \(m^{2m}\) maps. Two characters are bijective and always regular. For each constant character, an inner inverse exists precisely when one restriction image contains the other; the constructive proof addresses both implications. The Stirling formulas count ordered pairs by the common or containing image set and subtract the equal-image overlap once. The admissible occupancy generating function, unique positive saddle, covariance, lattice aperiodicity, local limit constant, and exponential suppression of the equal-image intersection are independently spelled out and give the exact stated prefactor. Exhaustive composition tests agree for \(m=1,2,3\); further exact arithmetic checks and large-degree ratios corroborate the derivation. These finite tests are not substituted for the infinite proof.

## Originality — PASS relative to inspected evidence

The general regularity criterion is **prior work**: Sarkar–Singh, arXiv:2310.19414v1, Proposition 3.4. The new claim does not re-label that criterion as a discovery. Inspection of the source's regularity section and its other sections found structural classification and Green-relation results, not the density formula or its sharp exponential correction. Sarkar–Singh, arXiv:2010.14033v1, counts regular elements in the *onto-block* subsemigroup \(\Gamma(X,\mathcal P)\), not in all of \(T(X,\mathcal P)\). Dolinka–East–Mitchell, arXiv:1504.02520v1, count idempotents and minimal idempotent generators, which do not determine the regular-element census. Searches for equivalent image-containment occupancy asymptotics and partition-semigroup regular fractions found no decisive dominating statement. This is an evidence-limited originality judgment; older occupancy and transformation-semigroup literature may contain equivalent formulas.

## Mathematical value — PASS

The regularity of the full partition-preserving monoid fails whenever its partition is nontrivial, so the size and rate of its regular subset are natural quantitative questions. The result supplies a complete exact count for every equal two-block size and a *sharp* probability asymptotic, including a non-obvious exponential base and prefactor. It explains why the two bijective block characters dominate despite the existence of many regular maps with collapsed block characters. The exponential correction requires an independent two-dimensional occupancy saddle and is not merely a restatement of the pre-existing yes/no classification. The two-block family is structurally canonical: it is the first nontrivial character monoid and admits a nondegenerate regularity transition.

## Closest literature and limits

Primary material compared: arXiv:2310.19414v1, arXiv:2010.14033v1, and arXiv:1504.02520v1. An occupancy-theoretic equivalent could still exist under different terminology, and no exhaustive search of all older probability literature is claimed. The direct-composition verifier is exhaustive only for \(m\leq3\); its larger calculations check the proposed arithmetic formulas rather than semigroup products. No independent mathematical review has been performed.

Self-review: passed. Independent audit: not yet performed.
