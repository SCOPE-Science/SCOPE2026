# Same-model review

## Correctness

PASS. Every affine minorant of the scalar quadratic is dominated, at fixed slope, by the tangent minorant with the same slope. This reduces the full extremal problem to one tangent parameter. For targets below the true gap, the exact identity
\[
d_{y_\star}-d_y=\frac{(y-y_\star)^2}{2y}
\]
proves the unique global maximizer. The exact-gap case is handled separately and gives a finite but nonattained supremum; targets above the gap give infinite descent-slowness through the zero minorant. Substitution into the source W inequality yields necessary-and-sufficient certificate thresholds, including the strict inequality at the nonattained boundary.

The bundled exact-arithmetic replay checks the algebra on several rational parameter families. It is supporting verification only; the quantified proof is analytic.

## Originality

PASS. The recent primary paper was inspected through the full certificate section and its quadratic experiment. It introduces affine descent-slowness and proves a one-way gap bound, but no exact scalar optimization over all affine minorants, modulus-inflation law, or exact-gap nonattainment statement was found.

The closest prior W-stationarity paper was inspected in full around its certificate and search subroutine. Its W-gap/radius construction is materially different. The foundational accelerated bundle-level paper was also inspected and contains the level-set architecture but neither descent-slowness nor this quadratic-growth certificate. Targeted semantic and exact-form searches found no equivalent statement.

Residual risk remains that an older elementary bundle/error-bound calculation under different notation contains the same scalar envelope.

## Value

PASS. The trial growth modulus is a central adaptive quantity in the new W-certificate framework, and the scalar quadratic is the canonical exact quadratic-growth test. The result gives a complete calibration of certificate existence, not just a numerical example: it quantifies the precise inflation required for an under-target gap and exposes a nonattainment phenomenon exactly at the true gap and true modulus. This clarifies what certificate failure means geometrically and can inform analysis of trial-modulus search rules.

Same-model review: passed. Independent audit: not yet performed.
