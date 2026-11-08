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

# Verification of the finite calculations

Run `python3 verify.py` from the directory containing this file. The script uses only Python 3's standard library and prints `PASS 131 finite checks; exact enumeration and asymptotic numerical checks` on success. The checks compare exact rational falling-factorial moments against exhaustive missed-set sequences for small universes; verify pairwise negative correlation and the star mean identity; and test numerical Stirling-scale consistency on large integer instances. Numerical and finite exhaustive evidence does not certify the analytic Poisson limit: its proof is given in RESULT.md, Steps 1–6. No independent mathematical audit has been performed.
