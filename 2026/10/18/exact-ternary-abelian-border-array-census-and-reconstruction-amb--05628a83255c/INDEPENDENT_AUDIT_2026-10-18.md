# Independent mathematical audit

## correctness

PASS

Every global alphabet renaming orbit has one restricted-growth representative. For each prefix i and candidate border k, the abelian condition is equality of three symbol-count differences; the 4-bit-per-entry encoding is injective up to n=16. Independent C++17 exhaustive enumeration over all 3^15 words with first symbol 0 (different from canonical restricted-growth enumeration), division by two for nonconstant relabeling classes and direct prefix-count checks recovered all 16 rows including 1151825 at n16; its complete 353-level n16 histogram matched the committed CSV byte for byte, including SHA-256 6cd4f6d044008762b8bba80e45ad656d7de02b9eb3d5c2539fe64348157ed3b1. For the infinite extremal claim, b_i=i-1 iff w_i=w_1, so an array fixes exactly which later positions repeat the first letter; any nonzero array fixes at least one such position, leaving at most two choices per other position, giving at most 3*2^(n-2) labeled words, versus 3*2^(n-1) for all zero. Canonical class count follows after fixing first 0 and factoring symbol permutation. Finite exhaustiveness is not extrapolated beyond n16.

## originality

PASS

Habib-Shamil-Rahman prove the binary array count and only an upper bound for ternary arrays T3(n)<=(3^(n-1)+1)/2, not the exact n<=16 census or inverse-fiber histogram. Blanchet-Sadri-Chen-Hawes and Christodoulakis et al concern binary words by abelian border features, not the full distinct ternary all-prefix array distribution. No matching Resultary table identified, with finite-enumeration duplication a residual priority risk.

## value

PASS

The exact finite census and full ambiguity histogram give motivated natural invariants of ternary abelian border arrays and benchmark the inverse reconstruction ambiguity left unspecified by the known ternary upper bound. The infinite maximal-fiber theorem identifies a qualitatively sharp worst-case reconstruction obstruction independent of any unproved asymptotic census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
