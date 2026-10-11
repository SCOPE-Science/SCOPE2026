# Review

## Correctness
PASS. Each operator
\[
\Lambda_j=P_j+2^{-2j}I
\]
is positive, diagonal, invertible, and bounded below. Its norm tends to \(1\), while its minimum modulus tends to \(0\). The full \(g\)-frame sum is exactly
\[
\sum_k\left(1+2^{1-2k}+\frac1{15}\right)|x_k|^2,
\]
so the family is a \(g\)-frame.

For
\[
D_j=2^{-j}\Lambda_j^{-1},
\]
one has
\[
D_j\Lambda_j=2^{-j}I,
\]
so the scaled family is tight with bound \(1/3\). Yet
\[
\|D_j\|=2^j,
\]
and the ambient block diagonal operator is unbounded.

## Originality
PASS. The 2021 proposition and 2024 theorem were inspected together because the latter is a direct \(K\)-\(g\)-frame extension of the former. Searches covered exact identifiers, theorem labels, errata, the operator-norm/minimum-modulus distinction, ambient block boundedness, and range-restricted formulations.

The closest published unbounded-scaling result concerns scalar \(K\)-frame coefficients and boundedness of a diagonal composition on an analysis range. It does not imply this counterexample, whose analysis blocks are invertible operators with positive limiting operator norm.

## Value
PASS. The false inference appears in a criterion intended to produce a globally bounded block preconditioner and is propagated into a later \(K\)-\(g\)-frame theorem. The example is not a boundary pathology: all analysis blocks are positive diagonal isomorphisms and the scaled family is exactly tight. The correction identifies analysis-range control as the relevant invariant.

## Limitations
No weakest additional hypothesis for global ambient-block boundedness is claimed. The result does not reassess other scalability statements in the two papers, and a nonindexed correction may exist.

Same-model review: passed. Independent audit: not yet performed.
