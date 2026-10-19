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

Run `python verify.py` with Python 3. The script directly multiplies the 2-cycle truncated polynomial coordinates modulo the relevant path-length bounds. Since the highest diagonal coefficients do not enter the square equations, it exhaustively checks all remaining ten coordinates over the three-element field and multiplies the result by the square of the field order. It also verifies coverage by the four stated component equations on each enumerated point, and performs a separate change-of-variable test for the modular dihedral realization over the seven-element field.

Expected terminal output: `VERIFY_OK`. The observed finite-field result is 6561 square-zero elements over the three-element field with zero component-coverage discrepancies. The seven-element field substitution passes. No computation proves the entire arbitrary-field theorem, geometric irreducibility or uniqueness in the literature; those rely on the explicit argument and comparisons.
