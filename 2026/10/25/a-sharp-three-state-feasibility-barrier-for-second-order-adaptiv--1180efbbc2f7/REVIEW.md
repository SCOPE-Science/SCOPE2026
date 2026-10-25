# Scientific review: adaptive SSPRK(3,3) endpoint feasibility

## Correctness — PASS
All weight vectors retaining the first two RK order conditions are parameterized by a single real number. The exact polynomial map reduces the three-state positivity constraints to two opposing inequalities, proving infeasibility strictly beyond the dimensionless step \(4\), and the displayed piecewise weights prove sufficiency below it. The projector identity proves the all-two-state assertion for every rate choice. Boundary uniqueness and the identity map are exact, not numerical extrapolations. The rational checker passed, but the proof is analytic.

## Originality — PASS
The closest source is Nüßlein--Ranocha--Ketcheson, *Positivity-Preserving Adaptive Runge--Kutta Methods* (arXiv:2005.06268): it uses the same stages and exhibits a two-state weight adjustment, but does not state or imply the universal two-state/three-state adaptive feasibility frontier. Horváth's 2005 threshold paper addresses fixed Runge--Kutta tableaux; Higueras--Ketcheson--Kocsis (arXiv:1505.04024) optimize downwind perturbations. A distinct public SSP-SDIRK result happens also to have a two-state/three-state contrast at the value \(4\), but applies a squared implicit-midpoint rational propagator, not this adjustable explicit polynomial. The detailed implication comparisons appear in the structured review. Unindexed identical results remain possible.

## Value — PASS
A time integrator that repairs positivity by solving for endpoint weights needs to know when its constraints can become impossible without lowering order or the step size. The classification supplies a sharp minimal-state obstruction even with unrestricted real weights, and shows the last feasible step may be exactly stagnant despite real positive transfer. These statements distinguish feasibility from physical accuracy and provide a concrete diagnostic for timestep selection.

## Scientific limitations
Only autonomous finite-state Markov generators and endpoint positivity are addressed. Stages may be negative, large-step accuracy can be poor, and a complete adaptive implementation may reject steps because of additional error constraints. No independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
