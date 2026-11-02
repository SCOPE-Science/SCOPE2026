# Scientific review

## Correctness (PASS)

The statement has exact quantifiers: an arbitrary even \(n\ge4\), a shared complete strict rank order, one selected participant, and one adjacent position in their list. Mutual first choices force all unaffected pairs. There are precisely two partner-demoting cases, one creating a different uniquely stable four-person block, the other creating an odd directed first-preference cycle of three people with only lower-ranked external partners. In the latter case every perfect matching is blocked. The \(n(n-2)\) choices yield exactly \(n/2-1\) impossible and the same number changed-but-stable. The analytical argument covers all sizes; the packaged exhaustive integer checker independently verifies every one-swap instance for sizes \(4,6,8,10\). No finite run is treated as an infinite proof.

## Originality (PASS, qualified)

The original shared-order solvability and its adjacent-pair matching are prior knowledge, not claimed as discoveries. General odd-cycle obstructions are also known. Chin–Michelen (arXiv:2601.07612) consider independent random rankings and asymptotic nonexistence, not a single Kendall inversion around consensus. Bredereck–Heeger–Knop–Niedermeier (arXiv:2009.14191) address master lists primarily in multidimensional roommate matching and contain the shared-order baseline, but not this complete single-swap classification. Chen–Schlotter (arXiv:2502.01215) study arbitrary swap bribery/control complexity rather than the precise one-swap structural law. A related published four-person isomorphism census tabulates unsolvable configurations but does not imply the all-size characterization and exact probability without further structural proof. Previously unindexed special-case literature remains a genuine priority risk.

## Value (PASS)

A master ranking is a natural benchmark of perfectly aligned preferences. One adjacent transposition is the smallest nonzero Kendall distortion, so a complete sharp description of whether it preserves unique stability is substantively motivated. The result distinguishes loss of solvability from a changed but unique stable matching, and gives exact all-size frequencies, useful in modeling preference-data errors and robustness near consensus. It is not merely a constructed four-person counterexample or a renamed textbook lemma.

## Verification and limits

The code independently enumerates complete perfect matchings and checks blocking pairs, not just the predicted output. No independent expert audit has taken place. The all-size claim does not cover more than one inversion, incomplete lists, ties or random independent rankings.

Self-review: passed. Independent audit: not yet performed.
