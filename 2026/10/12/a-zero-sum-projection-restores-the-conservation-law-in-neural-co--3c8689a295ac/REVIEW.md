# Self-review

## Correctness
PASS. The mechanistic SIR vector field sums identically to zero, so the hybrid mass drift is exactly
\[
\dot M=\lambda\,\mathbf 1^\top f_{\mathrm{NN}}.
\]
The residual target likewise satisfies
\[
\mathbf 1^\top Y=
\frac{d}{dt}\mathbf 1^\top x_{\mathrm{obs}}^{\mathrm{SG}}.
\]
The exact parameter-bias residual is the difference of two SIR fields and is therefore tangent to the simplex. Orthogonal projection with
\[
P=I-\frac13\mathbf 1\mathbf 1^\top
\]
guarantees conservation and yields the exact Pythagorean non-worsening inequality.

## Originality
PASS. General invariant-preserving Neural ODE literature already establishes that unconstrained learned vector fields can violate conservation, so that broad principle is prior art. The motivating paper does not state the exact mass-drift identity, the residual-target normal-component identity, or the source-specific fact that projection cannot worsen Euclidean error to the exact same-structure SIR residual. Current and prior own ledgers and source-specific indexed searches found no equivalent claim.

## Value
PASS. Conservation is a defining structural property of the normalized SIR experiment and is explicitly cited by the source as a distinction from its earlier Lotka–Volterra setting. Because the paper's optimized coupling places substantial weight on the neural correction, a structural guarantee matters. The projection removes only a direction that cannot belong to the exact parameter-bias residual, so the repair is mathematically aligned with the stated learning task rather than an external modeling preference.

## Closest literature and limitations
Yu et al., arXiv:2603.23861, provide a broad invariant-by-construction Neural ODE framework. Zinihi, Ehrhardt, and Sidi Ammi, arXiv:2607.10858, treat structure-preserving Neural ODEs with SIR examples and conservation-preserving extensions. These works bound the novelty claim to the exact diagnosis and non-worsening projection theorem for the Annuš–Kmeť residual pipeline. The trained network weights were not independently reconstructed, so no numerical mass-drift magnitude is claimed.

Self-review: passed. Independent audit: not yet performed.
