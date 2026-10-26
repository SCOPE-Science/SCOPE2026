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

# Verification and limits

Execute `python3 artifacts/verify.py` from the package root. The script uses only the Python standard library. Its output is preserved verbatim in `artifacts/verification_output.txt`; successful execution prints `VERIFY_OK` and the number of completed assertions. Checks include exact Laurent sign counts, all mixed moment values, deterministic randomized complex coefficient comparisons, discrete dihedral averaging, and the global amplitude–phase deficit. In particular, tests across finitely many orders do not establish the all-order theorem; its analytical justification is the support bound on Fourier exponents together with an exact one-variable factorization in `RESULT.md`.

No independent mathematical audit, outside validation, or machine proof assistant certification has been performed.
