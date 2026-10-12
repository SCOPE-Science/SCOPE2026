# Review

## Correctness

PASS. The defining Algorithm 1 is reconstructed directly. The source states \(\gamma_k=2\bar f_k\) on the scalar quadratic, the first step is exactly a half-step, and an induction proves all later adaptive proposals remain below the cap. The resulting one-dimensional state map is globally contractive and its unique fixed point gives the exact asymptotic factor.

Risk: the theorem is for deterministic one-dimensional MoMo with a nonbinding cap.

## Originality

PASS. The defining paper gives a generic interpolation bound and remarks that its bound constant is best without momentum, but does not state the exact scalar recurrence or rate. The zero-momentum Polyak branch is treated as prior. Highly relevant generalized-Polyak momentum and stochastic-heavy-ball Polyak methods use different update rules and do not imply the MoMo factor.

Residual risk: an unindexed note may contain the same scalar reduction.

## Value

PASS. The result isolates a sharp mechanism on the simplest strongly convex benchmark: momentum alone makes MoMo's adaptive learning rate collapse and changes the objective factor from \(1/4\) at zero momentum to about \(0.933\) at the defining default \(\beta=0.9\). This is a meaningful diagnostic for a method whose central purpose is momentum-compatible adaptive learning rates.

Self-review: passed. Independent audit: not yet performed.
