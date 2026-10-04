# Review

## Correctness

PASS. The alternating-gradient first moment is an exact geometric series. The second moment becomes a bias-corrected exponentially weighted average of its square plus the exact accumulated damping floor, giving the stated limit. The raw-gradient ablation is exactly solvable because the squared input is constant. The restoration factor and its endpoint limits follow algebraically.

Risk: the theorem is an input-response result and does not assert convergence on a single fixed objective.

## Originality

PASS. The defining AdaMomentum paper gives the momentum-squared second moment and calls it a twofold EMA, but the inspected algorithm, motivation, theory, and appendix do not state the alternating-gradient attenuation cancellation. The closest inspected momentum/adaptivity analysis uses the different LaProp recurrence. Focused published-record searches found no implication-equivalent AdaMomentum result.

Residual risk: an equivalent short frequency-response calculation may exist in unindexed notes.

## Value

PASS. The result tests AdaMomentum's defining twofold-EMA mechanism at the frequency most strongly attenuated by ordinary momentum. It shows that adaptive normalization can exactly undo that attenuation, with a signal-dominated restoration factor \((1+\beta_1)/(1-\beta_1)\), equal to \(19\) at \(\beta_1=0.9\). This is a direct, interpretable design diagnostic for the method's core normalization.

Same-model review: passed. Independent audit: not yet performed.
