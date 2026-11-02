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

# Reproducibility checks

Run `python3 verify.py` with Python 3.9 or later; no third-party packages are needed. The script checks the explicit tenth-power matrix, its factorization as identity plus four times an integral matrix, both negative-index zeros, and both odd first-order coefficients (one and nine). It verifies the recurrence valuation formula for the first 139 values of the integer parameter in both progressions, and checks the defining binomial-parity sum directly for Mersenne indices with lengths 0 through 9 and 14 using Lucas' theorem.

Expected output begins with `VERIFY_OK`. These arithmetic checks cannot replace the infinite 2-adic binomial argument in RESULT.md. The published run-length equivalence is cited as a literature premise rather than independently recertified here. An external independent mathematical audit has not been performed.
