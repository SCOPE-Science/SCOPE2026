# Review

## Correctness

PASS. The local state matrix in the unclipped region has characteristic polynomial \(\zeta^2-(1+\beta-q)\zeta+\beta\), so the second-order Jury inequalities give the exact origin-stability interval \(0<q<2(1+\beta)\). For any nonzero period-two orbit, the two position equations force opposite velocities, and the two momentum equations force \(g(a)=-g(b)\) with equal magnitude. Because scalar clipping has only a linear branch and a saturation branch, the orbit classification splits exhaustively into two cases. The unsaturated case forces the exact boundary; the saturated case forces the boundary or supercritical regime and yields the complete center band. In the strictly saturated alternating region, the forcing derivative vanishes and the transverse velocity error obeys the exact recursion \(e_t=\beta e_{t-1}\), proving normal attraction to the cycle manifold.

Risk: the theorem does not claim a global basin, longer-cycle exclusion, or normal attraction at the kink endpoints. Those limits are explicit in the claim package.

## Originality

PASS. The inspected clipping literature establishes acceleration, stability, stochastic bias, and convergence guarantees for clipped or normalized gradient methods. One inspected work includes a momentum extension for stochastic weakly convex optimization, while another studies normalized SGD with momentum; neither uses the exact fixed-step recurrence of clipping the scalar gradient before a raw heavy-ball state and neither states this complete two-cycle bifurcation. The inspected heavy-ball quadratic work is unclipped. Targeted searches using clipping, momentum or heavy-ball, quadratic, saturation, period-two, limit-cycle, and the derived boundary did not find a statement implying the full classification.

Residual risk: an equivalent saturated second-order recurrence may have been analyzed in switched-systems or control terminology without optimization keywords. This risk is recorded rather than treated as disproved by search failure.

## Value

PASS. Gradient clipping and momentum are routinely combined, yet clipping is often described only as a stabilizer. The theorem identifies a sharp counterpoint on the simplest quadratic benchmark: clipping does not extend the local asymptotic-stability range of heavy-ball, and beyond the classical boundary it produces a persistent continuum of cycles rather than restoring convergence. The exact center-band formula and transverse contraction rate separate bounded-looking oscillation from true optimizer convergence and give a reusable diagnostic for fixed-step clipped momentum dynamics.

Same-model review: passed. Independent audit: not yet performed.
