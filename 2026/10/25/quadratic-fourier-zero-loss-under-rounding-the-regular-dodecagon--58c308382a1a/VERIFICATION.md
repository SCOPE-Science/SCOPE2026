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

Run `python verify.py` with mpmath installed. It checks the sign changes and interval coefficient as described in RESULT.md, using the exact elementary trigonometric formula. The theoretical remainder estimate uses the geometry and differentiability proofs in RESULT.md; the script does not certify global uniqueness or independent audit. The computed upper bound uses a single Fourier direction and may not equal the full minimization over directions.
