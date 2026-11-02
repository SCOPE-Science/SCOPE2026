# Mathematical review of the corrected claim

## Correctness
For the original 2023 adaPGM scalar recurrence, the forced strict branch itineraries yield the unique positive plastic-constant two-cycle and an explicit three-cycle satisfying the seventh-degree ratio identity. The cap/growth branch inequalities are strict; exact root and multiplier interval enclosures are supplied by `verify_cycles.py`. The Jacobian of a cap step has rank one, so each complete return has multiplier zero as well as an expanding real multiplier less than minus one. These cycles are locally unstable but not repellers in all directions. Indeed, a one-parameter family of nearby two-cycle states maps exactly onto the cycle in two steps. The corrected statement accurately distinguishes saddle-type instability from full repulsion. All cycle steps avoid the degenerate value one, and the primal factors contract strictly.

## Originality and prior coverage
The 2023 defining work observes oscillatory stepsizes but gives no exact positive two- and three-period algebraic construction. The 2024 generalized update changes the cap rule. The closest published plastic-constant two-cycle concerns a different Bregman-adaptive algorithm and does not imply the exact three-period original recurrence or its return spectrum. General convergence results for the primal iterates likewise do not imply these periodic-step constructions. Earlier unpublished or differently named treatments of the same scalar map remain a genuine priority risk.

## Value and boundaries
The exact simultaneous occurrence of two prime periods for a concrete adaptive rule on a strongly convex objective is a motivated nonlinear-feedback finding. The corrected result additionally demonstrates why an expanding multiplier does not make a planar map an all-directions repeller when a cap step collapses one direction. The claim does not assert typical attraction, universal cycling, or a full classification of periods.
