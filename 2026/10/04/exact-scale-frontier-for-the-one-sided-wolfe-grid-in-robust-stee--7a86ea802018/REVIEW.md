# Same-model review

## Correctness

PASS. The scalar source specialization is exact: the robust direction problem becomes \(axY+\tfrac12Y^2\), hence \(Y=-ax\). Substitution into the source's two standard Wolfe inequalities gives
\[
1-\gamma\le\alpha a\le2(1-\beta).
\]
The source trial grid has maximum step \(1\), so \(a<1-\gamma\) makes every trial fail the curvature condition. Conversely, if \(a\ge1-\gamma\), factor-two spacing together with \(1-\beta>1-\gamma\) guarantees a grid hit.

The explicit example \(\beta=\tfrac14\), \(\gamma=\tfrac34\), \(a=\tfrac18\) has continuous Wolfe interval \([2,12]\) and no admissible source-grid step.

## Originality

PASS. The primary paper proves continuous Wolfe-step existence and separately prescribes a one-sided dyadic search, but does not compare the admissible interval with that grid. Standard Wolfe references use an expansion/bracketing phase, not shrink-only search. Targeted searches found no exact \(a=1-\gamma\) frontier for this method.

The residual risk is that the generic observation that curvature conditions may require increasing a trial step is classical. The new content is the source-specific exact boundary and minimal dyadic repair.

## Value

PASS. The result identifies an implementation-level mathematical obstruction that can stop the published algorithm on the first iterate of a one-dimensional strongly convex quadratic, even though all assumptions of the continuous existence theorem hold. The exact frontier is scale-transparent and the repair is immediate and structurally motivated.

Same-model review: passed. Independent audit: not yet performed.
