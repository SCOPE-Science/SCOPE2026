# Mathematical review

## Correctness — PASS

The theorem concerns the total internal path length of a uniformly inserted unbalanced binary search tree, conditional on the time at which its maximum key is inserted. The deletion lemma reconstructs the tree on the remaining keys and counts precisely the depth of the maximum and its descendants, yielding \(P_t-P_-=L_{t-1}+n-1-R_{t-1}\). Subtraction establishes the pathwise gap, without an independence assumption. Direct sampling-without-replacement counting proves the decrement tails. Independence of prefix relative order and unordered prefix set proves the increment generating function and harmonic mean. Every base permutation through seven keys was replayed by an independently implemented insertion algorithm and all exact-rational assertions passed. Exhaustion in small orders is not substituted for the unrestricted combinatorial proof.

## Originality — PASS (residual historical-priority risk)

The comparison distinguishes generic marginal path-length results from the precise simultaneous conditional stochastic ordering, finite decrement tails, and equality at the final two slots. Prodinger (arXiv:math/9910070v1) gives an earlier permutation representation and marginal moments; the material inspected did not assert this coupled conditional-order theorem. Holmgren and Janson (arXiv:1406.6883v1) treat fringe-tree functionals and limit laws, not insertion-age conditioning of total path length. The published records search found nearby work on random-BST root imbalance and recursive-tree root attachments, neither of which logically implies the maximum-insertion-slot identity. The Mahmoud–Pittel 1988 insertion-path paper remains incompletely inspected, so implicit earlier coverage is possible; no independent priority audit has occurred.

## Value — PASS

The maximum key's arrival time is a natural observable of the randomized BST construction, and total internal path length is a fundamental search-cost statistic. A *single* natural coupling orders all \(n\) conditional laws, identifies the two terminal slots as pathwise indistinguishable, and supplies exact laws for every adjacent decrement. The theorem is stronger than moment comparison and describes the dependence between a marked key's arrival age and an entire global cost functional. It is not presented as a general theorem for balanced trees or as a claim that the entire path-length distribution factors into independent components.

Self-review: passed. Independent audit: not yet performed.
