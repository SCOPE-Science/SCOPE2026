# Self-review

## Correctness — PASS

The stated positive-definiteness conditions are equivalent to positivity of the first leading pivot and its two-dimensional Schur complement. Block inversion proves the boundary alignment \(S^{-1}e_1\parallel(b,-c)\). The deleted covariance coupling is exactly \(-c/(b^2+c^2)\); the determinant ratio is \(1+\delta\) and the two Gaussian relative-entropy trace factors are \(3\) and \(3+2\delta\). Exact one-variable differentiation of the spectral rotation profile proves the sharp condition-number envelope, including all equality cases. Independent direct matrix computations and symbolic checks in `verify.py` corroborated the proof across 4,513 test conditions. The proof—not those finite checks—supports the universal quantifiers. No error term, empirical-only step or unproved infinite-dimensional generalization is used.

## Originality — PASS, with residual bibliographic risk

Fifen, Karambal and Hennig (arXiv:2609.10080v1, 2026) introduce coupling-aware Lanczos covariance completion and give general isotropic-complement and Gaussian KL bounds. Their accessible Theorem 13 has a condition-number upper bound rather than the two exact, coupling-invariant relative entropies derived here; their spectral bound is expressed through the corrected complement. The new statement fixes a precisely defined one-resolved/two-complement covariance operator and proves its complete Gaussian-KL profile, exact cancellation of the boundary-coupling parameter, sharp extremizing orientation at fixed uncorrected-complement condition number, and a family with diverging Schur condition but fixed KL loss. The standard Gaussian KL identity and block inversion are not claimed as new. Zhang et al. (arXiv:2102.05485) address general Gaussian KL inequalities, not in their accessible abstract this particular block-inverse compression. Search of published mathematical records and comparison with earlier mathematical findings found no dominating equivalent theorem; this is not a proof of global novelty. The motivating article's inaccessible full supplementary detail, incomplete text access to the older KL paper, and unindexed literature are residual risks.

## Value — PASS

This is a sharp stability guarantee for a natural, concrete and reproducible minimal covariance approximation motivated by a new numerical uncertainty method. It makes the *uncorrected* complement's condition number an exact worst-case diagnostic for both directed Gaussian KL errors, irrespective of the potentially divergent coupling-corrected Schur condition number. The equality construction and invariant near-singular family show when global condition-number bounds can be much too pessimistic. Unlike a routine small-parameter check, the theorem establishes the complete admissible parameter dependence, exact best constants, and a precise boundary mechanism. No claim is made for higher-dimensional bulks, stochastic quadrature, finite precision, or posterior calibration in applications.

## Closest sources and limitations

Primary: H. Fifen, I. Karambal and P. Hennig, *Stochastic Lanczos Quadrature for Computational Uncertainty in Linear Algebra*, arXiv:2609.10080v1 (2026-09-09), particularly its Lanczos-complement covariance construction and Theorem 13. General comparator: Y. Zhang et al., *On the Properties of Kullback-Leibler Divergence Between Multivariate Gaussian Distributions*, arXiv:2102.05485 (2021). Their original assertions are not re-reviewed. The claim applies to the fully specified new compression alone. Access to complete source appendices was limited; other equivalent exact results may exist.

Self-review: passed. Independent audit: not yet performed.
