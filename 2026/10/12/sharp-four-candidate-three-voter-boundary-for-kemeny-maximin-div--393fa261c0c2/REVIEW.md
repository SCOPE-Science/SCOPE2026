# Self-review

## Correctness
**PASS.** The complete four-candidate domains with one, two, and three voters are exhausted. Kemeny is computed independently by maximizing pairwise agreement and minimizing total Kendall distance, whose exact complementary identity is checked for every candidate ranking. Maximin is computed independently from minimum support and maximum opposition. All implementations agree on every profile. The eight orbit classes are verified under the full candidate-and-voter relabeling action.

Risk: the candidate lower bound relies on the published universal three-candidate equivalence theorem; the finite verifier itself does not prove an infinite-electorate statement for three candidates.

## Originality
**PASS.** Prior work decisively covers the universal three-candidate equivalence and states that the equivalence need not persist beyond three candidates. Those are treated as prior. Searches by rule names, aliases, exact candidate/voter parameters, the count \(1056\), the fraction \(11/144\), and isomorphism language did not locate the sharp two-voter lower bound, the exact three-voter census, the universal first-layer containment, or the eight-orbit quotient.

Risk: failed search is not proof of bibliographic uniqueness. An unindexed computation may contain the same small-profile census.

## Value
**PASS.** Kemeny and maximin are canonical Condorcet extensions built from substantially different optimization principles, yet they collapse exactly at three candidates. Identifying the complete first layer where this collapse fails is a natural structural boundary. The result is more informative than a single counterexample because it proves the smallest electorate, the exact incidence, the direction of every disagreement, and the symmetry types.

Self-review: passed. Independent audit: not yet performed.
