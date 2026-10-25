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

The critical-scales calculation derives the coefficient -2/3 from the first Edgeworth term and the quartic -1/12 from the Gaussian mixture, independently checked by exact symbolic differentiation. The standalone script critical_shells_check.py performed 20 finite numerical assertions for kappa -1, 0, 0.2, 0.7 and 1 and R=100000,1000000, all passed. It verifies positions and scaled spectral norm; finite numerics cannot prove the large-R root count or asymptotics. The written proof supplies exact integral, sign-variation and analytic bounds. No independent audit has been performed.
