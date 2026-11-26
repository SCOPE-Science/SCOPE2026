# Independent mathematical audit

## correctness

PASS

The publisher's Eq. (2.27), as used in (2.28), evaluates the signal at the current time outside the history sum. For a fixed time and input history, Riemann integrability of the summand's weight makes the result converge to a scalar times the current signal. Eq. (2.18) instead defines a weighted functional of past signal values. On an interval with nonnegative weight of positive mass strictly before the endpoint, a continuous nonnegative history that vanishes at the endpoint and is positive earlier makes the time-local limit zero and the history functional strictly positive. This proves operator inequivalence under the stated nondegeneracy and does not require a grid experiment. They can agree on special inputs, and no discrepancy is asserted when the weight vanishes. The frozen witness uses the same distinction and its strict sign follows from positive weight on a set of positive measure away from the endpoint. RESULT.md, VERIFICATION.md and the witness script were inspected, not executed. The scope is pointwise operator consistency on prescribed histories, not stability, convergence of coupled trajectories, implementation behavior, or a pathogen simulation.

## originality

PASS

The distinct result is the diagnosis of a specific published quadrature's different continuum operator. The general Riemann-sum calculation is standard and an earlier paper already printed the same kind of time-index replacement, but the inspected earlier passage does not identify it as a defect.

## value

PASS

The time discretization changes the type of input dependence rather than merely producing a finite-step error. Showing that mesh refinement cannot remove this mismatch at the operator level gives a concrete, consequential reproducibility check on the published scheme, independently of any empirical prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
