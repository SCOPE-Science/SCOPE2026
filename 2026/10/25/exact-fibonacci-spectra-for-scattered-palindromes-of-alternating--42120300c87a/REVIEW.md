# Scientific review

## Correctness

**PASS.** The greedy embedding is lexicographically earliest at every matched coordinate. For an alternating host, the first-bit offset and equal-versus-changed adjacent letters give the exact minimal prefix cost, with no gap in quantifiers. Reflecting palindrome halves doubles all noncentral equality indicators and accounts for the unique middle adjacency in even length or two equal/different center adjacencies in odd length. The formal geometric-series enumeration is exact and separates length-one palindromes from longer cases. Algebraic specialization and even/odd coefficient extraction give the claimed totals, while Binet asymptotics respect the parity difference. The independent finite checker confirms the full length profile for host lengths through 22 but is not used as an infinite proof.

## Originality

**PASS, subject to residual literature risk.** The 2021 Mahalingam–Pandoh source explicitly lists the first ten binary maximal counts, which are **not** claimed new, and establishes broad general bounds rather than the all-length length-refined alternating-family identity. Its q-large theorem does not cover a fixed binary alphabet once the host length exceeds four. The 2019 Müllner–Ryzhikov source addresses longest-palindromic-subsequence length, not the cardinality and complete length spectrum of palindromic languages. Related previously recorded results concern random-word expectations, bounded-run families, and alternating-string attractors; none implies the displayed all-length rational identity under a published stronger statement identified in the performed searches. Unindexed equivalents or a general weighted-automata formulation remain possible.

## Mathematical value

**PASS.** Alternating words furnish an explicit, intrinsic benchmark for the fixed-binary-alphabet case of the 2021 exact-enumeration problem. A complete length-by-length generating function, all-order Fibonacci formulas, and an exact growth exponent provide infinitely many data and a structural contrast with the growth of all subsequences. This is not an arbitrary finite slice or mere recomputation of the old ten-entry table. It does not establish global optimality, and that limitation remains explicit.

## Scope and risk

The only proved objects are alternating binary prefixes. The older 2009 bibliographic source was not read in full. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
