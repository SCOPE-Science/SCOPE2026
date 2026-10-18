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

Run `python verify.py` with SymPy installed. It independently builds the transient generator, computes its resolvent and absorption vector, and verifies the exact symbolic Laplace-transform identity and moment formulas. It checks five rational directional allocations for a heterogeneous extinction-rate pair and confirms exchange invariance, the balanced increase of mean and variance, and the rational Laplace-transform values at argument one. These tests are checks rather than a substitute for the analytical theorem; general validity follows from the displayed first-step equations. No external validation has been performed.
