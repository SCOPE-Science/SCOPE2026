# Mathematical assessment

## Correctness — PASS

The theorem is established by exact Gaussian flow and Euler product formulas, exhaustive quadratic root classification with unique scalar threshold crossings, and a complete analytic median-separation argument using concavity, Jensen, and elementary strict inequalities. The positive-profile strict-contraction extension follows from two simple nondegenerate roots, the implicit-function theorem, and continuity of the quantile. All parameter boundaries and the distinction between terminal marginal equality and paired-sample equality are explicit. `check.py` ran successfully after extraction from the package; its finite checks are supplemental and cannot certify the continuum claim by themselves.

## Originality — PASS, with bounded historical-priority risk

The motivating 2026 source proves *local-surrogate* quantile optimality and explicitly cautions against reading it as terminal-error optimality. It also studies propagation-related surrogate loss, while the present claim is an exact nonasymptotic terminal-error phase diagram plus a strictly contracting, positive-profile construction disproving every finite terminal-error approximation factor. Gaussian Wasserstein identities are known from the 2024 precursor and are used, not presented as new. Related published schedule-optimization and mesh-acceleration statements were checked by objects, parameter regimes, and implications. A broader classical two-step scalar-flow result, if found, could subsume the classification; priority is therefore not independently certified.

## Mathematical value — PASS

The finite-N theorem gives a sharp structural boundary for what a local density-error surrogate can guarantee about the terminal marginal. The four-grid regime exhibits multiple exact marginal meshes, including sign-reversing particle maps, and the positive-profile, strictly contractive construction rules out the trivial interpretation that only an isolated vanishing residual or a noncontractive drift causes failure. This delineates the correct role of local quantile schedules and motivates explicit terminal-error checks when the solver budget is extremely small; no broader claim about high-NFE performance is made.

## Primary comparisons and limitations

Obzherin–Khrulkov, arXiv:2610.29475v1, Sections 4–7 and Appendices G/H/N: exact finite-N surrogate optimizer, Gaussian local-Wasserstein formulas, and a different surrogate-ratio separation; not an exact two-step terminal-error phase diagram. Pierret–Galerne, arXiv:2405.14250v1: general Gaussian error formulas, but no displayed root-count thresholds or propagated-residual quantile obstruction. Pei–Hu–Gu, arXiv:2503.21774v1: reference-trajectory schedule optimization, not a universal bound for the local surrogate. The result is restricted to a scalar contracting Gaussian ODE and two Euler steps; no external expert audit has occurred.

Self-review: passed. Independent audit: not yet performed.
