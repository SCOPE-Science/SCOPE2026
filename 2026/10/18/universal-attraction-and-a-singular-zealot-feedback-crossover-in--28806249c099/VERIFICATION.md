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
# Mathematical verification

The stationary condition was derived from the exact deterministic fluxes stated in RESULT.md. Its logarithmic ratio was differentiated through a positive integral, giving a strict sign throughout the interval. Hyperbolicity follows because the flux-ratio derivative is strictly negative at the unique zero. The zero-commitment double limit uses locally uniform convergence and monotone root bracketing; the fixed-bias minority law uses a distinct boundary estimate.

Run `python3 check.py` using Python 3 and its standard library. The program checks the original vector field at numerically determined stationary roots, the reflection property, one-sided flow signs, the derivative at neutral feedback and representative asymptotic regimes. Such checks are finite diagnostics and do not certify the infinite-parameter theorem. The analytic proof is self-contained in RESULT.md.

No finite-population convergence, nonlinear time-varying feedback, network effect, or independent scientific audit has been established.
