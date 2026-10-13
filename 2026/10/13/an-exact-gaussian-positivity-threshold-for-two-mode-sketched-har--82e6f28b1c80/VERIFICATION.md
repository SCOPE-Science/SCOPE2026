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

Run `python verify.py` using Python 3 with NumPy and SciPy installed. This checks the independent 2-by-2 Sylvester determinant identity on 2,480 integer/rational sketch-and-spectrum combinations, including 624 exact negative witnesses; tests 1,800 direct Jordan-product eigenvalue signs; tests low-row incomplete-Beta identities; simulates Gaussian sketches with a seeded random generator; and compares numerical values against the proved normal and fixed-dimension limits.

All numerical tests use finite inputs and have no claim to certify a universal infinite family. The universal results instead rest on the explicit determinant criterion, the Gaussian spherical-coordinate distribution, monotone Beta ordering, the Gaussian limit, and elementary incomplete-Beta asymptotics provided in `RESULT.md`. No independent mathematical audit has been performed.
