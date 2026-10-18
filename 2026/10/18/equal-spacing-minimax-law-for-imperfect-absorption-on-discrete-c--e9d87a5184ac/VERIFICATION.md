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

Run `python3 verify.py` with Python 3 and NumPy. The checker independently forms the finite-cycle matrix, computes the largest row sum of the inverse through a linear solve, and checks every trap placement in the specified small test dimensions at two rational killing rates and three floating-point rates. It also confirms that equal-spacing placements attain the proposed formula. The completed run returned `VERIFY_OK exact_cases= 516 float_cases= 17274`.

The analytic proof is the mathematical certificate for all admissible parameters. Finite exhaustive enumeration in the listed sizes neither proves the infinite family nor excludes earlier equivalent literature; no external independent mathematical audit has been carried out.
