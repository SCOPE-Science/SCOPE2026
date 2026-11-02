# Scientific review: circular numerical-range projection

## Correctness — PASS

The numerical-range support function forces a disk-centered matrix to have trace-free square-zero part of prescribed Frobenius norm. An identity specific to traceless \(2\times2\) matrices guarantees that a top singular pair can be chosen orthogonal; a Frobenius inner-product upper bound is then attained. Equality conditions classify the entire minimizer set, and a real symmetric-part argument supplies a real minimizer when both input matrix and target center are real. The algebraic proof handles scalar, normal and nonnormal cases without relying on numerical samples. The included reproducibility script passed 1,386 exact-rational identity checks and 32,810 deterministic numerical comparisons.

## Originality — PASS, subject to priority risk

Wang--Li--Lim (arXiv:2605.30181) and Li--Lim (2023) solve other norm/rank/eigenvalue nearness tasks, but the inspected theorem lists and solution sections do not provide the simultaneous exact circular field-of-values, radius, projection-uniqueness, and real-minimizer classification. O'Loughlin's unitary-orbit characterization and the SVD best rank-one approximation are foundational ingredients, not alone statements of this fixed-radius constrained target problem. Gnazzo--Guglielmi--Poloni--Sicilia (arXiv:2603.05419) handles generic structured distance to singularity, covering related free-radius objectives but not a fixed disk or the stated equality classification. Noferini--Zhukov (arXiv:2609.14828) studies real minimizers for normal and stable target sets, not prescribed circular numerical ranges. Targeted mathematical-record and literature searches did not yield an exact duplicate. Equivalent classical results hidden under nilpotent-orbit or field-of-values terminology remain a risk; absence of a search hit is not a proof of novelty.

## Value — PASS

The exact constrained metric projection is a natural finite-dimensional calibration for nonconvex numerical-range repair and has an explicit one-SVD construction. It distinguishes the unique nonnormal regime from the normal minimizer continuum, gives the exact radius-selection rule, and identifies a real-data solvability phenomenon in a conjugation-invariant nonconvex target. The result is confined to complex \(2\times2\) matrices in Frobenius norm; floating-point stability and larger sizes are not asserted.

Self-review: passed. Independent audit: not yet performed.
