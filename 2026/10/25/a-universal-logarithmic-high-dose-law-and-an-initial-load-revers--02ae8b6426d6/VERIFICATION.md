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

The accompanying `check.py` uses only the Python standard library. It checks the closed-form exact zero-dose threshold and derivative for the witness \(T=3\), \(x_0=0\), \(y_0=2\), then independently integrates the differential equation over the observation interval at small and large finite doses. `check_output.txt` is its recorded output. Reproduce with `python check.py` in the directory containing these two files.

The global existence of a positive minimizer and the universal \(C(u,T)/\log u	o1/2\) result are supplied by the analytical proof in RESULT.md. Neither is a finite-checker conclusion. No independent audit was performed. No finite-dose error bound on the asymptotic is established.
