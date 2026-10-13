# Self-review

## Correctness

PASS. The source fixed-\(p\) LEFT scalar is a Rayleigh quotient divided by \(p\), so the actual step length puts every spectral product in \([p/\kappa,p\kappa]\). This gives the universal modal bound \(p\kappa-1\). Both squared gradient norm and quadratic objective gap are weighted sums of the squared modal multipliers. A two-dimensional exact-line-search warm-up makes the next gradient concentrate arbitrarily strongly on the high-curvature mode while the LEFT step tends to \(p/\mu\), proving sharpness.

## Originality

PASS. The primary full text, source-specific searches, the closest indexed BB objective frontier, and recent quadratic BB convergence and Lyapunov literature were compared at the implication level. The closest sharp BB result is confined to the ordinary BB1--BB2 interval; the recent spectral-weight results also remain within Rayleigh quotients. None of the inspected sources states the outside-BB1 factor \((p\kappa-1)^2\) or the exact frontier \(\kappa=2/p\).

The main residual risk is an equivalent older spectral-gradient transient bound under different notation.

## Value

PASS. The result supplies an exact finite-horizon safety boundary for the source parameter \(p\). It shows that the regime reported as locally more stable can have a strictly smaller worst-case monotonicity window and can exhibit arbitrarily large condition-number-driven transient spikes before later \(R\)-linear convergence. This directly informs the source's motivation for truncating extended scalars back toward the Hessian spectrum.

Self-review: passed. Independent audit: not yet performed.
