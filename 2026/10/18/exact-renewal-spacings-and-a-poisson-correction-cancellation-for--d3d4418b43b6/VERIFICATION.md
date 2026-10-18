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

# Verification of the interarrival law

The included `verify.py` is a standalone numerical-and-symbolic checker. Run `python verify.py` with Python 3, NumPy, and SymPy installed.

The finite checker verifies: (1) the exact two-state Laplace-recursion solution and geometric-compounding form; (2) algebraically independent closed-form and \(A,B\) representations; (3) the first two isolated-gap moments via exact symbolic differentiation; (4) the sign and sharp root of the first-order correction; (5) finite-\(n\) values approaching the analytically derived limit; and (6) seeded synthetic Poisson-gap sequences, with their mean Palm spacing and negligible lag-one empirical correlation.

The checked finite calculations do not constitute a proof of renewal independence, of the exact formula for all parameters, or of asymptotic convergence. Those assertions are proved directly in RESULT.md. In particular, no total-variation convergence rate, uniformity over the Laplace variable, or higher-dimensional generalization is asserted.
