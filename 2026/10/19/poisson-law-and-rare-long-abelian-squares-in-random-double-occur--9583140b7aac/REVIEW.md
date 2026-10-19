# Mathematical review

## Correctness — PASS

Each labeled double-occurrence word corresponds, modulo the exactly \(q!\) possible relabelings, to a perfect matching. The cross-half matching criterion is necessary and sufficient for Abelian-square windows, yielding an exact formula for all first moments. The ratio bound across half-lengths gives an \(O(q^{-1})\) probability of *any* square longer than two letters. For the adjacent-pair statistic, disjoint path-edge counting yields explicit binomial moments; the absolutely convergent binomial-inversion bound proves total-variation convergence to Poisson(1), including the stated rate. Independent brute enumeration of the finite sample spaces verifies the combinatorial formulas for the first seven alphabet sizes; finite computation is not used as proof of the asymptotic claims.

## Originality — PASS, subject to identified residual risk

Directly relevant papers have been compared by their mathematical conclusions: the 2018 double-occurrence insertion-equivalence classification, the 2022 Abelian-word survey's counting/avoidance results, and the 2023 noncontiguous shuffle-square theory. Neither fixed-alphabet Abelian-square counts nor deterministic insertion relations imply the local random matching law here. Rare adjacent matched edges have classical Poisson-type behavior and are not independently claimed as new. The new substantive comparison is the uniform all-half-length window suppression that converts a rare-edge law into the total Abelian-square law. An exact equivalent result under specialized matching or chord-diagram terminology may remain unindexed.

## Mathematical value — PASS

The uniform two-occurrence ensemble is mathematically natural: its words are ordered chord diagrams with arbitrary letter labels. In it, every contiguous Abelian square of length at least four must form a complete cross-half matching. The theorem proves that these longer squares vanish in probability, while an asymptotically Poisson number of adjacent repetitions remain, giving the nonzero exact limiting avoidance probability \(e^{-1}\). This explains a nontrivial difference from fixed-small-alphabet avoidance/average-count problems. The result covers all alphabet sizes and all possible Abelian-square window lengths, not a selected computational slice.

## Literature, limits, and audit status

Closest published full texts: Cruz–Ferrari–Jonoska–Nabergall–Saito (arXiv:1811.11739, first published November 28, 2018); Fici–Puzynina (arXiv:2207.09937, first published July 20, 2022; Section 4.3); Grytczuk–Pawlik–Pleszczyński (arXiv:2308.13882, first published August 26, 2023). The result is restricted to linear words with each label occurring exactly twice; the Poisson estimate has a non-optimized constant and could conceivably be equivalent to a differently named rare-pattern theorem. No expert or independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
