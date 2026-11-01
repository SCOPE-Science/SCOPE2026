# Scientific review

## Correctness: PASS

For unit-normalized Gaussians, the symmetric ambiguity functions are positive rotated ellipses and decrease radially. A rigorous angular comparison uses the positivity of \(e^{kz}-\cosh z-k\sinh z\) for \(k\ge1\), giving the exact minimum of the three-angle sum. The squeeze optimization is reduced to a scalar logarithmic derivative. Its unique sign change follows from the strict positivity of \(P''(t)=e^t-te^{-t}\), and the critical radius and limiting parameter are derived without numerical extrapolation. The checker passes 8,823 finite assertions but does not replace the proof.

## Originality: PASS (subject to historical-priority risk)

The 2024 public preprint of Alaifari and Yang derives the rotated-Gaussian ambiguity construction and a threshold-ellipse covering radius but not an aggregate-denominator maximin squeeze transition. Hardin, Kendall and Saff establish a different angular polarization principle under strict-convexity hypotheses that the present Gaussian angular potential does not satisfy globally, and do not optimize squeezing. Search comparisons against published mathematical records, spectral aliases and possible equivalent formulations found no statement establishing the sharp \(T=2\) transition and unique limit \(a_T\to\sqrt3\). This is a best-knowledge originality assessment, not proof that no prior equivalent work exists.

## Value: PASS

The aggregate ambiguity denominator is the divisor in a direct multi-window inversion formula, so maximizing its worst value over a prescribed disk is a natural stability-oriented design criterion. The exact transition distinguishes when isotropic windows are genuinely optimal from when three squeezed windows offer an improvement, and the asymptotic squeeze gives a parameter-free design limit. The result treats the complete continuum of radii, rather than an arbitrary finite sample or a cosmetic formula rewrite.

## Limitations

No assertion covers arbitrary angle configurations or weights, noise statistics beyond the stated denominator, or full nonlinear reconstruction stability. The result is not independently audited; equivalent work might exist outside indexed records. The source preprint supplies the mechanism but not the optimization classification.

Self-review: passed. Independent audit: not yet performed.
