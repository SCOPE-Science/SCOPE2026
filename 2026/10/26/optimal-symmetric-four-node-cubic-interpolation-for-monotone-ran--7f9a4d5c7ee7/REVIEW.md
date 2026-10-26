# Scientific review

## Correctness
PASS. The bounded monotone data polytope is exactly the convex hull of constants and three increasing step vectors. Explicit cardinal polynomials reduce the full-interval extrema to a terminal-step cubic and an antisymmetric middle-step cubic. Their stationary points and values are calculated exactly; strict opposite monotonicity of the resulting envelope branches proves existence and uniqueness of the minimizing node parameter. A standalone SymPy script verifies the identities and uses exact rational bounds to enclose the unique crossing. The independent grid samples in that script are supplementary, not a proof of infinite quantifiers.

## Originality
PASS subject to residual literature risk. Read-only searches of published-finding corpus and the primary literature covered variable symmetric interior nodes, monotone range violation, and minimax placement. The closest public uniform four-node result proves only a central-cell constant and explicitly excludes nonuniform nodes; the fixed Chebyshev–Lobatto value is a special case of the present stronger parameter-family result. Berrut–Trefethen's full public manuscript addresses barycentric formulas and ordinary Lebesgue stability, not this restricted-cone minimax. No equivalent global optimizer was located. Older interpolation tables or unindexed presentations may nevertheless contain the same algebraic minimax value.

## Mathematical value
PASS. The choice of nodes is a natural design decision in bounded-data interpolation. The problem optimizes a meaningful safety margin specific to ordered observations; it is not just the unrestricted Lebesgue norm or a relabeling of a fixed-grid coefficient. Two different step-data mechanisms dominate on opposite sides of a unique equioscillation point, and the optimal symmetric nodes improve the sharp Chebyshev–Lobatto and equally spaced defects strictly. The claim does not require any further downstream theorem to make this exact finite-dimensional optimum useful.

## Scope and limitations
The optimum is only among symmetric endpoint-fixed four-node grids, not all possible grids, and the interpolant need not itself be monotone. The bibliography is incomplete with respect to possible unindexed older computations. An independently commissioned scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
