# Scientific review: rook-graph biharmonic heat

## Correctness
PASS. The four mutually orthogonal tensor-product eigenspace projections reconstruct the unnormalized Laplacian and its squared heat semigroup. Every kernel entry belongs to one of four explicitly evaluated equality-pattern classes. Three classes remain strictly positive; the sole possible negative class is controlled by the strictly increasing ratio \(H(t)\), proving a single positive crossing. Row-sum conservation gives the exact maximum norm; a separate monotonic exponential equation proves the unique peak. The balanced constants follow from a cubic factorization and the thin-board expansions from uniform positive-parameter series in the scaling variable. The extracted checker reconstructed the actual finite graph exponential and passed 6,465 assertions. Universal claims depend on the proof, not sampled cases.

## Originality
PASS within examined evidence. Daners–Glück–Kennedy [1,2] give broad spectral and eventual-positivity criteria, but their inspected finite-matrix and fourth-order sections do not state the four kernel classes, sharp norm, or rectangular shape scalings. The published three-level spectral barrier [3] controls the shape of positive-time sets with at most three spectral values; for unequal side lengths the rook graph has four, and the barrier is insufficient. Prior complete-multipartite and Boolean-cube formulas do not imply the two-parameter rook-graph result except in the four-cycle intersection. published-finding corpus searches and accessible historical claims were checked by operator, graph family, and statement implication. Residual risk: equivalent expressions might occur in older Hamming-association-scheme or product-graph matrix-exponential literature; priority is provisional.

## Value
PASS. Entrywise positivity is exactly simultaneous preservation of all nonnegative input data by this constant-preserving fourth-order graph smoother, and maximum-coordinate norm quantifies worst-case amplification. Rectangular rook graphs form a natural family of line graphs with up to four spectral values, for which the no-gap positivity property is not guaranteed by a general three-level result. An exact norm, unique peak, sharp cutoff, and the contrasting square/thin-board time and amplitude laws give a motivated, reusable stability classification rather than a small numerical exercise.

## Limitations and literature
Only unweighted, undirected \(K_a\square K_b\) and its squared combinatorial Laplacian are covered. No independent audit or complete literature priority search has been performed. Closest inspected primary source: [1] Sections 1, 6, and 9, and [2] Sections 1 and 6; closest inspected published mathematical record: [3] full RESULT.md.

[1] Daners, Glück, Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294 (2015).

[2] Daners, Glück, Kennedy, *Eventually Positive Semigroups of Linear Operators*, arXiv:1511.09020 (2015).

[3] *A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups* (2026), published mathematical record in published-finding corpus.

Self-review: passed. Independent audit: not yet performed.
