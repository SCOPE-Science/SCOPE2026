# Independent audit — 2026-10-01

## Final claim

On quadratic Gaussian targets, fractional retention of the classical UBU midpoint position noise leaves the deterministic map unchanged and yields the stated parameter-quadratic stationary covariance; one-third retention cancels the full second-order configurational bias and the friction correction raises stationary position-covariance accuracy to fourth order.

## Correctness — PASS

The assigned recurrence was reconstructed mode-by-mode. Its deterministic matrix is independent of the interpolation parameter, while the one-step covariance is a quadratic polynomial in that parameter, so the stationary Lyapunov solution is exactly quadratic whenever the matrix is stable. A fresh numerical Lyapunov replay at three unrelated parameter tuples showed the displayed expansion residual scaling as the fifth power of the step. The special choices cancel the second-order and then the second- and third-order terms exactly, and the scalar implicit-function derivative at one third is nonzero, validating the local exact-zero-bias branch.

Checked sources: A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New, arXiv:2609.20713; Robust and efficient configurational molecular sampling via Langevin dynamics, J. Chem. Phys. 138 (2013); Wasserstein distance estimates for the distributions of numerical approximations to ergodic stochastic differential equations, JMLR 22 (2021), with 2024 correction; Published-findings semantic searches for LC-UBU, UBU, midpoint-noise interpolation, harmonic stationary covariance and configurational superconvergence; Assigned Git package and its Lyapunov verification artifact; fresh independent high-precision Lyapunov replay

Residual risks: The very recent LC-UBU primary paper was accessible only at abstract level through the available lawful retrieval path, so an unindexed formula inside its full text remains a residual originality risk.; The result is quadratic-target invariant-covariance analysis only; it does not imply nonlinear trajectory order or exact finite-step unbiasedness across anisotropic modes.

## Originality — PASS

Best-of-knowledge originality passes for the explicit LC-UBU/UBU covariance interpolation, endpoint bias constants, universal one-third cancellation, friction-only fourth-order correction and scalar exact-root expansion. The closest retrieved work gives the algorithms and broad Wasserstein orders, while related published findings concern randomized schemes or harmonic stability rather than these covariance formulas.

### Equivalent formulations

Searches: Resultary semantic searches for `UBU theta one third midpoint noise covariance bias`, `LC-UBU stationary covariance interpolation`, and `configurational superconvergence UBU`; arXiv:2609.20713

Evidence: The exact-topic searches returned the assigned result first; the closest distinct findings concern randomized ULMC covariance or LC-UBU stability, not the midpoint-noise interpolation.; The primary abstract states the universal/low-cost UBU framework and broad second-order Wasserstein behavior but not the audited stationary covariance identities.

Reasoning: Equivalent formulations include the quadratic stationary covariance law, cancellation of its low-order coefficients and the local exact variance root; none of the inspected distinct statements is equivalent.

### Broader coverage

Searches: arXiv:2609.20713; classical configurational superconvergence literature; published harmonic-equilibrium and LC-UBU stability findings

Evidence: Prior work covers UBU algorithms, configurational superconvergence phenomena and broad error orders.; No inspected broader theorem supplies this interpolation's exact parameter-dependent covariance coefficients.

Reasoning: General UBU convergence and configurational-superconvergence theorems do not mechanically determine the displayed coefficient polynomial for the new interpolation.

### Exact database or table

Searches: exact constants `1/3`, `gamma h/9`, LC bias `1/12`, UBU bias `-1/6` in semantic literature searches

Evidence: No independent exact table or formula with the audited constants was located.

Reasoning: Search absence is used only as best-of-knowledge evidence, not as proof of novelty.

### Claim versus prior implication

Searches: comparison against the LC-UBU source and classical harmonic stationary-covariance methods

Evidence: The source defines the relevant algorithmic family context, but the audited cancellation law requires solving and expanding a parameterized discrete Lyapunov equation.

Reasoning: That additional computation is not a routine substitution into a stated prior theorem.

### Source inspections

- **A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New** — https://arxiv.org/abs/2609.20713
  Trigger: Primary source introducing the LC-UBU family and universal integrator
  Material read: Abstract and bibliographic metadata; the complete paper was not retrievable through the available lawful text route during this audit
  Method: Primary-source abstract inspection plus independent reconstruction from the assigned algorithmic formulas
  Assessment: Highly relevant and retained as an access risk, but the accessible material does not cover the audited covariance formulas.
  Evidence: The abstract states the low-cost UBU construction and broad Wasserstein rates, not the one-third stationary-covariance cancellation.

Checked sources: A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New, arXiv:2609.20713; Robust and efficient configurational molecular sampling via Langevin dynamics, J. Chem. Phys. 138 (2013); Wasserstein distance estimates for the distributions of numerical approximations to ergodic stochastic differential equations, JMLR 22 (2021), with 2024 correction; Published-findings semantic searches for LC-UBU, UBU, midpoint-noise interpolation, harmonic stationary covariance and configurational superconvergence; Assigned Git package and its Lyapunov verification artifact; fresh independent high-precision Lyapunov replay

Residual risks: The very recent LC-UBU primary paper was accessible only at abstract level through the available lawful retrieval path, so an unindexed formula inside its full text remains a residual originality risk.; The result is quadratic-target invariant-covariance analysis only; it does not imply nonlinear trajectory order or exact finite-step unbiasedness across anisotropic modes.

## Scientific value — PASS

The cancellation law identifies a concrete stochastic mechanism behind opposite LC-UBU/UBU Gaussian invariant biases and gives a spectrum-independent tuning rule that raises configurational covariance accuracy without altering deterministic stability. This is a motivated structural property of a newly introduced integrator family, not an arbitrary numerical slice.

Checked sources: A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New, arXiv:2609.20713; Robust and efficient configurational molecular sampling via Langevin dynamics, J. Chem. Phys. 138 (2013); Wasserstein distance estimates for the distributions of numerical approximations to ergodic stochastic differential equations, JMLR 22 (2021), with 2024 correction; Published-findings semantic searches for LC-UBU, UBU, midpoint-noise interpolation, harmonic stationary covariance and configurational superconvergence; Assigned Git package and its Lyapunov verification artifact; fresh independent high-precision Lyapunov replay

Residual risks: The very recent LC-UBU primary paper was accessible only at abstract level through the available lawful retrieval path, so an unindexed formula inside its full text remains a residual originality risk.; The result is quadratic-target invariant-covariance analysis only; it does not imply nonlinear trajectory order or exact finite-step unbiasedness across anisotropic modes.

## Limitations

- Quadratic Gaussian targets and stable steps only.
- Nonzero midpoint-noise interpolation does not preserve the low Gaussian count of LC-UBU.
- The exact finite-step zero-bias root is generally mode dependent.

## Conclusion

Disposition: **passed**. Acceptance requires PASS on all three axes.
