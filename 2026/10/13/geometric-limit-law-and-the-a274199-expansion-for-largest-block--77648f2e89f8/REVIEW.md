# Self-review

## Correctness
PASS. The shortest-border decomposition is exact: a shortest border must be unbordered, and an unbordered matching prefix and suffix cannot hide a shorter border. This makes the first \(r\) peeled pairs an exact renewal construction with weights \(u_m(q)q^{-2m}\). The resulting tail probabilities converge to \(s_q^r\), the empty-center mass vanishes because its renewal coefficients are summable, and dominated convergence gives the exact mean.

The coefficient proof is independent of numerical fitting. The normalized shortest-border weights satisfy a triangular formal-series recursion. Constrained compositions satisfy the same recursion after normalization, and the composition counts are identified by induction with the defining stabilized reverse row of A274190. The verifier independently checks all finite identities used as regression evidence.

## Originality
PASS. The 2022 thesis proves only existence of the limiting expected width and tabulates numerical values. The 2023 primary paper explicitly labels the A274199 expansion as Conjecture 5. The foundational 2018 block-palindrome paper supplies the greedy factorization rule but no random-word limit theorem.

OEIS A330886 already records the binary numerical asymptotic constant, and A274199 records the coefficient sequence and a constrained-composition observation. Those records are therefore treated as close prior evidence, not as novelty support. Neither checked record supplies the all-alphabet geometric law or the proof connecting the defining A274190 reverse row to the expected width.

Residual risk remains that an unindexed or unpublished note contains the same renewal derivation.

## Value
PASS. The result resolves the explicit expected-width series conjecture and simultaneously determines the full limiting distribution. The geometric law is a structural explanation, not merely a longer coefficient table: every limiting width probability is determined by the same shortest-border renewal parameter.

Self-review: passed. Independent audit: not yet performed.
