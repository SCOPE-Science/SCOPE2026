# Review

## Correctness

PASS. The exact positive two-task solution of the Nash equation is obtained by subtracting the two multiplied scalar equations. Reusing the resulting coefficients after independent magnitude drift gives an explicit stale direction, and the two current task projections reduce to two linear sign inequalities. Their intersection is exactly the claimed reciprocal interval.

Risk: the theorem isolates fixed gradient directions and does not classify angular drift.

## Originality

PASS. The defining paper contains both the fresh scale-invariance property and the practical recommendation to reuse task weights, but the inspected full text does not analyze the interaction between them. A later unified primary theory establishes the importance of non-conflicting directions and treats fresh Nash-MTL as non-conflicting, without covering stale reuse. Focused published-record searches did not locate the sharp two-task scale-drift window.

Residual risk: an equivalent elementary calculation may exist in unindexed implementation notes.

## Value

PASS. Scale invariance is a stated motivation of Nash-MTL, and weight reuse is a stated compute-saving mechanism. The result shows exactly when the latter can break the former and even turn one task's first-order improvement negative under pure relative magnitude drift. The safety margin shrinks to zero under severe gradient conflict, giving a natural theoretical diagnostic for refresh frequency.

Self-review: passed. Independent audit: not yet performed.
