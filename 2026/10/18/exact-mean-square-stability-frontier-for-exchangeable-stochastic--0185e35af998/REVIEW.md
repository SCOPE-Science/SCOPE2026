# Scientific review

## Correctness

**PASS.** The theorem is for the independent-channel Itô linearization only. The Itô covariance equation is derived without closure approximation, and the symmetry reduction is sufficient for every deterministic initial vector because the moment flow preserves positive-semidefinite order and any rank-one input is dominated by a scalar multiple of the identity. The two-dimensional trace/determinant test and exact counterexample have been reconstructed symbolically; the provided executable supplies separate exact-rational checks. For the stated numerical witness, the moment generator has three strictly negative eigenvalues, not merely negative diagonal drift.

## Originality

**PASS, with priority risk.** The directly motivating source arXiv:2608.30655v1 asserts a stricter noise condition as necessary and sufficient for precisely the same linear Itô system. Its full accessible relevant text has been compared to the derived exact condition and its failed integer-species prediction. Mathematical-record searches for covariance aliases, independent Brownian matrix channels, and mean-square thresholds found no covering case-specific statement. The closest indexed mean-square result concerns a structurally different square-root predator–prey equilibrium. Generic Kronecker second-moment theory and incompletely inspected historical stochastic-system literature remain residual priority risks.

## Mathematical value

**PASS.** The correction alters a claimed critical diversity phase classification: at explicit model-compatible parameters the cited threshold excludes two-species stability while the sharp covariance calculation proves it. The theorem additionally gives the entire growth/decay exponent and isolates the collective covariance mechanism responsible for the gap. This is a natural qualitative and quantitative boundary of the motivating model, not a detached example.

## Closest literature and limitations

Zheng et al., arXiv:2608.30655v1, Eqs. (10)–(12), are the closest direct source. Bishop and Del Moral's linear stochastic-system stability framework and Senosiain–Tocino's general mean-square destabilization survey supply broader methodology, not an inspected exact formula for these parameters. Valenti et al. examine a distinct colored-noise spatial Lotka–Volterra model. The calculation does not establish nonlinear persistence, extinction probabilities, or stationary-law existence; bibliographic completeness is not guaranteed.

Self-review: passed. Independent audit: not yet performed.
