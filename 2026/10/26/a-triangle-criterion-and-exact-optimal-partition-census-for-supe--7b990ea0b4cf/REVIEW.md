# Review of the triangle criterion for super coalitions

## Correctness
**PASS.** With no isolates, every one-vertex deletion is super dominating. The hypothesis that super domination number is at least \(n-2\) rules out all complements with three or more vertices. A four-block coalition therefore has exactly one nonsingleton class and three singleton classes; the three required private-witness remainders encode a triangle in the two-deletion graph. The reverse construction gives a coalition partition. For three blocks, a coalition is possible exactly when its opposite block is an eligible singleton or two-deletion edge, and all classes must have a partner. Counting the three choices of small pairs yields the stated binomial/edge/matching formula with correction for small tripartitions at orders five and six. The exhaustive verifier independently tests 2,388 qualifying graphs at orders five through seven. Finite testing is not used as an infinite proof.

## Originality
**PASS, subject to bibliographic uncertainty.** The founding full text, Alikhani and Ghanbari's *Super Coalition Number in Graphs* (arXiv:2607.22686, submitted July 15, 2026), proves \(C_s(G)\le n+2-\gamma_{sp}(G)\) in Theorem 3.2 and asks for equality cases in Problem 7.1. It does not state the triangle criterion or exact partition census. The public indexed record *All super dominating sets of complete multipartite graphs* provides and owns the exact eligible-pair rule for that special family, which is credited rather than claimed new. Targeted published-record and literature comparisons found no equivalent general theorem. The full text of the separate multipartite record was not available, and unindexed overlaps remain possible.

## Mathematical value
**PASS.** Sharp attainment, exact multiplicities of maximal partitions and the universal three-class census answer natural structural enumeration questions for all graphs at the high super-domination boundary. The reduction to triangles and matching numbers of an auxiliary graph is stable under graph size and supplies concrete infinite-family consequences such as complete multipartite formulas.

## Remaining limitations
The theorem assumes \(n\ge5\), no isolates and \(\gamma_{sp}(G)\ge n-2\); an efficient general method for finding qualifying graphs is not claimed. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
