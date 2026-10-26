# Scientific review

## Correctness — PASS

Every scattered palindrome of a word with five nonempty binary runs has one, three or five alternating runs. The proof enumerates disjoint families by the resulting word, with the critical identity \(\min(\min(a,c+e),\min(e,a+c))=\min(a,e)\). All exponents, inequalities, and equality conditions are explicit. Exact polynomial evaluation gives the cardinality. AM–GM on \((2E,2T,c)\) and an explicit near-balanced family give the cubic extremum, and equality stability plus exhaustion of the length budget prove uniqueness of the limiting proportions. The embedded checker reconstructs all subsequence strings independently for 1024 tuples; this is finite corroboration, not an infinite proof.

## Originality — PASS, with residual risk

Mahalingam and Pandoh (arXiv:2108.02729, sections 3–5) establish general scattered-palindrome counting bounds and an alphabet-support extremal theorem; neither yields this exact fixed-five-run spectrum or the coefficient \(1/108\). Holub and Saari (DOI:10.1016/j.dam.2008.03.039) investigate palindrome-set reconstruction, longest subsequences, and extension ratios, not five-run cardinalities. Müllner and Ryzhikov (arXiv:1901.07502) investigate longest palindrome/antipalindrome lengths and circular problems rather than distinct palindrome counts. Searches for run-count aliases, exact polynomial and leading coefficient identified no published equivalent or stronger implication. Unindexed or differently formulated run-restricted enumerations remain a residual risk.

## Mathematical value — PASS

Five runs are the first binary run budget supporting a five-run scattered palindrome and hence a cubic-scale three-parameter counting family. The theorem classifies the complete length spectrum and determines the sharp extremal leading constant and its unique limiting geometry, while the preceding four-run class has only quadratic richness. This structural threshold is motivated by the studied scattered-palindromic complexity invariant rather than an arbitrary parameter slice.

## Scientific limitations

Only five-run binary words and a four-run degree boundary are covered; the exact finite-size maxima and lower-order asymptotic coefficients are not claimed. The verifier checks only finite instances. No external independent validation has been performed. Literature coverage is necessarily nonexhaustive.

Self-review: passed. Independent audit: not yet performed.
