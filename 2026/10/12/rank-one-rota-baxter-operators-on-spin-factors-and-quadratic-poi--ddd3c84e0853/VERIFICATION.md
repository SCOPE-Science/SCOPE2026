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

Run `python3 verify.py` with Python 3. The script constructs the indicated diagonal spin-factor multiplication over eight prime-field instances and exhaustively checks every rank-one linear map with normalized projective image generator and nonzero functional. A bilinear identity is checked on all pairs of basis vectors, without presupposing the theorem's parameter restrictions. The resulting solution sets are compared with the proven classification and the closed count formula. The performed run returned `VERIFY_OK` with counts `8, 24, 48, 80, 128, 864, 624, 1040` in the order printed by the script.

These finite checks do not establish a theorem over arbitrary fields, extension fields or unbounded dimension; those conclusions require the proof in `RESULT.md`. The complete classification and the standard quadratic Gauss-sum zero-count formula are the two mathematical ingredients, with conventions and determinant sign spelled out in that proof. No independent audit has been performed.
