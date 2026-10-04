# Review

## Correctness

PASS. Direct expansion of the normalized row-column outer product gives the exact checkerboard determinant error. The explicit matrix families make the factored-to-full coordinate ratio tend to zero and infinity. The marginal-only impossibility follows from two strictly positive matrices with identical marginals but unbounded target-entry ratio. The two-step construction preserves identical compressed state while the corresponding full target moments diverge multiplicatively.

Risk: update clipping can bound norm-level effects, so the theorem is about coordinatewise second-moment fidelity rather than complete-optimizer divergence.

## Originality

PASS. The defining Adafactor paper derives the generalized-KL rank-one reconstruction and notes rank-one exactness, but the inspected full text does not state the determinant checkerboard identity or a coordinatewise impossibility theorem. The later convergence analysis studies the nonlinear factored adaptive step under regularization and clipping without claiming uniform coordinatewise approximation to the full second moment. Focused semantic and full-text searches did not identify a covering statement.

Residual risk: the two-dimensional determinant identity may be known in contingency-table or independence-model literature without explicit connection to adaptive optimization.

## Value

PASS. Adafactor's defining tradeoff is memory savings from replacing a full second moment with row-column marginals. The result identifies the exact smallest-dimensional information loss and proves that no marginal-only reconstruction can uniformly preserve coordinatewise adaptive scales. The dynamic same-state construction makes the obstruction directly relevant to optimizer behavior.

Same-model review: passed. Independent audit: not yet performed.
