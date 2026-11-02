# Scientific review

## Correctness — PASS

The finite domain is explicitly fixed at all binary order-five de Bruijn necklaces, with 32 distinct rotations each and conventional non-increasing Chen–Fox–Lyndon factorization. Every de Bruijn successor induces one of the 65,536 four-suffix feedback maps; each such map is a permutation and the full-orbit predicate is necessary and sufficient. The separate 16-vertex Euler graph enumeration produces exactly the same 2,048 canonical cycles. Both a direct definition-level Lyndon-prefix method, checked for Lyndon factors in non-increasing order, and Duval's algorithm agree on all 65,536 rooted traversals. The attached executable has been run and returned `VERIFY_OK` with both integer distributions. The result is an exact finite theorem, not an extrapolation.

## Originality — PASS, with historical risks

The nearest established results are Fredricksen–Maiorana's Lyndon-concatenation construction of a distinguished de Bruijn sequence; the ranking and decoding results of Kociumaka–Radoszewski–Rytter; Daykin's general factorization algorithms; and Bonomo–Mantaci–Restivo–Rosone–Sciortino's connection between conjugates, Lyndon factorization and suffix sorting. Their checked statements concern special-sequence construction, algorithmic factorization, or ordering/decoding—not the exact count of Chen–Fox–Lyndon factors over **every root of every** order-five de Bruijn cycle. Published-literature queries and semantic mathematical-record searches found no identical or stronger table. This is evidence of non-coverage, not a proof of global priority. The 1978 original full text and some potentially unindexed enumeration records remain risks.

## Value — PASS

Lyndon factorizations are canonical primitives for lexicographic combinatorics and text algorithms; de Bruijn cycles are canonical finite universal-factor strings. FKM construction makes their interface especially natural. The complete rooted census shows that full five-factor coverage does not control the number of Lyndon factors: the range is 1–16, with exact frequency distribution, exactly one one-factor cut per cycle, and a nontrivial sharp distribution of the *maximum* across roots. Order five is the first binary order with 2,048 distinct necklaces, and the complete result gives a reproducible baseline for comparing construction schemes and root sensitivity. The value is the natural finite classification, not an asserted higher-order consequence.

## Closest literature and limitations

- Kociumaka, Radoszewski and Rytter, arXiv:1510.02637 (original 2015 posting): specifically rank/unrank of Lyndon words and decoding lexicographically minimal de Bruijn sequences, rather than the complete rooted factor-count spectrum.
- Fredricksen and Maiorana, *Discrete Mathematics* 23 (1978), 207–210: distinguished necklace-concatenation construction, not the claimed all-cycle histogram; original full text was not inspected.
- Daykin, *JCMCC* 77, 65–74: general algorithms for Lyndon unique maximal factorization but not de Bruijn enumeration.
- Bonomo et al., *DLT* 2013, 131–142: conjugacy, Lyndon words, BWT and suffix-array sorting; the conference slides and abstract were inspected, but the complete article text was not.

Higher binary orders, nonbinary alphabets, and alternate factoring conventions are outside the result. Exhaustive independent historical-priority verification is not claimed.

Self-review: passed. Independent audit: not yet performed.
