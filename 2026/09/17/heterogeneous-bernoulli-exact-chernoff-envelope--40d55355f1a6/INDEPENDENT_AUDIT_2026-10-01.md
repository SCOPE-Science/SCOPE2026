# Independent scientific audit — SCOPE-20260917-40d55355f1a6

Audited at: 2026-10-01T06:12:13.318800Z

Disposition: **passed**

## Correctness — PASS

The estimator error identity is exact: each summand is a centered Bernoulli variable multiplied by a coefficient \(d_i/[\pi_i(1-\pi_i)]\), where \(d_i=(1-\pi_i)Y_i(1)+\pi_iY_i(0)-m_i\). The attainable set of \(d_i\) is exactly the interval \([a_i-m_i,b_i-m_i]\), and convexity of the Bernoulli log-mgf in \(d_i\) puts the worst case at an endpoint. Independence makes the supremum separable. Reflection through the unitwise midpoint exchanges upper and lower endpoint deviations, so convexity of the two-sided envelope proves pointwise midpoint minimaxity. At the all-upper-endpoint configuration the variance is exactly \(V_n\); the no-dominant-unit condition \(M_n/\sqrt{V_n}\to0\) implies Lindeberg and yields the claimed endpoint CLT.

## Originality — PASS

The primary contemporary comparison sources use related concentration or midpoint ideas under different criteria, but the inspected material does not state the combined exact heterogeneous endpoint cgf, pointwise midpoint minimax theorem for the two-sided cgf, and matching endpoint rate obstruction.

### Equivalent formulations

Neither accessible primary statement is equivalent to pointwise minimization of the exact two-sided bounded-outcome cgf.

### Broader coverage

These are broader in design or decision-theoretic scope but do not imply the exact cgf envelope/minimax statement because the optimized loss functional is different.

### Exact database or table

The result is analytic rather than a table lookup.

### Claim versus prior implication

The final claim is not mechanically implied by the inspected prior results.

## Value — PASS

The exact exponential envelope is a natural inferential object, gives an immediately computable finite-sample confidence certificate under genuinely heterogeneous propensities, and identifies a matching worst-case rate scale. This is not merely a numerical sharpening of a constant.

## Sources inspected

- Randomization Inference with Concentration Inequalities — https://arxiv.org/abs/2609.18586. NOT_COVERING: The accessible statement gives concentration-based intervals and heterogeneous-propensity treatment, not the record's exact endpoint cgf and cgf-minimax centering theorem.
- Minimax unbiased estimation for finite populations with bounded outcomes — https://arxiv.org/abs/2605.20572. NOT_COVERING: The optimized criterion is squared error, not the two-sided cumulant-generating-function envelope.
- Optimal Experimental Design and Estimation when Potential Outcomes are Bounded — https://arxiv.org/abs/2608.09812. NOT_COVERING: The result concerns minimax estimation/design under bounded outcomes rather than exact Chernoff envelopes.

## Residual risks

- The full text of Freidling's very recent preprint was not available through the inspected primary-text path, so the strongest NOT_COVERING statement is limited to material actually read.
- Older survey-sampling or Poisson-sampling literature may encode an equivalent endpoint-cgf observation under different notation.

## Limitations

- Independent Bernoulli assignment and deterministic outcome bounds are essential.
- Midpoint optimality is only within the stated centered Horvitz-Thompson family and for the two-sided cgf criterion.
- Exactness is for the worst-case cgf, not exact finite-sample tails or shortest intervals.
