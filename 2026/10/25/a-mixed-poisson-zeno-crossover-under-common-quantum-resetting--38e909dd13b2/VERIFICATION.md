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

# Verification record

The exact stationary spin-count generating function follows from the exponential reset-age representation and conditional independent Bernoulli readouts. The variance identity and individual first/second transition-probability moments were algebraically reconstructed and compared with numerical quadrature. The mixed-Poisson limit uses a dominated convergence argument, the subcritical statement uses an explicit \(L^2\) coupling, and the tail statement uses Poisson Chernoff inequalities on both sides of the mixing-age transition.

The included `checker.py` (Python with `mpmath` 1.3.0; installation range in `requirements.txt`) was executed in the package working directory. It passed 132 deterministic assertions, including quadrature of finite-size generating functions for multiple \(N\), independent evaluations of stationary moments, limiting generating-function identity with `erfc`, analytic factorial moments and off-critical numerical trends. The execution summary is `CHECK_RESULTS.json`. The code is an independent numerical corroboration, not a proof of the asymptotic statement, which is given in `RESULT.md`.

The claimed domain assumes fixed Hamiltonian coefficients, global complete Poisson resets, stationary preparation, and one projective readout; it does not establish finite-time uniformity, interactions, or cost of reset operations. Priority has been compared with the identified underlying published model and general renewal literature; independent scholarly verification is not yet available.
