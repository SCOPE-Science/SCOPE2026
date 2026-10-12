# Scientific review: mixed length-three block-counting constant runs

## Correctness — PASS
The exact change indicator is obtained by writing the two neighboring binary integers as a common prefix followed by `0` and trailing ones, versus `1` and trailing zeros. Because all six tested patterns have length three and both symbols, the indicator depends only on two prefix bits, the last at most four suffix bits, and two explicitly handled exceptional short odd parts. A 64-phase exhaustive exact-rational residue case split checks all possible separations of successive change indicators for all sufficiently large positions; a finite boundary check covers the remaining starts. The same residue cases and the elementary equidistribution of odd residues at each fixed \(2\)-adic valuation prove every asserted rational density. The attached standard-library verifier independently replays all cases. It does not infer an infinite theorem from finite samples: a symbolic carry-locality reduction makes the complete case check finite.

## Originality — PASS, with residual risk
The closest same-object source is Abram–Hu–Li (arXiv:2304.14595), which studies morphic generation and algebraicity of the block-counting sequences, not maximal constant-run spectra or density distributions. Hendel (arXiv:2505.20547) investigates maximal runs for the structurally different all-one pattern family; Li (arXiv:2406.16411) studies orthogonality and partial sums; Konieczny (arXiv:1905.03283) studies correlation classification. None of the inspected source results implies the six mixed-pattern tables. Targeted claim and parameter searches in publicly available mathematical records found no equivalent result. Absence of a search hit is not a uniqueness proof; unindexed earlier computations remain a genuine possibility.

## Value — PASS
The theorem completely resolves a natural elementary invariant, maximal constant-run length, in the first nontrivial family of six genuinely mixed digit patterns and goes beyond occurrence classification to exact rational frequencies for every attainable ordinary length. The complement pairs unexpectedly have identical asymptotic distributions despite distinct origin-only anomalies. This is a natural complete classification of a motivated family rather than a picked interval or a routine restatement of existing automaticity theorems.

## Scope and limitations
The definition explicitly excludes padded leading zeros and uses overlapping occurrences; alternative conventions can change short boundary runs. The proof gives exact limiting run-start densities, not distributions conditional on output symbol, and only covers mixed length-three patterns. Independent validation and an independent originality audit are not asserted.

Self-review: passed. Independent audit: not yet performed.
