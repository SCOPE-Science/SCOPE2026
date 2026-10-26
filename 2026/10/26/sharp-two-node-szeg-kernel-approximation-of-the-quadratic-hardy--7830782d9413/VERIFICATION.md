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

# Reproducibility and verification
Run `python3 check_exact.py` with Python 3.9 or newer. The script verifies the exact polynomial identity after square completion; computes the Blaschke coefficients for the explicit extremizing roots using exact rational Gaussian arithmetic; independently evaluates the two-kernel Gram projection; and samples finite randomly generated complex node pairs to stress the universal bound. The random sampling is corroboration only and cannot certify the global optimum. The universal bound and optimizer classification are proved in `RESULT.md` using Hardy model spaces, Schwarz--Pick, and a nonnegative exact polynomial decomposition. No independent audit or independent validation is represented.
