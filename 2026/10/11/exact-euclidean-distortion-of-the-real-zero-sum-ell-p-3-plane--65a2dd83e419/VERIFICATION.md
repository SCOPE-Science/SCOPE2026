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

Run `python3 verification/check.py` in a standard Python 3 environment (no third-party packages). The program is embedded in this package and tests the exact integer quartic identity in 289 cases; finite-difference derivative certificate identities at \(p=2,4\) in 1,998 cases; and radial endpoint bounds in 20,020 configurations, including \(p=1\) and \(p=\infty\). The deterministic output should start `VERIFY_OK quartic_exact=289 derivative_special=1998 radial_bounds=20020`.

# Scope of checks

The exact formula for all real exponents relies on the written strict-convexity proof. Numerical sampling does not prove all radial values or all exponents. Nor does the finite script certify bibliographic originality. No external independent audit has been performed.
