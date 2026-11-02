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

# Verification scope

Run `python3 CHECK.py` with Python 3 and the standard library. The program performs exact-rational solution of stationary second- and fourth-order generator systems and checks the resulting covariance resolvent against spectral integration. It also compares independent quadrature of the stationary autocovariance to its closed-form finite-window variance and tests the predicted large-bath observation-window scaling and higher joint moments. The actual run passed 282 deterministic assertions.

The main proof is analytic. A finite checker does not prove tightness, invariant-law uniqueness, Gaussian weak convergence, or infinite-parameter assertions. Those claims are supported by the Lyapunov, compensated-martingale, stationary Ornstein--Uhlenbeck and frozen-conditional-generator arguments in `RESULT.md`. The test suite makes no claim of independent audit or external verification.
