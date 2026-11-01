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

# Reproducible verification

The standalone `checker.py` uses Python 3.10+ and the standard library only. Execute from a directory containing this file with `python checker.py`. A successful invocation reports 2841 finite checks. The checks include 200 rational secant identities at three assertions each, 480 numerical implicit-sampling checks at three assertions each, 160 supercritical-cycle cases at five assertions each, and a separate 120000-step critical-decay test.

The mesh root is located by bisection; the numerical checks use floating-point tolerances appropriate to their finite resolution. The exact rational tests do not depend on approximating exponentials. The analytical proof independently derives the implicit map, proves strict contraction for all admissible activation secants, derives the sharp linear-activation boundary and the nonlinear two-cycle, and establishes the critical \(k^{-1/2}\) convergence rate by inverse-square increments. Finite arithmetic does not prove universal quantifiers or historical priority.

Scientific limits: the result assumes a scalar nonimpulsive network, constant mesh and coefficients, and monotone Lipschitz negative feedback. Critical rates and two-cycles are specific to the sigmoid. The conclusion concerns local stability of the supercritical two-cycle. Independent audit has not been performed.
