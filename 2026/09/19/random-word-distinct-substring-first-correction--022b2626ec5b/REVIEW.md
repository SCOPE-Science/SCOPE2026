# Review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

The proof has two independent sides. The deterministic side uses only the alphabet cap D_{n,k} <= d^k. The probabilistic side bounds the occupancy deficit by the number of equal pairs of length-k windows. The potentially delicate point is overlap: for windows shifted by s<k, equality imposes period s on k+s independent uniform letters, leaving exactly s free symbols, so the matching probability is exactly d^{-k}, the same as for disjoint windows. Summing pair probabilities gives the stated finite upper bound.

The transition index m=floor(log_d n) was checked algebraically in both directions. The geometric tail is O_d(n) because d^{-m} <= d/n, and the alphabet-cap contribution is O_d(n) because d^m <= n. These yield matching n log_d n leading terms. The additive comparison with the maximum follows directly by placing the maximum between the deterministic cap and the random expectation.

The compact verification artifact exhaustively enumerates binary words through n=16 and ternary words through n=10 and confirms the finite sandwich throughout those ranges.

## Originality

The closest recent source is Godbole, arXiv:2609.19409 (2026), which studies exactly the all-length expectation. Its binary Theorem 2.3 gives a lower bound with a 3 n log_2 n loss term, while its uniform d>=3 equation (30) gives a 2 n log_d n-scale loss. It does not state the coefficient-one first correction proved here.

Flaxman, Harrow and Sorkin (2004) prove that random words are asymptotically maximal for distinct substrings and identify the transition range between about log_d n and 2 log_d n, but the inspected comparison does not state an additive n log_d n + O(n) deficit or O(n) distance from the optimum. Ahmadi and Ward (2020) give detailed first-order asymptotics for kth subword complexity when k=Theta(log n); their stated results concern individual levels rather than the all-length sum. OEIS A340885 and a 2021 computational note provide exact finite binary totals without a located statement of this asymptotic formula.

Searches were made using distinct-substring, subword-complexity, random-word, suffix-tree/LCP, and n log n formulations. No source located stated the finite sandwich, the coefficient-one all-length correction, or the explicit O(n) additive optimality consequence. The originality assessment is therefore to the best of our knowledge.

A residual risk remains from older analytic suffix-tree and trie literature, including work of Jacquet and Szpankowski: sufficiently general path-length or profile theorems may imply the same correction after a standard translation, even if the distinct-substring result is not presented in this form. This prevents any stronger originality claim.

## Value

The result sharpens the first nontrivial scale in the new all-length expectation problem: the leading quadratic term was already known, while the logarithmic deficit coefficient was not identified in the recent source. The argument also replaces the transition-region Poisson analysis by an elementary exact overlap identity and yields a finite-n sandwich. The additive O(n) comparison to the extremal count strengthens the earlier statement that random words are merely asymptotically optimal on the n^2 scale.

## Limitations

The result is restricted to fixed d and uniform i.i.d. letters. It does not identify the O_d(n) second-order term, does not cover general nonuniform memoryless sources, and does not address variance or concentration. Older suffix-tree/trie literature remains a residual originality risk. No independent validation is claimed.
