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

The included standard-library `verify.py` reproduces rational Dirichlet moments, the local polynomial identities underlying the interior normal form, and the upper-endpoint quadratic form. It also checks Monte Carlo moment estimates using a fixed seed and produces `VERIFY_OK` on success.

The infinite-direction density and asymptotics are proved analytically in `RESULT.md`. A finite Monte Carlo experiment does not certify the logarithmic coefficient or endpoint limits. The directional projection-area formula and sharp admissible support-function range are acknowledged as previously published inputs, not new results.
