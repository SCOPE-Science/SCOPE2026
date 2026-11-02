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
# Reproducibility and limits

Run `python3 verify_symbolic.py` with SymPy installed. It checks the whole 10-by-10 Cartier matrix in characteristic five against independently constructed coefficient expansions; it also verifies the 2-by-2 block determinant and the cone-coordinate transformation. Successful output: `CHAR5_CONDUCTOR6_EXACT_CARTIER_Q_AND_A1_OK`.

Run `python3 verify_finite.py` with Python 3 and only the standard library. Its independent finite-field arithmetic reconstructs the matrix and its rank for every one of the 625 tuples over the prime field. Expected output: `CHAR5_CONDUCTOR6_GF5_ALL_625_Q_STRATA_OK {0: 5, 3: 120, 4: 500}`.

These computations checked the formulas. The geometric statement over the algebraic closure additionally uses the explicit Cartier-rank proof and the normal-cone proof in `RESULT.md`. Neither the prime-field census nor the program exit status is an infinite proof. External independent audit and mathematical validation have not been performed.
