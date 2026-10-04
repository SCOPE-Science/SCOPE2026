# Review

## Correctness

PASS. The exact alternating orbit follows from the source AdamW update and bias correction: constant gradient magnitude makes the corrected second moment equal to \(h^2a^2\) for every \(\beta_2\). In the \(\beta_2=0\) slice, the map reduces to a scalar odd recurrence. Its multiplier interval proves global convergence below \(c=2-\delta\), and the explicit derivative proves local attraction of the nonzero two-cycle above it.

Risk: the full positive-\(\beta_2\) stability problem is not claimed.

## Originality

PASS. The AdamW source proves decoupled weight decay is distinct from \(L_2\) regularization but contains no periodic-orbit analysis. The strongest inspected Adam limit-cycle paper treats Adam without decoupled weight decay. Focused published-record searches found no implication-equivalent decay-dependent threshold or exact \(2-\delta<c\le2\) regime.

Residual risk: a similar short scalar calculation could exist in unindexed implementation notes.

## Value

PASS. AdamW's decoupled shrinkage is widely interpreted as regularizing parameter magnitude. The exact theorem shows that, in a canonical adaptive-normalization slice, the same shrinkage can lower the onset of chattering and create a stable nonzero orbit where the no-decay method still converges. The explicit threshold and amplitude make this a useful boundary phenomenon for understanding optimizer dynamics.

Same-model review: passed. Independent audit: not yet performed.
