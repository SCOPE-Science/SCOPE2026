# Scientific assessment

## Correctness — PASS

The all-order proof reconstructs the full-translation eigenvalue normalization, uses orthogonality of five distinct Fourier characters when \(N\ge5\), and proves the exact potential identity. The coefficient-phase formula yields an exact nonnegative sum, while the remaining positive-definite quadratic is minimized on the actual finite grid. The boundary at an antipodal gap is handled separately. A unit-circle-root obstruction rules out singular systems among all minimizers. The tightness criterion and symmetric-window threshold are derived from the same identity, without extrapolating from experiments. The standalone checker completed 43,821 deterministic supplementary numerical assertions.

## Originality — PASS relative to inspected sources

The main motivating paper, Asipchuk–De Carli–Rodriguez (arXiv:2605.16139, full text: introduction, Corollary 1.2, Corollary 5.1, and their proofs), gives the spectrum for arbitrary full-translation Gabor systems, but does not solve a prescribed-three-tap, two-modulation joint phase/frequency optimization or classify all its equality cases. Magsino's tight-frame criterion (arXiv:1611.00818, introduction, Theorem 2.8 and illustrative applications) has a different conclusion: a general necessary/sufficient ambiguity-zero criterion, not the exact finite spectral variance and optimal design. The 2003 Benedetto–Fickus principle supplies the universal lower bound, which is not claimed as new. Closely related published three-site Fourier Riesz and positive sampling designs have different ambient spaces, numbers of frequencies and objectives; their available descriptions do not give a decisive implication to this theorem. The full texts of those particular related records were not accessible, so an older equivalent computation remains a risk. Search absence is not proof of novelty.

## Value — PASS

The constrained frame potential is a natural measure of mean-square reconstruction spectral irregularity, and optimizing phase and channel placement jointly matters when magnitudes are physically prescribed. This is a complete all-order optimum and equality classification, not a numerical sample. The exact deficit provides quantitative rigidity, and the sharp, finite-size amplitude threshold detects when the best frequency separation switches to antipodal. At identical magnitudes, a phase-only change produces a tight frame instead of a strictly non-tight one. Frame-potential optimality must not be interpreted as sharp worst-case conditioning.

## Residual scientific limitations

No worst-case condition-number optimum is asserted. The support is three consecutive nonzero taps, every translation is used, and the modulation count is two. Earlier unindexed equivalent calculations and the uninspected full texts of some published related records remain originality risks; these are not presented as independent validation.

Self-review: passed. Independent audit: not yet performed.
