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

Run `python3 verify.py` with a standard Python 3 interpreter. The script reconstructs the integer formal-series coefficients through degree 22, checks the first six coefficients exactly, independently calculates the original exponential-series coefficients through degree 15 and compares them with the Stirling-transform expansion, and tests seven ternary prime-power levels with thirty-six consecutive indices each. The checked command returned:

`VERIFY_OK exact_g_prefix=6 independent_egf_coefficients=16 prime_power_levels=7 shifts=252`

All calculations are exact. The script verifies the finite base certificate and provides independent finite checks, while the unrestricted prime-power statement relies on the published written proof. No independent mathematical audit was performed.
