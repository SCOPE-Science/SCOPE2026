# Self-review

## Correctness — PASS

For each integer \(k\ge2\), the transition matrices \(A=J-E_{pq}\), \(B=J-E_{rs}\) encode exactly the allowed overlapping digit pairs. Their product preserves a two-dimensional subspace, and its trace, determinant, and initial path counts give the stated four rational generating functions for every parameter quadruple. Direct algebraic subtractions prove strict coefficientwise ordering, and a root comparison gives three ordered exponential rates. The binary double root gives the exact prefactor rather than an invalid simple-root approximation. The standalone Python checker returned `VERIFY_OK` and exhaustively checked bases 2–6, including brute finite-word counts. These computations support, but do not replace, the symbolic proof.

## Originality — PASS with residual bibliographic risk

The 2013-12-25 preprint of Livorati, Georgiou, Dettmann and Leonel considers oscillating and breathing moving holes numerically and through approximations, not every ordered pair of exact length-two cylinders in every integer base. Georgiou, Dettmann and Altmann treat static escape through Markov holes. Cheriyath and Agarwal treat a fixed simultaneous set of forbidden words in a shift, whereas the present phase-separated exclusion is not that fixed-union survivor language. In particular, static simultaneous exclusion of binary \(00\) and \(11\) differs from forbidding them on alternating times, where the count is linear in the observation horizon. Comparisons also considered statements about other survivor sets and finite-state dynamical zeta functions; none implies the claimed complete four-case finite-horizon law or the exceptional binary multiplicity. The matrix-product approach is classical; an unknown equivalent derivation or disguised phase-augmented formulation remains possible.

## Mathematical value — PASS

For a natural finite Markov discretization of time-dependent holes, the result obtains the exact ensemble survival law at every horizon and for every base, not just an asymptotic escape rate. The four strict finite-horizon classes collapse into three spectral classes; exchanging temporal phases in the mixed-overlap cases leaves the spectral exponent invariant but changes *every positive even-horizon count*, a meaningful observable hidden from escape-rate measurements. The exceptional binary case exhibits a true polynomial prefactor from a defective transfer root. These structural distinctions answer natural questions suggested by earlier studies of moving-hole escape and fixed-hole symbolic correlations, rather than an arbitrary parameter slice.

## Closest sources and limitations

1. A. L. P. Livorati, O. Georgiou, C. P. Dettmann, E. D. Leonel, *Escape through a time-dependent hole in the doubling map*, 2013 preprint arXiv:1312.7030, *Phys. Rev. E* 89 (2014) 052913; full introduction, model, numerical escape results and discussion compared.
2. O. Georgiou, C. P. Dettmann, E. G. Altmann, *Faster than expected escape for a class of fully chaotic maps*, *Chaos* 22 (2012) 043115; full source introduction and static-hole spectral calculations compared.
3. H. Cheriyath and N. Agarwal, *Subshifts of Finite Type with a Hole*, preprint arXiv:1905.11767, online journal publication 2022, printed 2023; introduction and fixed-word-correlation results compared.

Scope is restricted to one forbidden length-two cylinder per alternating phase with uniform base digits. The literature search cannot prove global uniqueness. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
