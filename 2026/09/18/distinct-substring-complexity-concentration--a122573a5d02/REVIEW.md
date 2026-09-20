# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof has three independent ingredients.

First, for any two starting positions, equality of two length-\(r\) blocks has probability at most \(p_*^r\), even when the blocks overlap. In the overlapping case, revealing the later block from left to right turns equality into \(r\) successive constraints, each requiring an independent fresh symbol to take one already determined value of mass at most \(p_*\). A union bound therefore gives
\[
\mathbb P(L_n\ge r)\le\binom n2p_*^r.
\]

Second, if two deterministic strings both have longest repeated substring at most \(\ell\), then all substring counts of lengths greater than \(\ell\) are maximal and identical. At length \(k\le\ell\), changing one coordinate changes at most \(k\) windows and hence changes the number of distinct window values by at most \(k\). Summing over \(k\le\ell\) gives the Hamming Lipschitz constant
\[
c_\ell=\ell(\ell+1)/2.
\]
This endpoint argument does not require intermediate strings along a Hamming path to stay in the good set.

Third, a McShane extension of the statistic from the good set, clamped to its deterministic range \([0,n(n+1)/2]\), preserves this Lipschitz constant. Standard bounded differences then gives the displayed sub-Gaussian tail for the extension. The extension differs from the original statistic only on the longest-repeat exceptional event, which controls both the centering shift and the variance remainder.

The deterministic Lipschitz lemma was also exhaustively checked for every binary string of length at most seven and every admissible cutoff. These finite checks are supportive only; the published result rests on the proof above.

For \(\ell_n=\lceil8\log n/\log(1/p_*)\rceil\), the exceptional probability is at most \(1/(2n^6)\), while \(c_{\ell_n}=O((\log n)^2)\). This yields the stated \(O(n\log^4 n)\) variance bound and \(O_{\mathbb P}(\sqrt n\log^2 n)\) fluctuation scale. Edge cases were checked: a uniform alphabet gives exact pair-collision probability \(d^{-r}\), while the excluded case \(p_*=1\) is deterministic and has zero variance.

## Originality

Janson, Lonardi and Szpankowski (2004) explicitly state that asymptotic analysis of the variance of the total string-complexity index remained open. Their paper gives a sharp mean expansion and probabilistic bounds based on suffix-tree height, but not a variance or concentration theorem for the total index.

Gheorghiciuc and Ward (2007) analyze the expected fixed-length subword complexity, including nonuniform memoryless sources. Ahmadi and Ward (2020) derive first and second moments for the fixed-\(k\) subword complexity. Those fixed-length moment results do not resolve the covariance terms across all lengths in the total complexity.

Godbole (2026) revisits the expected total number of distinct substrings and explicitly asks whether concentration around the expectation can be understood by estimating the variance. The present contribution is restricted to a finite-sample concentration inequality for the total complexity, the resulting \(O(n\log^4 n)\) variance upper bound, and the \(O_{\mathbb P}(\sqrt n\log^2 n)\) fluctuation scale.

Searches were made under the terms distinct substrings, string complexity, sequence complexity, subword/factor complexity, variance, concentration, longest repeated substring, suffix tree, and combinations thereof, as well as by the main source-paper titles. No equivalent total-complexity concentration theorem or variance upper bound was located in the inspected literature. The older random-trie and suffix-tree literature is broad and remains the principal residual originality risk; an equivalent consequence under different terminology may exist. The originality judgment is therefore to the best of our knowledge.

## Value

The result gives a direct partial answer to a variance/concentration question stated both in the classic 2004 sequence-complexity paper and again in a 2026 paper. It improves the available probabilistic description from an order-\(n\log n\) deficit from the maximal \(n^2/2\) scale to concentration around the exact mean on the much smaller \(\sqrt n\,\log^2 n\) scale.

For uniform alphabets, combining the concentration theorem with the known sharp mean expansion promotes the deterministic expectation asymptotic, including its periodic order-\(n\) term, to a sample-level expansion with stochastic error \(O_{\mathbb P}(\sqrt n\log^2 n)=o(n)\).

The proof also isolates a reusable mechanism: the only strings on which the complexity can have large coordinate sensitivity are those with unusually long repeated substrings, whose probability decays exponentially under an i.i.d. nondegenerate source.

## Limitations

The result is an upper bound, not an asymptotic evaluation of the variance. The logarithmic exponent may be nonoptimal. No matching lower bound, limiting variance constant, or central limit theorem is proved. The theorem assumes independent symbols and does not cover the general mixing models treated in part of the 2004 work. The literature search cannot exclude an equivalent consequence hidden in older random-trie or suffix-tree results.
