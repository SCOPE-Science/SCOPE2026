# Same-model scientific review

## Correctness
**PASS.** The complete domains for one, two, and three agents per side are covered. All \(46656\) three-by-three profiles and all \(6\) perfect matchings per profile are checked. Stability, rank-maximality, and sex equality are each replayed in two exact formulations. The full relation histogram and the disjoint witness are reproduced from the packaged verifier.

Risk: the claim is finite and does not extrapolate beyond three agents per side.

## Originality
**PASS.** The literature already defines both fairness criteria, gives algorithms and complexity results, and directly compares rank-maximal stable matchings using sex-equality scores. Those facts are treated as prior. The accepted claim is narrower: equality through two-by-two and the exact complete three-by-three relation census. Searches using both criterion names, the market size, exact counts, exact reduced probabilities, and set-relation language did not locate an equivalent published theorem or table.

Risk: failed search is not proof of bibliographic uniqueness. An unindexed small-instance enumeration may contain the same census.

## Value
**PASS.** Rank-maximality lexicographically rewards highly ranked assignments, while sex equality balances aggregate rank burdens between the two sides. Their first exact conflict is therefore a natural fairness boundary. The complete relation census is informative beyond an isolated witness because it distinguishes disjoint conflict from both possible one-sided containments and proves that nonnested overlap does not occur at the first layer.

Same-model review: passed. Independent audit: not yet performed.
