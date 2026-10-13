# Review

## Correctness

PASS. Kernel dimension is invariant under invertible row and column transformations of \(B\), with \(U\mapsto PUQ^{-T}\). In rank-normal form, all \(k(r-t)\) trailing entries are free, the lower-left block vanishes, and the leading \(t\times t\) block is symmetric, giving \(t(t+1)/2\) more dimensions. Rank-nullity gives the image rank. The primary Proposition 5.3 identifies fixed-residue shortest lifts with an affine translate of this kernel, so its cardinality is exactly the displayed power of two. Exhaustive finite replay checks every binary matrix through \(3\times3\).

## Originality

PASS. The primary June 2026 paper parametrizes all fixed-residue shortest lifts by \(\ker(U\mapsto BU^T+UB^T)\) but does not state the kernel dimension or number of lifts. Searches under the source identifier, exact map, kernel-dimension, lift-count, and closed-form aliases found no covering result. The new statement converts an instancewise kernel computation into a rank-only closed formula.

## Value

PASS. The source's algorithm enumerates these lift fibers and uses them to find twelve database-improving codes. The formula gives the exact size of that search stage, identifies rank as its only binary-block invariant, and quantifies how the search cost changes with rank.

Self-review: passed. Independent audit: not yet performed.
