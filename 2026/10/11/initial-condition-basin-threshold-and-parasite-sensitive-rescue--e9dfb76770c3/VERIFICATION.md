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

# Reproducibility and mathematical limits

The exact polynomial factorization, positive saddle eigenvalue, example fold inequality, and constant-parasite first-order coefficient are reconstructed by running the accompanying `check.py` with a standard Python interpreter. The ODE numerical shooting estimates stated in the result were separately obtained using finite-time integrations; they are illustrative only. The proof establishes all positive-time and infinite-time conclusions analytically through comparison, scalar order, continuous dependence, and the stable-manifold linear response. This package does not provide an independent audit and does not claim a computer-assisted proof of infinite-time behavior.
