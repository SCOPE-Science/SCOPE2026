# Review

## Correctness

PASS. The construction solves the first two source SWATS Adam-phase updates exactly. Both projection estimates equal the prescribed \(q>2\), so the bias-corrected monitor equals the same \(q\) and the switch criterion holds with zero discrepancy. With \(\beta_1=0\), the switched phase is ordinary SGD and has multiplier \(1-q\), hence geometric divergence.

Risk: the theorem is for the source-supported no-momentum mode and does not cover the default \(\beta_1=0.9\) setting.

## Originality

PASS. The defining paper introduces the projection estimate and switch-on-stationarity rule but does not provide a deterministic safety theorem for the learned SGD rate. A recent broad survey repeats that mechanism without a scalar stability caveat. Focused searches for SWATS counterexamples, quadratic instability, and false switches found no implication-equivalent result.

Residual risk: an equivalent observation may appear in unindexed code discussions or optimizer notes.

## Value

PASS. SWATS is specifically designed to learn both when to switch and what SGD rate to use. The finding shows that its trigger can regard an arbitrarily unstable rate as perfectly settled, separating temporal stationarity from dynamical safety. The obstruction uses positive tolerance and an interior second-moment coefficient, and therefore gives a concrete design reason for a post-estimation stability safeguard.

Same-model review: passed. Independent audit: not yet performed.
