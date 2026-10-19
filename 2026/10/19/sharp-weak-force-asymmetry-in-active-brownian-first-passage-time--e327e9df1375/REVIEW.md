# Scientific review

## Correctness

PASS. The stopping-time Girsanov density is valid for small force because the bounded-interval exit has an exponential moment for each fixed positive diffusivity and bounded propulsion. Differentiation after conditioning yields an exact covariance identity. The four backward equations for exit, time, orientation-integral and their product close at the required angular orders. The Dirichlet inverses are unique, the centered Green kernel is explicit, and elementary integration yields the displayed rational-hyperbolic susceptibility. Taking the exponential boundary parameter to zero gives the sharp two-term expansion. The supplied checker independently compares this identity against Green quadrature and a discretized angular-harmonic boundary problem.

## Originality

PASS, with residual risk. Tasinkevych, Le and Ryabov (arXiv:2609.27425v1), Sections IV.1 and Appendix C, establish a common leading weak-activity correction to the two conditional first-passage means and an upper bound of order \(\varepsilon^{-3/2}\) on their difference; they explicitly leave the difference's sharp scale unresolved. This finding evaluates its zero-force derivative as an exact function of diffusivity, resolving a nontrivial cancellation and giving the smaller \(\varepsilon^{-1}\) scale with explicit coefficient. Caraglio (arXiv:2410.07226) studies a parabolic barrier; Baouche et al. (arXiv:2503.05401) treat one absorbing wall; Iyaniwura and Peng (DOI:10.1088/1367-2630/ae635d) study splitting probabilities, not conditional-time difference response. The use of Girsanov, elliptic Green functions, and perturbation theory is established methodology, not a novelty claim. A broader, implicit coverage by general first-passage theory remains possible.

## Value

PASS. Bias-dependent exit timing measures a physical distinction that is absent for passive drift diffusion. The motivating work isolates the difference in a boundary-layer remainder without computing its leading order. The new result identifies the exact small-force susceptibility for the same model and shows that the leading putative \(\varepsilon^{-3/2}\) term cancels, leaving a calculable \(1/(12\varepsilon)\) response and an unusually simple next correction. This gives a natural quantitative scale for experiments or simulations designed to resolve directional timing asymmetry in the rapid angular-relaxation regime.

## Limits of assessment

The result is restricted to a centered symmetric interval, isotropic initial orientation, constant force and sequential perturbative limits. Numerical corroboration is not an infinite-dimensional certificate. The inspection establishes no uniqueness claim against every conceivable general first-passage theorem. The use of the source paper's backward hierarchy is acknowledged, and the additional explicit evaluation is the assessed contribution.

Self-review: passed. Independent audit: not yet performed.
