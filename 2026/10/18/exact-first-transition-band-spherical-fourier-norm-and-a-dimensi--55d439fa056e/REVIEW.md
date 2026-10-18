# Scientific assessment

## Correctness (PASS)

Compact-group averaging lowers norm and leaves the reproduction/range conditions invariant. The real orthogonal spherical-harmonic decomposition reduces every equivariant operator to exactly one free degree-two multiplier. The dual witness is the sign of the polar coordinate, and its norm lower bound is saturated only by the factorized kernel \(K(u)=(d+1)u(1+u)\) within the equivariant class. Beta integration supplies the exact global norm. For the one-sided asymptotics, only two small wrong-sign regions contribute: one around zero for either sign and a second near the antipode for positive perturbations. Explicit weighted triangular integration gives the coefficients and the dimension transition. Verification code passed 60 illustrative finite tests; no finite sample substitutes for proof.

## Originality (PASS, subject to historical-priority risk)

The closest primary source is Wu, arXiv:2609.02695 (September 2, 2026), whose general two-band spectral reproduction problem and group-averaging principle are credited. Its proved bandwidth-ratio estimates do not state the first-band exact optimizing multiplier, its uniquely optimal equivariant parameter, or its dimension-sensitive perturbation cusp. The two examined Defant et al. manuscripts study full projections onto polynomial ranges rather than maps fixing degree at most one while merely landing in degree at most two; their full-range normalization cannot optimize a freely chosen second-degree multiplier. Research-record searches for the same sphere, degree bounds, projection equivalences, sign duality, and dimensional cusp found no dominating claim. The low-dimensional circle constant may be classical; its isolated value is not claimed new. Equivalent identities outside the inspected texts remain possible.

## Value (PASS)

The first output band beyond affine spherical harmonics is the first nontrivial instance of bandlimited reconstruction permitting a freely adjustable high multiplier. The exact global norm and optimal multiplier determine the smallest unavoidable violation of positivity and give an all-dimensional benchmark missing from order-only bandwidth estimates. The transition from a circle-only fractional cusp to a dimension-two one-sided quadratic coefficient and then symmetric quadratic leading behavior for higher dimensions pinpoints the antipodal density mechanism. The calculation is therefore a natural exact endpoint together with structural local information, not an arbitrary parameter table.

## Closest literature and limitations

- H.-N. Wu, arXiv:2609.02695: same admissible class and group symmetry, general order estimates, but no identified exact first-transition formula or cusp.
- A. Defant et al., arXiv:2405.12123 and arXiv:2609.22050: minimal norms of projections fixing all of their range; not the partially reproducing class here.
- The classification is primarily spherical harmonic Fourier multipliers (MSC2020 42C10), although the motivating source principally classifies its more general approximation problem under another heading.
- Non-equivariant minimizer uniqueness is not claimed. Detailed full-text priority screening is necessarily incomplete, particularly for older generalized-projection identities.

Self-review: passed. Independent audit: not yet performed.
