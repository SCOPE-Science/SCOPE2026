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

# Reproducibility checks

Run `python3 verify_so_incidence.py` to enumerate the complete three-color assignments on ten small parameter pairs and four-color assignments on the two-by-two and two-by-four cases. This checks the mathematical neighborhood definition directly.

Run `python3 verify_theta_so.py` to perform a separate dynamic-programming census of all page configurations, independently reconstruct the signed-character expression, and verify the closed four-color count at even parameter values 2, 4, 6, and 8.

Observed outputs: `VERIFICATION_OK` and `THETA_VERIFICATION_OK`, including four-color counts 168, 3264, 52368, and 821184. The mathematical proof of all-parameter statements appears in `RESULT.md`, and no finite computation should be treated as a proof outside its tested range. All source references describe public literature, not external certification of these claims.
