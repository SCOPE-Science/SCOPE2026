# Review

## Correctness

PASS. At zero second-moment memory the source running maximum is exactly the largest squared gradient norm. On an isotropic quadratic this produces one scalar max recurrence. The subcritical, resonant, and supercritical cases are solved by direct substitution; in the supercritical case the first overshoot freezes the max and every later multiplier is exactly \(-1/A\).

Risk: nonzero second-moment memory or a nonisotropic Hessian can alter the one-reset structure.

## Originality

PASS. The defining source already proves broad AdaSGDMax convergence and explicitly explains eventual freezing after the adaptive rate enters the ordinary gradient-descent range. Those statements are treated as prior. The inspected theorem and proof do not state the exact one-step overshoot, exact return \(x_2=x_0\), or the reciprocal transient-versus-contraction identity. Focused published-record searches found no implication-equivalent statement.

Residual risk: an equivalent calculation may exist under generic max-normalized-gradient terminology.

## Value

PASS. AdaSGDMax was introduced specifically to make the global adaptive learning rate robust. The result quantifies the transient price of that robustness exactly: a larger first overshoot buys proportionally faster later contraction, while the unique resonance explains the source theorem's exceptional boundary.

Self-review: passed. Independent audit: not yet performed.
