# Scientific review

## Correctness: PASS

The identity is proved by a disjoint partition according to the number of one-symbols in a palindromic subsequence. The zero-only and one-one counts are intervals; two-one palindromes correspond to the union of three explicit lattice rectangles, two of which simplify to a base rectangle and at most one positive excess rectangle; three-one palindromes are independently parametrized by two zero lengths. This establishes all parameters, including zero gaps and equality of exterior gaps. The restricted optimum follows from an exact concave quadratic, with unique integer maximizer. Two independent finite algorithms and a restricted-extremum check corroborate the proof; they are not the basis of the infinite claim.

## Originality: PASS, subject to residual priority risk

Semantically related published and indexed work was compared by object and implication. Elzinga–Rahmann–Wang (2008) addresses general subsequence-enumeration algorithms, not the sparse-word palindrome-specific formula or symmetric-source extremum in the available author overview. Guo–Shallit–Shur (2015), whose full arXiv article was inspected, treats palindromic pairs, rich words, conjugates and antipalindromes, and does not state this scattered-subsequence formula. Searches of published mathematical research records for palindromic subsequences with exactly three ones and four zero gaps returned no covering claim. The earlier all-subsequence count for weight three does not imply the palindrome-specific count: a same-total/different-palindrome example is supplied in RESULT.md. Residual risk: unavailable full text of the 2008 paper and unindexed specialized results may contain an equivalent formula.

## Value: PASS

The exact four-gap law removes the need for quadratic-length interval dynamic programming on this natural low-weight family, and the restricted extremal result classifies *all* maximizing symmetric words at every admissible length. It distinguishes palindrome-constrained deletion observations from unconstrained subsequence spectra. This is not merely a numerical table: the rectangle decomposition gives a structural account of the dependence on asymmetric zero gaps and a clean equality characterization for mirror-symmetric sources. The theorem is intentionally limited to weight three; it does not claim a general unrestricted optimum.

## Closest literature and limitations

- C. H. Elzinga, S. Rahmann, H. Wang, *Algorithms for Subsequence Combinatorics*, TCS 409 (2008): an algorithmic subsequence framework, abstract/author overview inspected; full text not available in this review.
- C. Guo, J. Shallit, A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112 (2015): full accessible arXiv text inspected, with no reported scattered-palindromic-subsequence count.

Self-review: passed. Independent audit: not yet performed.
