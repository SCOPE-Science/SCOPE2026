# Scientific review

## Correctness — PASS

The claim follows from the exact contact relaxation equation and a monotonicity envelope for the contact density. At the reproduction threshold, a Riccati comparison forces prevalence to zero. The normalized contact defect \((z-z_0)/y\) obeys an exact asymptotically stable linear equation and converges to \(Z'(0)\); an exact equation for \((1/y)'\) then proves both critical limits. The endemic-onset result is a justified implicit-function expansion with strictly positive denominator \(K\). The full supercritical attraction uses the source's negative Dulac divergence and the fact that the only positive-infection equilibrium is a sink, while the disease-free saddle has stable manifold on the disease-free boundary. The reproducible symbolic and ODE tests corroborate the formulas for multiple response shapes, including a zero baseline break rate.

## Originality — PASS, with limitations

The earlier original model article (Achterberg–Sensi, arXiv:2209.01224, Sections 2–6) supplies the equations, reproduction number, nonexistence of periodic orbits and conditional global stability, but leaves critical linearization nonhyperbolic and does not derive the general \(t^{-1}\) amplitude or its matched endemic branch coefficient. The 2024 multigroup sequel (Achterberg–Sensi–Sottile, arXiv:2407.17639, Sections 2–4) proves a strictly subcritical result, not the equality case nor the sharp prefactor. Special-case stationary formulae in the first article imply the near-threshold endemic slope in those special cases, but do not imply the nonlinear critical rate or the general shape-dependent law. Exact implication comparisons with related research records and prior adaptive-SIS special cases did not reveal the full statement. General center-manifold theory explains the local mechanism but does not itself supply the exact model-specific global critical asymptotics without calculating and justifying the reduction. Risk remains that an alternate formulation occurs in uninspected mathematical epidemiology literature; independent literature validation has not been performed.

## Mathematical value — PASS

The source literature explicitly leaves critical behavior unresolved for natural contact rules. The exact normalized coefficient \(K=1-\tau_c Z'(0)\) quantifies how adaptive contacts accelerate critical prevalence decay, simultaneously sets the leading endemic burden just above invasion, and is independent of how fast the contact network adjusts when the break-to-create ratio is held fixed. This is a new structural, interpretable critical-to-endemic correspondence across smooth monotone response functions, rather than an isolated calculation at one parameter point.

## Limitations and attribution

The result applies only to deterministic, smooth, monotone one-group SIS contact adaptation with positive contact creation; it supplies no finite-time convergence bound or stochastic-extinction prediction. Qualitative no-cycle and some global-stability statements are credited to the original source, not counted as independent novelties. All numerical evidence is supplementary to a fully analytic proof.

Self-review: passed. Independent audit: not yet performed.
