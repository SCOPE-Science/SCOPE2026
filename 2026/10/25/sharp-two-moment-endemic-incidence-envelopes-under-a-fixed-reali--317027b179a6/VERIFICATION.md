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

# Reproducibility

Run `python3 CHECK.py` using only the Python standard library. It verifies exact rational first and second moments of extremal and intermediate laws, stationary population conservation, the actual administered-dose constraint, and independent consistency with the original fixed-hazard SIRVS stationary formula. It also checks sharp ordering numerically across a parameter grid.

The universal distributional bounds are proved analytically in `RESULT.md` by the signed third-derivative Hermite remainder and the strictly increasing dose-budget map; the finite checker does not independently establish those quantified claims. Two-point laws are permitted in the renewal formulation; a duration-density-only formulation requires an appropriate limiting interpretation. Verification concerns a stationary system rather than dynamical stability or external validation.
