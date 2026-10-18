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

# Reproducibility and checks

Run `python3 check_bicone.py` (Python standard library, no external data).

Expected final token: `BICONE_ALL_CHECKS_OK`.
The script separately computes a complete directional section profile by (i) a polar-coordinate integral, (ii) a Cartesian chord integral, and (iii) elementary closed-form antiderivatives. It checks seventeen representative dimensionless slopes, probes thirteen half-height/radius ratios at 500 nonzero oblique slopes each, and confirms the endpoint disk and diamond areas.

The universal maximum and all equality cases follow from the symbolic proof in `RESULT.md`. Numerical integration or finite angle sampling alone cannot certify the strict inequalities for all positive slopes. The cosine-product partial-fraction identity and coefficient comparison in `RESULT.md` are the key noncomputational lemma. No independent mathematical audit has been performed.
