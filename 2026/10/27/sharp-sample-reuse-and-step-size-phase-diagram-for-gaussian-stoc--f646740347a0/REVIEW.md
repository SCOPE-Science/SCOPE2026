# Scientific assessment

## Correctness — PASS

The exact orthogonal-rotation update is verified directly: the stochastic predictor and corrector reduce to a scalar multiple of the identity plus a skew rotation. The squared norm is therefore an exact scalar multiplier, not merely a spectral upper bound. Gaussian fourth-moment pairing establishes each coefficient of the polynomial. Temporal independence yields its exact all-iteration power. Positivity of its quartic coefficient and an elementary factorization give necessary and sufficient strict stability. Strict convexity in the cross-call correlation establishes the unique fixed-step optimum, and a rational example verifies a stable interior optimum. These proofs explicitly cover the zero-correlation and perfect-reuse boundaries.

## Originality — PASS, with residual bibliographic uncertainty

The motivating 2026 article studies independent versus same-sample SEG under much broader stochastic-VI hypotheses, with convergence and counterexamples, while the present precise Gaussian partially overlapping pair and fixed-step mean-square phase diagram are not stated in the accessible abstract or detailed published secondary reading. Primary full text could not be inspected, a material risk that remains documented rather than being construed as evidence of novelty. Primary full texts of the 2022 papers on bilinear restarted SEG and general SEG sampling were inspected: their convergence guarantees and algorithmic sampling discussions do not logically imply the exact correlation-quartic amplification factor, the strict noise-overlap stability frontier, or the fixed-step interior optimum. Related published exact deterministic extragradient degree-two results have different operators and quantifiers. Gaussian fourth-moment algebra and stochastic extragradient are established prior knowledge, not new inventions. The comparison is claim-level, not based merely on terminology.

## Value — PASS

The parameter \(\rho\) has a direct interpretation as a minibatch overlap fraction. The theorem distinguishes the ability to find a convergent stepsize from merely minimizing a potentially unstable amplification factor, identifies an exact high-variance reuse threshold, and exhibits a provably stable case where partial rather than endpoint reuse is best. These are concrete design/diagnostic distinctions not captured by two-endpoint qualitative comparisons or conventional upper bounds.

## Closest literature and scientific limits

Yoon–Loizou, arXiv:2608.06182v1 (2026; full text inaccessible); Li et al., arXiv:2107.00464 (primary full text inspected); Gorbunov et al., arXiv:2111.08611 (primary full text inspected). The analytic result applies only to multiplicative jointly Gaussian scalar coefficients of one planar skew rotation, temporally independent paired calls and equal constant steps. The 2026 article's full text could still contain a covered specialized calculation. No general stochastic variational-inequality convergence result, Gaussian universality, and no independent mathematical audit are claimed.

Self-review: passed. Independent audit: not yet performed.
