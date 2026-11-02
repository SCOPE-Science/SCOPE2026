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

# Verification

The theorem is proved analytically in `RESULT.md`. A reproducible, geometrically independent diagnostic is included as `verify_prisms.py`: for several integer base orders and heights, it draws Gaussian normals and counts intersections of the plane with every prism edge directly from endpoint signs. It compares empirical maximal-side probabilities to the closed-form prediction, tests the local height optimizer, checks deterministic crossing configurations and compares large-base values with the exact leading constant.

Run `python3 verify_prisms.py` with Python 3 and NumPy installed. The executed standalone program terminated with `ALL_CHECKS_PASSED`; representative random-sampling discrepancies for 220,000 normals per case were below 0.0042. Random tests and finite grid checks cannot certify universal statements; the exact integral and derivative in the proof do so. No independent mathematical audit has been performed.
