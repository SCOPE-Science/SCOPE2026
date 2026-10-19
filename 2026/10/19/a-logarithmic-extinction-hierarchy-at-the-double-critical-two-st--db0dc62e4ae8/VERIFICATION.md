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

The accompanying `verify.py` exercises exact rational parameter identities and independently integrates the stated eight-dimensional deterministic dynamics for two biologically permissible parameter sets. It checks population conservation, aggregate-infection algebra, positive densities, and finite-time tail indicators. Finite integration does not establish the asserted infinite-time limits: those depend on the Riccati inequalities, exponential convolution bounds, logarithmic-time competition argument, and stable-convolution asymptotic in RESULT.md.

The numerical indicators approach their limits slowly because of logarithmic corrections. Integrator tolerances and maximum integration time are explicit in `verify.py`; simulations should not be mistaken for a proof of a limit or for a stochastic-population prediction.
