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

The symbolic checker `verify.py` directly reconstructs the mass-balance identity and the generalized Dulac divergence from the model's equations, and checks exact-rational coefficient identities over 648 parameter combinations, including \(\eta=0\), \(\alpha=0\), and \(k=0\). It checks two coexistence equilibria exactly and runs sample ODE integrations on either side of the invasion threshold and at equality. Command: `python verify.py`, with `sympy` and `scipy` installed.

The analytic proof, not the finite parameter grid or integrator, establishes the universal quantifiers. In particular, finite-time numerical proximity to a limiting constant is **not** a rigorous infinite-time asymptotic certificate; the critical center-manifold expansion and global phase-plane argument supply those steps. No independent audit has been performed.
