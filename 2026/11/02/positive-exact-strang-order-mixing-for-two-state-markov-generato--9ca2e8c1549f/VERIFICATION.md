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

Execute `python3 verify.py` from the directory containing this file and `verify.py`. No third-party packages or internet connection are needed. The verifier checks 300 reproducible two-state positive-rate instances, 15 equal-rate special cases, four positive-step three-state trace defects, and exact rational trace polynomials. Five distinct rational interpolation nodes certify that the difference of the two polynomial sides (degree at most four) is identically zero. All universal two-state inequalities and identities are proved analytically in `RESULT.md`; the floating-point tests are diagnostic only.

Expected output begins `VERIFY_OK` and reports the number of checks. Testing does not provide an independent audit, numerical conditioning claim, or formal proof of the universal two-state statement.
