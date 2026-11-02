# Self-review

## Correctness — PASS
The boundary generator treats the two sticky states explicitly and retains both independent rates, and the two bulk backward equations give a two-constant polynomial solution. Differentiation reduces every admissible allocation to a monotone quadratic with endpoint signs bounded away from zero whenever wall release has positive rate. This proves a unique global *interior* minimizer for every positive parameter set and every initial orientation mixture. Both numerical minimization and event-driven Monte Carlo independently corroborate the formulas; neither numerical check proves the universal statement.

## Originality — PASS, qualified
The same underlying stochastic process and strong general exit-time formulas are known in the papers by Bressloff (arXiv:2302.01158) and Angelani (J. Phys. A 56 455003). Those are directly acknowledged as prior work rather than represented as new. The evaluated claim is a constrained global optimization theorem, specifically the always-interior fixed-total boundary-reactivity optimizer, its closed algebraic form, and collapse of arbitrary starting position and direction bias into one effective bias. In Angelani's *Optimal escapes in active matter* (arXiv:2311.11873), the control parameter optimized is the bulk tumble rate, not the split of a fixed absorption budget. Direct paper inspections and mathematical-research searches found no corresponding optimizer theorem. Residual risk: the optimizer is algebraically accessible from more general prior first-passage expressions, and a presently unlocated resource-allocation theorem could subsume it.

## Mathematical value — PASS
The problem models allocation of a limited reactive coating or killing capacity across two sticky surfaces. The universal refusal of a corner solution is non-obvious, especially for completely polarized starts, and the effective-bias rule gives a simple experimentally meaningful equivalence between spatial and angular preparation. It provides a complete optimization classification without requiring density reconstruction or a stochastic approximation. This is a finite-dimensional exact design result, not a claim of a new first-passage formalism.

## Closest literature and scientific limits
Bressloff's §§2 and 5 furnish general sticky-wall boundary dynamics and nonidentical reactivities. Angelani's 2023 J. Phys. A article supplies a generic mean exit-time expression for wall boundary conditions and could make the new optimizer derivable by a separate calculus argument. The 2023 *Optimal escapes* article explores optimization over a different physical parameter. The present proof requires strictly positive common wall-release rate; the zero-release boundary can admit degenerate optima. Generalized residence-time distributions, asymmetric release rates, noisy statistical estimation, and time-varying wall budgets are not addressed.

Self-review: passed. Independent audit: not yet performed.
