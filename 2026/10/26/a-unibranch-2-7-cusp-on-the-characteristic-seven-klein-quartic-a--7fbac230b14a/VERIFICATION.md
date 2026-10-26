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
Run `python3 verify.py` in a Python 3 environment. The exact arithmetic script enumerates all projective \(\mathbf F_7\) and \(\mathbf F_{49}\) points and checks the three partial derivatives at all points. The observed output includes `FIELD 7 POINTS 8 EXPECTED 8 SING [(1, 2, 4)]`, `FIELD 49 POINTS 50 EXPECTED 50 SING [(1, 2, 4)]`, and `VERIFY_OK`.

These finite tests do not certify the universal point-count statement. That statement follows from the symbolic local proof, geometric integrality, genus-zero normalization and bijection on rational points. Independent audit has not been performed.
