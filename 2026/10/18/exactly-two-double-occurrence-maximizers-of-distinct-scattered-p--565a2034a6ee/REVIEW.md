# Scientific review

## Correctness — PASS

The support lemma proves the sharp upper bound without relying on computation. In a double-occurrence word, a palindrome of specified symbol support has either all paired letters or exactly one odd center; paired occurrence intervals must be nested. If an even palindrome is available, at most one odd palindrome exists. Otherwise three potential centers would force every pair of intervals to be nested, a contradiction. Equality on two-symbol supports forces all first occurrences before all second occurrences. Equality on full support then forces either the reversed second half or its unique top-two swap. A direct case analysis of supports verifies both constructions and the length-resolved formulas. The standalone checker independently enumerates matching words through five symbols and second-half permutations through seven symbols.

## Originality — PASS, residual risk recorded

The sharp total \(2^{q+1}-2\) and the nested extremal witness were already obtained by Mahalingam and Pandoh (arXiv:2108.02729v1, Proposition 5.1 and Theorem 5.4). They are not claimed as novel. The same paper explicitly identifies characterization of maximally scattered-palindromic-rich words as an avenue for study. The new claim determines **all** equality cases under the natural requirement of two occurrences per letter, showing precisely two renaming classes, and gives their full parity-resolved distributions. The inspected earlier literature on longest palindromic subsequences does not imply this equality classification. A complete-text comparison with Holub and Saari (2009) was not available; it remains a secondary bibliographic risk.

## Mathematical value — PASS

The classification identifies the complete equality structure in the balanced boundary case \(n=2q\) of a published extremal problem. The nonpalindromic second family is not exhibited by the earlier nested construction. Its precise spectrum reveals how swapping the two inner letters converts even palindromes into additional odd palindromes while preserving the exact maximum. This is a natural, non-arbitrary all-alphabet theorem, not a next-index computation.

## Closest literature and limits

The nearest source is Mahalingam–Pandoh, *Counting Scattered Palindromes in a Finite Word*, arXiv:2108.02729v1 (2021), inspected through the extremal propositions and conclusion. Other inspected work: Müllner–Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502v1 (2019). The theorem is restricted to double-occurrence hosts; no classification for arbitrary symbol multiplicities is asserted. Search-based originality is not proof against unindexed literature.

Self-review: passed. Independent audit: not yet performed.
