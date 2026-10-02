# Independent scientific audit — SCOPE-20260917-e3edbe40faf5

Audited at: 2026-10-01T05:14:16.390825Z

Disposition: **passed**

## Correctness — PASS

The accumulator identity is exact because the gradient mapping equals the iterate increment divided by the adaptive stepsize. If the accumulator is bounded, telescoping its squared update gives square-summable increments. If it is unbounded, monotonicity eventually forces the stepsize below the reciprocal smoothness threshold, after which the standard proximal-gradient descent inequality bounds every later increment. In the convex case, proximal optimality and monotonicity of the convex subdifferential, followed by cocoercivity, give the stated one-step distance inequality; bounded accumulation then sums the positive part and unbounded accumulation gives eventual Fejer decrease. The finite prefix is harmless. The numerical artifact was read only as a diagnostic, not as the proof.

## Originality — PASS

The source method still states a bounded-iterates hypothesis, and targeted searches for the same gradient-mapping-accumulation recursion did not locate a theorem making the deterministic smooth increment and optimizer-distance bounds automatic. Nearby adaptive proximal-gradient methods remove boundedness by different step-selection mechanisms rather than by this accumulator dichotomy.

### Equivalent formulations

No equivalent published statement for the same recursion was located.

### Broader coverage

No broader theorem inspected mechanically implies this self-bounding dichotomy for the exact Algorithm 1 recursion.

### Exact database or table

Database search found no separate exact coverage.

### Claim versus prior implication

The final implication needs the accumulator dichotomy specialized to this method and is not a one-line restatement of the source guarantee.

## Value — PASS

Removing a standing boundedness hypothesis from the deterministic smooth guarantees of the same recent adaptive composite method is a motivated technical improvement. The proof identifies a reusable self-bounding mechanism and is not a routine numerical check.

## Sources inspected

- Universal Adaptive Proximal Gradient Methods via Gradient Mapping Accumulation — https://arxiv.org/abs/2605.05944. NOT_COVERING: The source presents the method under bounded-iterates assumptions; no automatic-boundedness theorem is stated in the material retrieved.
- Adaptive Proximal Gradient Methods Are Universal Without Approximation — https://arxiv.org/abs/2402.06271. NOT_COVERING: Different algorithmic mechanism; does not imply the gradient-mapping-accumulator dichotomy audited here.

## Checked sources

- https://arxiv.org/abs/2605.05944
- https://arxiv.org/abs/2402.06271
- Resultary semantic search for the exact recursion

## Residual risks

- The source preprint is recent and could later be revised to include the observation.
- Full arXiv body retrieval failed in this run, so exact source numbering was cross-checked only through the public abstract/indexed descriptions and the assigned package.

## Limitations

- Deterministic exact full-gradient/exact-proximal Algorithm 1 only.
- No stochastic, convex-nonsmooth, or accelerated-Algorithm-2 assumption removal is claimed.
- The bound may depend on a finite pre-threshold trajectory rather than only on a small a priori problem-data constant.
