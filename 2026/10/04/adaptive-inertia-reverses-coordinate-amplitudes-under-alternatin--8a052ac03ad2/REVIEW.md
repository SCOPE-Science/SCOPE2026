# Review

## Correctness

PASS. The source second-moment recurrence is exactly solvable because an alternating gradient has constant coordinatewise square. Bias correction removes the entire \(\beta_2\) transient, so the inertia coefficients are fixed from iteration one. The first-moment recurrence and product correction then give a closed alternating response. The three clipping branches and strict derivative sign of the interior branch establish the amplitude reversal.

Risk: the theorem is an optimizer input-response result, not a convergence theorem for a fixed objective.

## Originality

PASS. The defining Adaptive Inertia paper contains the exact parameterwise ratio-and-clip rule but analyzes saddle escape, flat minima, and convergence rather than periodic-input response. Full-text searches for alternating, periodic, oscillatory, and frequency terminology found no covering statement, and focused published-record searches found no implication-equivalent Adai result.

Residual risk: an equivalent short frequency-response calculation may exist in unindexed implementation notes.

## Value

PASS. The finding probes the optimizer's defining parameterwise inertia mechanism and identifies a strong, interpretable effect: in the unclipped regime, higher alternating-gradient energy produces a smaller asymptotic update. At the source defaults, a coordinate with twice the gradient magnitude receives only \(14/31\) of the other coordinate's update magnitude. This is a substantive boundary on how adaptive inertia redistributes high-frequency motion.

Same-model review: passed. Independent audit: not yet performed.
