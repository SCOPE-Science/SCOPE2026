# Review of the exact shortest-supersequence family

## Correctness
PASS. The proof establishes the length lower bound, the exact boundary criterion for shortest supersequences, and a two-sided, parameter-uniform forced-step bijection. Its crucial termination lemma counts milestone events and shows all required insertions occur before the final input letter. The packaged standalone checker independently confirms 84 DP parameter pairs, 14,706 bijective bridges, and 5,960 direct short-word tests. Computational checks support, but do not replace, the all-parameter proof.

## Originality
PASS, subject to unindexed-priority risk. Lin (arXiv:2609.26650v1) proves the general binomial upper bound and supplies the natural comparison; the checked statement does not give this explicit periodic equality case or a balanced bridge bijection. Sopp et al. (arXiv:2603.22591v1) address general minimal-supersequence enumeration algorithms. The nearby opposite-single-block calculation has different input strings and cannot imply the claimed repeated-run result for both parameters at least two. Targeted published-record and literature searches yielded no statement that dominates the two-parameter equality family. The available inspection of the Sopp text was limited to its abstract/introduction and accessible exposition, and earlier full papers may conceal equivalent coverage.

## Value
PASS. Equality in a universal sharp binomial supersequence bound is achieved by an infinite two-parameter family whose longest common subsequence has positive length, not merely by disjoint-alphabet examples. The explicit inverse transducer identifies every shortest supersequence and enables direct enumeration or sampling from a balanced-word model; this resolves a structurally motivated equality-case question.

## Limits and closest literature
The finding does not classify longer deletion-minimal common supersequences and does not improve the general arbitrary-input bound. Priority should be checked independently against all older counting literature, especially earlier general common-supersequence estimates.

Self-review: passed. Independent audit: not yet performed.
