# Independent audit review — 2026-10-01

## Final claim

For the real-parameter Rucklidge flow, the displayed polynomial balance gives an exact periodic/invariant-measure energy identity; every non-equilibrium compact recurrent state requires positive damping parameter a, and every bounded forward orbit with \(a\le0\) converges to a single equilibrium.

## Correctness — PASS

Direct differentiation verifies \(\dot F=-a x^2+\tfrac12\dot z^2\). Integration gives the bounded-time and periodic identities; invariant-measure integration gives the stationary identity. For \(a\le0\) the zero-derivative set has only equilibria as its largest invariant subset, and LaSalle on the compact omega-limit set plus connectedness yields convergence of every bounded forward orbit to one equilibrium.

## Originality — PASS

A related published SCOPE theorem contains the same polynomial balance after a coordinate change in the positive-parameter Shimizu–Morioka/Rucklidge family, so that overlap is credited. It does not cover the real-parameter damping-sign boundary or the \(a\le0\) bounded-orbit convergence theorem. The full 2023 Demina–Ilyukhin paper was inspected and classifies special invariant algebraic manifolds; it does not state this balance or global recurrence barrier.

## Value — PASS

The sign of the damping parameter is a natural dynamical boundary. The theorem converts an exact balance into a global no-recurrence/convergence statement for every bounded orbit, and corrects a concrete misleading negative-damping attractor example in the literature. This is a motivated structural boundary, not a parameter-only normalization check.

## Sources and residual risk

- Invariant algebraic manifolds for the Rucklidge model of double convection — https://doi.org/10.1134/S0037446623050075: NOT_COVERING.
- Exact stationary balances and a recurrence-height barrier for the Shimizu–Morioka/Rucklidge family — SCOPE 2026/09/20/shimizu-morioka-rucklidge-recurrence-barriers--03af2ccdb58c: PARTIAL_COVERAGE.

- Residual risk: Older equivalent Lyapunov-function formulations under different Rucklidge normalizations remain a residual priority risk.
