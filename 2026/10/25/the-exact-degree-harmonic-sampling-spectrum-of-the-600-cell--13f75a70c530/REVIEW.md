# Scientific review: exact-degree harmonic sampling on the 600-cell

## Correctness — PASS

The degree-\(n\) spherical-harmonic kernel on \(S^3\) is the \(SU(2)\) character of \(\operatorname{Sym}^n(\mathbb C^2)\), up to explicit positive normalization. Decomposing this representation over the binary icosahedral group and using regular-representation Fourier orthogonality gives the stated nine-level Gram spectrum with multiplicities \(d_i^2\). The affine-\(E_8\) Clebsch–Gordan recurrence computes multiplicities without fitting; a 60-step Chebyshev identity proves the all-degree statement and strict eventual rank threshold. Exact modular Gram computations in `verify.py` agree independently for each degree 0 through 60. No numerical finite check is used as an infinite proof.

## Originality — PASS under bounded comparison

The closest literature studies geometric design strength and vanishing spherical *moments* (Mamone–Pileio–Levitt 2010; Boyvalenkov–Danev 2001), the \(E_8\) group correspondence (Dechant 2013), and complete scalar harmonic strengths (Hirao–Nozaki–Tasaka 2025). Hirao et al. explicitly cover the absence of the trivial harmonic at degree 58, so that observation is **not** claimed as new. The complete nine-isotypic Gram spectrum, periodic rank table and sharp interpolation thresholds are different statements and not supplied by the inspected full-text results. Published mathematical-record comparisons found nearby finite Fourier / spherical sampling results, but not the same 600-cell spectral classification. The result may be implicitly obtainable from older character tables, which is a residual priority risk, not evidence of exact publication coverage.

## Value — PASS

This is a sharp all-degree classification of a natural 120-point harmonic sampling problem with explicit spectral data, rank defects, and parity interpolation thresholds. It distinguishes scalar quadrature exactness from interpolation surjectivity and exhibits mathematically meaningful nonmonotone spectral aliasing. The algorithm is nine-dimensional independently of harmonic degree, and the 60-step identity solves infinitely many cases from a finite base table.

## Limitations and closest comparisons

The claim concerns the exact-degree harmonic space, not arbitrary low-pass combinations or an optimization of vertex configurations. Literature searches cannot establish absolute novelty. Primary comparisons used the source material cited in `RESULT.md`; exact finite-field computations supplement rather than replace the analytic proof. No independent external scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
