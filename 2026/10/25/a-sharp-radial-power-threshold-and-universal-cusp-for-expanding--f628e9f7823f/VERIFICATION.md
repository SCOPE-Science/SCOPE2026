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

# Reproducibility and verification

Run `python checks/verify.py` with Python 3 and mpmath installed. Its input is fixed; no network, private files, or unpublished data are needed. Expected output: `WEIGHTED_SPHERE_OK numerical_cases= 71`.

The script compares independent angular quadrature against a published spherical-potential closed form for 30 settings, tests 12 Newtonian boundary values, 16 two-sided cusp coefficient limits, 8 contact local-maximum inequalities, and 5 monotonic sequences. Floating-point evidence corroborates, but does not prove, the theorem. The actual universal proof and restrictions are in `RESULT.md`; arithmetic is provided as a supplemental consistency test.
