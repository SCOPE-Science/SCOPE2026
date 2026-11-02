# Scientific review: exact common-zero insertion distance at weight two

## Correctness (C): PASS

The proof reduces simultaneous zero padding to strictly positive lengths on the cyclic edges between original positions. Cyclic equivalence of two two-point supports requires equality of one of two oriented circular separations, so the optimization reduces to one equality between sums of positive gap lengths. Cancellation of intersecting arcs proves the stated exact integer minimum, including the obstruction for strictly nested arcs; increasing just one gap on the smaller exclusive side is constructive. The shared-one and disjoint-support classifications prove both the universal \(n-3\) maximum and the exact \(4n\) extremizer count. The packaged checker independently enumerates all padding allocations for every ordered two-one input pair through \(n=8\), plus checks endpoint formulas and actual padded rotations in broader ranges. This is an all-length symbolic proof, not inference from experiments.

## Originality (O): PASS with documented priority risk

The principal comparison is Thongjarast's *0-Cyclic Equalizability of Binary Words Characterized by Hamming Weight* (arXiv:2607.18452, first posted 2026-07-20). Its Theorem 3 proves feasibility, Theorem 12 gives a coarse polynomial output bound, and Section 10.1 expressly leaves exact required insertion length open. The complete freely readable primary text was inspected. Our exact instance-wise two-arc metric, optimal one-gap property, sharp \(n-3\) stratum maximum, and \(4n\) extremizer classification are not stated by those theorems and do not follow from an existence or coarse asymptotic bound.

The earlier Shinagawa--Nuida binary criterion (arXiv:2507.04916) and the general-alphabet Parikh-vector theorem (arXiv:2604.19504) permit unrestricted inserted symbols, so do not dominate the *zero-only* minimum. Their full primary texts were not available in the checked sources; abstracts and expanded public descriptions were compared. Search queries for variants of simultaneous common-zero padding, cyclic conjugacy, shortest insertion, sparse two-one supports, and sharp output length did not identify another quantitative result. Search non-detection is not a proof of priority, and an unindexed or inaccessible equivalent calculation remains a risk.

## Value (V): PASS

The first nontrivial fixed-weight stratum resolves a well-defined portion of an explicit 2026 optimal-padding question. The result is not a single example or a generic existence corollary: every pair has a closed exact cost and an optimal linear-size construction, every optimal solution can be replaced by a one-gap solution, and the sharp worst case and all its extremizing ordered pairs are classified for all lengths. This supplies a rigorous linear boundary for sparse inputs, distinguishable from the general polynomial feasibility construction. It does not claim a general-weight bound.

## Limitations and evidence

The proof does not cover varying-weight instances. The two older related full texts were not inspected, leaving some historical priority uncertainty. Checker output is corroboration, not infinite certification. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
