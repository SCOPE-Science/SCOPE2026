# Review

## Correctness

PASS. The scalar SARAH recursion collapses exactly to an iid random product
\[
v_t=v_0\prod_{j=1}^tR_j,
\qquad
R_j=1-\alpha(1+\sigma_jh).
\]
Its exact second-moment factor is \((1-\alpha)^2+\alpha^2h^2\), giving the stated necessary-and-sufficient mean-square range. In that range the iterate is an absolutely summable random perpetuity. Solving its first- and second-moment fixed-point equations yields the residual floor exactly. The \(\alpha=1\) multiplier sequence becomes symmetric, and a bijection of sign sequences makes the product signs iid Rademachers; the \(h=1/2\) binary expansion is therefore exactly uniform.

Risk: the theorem analyzes one infinite inner loop, not the restarted SARAH algorithm.

## Originality

PASS. The defining SARAH paper proves linear decay of the recursive direction inside an inner loop and studies finite inner loops. The 2019 last-iterate paper proves convergence of finite inner-loop endpoints across repeated outer resets. The 2019 averaging paper develops finite-loop weighted averaging and records the effect of SARAH estimator bias. None of the inspected full texts states the infinite-inner-loop random residual, its exact second moment, or the uniform-limit example.

Focused semantic searches covered SARAH single-loop limits, scalar quadratics, random products, residual floors, multiplicative recursions, and Bernoulli convolutions. No inspected source or published database result implied the complete claim.

## Value

PASS. SARAH's defining theoretical feature is that its recursive direction shrinks inside a single inner loop, and SARAH+ even uses the direction norm as an inner-loop stopping signal. The exact two-curvature calculation shows why this signal must not be confused with direct proximity to the optimizer: the direction can vanish geometrically while the iterate settles at a nondegenerate random residual. The closed residual law quantifies the tradeoff with step size, and the uniform limiting example makes the distinction exact rather than qualitative.

Same-model review: passed. Independent audit: not yet performed.
