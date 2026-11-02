# Scientific review

## Correctness (C): PASS

The explicit transition matrix follows from independent edge states and uniform choice among available neighbors; the block-eigenvalue multiplicities, stationary weights and Kemeny sum are exact. Strict convexity of \(1/(1-r^x)\) and concavity of \(1-r^x\) give the strict balanced Kemeny optimum. Two oppositely monotone spectral-radius branches establish the complete integer crossover rule. A direct part-mass eigenmode proves the exponentially slow balanced total-variation lower bound, and a two-mode decomposition gives the constant-time star upper bound. A standalone rational-state checker independently tests these identities and hitting-time expectations. Risks are limited to the explicitly excluded endpoints and different temporal models.

## Originality (O): PASS, qualified

The 2017 model paper directly establishes the single-step transition formula; this familiar reduction is not claimed as new. Sections 3, 4.2, 5.3 and 6 of its accessible full manuscript develop the general evolving-graph mechanism and cover-time bounds, not the joint exact Kemeny/spectral optimization on bipartitions. Static-graph Kemeny and nonbacktracking results are conceptually adjacent but use different chains. Comparisons to indexed mathematical claims and recoverable prior records did not reveal an implication-equivalent theorem. Historical priority remains unverified and an inaccessible publication could cover this particular combined classification.

## Value (V): PASS

The two most common performance metrics for an evolving-network walk recommend opposite graph shapes, and the discrepancy is not marginal: for an identical edge-availability probability, balancing produces an exponential mixing bottleneck while the star has bounded mixing time, even though balancing halves the asymptotic stationary-target hitting time. The complete crossover rule gives a nontrivial structural network-design boundary rather than an isolated numerical example.

## Closest literature and limitations

Lamprou–Martin–Spirakis (arXiv:1702.05412) supplies the edge-availability reduction. Breen et al. (arXiv:2203.12049) studies static nonbacktracking walks; Faught–Kempton–Knudson (arXiv:2108.01061) gives static Kemeny structural formulas. The statement excludes temporally correlated edge states and does not optimize the exact total-variation mixing time for arbitrary availability or arbitrary graphs. Priority assessment is qualified by accessibility and indexing limits.

Self-review: passed. Independent audit: not yet performed.
