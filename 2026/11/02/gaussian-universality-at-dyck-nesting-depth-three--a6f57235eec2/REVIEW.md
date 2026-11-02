# Scientific assessment: Dyck nesting height and universality

## Correctness — PASS
The proof identifies the universal-subsequence index with the count of greedy binary arches, constructs a three-state weighted transition representation, and uses the unambiguous first-return decomposition of bounded-height Dyck words. Exact symbolic inversion of three matrix recurrences yields the asserted rational generating functions. The height-two law follows by coefficient extraction. For height three the simple dominant pole, separated remainder of the pole spectrum, nonvanishing amplitude, and explicit implicit derivatives yield a quasi-powers central limit theorem with strictly positive variance. The standalone verifier reproduces symbolic identities, independent finite enumeration, direct subsequence tests and the variance constants; finite checks are not the infinite justification.

## Originality — PASS with stated uncertainty
The inspected 2023 Dyck-word paper addresses nesting and avoidance, not this statistic. The 2023 arch-factorization paper gives the index construction rather than a bounded-height census. The 2023 regular-language paper provides a general counting method, which can handle the underlying finite automata, but does not assert the displayed height-three rational identity, its Gaussian constants, or the sharp fluctuation-order transition. The distinct earlier all-height Dyck enumerator does not mark nesting height and cannot be specialized to recover this joint distribution. published-finding corpus semantic and exact-parameter searches revealed no equivalent claim in the retrieved records, but search absence is not a proof of priority. A stronger, currently unindexed special-case formula could supersede this result.

## Value — PASS
Height three is a natural nesting constraint in the literature on repetition-free Dyck words. The exact index distribution describes a standard scattered-subsequence invariant under this constraint. The result exposes a nontrivial boundary: the index under height two concentrates on two adjacent values with exponentially decaying variance, while adding just one unit of allowed height creates linear fluctuations and a nondegenerate Gaussian law. This phenomenon and its explicit constants are not a routine restatement of the general regular-language counting algorithm.

## Limits
The theorem has no assertion for height four or greater and no claim about nonuniform probability models. All infinite statements rest on the formal matrix recursion and singularity argument, not on finite verification. Similarity searches may miss an equivalent existing formula, and no independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
