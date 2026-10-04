# Review

## Correctness

PASS. A nontrivial period-two position return requires opposite nonzero momentum signs, so the two positions differ by exactly one step \(\delta\). Solving the two periodic momentum equations yields the unique momentum pair for each positive-phase position \(u\), and the sign inequalities give exactly \(\beta\delta/(1+\beta)<u<\delta/(1+\beta)\). The exact two-step map in the alternating-sign neighborhood fixes \(x\) and contracts momentum toward the invariant graph by \(\beta^2\). This proves both the continuum of cycles and the neutral-versus-transverse multipliers.

Risk: the normal-attraction conclusion is local and must not be read as a global basin theorem.

## Originality

PASS. The original Signum paper defines the same recurrence and proves stochastic nonconvex convergence using decaying learning rates and growing batches, but the inspected full text does not state a constant-step deterministic quadratic cycle manifold. A later qualitative dynamics paper studies sign-gradient limits and adaptive-method oscillations rather than this Signum map. Recent sign-momentum theory continues to study stochastic convergence rates with horizon-dependent parameters and likewise does not state the exact two-cycle interval or normal multiplier.

Focused semantic searches covered Signum, signSGD with momentum, scalar quadratics, constant steps, limit cycles, period two, and relay-system language. No inspected source or published database result implied the complete claim. A residual risk remains for an equivalent relay-control calculation under non-optimization terminology.

## Value

PASS. Constant signed updates cannot shrink their step length near a minimizer, so persistent oscillation is a central structural issue rather than an arbitrary scalar curiosity. The result separates two effects of momentum exactly: it narrows the possible center bias of the oscillation, yet it cannot shrink the \(\delta/2\) half-amplitude and makes transverse attraction slower as \(\beta\) approaches one. The continuum and neutral tangent direction also show why an isolated-cycle stability picture is mathematically wrong for this basic Signum model.

Same-model review: passed. Independent audit: not yet performed.
