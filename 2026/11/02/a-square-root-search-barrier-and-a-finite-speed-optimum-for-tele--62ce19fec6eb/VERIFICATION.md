---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The analytical proof in `RESULT.md` establishes the result for every strictly positive parameter \(D,a,\rho,\nu\). The principal computations use the eigenvalues and projectors of an explicit symmetric two-by-two matrix. The differentiability and asymptotics are ordinary finite-dimensional functional-calculus calculations, not limits inferred from numerical data.

Run `python verify.py` with a standard Python 3 interpreter. The reproduced check run passed **739** tests: 720 deterministic positivity and equation-consistency checks on an explicit parameter grid, 15 asymptotic scale comparisons, one finite-rate optimizer witness, and three independent Brownian path Monte Carlo comparisons (48,000 exact-segment paths). Statistical checks use a fixed reproducible seed, explicitly computed standard errors, and a six-standard-error tolerance. Their role is diagnostic rather than a mathematical certificate; occasional tail-induced Monte Carlo fluctuations are possible.

The path sampler uses Brownian reflection-principle first-hitting times on each uninterrupted interval and the killed heat-kernel distribution for the position at switching/resetting times conditioned on not hitting earlier. This avoids the boundary overshoot error of time-discretized Brownian simulation. The phase process is never reset when the particle resets.

Scientific limits: full priority certification, arbitrary environmental state spaces, general resetting distributions, uniqueness of the minimizing rate, and the equality-threshold next-order expansion are not established. Independent audit status is not performed.
