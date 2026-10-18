# Scientific review: exact Heisenberg STFT Gaussian contraction and sharp constants

## Correctness

**PASS.** The universal \(L^p\) bound and entropy lower bound are established in Dabra–Dasgupta–Gulia, Theorems 5.1 and 6.2. Here the normalization is independently reconstructed: the Fourier-side Gaussian has unit \(L^2\) norm, and the anisotropic central coordinate change has cancelling phase-space Jacobians. The Gaussian Hessian has determinant \(2^{2n+1}(1+\epsilon^2|v|^2/16)\); its completed-square constant is \(|v|^2/2+c^2/[2(1+\epsilon^2|v|^2/16)]\). Performing the modulation, central translation and radial Gaussian integrals gives the exact Gamma expectation. Dominated convergence supplies a saturating sequence. Christ's strict Young-convolution result, used at the interior exponents appearing in the original Lieb upper-bound proof, excludes global equality for \(p>2\). Differentiation of the moment at \(p=2\) gives the entropy formula. These operations use integrable Gaussian expressions throughout.

The accompanying verification program passed all of its matrix, numerical integral, asymptotic, and entropy checks. Finite checks are not offered as substitutes for the analytic identities or the cited nonattainment theorem.

## Originality

**PASS (subject to independent priority checking).** The directly motivating paper arXiv:2608.20952 proves the inequality but explicitly states in Remark 5.2 that its proof cannot conclude sharpness. Christ's arXiv:1706.02005 supplies sharp noncommutative Young convolution and its nonattainment, not the sharp constant for this different short-time Fourier transform. The exact finite-anisotropy Gamma integral and entropy formula neither follow from the bare upper bound nor from the absence of convolution extremizers. Published record searches for Heisenberg STFT, Dynin–Folland, Lieb sharpness, Gaussian contraction and entropy, and comparisons with adjacent Gaussian and finite-group problems did not reveal an equivalent or stronger assertion. A general contraction idea in convolution inequalities is known, so its availability does not by itself establish historical priority for the STFT statement; an unindexed equivalent argument is a residual risk.

## Value

**PASS.** The motivating source expressly leaves sharpness of a natural noncommutative Lieb bound unresolved. The identity settles that mathematical gap for the full exponent and dimension ranges of the bound, reconciles nonattainment with sharpness, and supplies a quantitative rate measuring approach to the optimal constant. The same calculation proves optimality of the associated Shannon entropy lower bound. This is not an arbitrary parameter slice or a numerical approximation.

## Closest literature and limits

Dabra–Dasgupta–Gulia, arXiv:2608.20952 (21 August 2026), Theorem 5.1, Remark 5.2, and Theorem 6.2; and Christ, arXiv:1706.02005 (2017), Section 5. The sharp constants and nonattainment refer to the defined noncommutative transform for \(p>2\), not to all alternate definitions of STFT on a group. The exact Gaussian formulas do not classify all extremizing sequences or imply an arbitrary-data stability estimate. No assertion of global entropy nonattainment is made.

Self-review: passed. Independent audit: not yet performed.
