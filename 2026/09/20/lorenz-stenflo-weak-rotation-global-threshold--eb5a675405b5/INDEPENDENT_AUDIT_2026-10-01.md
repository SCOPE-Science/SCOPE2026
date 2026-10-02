# Independent audit — 2026-10-01

## Record

**Exact weak-rotation global stability threshold for the Lorenz–Stenflo origin**

Final claim: For the classical positive-parameter Lorenz–Stenflo system, if \(0<s\le \sigma^2/3\), the origin is globally asymptotically stable exactly for \(\rho\le 1+s/\sigma^2\), including the nonhyperbolic equality case.

Disposition: **PASSED**

## Correctness — PASS

Fresh reconstruction verifies the explicit positive-definite storage matrix, the exact square factorization, the radially unbounded Lyapunov function, the LaSalle zero-dissipation argument at equality, and linear instability above the threshold. Independent symbolic expansion reproduced zero residual and positive determinant on the stated weak-rotation interval.

## Originality — PASS

The local stability/pitchfork boundary is prior and is not counted as new. Searches and inspected material on Lorenz–Stenflo stability, zero-Hopf bifurcation, regular/chaotic dynamics, and the 2026 generalized nonautonomous paper did not state the weak-rotation global iff theorem, its storage factorization, or equality-case global attraction.

Equivalent-formulation, broader-coverage, exact-database/table, and claim-versus-prior implication checks are recorded in the companion JSON audit. Primary-source inspections and residual access risks are also recorded there.

## Scientific value — PASS

Closing the known local pitchfork threshold to an exact nonlinear global boundary over a nontrivial rotation regime is a motivated dynamical-systems result; the storage identity also explains the cutoff where the dominant passive gain leaves zero frequency.

## Checked scientific sources

- Huang–Li–Niu–Xie, Stability and Zero-Hopf Bifurcation Analysis of the Lorenz–Stenflo System Using Symbolic Methods, DOI:10.1007/978-3-031-41724-5_10.
- Naser–Abdel Aal–Gumah, Global stability analysis of two nonautonomous generalized Lorenz systems with time-varying parameters, DOI:10.1007/s40324-026-00429-8.
- Xavier–Rech, Regular and Chaotic Dynamics of the Lorenz-Stenflo System, Int. J. Bifurcation and Chaos 20 (2010).
- Published-record semantic search for Lorenz–Stenflo global stability thresholds.

## Residual risks

- The 2023 symbolic-stability chapter was accessible at abstract/metadata level rather than complete chapter text; it remains a concrete coverage risk.
- The 2026 generalized nonautonomous Lorenz paper was inspected through its abstract-level scope and may contain nearby sufficient stability inequalities.

## Verification boundary

The audit reconstructed the argument and performed fresh algebraic or logical checks where needed. Existing package logs were treated as supporting evidence only. No formal proof-assistant or expert attestation is asserted.
