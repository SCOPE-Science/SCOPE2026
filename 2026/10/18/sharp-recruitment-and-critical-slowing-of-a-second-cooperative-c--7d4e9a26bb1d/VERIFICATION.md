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

Run `python check.py` with SymPy, NumPy and SciPy. Exact symbolic steps verify the normal-form coefficients and the five-dimensional threshold Jacobian; additional exact rational parameter tests verify the general endemic state and transverse eigenvalue identities. Numerical root solutions confirm the small stable coexistence branch; ODE integration checks transient convergence qualitatively. Infinite-time and all-parameter assertions come solely from the analytical proof. Independent audit has not been performed.
