# Scientific review: radial NGN/proximal stability ordering

## Correctness — PASS

Both indices are reconstructed from their original model minima, including all scaling factors. The radial reduction is exact. The proof separates the positive and negative parts of the affine square-root tangent, and for the concave-square-root case proves explicitly that a center candidate dominates an NGN model minimizer that crosses the origin. Thus the inequalities hold for all positive stepsizes and all permitted dimensions. The power-law strictness and two endpoint asymptotics follow from the exact scalar optimality equation. The packaged numerical checks are supplementary and do not certify the analytic quantifiers.

## Originality — PASS

The 2026 stability-index paper supplies each model's definition, a separate NGN expression and a general SPP upper bound, plus equality on scalar quadratics. It does not state an NGN-versus-SPP sign theorem for nonquadratic radial losses, nor does the p-power boundary follow from its SGD comparisons or quadratic equality. The original 2024 NGN paper's relevant Sections 2–4 address its adaptive step and convergence properties; they contain no corresponding exact proximal-index comparison. The 2025 momentum paper has a different object. Searches of published research records and primary-literature terms did not identify a covering equivalence. Residual risk: generic model-comparison or surrogate-minorization theory could contain an unindexed equivalent criterion; the momentum paper's full manuscript was not inspected.

## Value — PASS

The result answers a specific motivated comparison problem left by the separate-index framework: two ostensibly stable optimization models cannot be ranked unconditionally, but a natural geometric property of the square root of a radial loss ranks them for every regularization scale. The result is not merely quadratic equality: subquadratic and superquadratic classes give strictly opposite orderings, and the explicit endpoint gap limits quantify the reversal. This supplies structural benchmark cases without presuming an algorithmic performance or convergence theorem.

## Limitations

Only one-step indices on zero-floor convex radial profiles are covered. NGN's squared-tangent model is not always a global lower model, and the index ordering is not a general objective-descent comparison. The closest underlying formulas are known, unindexed equivalent literature remains possible, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
