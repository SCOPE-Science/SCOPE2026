# Review

## Correctness

PASS. Eliminating the two source auxiliary states yields an exact second-order parameter recurrence. Each Hessian eigenmode is a heavy-ball polynomial with root product \(\alpha+K_d(1-\alpha)\lambda\). Applying the strict Jury criterion gives the necessary-and-sufficient all-spectrum stability region. The modal spectral-radius lower bound is attained, and direct source-state replay matches the reduced dynamics.

Scientific risk: this is a deterministic fixed-Hessian theorem, not a stochastic deep-network convergence result.

## Originality

PASS. The defining and extended sources motivate the derivative channel through overshoot and continuous-control tuning but do not state the curvature-dependent-momentum equivalence, hard discrete gain ceiling, exact modal rate floor, or loss-scale obstruction. A later rethinking paper changes the derivative mechanism because of stochastic-noise sensitivity. Focused indexed and web searches did not identify an implication-equivalent optimizer-specific result.

Residual risk: general discrete-control theory contains related Schur-stability tools, and the full 2020 rethinking paper was not openly inspected.

## Value

PASS. The result directly characterizes the optimizer's defining derivative mechanism and proves a hard condition \(K_dL<1\): once violated, no positive learning rate can stabilize the highest-curvature quadratic mode. It also shows that positive derivative gain raises the best possible modal asymptotic rate floor and creates a learning-rate-independent sensitivity to loss rescaling.

Self-review: passed. Independent audit: not yet performed.
