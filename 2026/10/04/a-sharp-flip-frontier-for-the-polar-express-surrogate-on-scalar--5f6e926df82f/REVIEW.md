# Same-model review

## Correctness

PASS. Exact nondimensionalization reduces the source surrogate on a scalar quadratic to
\[
u_{k+1}=u_k\left[1-\frac{\tau}{(1+|u_k|^4)^{1/4}}\right].
\]
For \(0<\tau\le2\), the absolute multiplier is strictly below one at every nonzero state, which proves global convergence. Taylor expansion gives both the fifth-order matched-step law at \(\tau=1\) and the critical recurrence at \(\tau=2\); the latter implies \(|u_k|\sim(2k)^{-1/4}\). Above the frontier, the origin is linearly unstable and the exact symmetric two-cycle has squared multiplier \([1-32/\tau^4]^2<1\).

The bundled verifier replays representative identities and asymptotics. It is supporting evidence only; the quantified conclusions are proved algebraically.

## Originality

PASS. The primary source was inspected through its general deterministic update and its Polar Express sections. It introduces the \(\kappa=4\) smooth surrogate but does not state the scalar quadratic flip frontier, the fifth-order matched-step cancellation, or the critical algebraic rate.

The closest nonlinear-preconditioning predecessor was inspected at full-text statement level; it supplies the general framework and other sigmoid-like preconditioners but not the new \(\kappa=4\) surrogate. The original Polar Express paper studies polynomial matrix-sign computation rather than this outer optimization map. Targeted published-research and web searches using the exact surrogate and bifurcation aliases returned no equivalent claim.

Residual risk remains that an equivalent one-dimensional saturation-map calculation exists in dynamical-systems literature under different terminology.

## Value

PASS. The source presents the \(\kappa=4\) map as a faithful smooth model of practical Polar Express. The finding gives that model a sharp scalar learning-rate calibration: a globally convergent regime, a degenerate critical boundary, and a postcritical persistent two-cycle. It also identifies a special matched step with fifth-order local convergence. These facts clarify both successful tuning and a concrete oscillatory failure mode of the newly proposed model.

Same-model review: passed. Independent audit: not yet performed.
