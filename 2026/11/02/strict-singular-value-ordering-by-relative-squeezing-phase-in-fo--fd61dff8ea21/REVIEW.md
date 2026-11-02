# Mathematical review

## Correctness — PASS

The two quadratic weighted composition factors are Hilbert–Schmidt from the explicitly evaluated Fock Gaussian integral; hence their cross product is trace class. Multiplication of the reproducing kernels followed by a second Gaussian integral gives the positive Gram kernel with coefficients \(a,b\). The strict subcritical hypotheses prove \(2|a|+b<1\). The general positive Gaussian-kernel spectral lemma is derived by an exact analytic eigenfunction family; nonzero eigenvectors occur at all geometric eigenvalues, while diagonal trace integration and an exact quadratic-root identity exhaust the entire positive spectrum. Thus all indexed singular values, the Schatten formulas, and strict phase ordering are proved, without extrapolating finite truncations. A deterministic matrix-and-algebra checker passed 696 assertions. Remaining numerical risk is limited to floating-point truncation in supplementary diagnostics, not an assumption of the theorem.

## Originality — PASS (best-knowledge)

Direct full-text comparison with Sang–Zhao's October 2026 Gaussian-operator paper finds boundedness, compactness, Schatten membership, and the Hilbert–Schmidt formula, but not the indexed spectral law or strict relative-phase ordering. Tian's October 2026 Fock cross-product paper treats operator classes without this spectral comparison. Dong–Zhu (September 2025) gives a singular-value formula for canonical kernels whose two quadratic coefficients satisfy a constrained relation, not for independent squeezes. Published mathematical-record searches for both the kernel and phase-majorization aliases returned no statement that implies this universal comparison. An equivalent result could still be implicit in oscillator-semigroup literature; such priority is not independently certified.

## Mathematical value — PASS

The independent relative phase is a natural parameter of products of subcritical quadratic weighted composition operators. The result gives the entire singular sequence, every Schatten norm, and simultaneously sharp optimizers for all ordered singular values and Ky Fan sums, instead of a single Hilbert–Schmidt integral or isolated finite invariant. This quantitative comparison is meaningful for compact Gaussian operator geometry and approximation. The theorem does not address critical squeezing, affine shifts, arbitrary slopes, or multi-variable operators.

## Closest literature and residual risks

- Sang–Zhao, arXiv:2610.28279v1, Sections 3 and 5: direct Gaussian kernels and Hilbert–Schmidt calculations, but no full indexed phase order in inspected text.
- Tian, arXiv:2610.29786v1, Sections 3–4: cross-product compactness and Hilbert-space properties, not the spectral comparison.
- Dong–Zhu, arXiv:2509.16672v1, Theorem A and Section 4: constrained canonical kernels, not independent quadratic coefficients.
- Older oscillator-semigroup normal forms remain a residual potential implication, and publication priority awaits independent scrutiny.

Self-review: passed. Independent audit: not yet performed.
