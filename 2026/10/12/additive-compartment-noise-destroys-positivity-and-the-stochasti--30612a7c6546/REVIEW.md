# Self-review

## Correctness
PASS. Equation (24) supplies a constant nonzero Brownian coefficient in each compartment. At a zero coordinate, Brownian displacement is order \(\sqrt t\) while the drift is order \(t\), so the probability of becoming negative tends to \(1/2\). The disease-free state therefore fails the defining fixed-point property of a stochastic equilibrium whenever any zero compartment has positive additive noise.

## Originality
PASS. Exact-title, source-specific, alias, and boundary-invariance searches did not locate this correction. The primary full text was inspected at equation (24) and Remark 2. The closest stochastic epidemic comparisons use state-dependent diffusion and therefore do not imply that the present additive model is positive. Checked earlier ledger findings concern a different Milstein discretization error and a different ergodicity proof gap, not this boundary obstruction.

## Value
PASS. Population nonnegativity is foundational to the biological meaning of every compartment, and an asserted stochastic asymptotically stable disease-free state must first be a stochastic equilibrium. Identifying that constant additive noise defeats both properties materially changes how the stochastic conclusions can be interpreted and pinpoints the required model repair.

## Closest literature and limitations
Positive-solution results for stochastic epidemic models commonly use multiplicative or incidence-proportional noise that vanishes on relevant boundary faces. The present finding is limited to the printed additive-noise equation and does not deny existence of an unconstrained diffusion on all of \(\mathbb R^{12}\). The general boundary-invariance principle is standard; the source-specific incompatibility was not found in the inspected literature.

Self-review: passed. Independent audit: not yet performed.
