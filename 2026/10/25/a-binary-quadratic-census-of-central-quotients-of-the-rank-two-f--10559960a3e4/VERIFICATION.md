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

Run `python3 verify.py` with Python 3 and no third-party dependencies. On the packaged source, the checker reports `CENTRAL_QUOTIENT_RANKS_OK` after exact finite-field checks over fields of sizes 2, 3, 4, and 5. The checker constructs the Lie bracket coefficients, independently checks Jacobi identities, calculates quotient-adjoint ranks, and generates the projective orbit partition of central lines. Fields of sizes 2, 3, and 4 are exhausted; size 5 is checked by orbit representatives, with the complete orbit partition independently verified. The test is finite and does not establish uniformity over all prime powers; the mathematical proof in RESULT.md establishes that claim.

No independent mathematical audit has been performed.
