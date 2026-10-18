# Scientific review of the two-community saturation threshold

## Correctness

**PASS.** The equilibrium problem is exactly planar because the graphon convolution takes a constant value on each of two equal-measure blocks. Subtracting block averages gives a transverse mode that decays exactly as \(e^{-dt}\), including for arbitrary square-integrable initial functions. A scalar monotonicity inequality yields unique positive polarized amplitudes, and a direct symmetric/antisymmetric Jacobian diagonalization yields both nontrivial eigenvalues. The relevant hyperbolic ratio is strictly increasing, proving a single sign change. The branch's full-space local stability follows from planar hyperbolicity and exact transverse decay; no claim is made at the nonhyperbolic endpoint. The packaged standard-library checker ran successfully.

## Originality

**PASS, subject to independent priority review.** The 2026 motivating graphon paper develops the continuum saturation model and approximation/equilibrium results; the 2024 nonlinear-opinion community paper concentrates on spectral/near-onset structure; and the earlier nonlinear-opinion theory proves broader agreement and disagreement mechanisms. These precedents prevent interpreting polarization or multistability themselves as novel. The precise positive-kernel, no-self-feedback, equal-two-community unrestricted-gain stability switch \(\sinh(2z_*)/(2z_*)=(a+b)/(a-b)\) and its continuum transverse stability were not explicitly identified in the compared statements. A more general Hopfield or nonlinear cooperative-systems theorem might still imply the specialization. Related mathematical research records on bounded-confidence switching and competitive gene-system bistability concern different equations and do not directly dominate this statement.

## Mathematical value

**PASS.** A positive influence network might appear to select agreement; the result exposes a mathematically sharp saturation regime in which robust opposite community opinions coexist with robust agreement. The exact threshold is a structural property of within- versus between-community coupling, rather than a selected numerical example. The exact full-space reduction makes the result relevant to the continuum graphon approximation program and distinguishes near-onset unstable polarization from high-gain stable polarization. The two-block equal-mass restriction and the lack of global basin classification limit the conclusion.

Self-review: passed. Independent audit: not yet performed.
