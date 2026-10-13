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
# Verification notes

The proof is analytic and complete under the stated positivity and equal-marginal assumptions. The attached `verify.py` is a standalone Python 3 diagnostic and does not require external data, previous artifacts, or third-party packages. It checks finite numerical instances of: both multiplicative updates against their logarithmic reduction, exact conditional cosh ratios, strict potential descent for interior relaxation, preservation at the endpoint, ascent above the endpoint, and the mean-log scalar recurrence. It also verifies the local Jacobian stability inequalities in finite instances.

Finite numerical tests are not certifications of convergence for all initial conditions. The infinite-horizon convergence proof uses coercivity, strict Lyapunov descent, unique minimization and the local Schur inequalities. The endpoint obstruction uses an exact conserved quantity, not numerical behavior. The logarithmic ratio formula avoids asserting any gauge-specific limit for individual scaling factors.
