# Scientific assessment: length-nine binary palindrome covering

## Correctness
**PASS.** The lower-bound proof applies to every circular word containing the \(32\) binary palindromes: choose one occurrence per palindrome, order the starts around the circle, and lower-bound each gap by the corresponding suffix-prefix overlap shift. The \(32\) integer potentials in `certificate.json` have sum \(81\). Direct computation of all \(496\) undirected pairs shows precisely seven positive deficits totaling \(20\). Every Hamiltonian cycle consequently has cost at least \(2(81)-20=142\). The displayed \(142\)-symbol ordinary linear word contains each of the \(32\) palindromes. Both standalone checkers pass, including a second bit-level implementation. No probabilistic or infinite extrapolation is involved.

## Originality
**PASS, with historical-priority risk.** Orenstein and Shamir's 2013 optimal reverse-complement coverage treats all DNA \(k\)-mers up to an involution, not the binary palindrome-only shortest superstring. Fici et al.'s 2015 shortest-superstring-with-reversals paper gives general overlap-graph reasoning and approximation guarantees, but no exact length-nine palindrome instance. OEIS A330022 lists \(142\) as an order-nine greedy *upper bound*; the separate shortest-superstring census A390882 stops at order eight. Therefore these inspected sources do not imply the new lower-bound certificate. Search results on reversal superstrings, palindrome coverage, the exact parameter \(142\), and relevant research claims yielded no identified equivalent or dominating theorem. A missed unpublished computation or unindexed historical proof remains possible.

## Value
**PASS.** The smallest ordinary word containing all palindromes of a fixed length is a natural shortest-common-superstring invariant with a separately maintained public sequence. At order nine, the previously recorded upper bound lacked a corresponding documented lower bound. The integer certificate settles that question exactly using only \(32\) vertex values and seven exceptional pairs, and simultaneously settles the related shortest circular covering length. This is a concrete closure of a motivated finite-length gap, not an arbitrary string statistic or merely a new implementation of a general algorithm.

## Closest literature and limitations
The closest exact database is OEIS A330022; the number \(142\) was already publicly displayed as an upper bound in 2025, and no priority for the numerical guess is claimed. The mathematical contribution is its exact certification. A390882 reports shortest-superstring counts through order eight, but not at nine. The Orenstein–Shamir and Fici et al. problems share overlap machinery without resolving this specialized optimum. The theorem makes no assertion for other lengths or about the number of all optimizing words. Indexed-source coverage cannot exclude all earlier, unindexed work.

Self-review: passed. Independent audit: not yet performed.
