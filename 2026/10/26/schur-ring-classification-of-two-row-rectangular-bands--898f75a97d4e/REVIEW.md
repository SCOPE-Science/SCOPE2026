# Review: Schur-ring classification of two-row rectangular bands

## Correctness — PASS

The proof fixes the semigroup multiplication and characteristic-zero Schur-ring convention, and derives the exact block-product coefficient \(r_X(i)c_Y(j)\) by counting factor pairs. Summing over all right or left primitive blocks gives the *necessary* common row/column profile condition; the product formula proves its sufficiency. The two possible row-profile regimes yield disjoint normal forms. Even split blocks are counted only up to exchanging the two complementary blocks. Direct full-partition enumeration agrees with the resulting count for \(1\le m\le5\); direct block-product multiplication is used through \(m=4\), and explicit automorphism-group generators reproduce every accepted partition through \(m=5\). The written argument, not finite experimentation, establishes arbitrary \(m\).

## Originality — PASS (indexed-evidence qualified)

The closest paper is Marrow–Misseldine, *On Schur Rings Over Semigroups* (arXiv:2601.09940, 2026). Sections 2.1–2.2 construct automorphic and direct-product Schur rings, providing only the \(B_nB_m\) family for rectangular bands. Its order-four and order-six computations give the two-row values \(5\) and \(13\), without a general two-row classification or generating function. The new result gives the converse automorphic theorem, the complete labeled partition classification, and an explicit count of the non-direct-product rings for every \(m\ge1\). Searches for aliases and broader coverage produced no decisive covering work. Residual risk: older/unindexed semigroup or association-scheme literature may contain equivalent classification; search failures are not proof of uniqueness. Background papers on cyclic-group and double-coset Schur rings have different ambient multiplication and cannot imply this rectangular-band count directly.

## Mathematical value — PASS

A recently defined semigroup-Schur invariant was available only through a product lower bound and small tables for rectangular bands. Two rows are the first infinite genuinely rectangular family beyond left/right zero bands, and already exhibit additional non-direct-product Schur rings. The classification explains **every** extra partition by balanced splitting of even column blocks, proves that none requires nonautomorphic origins, and yields all-parameter enumeration and a closed exponential generating function. Values \(48\) and \(184\) are beyond the source's total-order-at-most-seven census. This is a motivated complete classification, not a renaming, arbitrary finite slice, or a restatement of the known lower bound.

## Sources, verification and limitations

Main source: https://arxiv.org/abs/2601.09940 (originally public 2026-01-14), especially Sections 2.1–2.2, 5.4, 5.6, 6. Background context: https://arxiv.org/abs/2112.03422 and https://doi.org/10.24330/ieja.2029225. The reproducible verifier is `verify.py`, using only the Python 3 standard library. Neither the present classification nor its orbit claim extends here to arbitrary multirow rectangular bands. The full proof remains a written mathematical argument; no separate external or independent mathematical assessment has been performed.

Self-review: passed. Independent audit: not yet performed.
