# Review

## Correctness

PASS. Renormalizing \(p^\alpha\) gives \(\operatorname{softmax}(\alpha z)\). Applying the chain rule through \(z=W h_\theta\) shows that both the head and feature PowerGrad pseudo-gradients are exactly the corresponding derivatives of \(\alpha^{-1}\mathcal L(\alpha W,\theta)\). The change of variables \(V=\alpha W\) then gives the stated block learning rates. Finite-difference and multi-step package checks independently reproduce these identities.

Scientific risk: the exact optimizer conjugacy is not asserted for momentum or adaptive-state optimizers.

## Originality

PASS. The defining PowerGrad source states the altered backward transform but not the explicit integrated surrogate or reciprocal block-rate conjugacy. Temperature scaling supplies the scaled-softmax interpretation and is treated as prior. Fixed-feature cross-entropy implicit bias is also prior and is invoked only after the new trajectory equivalence. Focused comparisons did not identify an implication-equivalent PowerGrad statement.

Residual risk: an unindexed note may contain the same change-of-variables observation.

## Value

PASS. The result identifies what objective plain PowerGrad actually differentiates and exposes an exact \(1/\alpha^2\) relative learning-rate shift between the representation and classification head. It also cleanly separates the trainable-feature mechanism from the fixed-feature boundary case, where matched PowerGrad and ordinary cross-entropy trajectories have identical predictions.

Self-review: passed. Independent audit: not yet performed.
