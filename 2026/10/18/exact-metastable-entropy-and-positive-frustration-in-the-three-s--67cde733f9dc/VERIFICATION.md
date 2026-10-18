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

# Reproduction and limits

Run `python3 artifacts/verify.py` with Python 3 and `artifacts/requirements.txt` installed. The checker deterministically regenerates the transfer from the three-neighbor multiplicity rule, computes and factorizes the exact integer characteristic polynomial, checks the Perron component's strong connectivity and aperiodicity, and computes the separate proper/strict transfers. It enumerates all labeled three-color spin assignments on two-row cyclic prisms with three through six columns (up to 531,441 assignments at six columns) and verifies weak minima, ground states, strict ground states, and their total energy sums against independent transfer traces. It evaluates the Perron root and energy density numerically.

The exact algebraic factorization and strict root separation are analytic statements in RESULT.md and rely on integer polynomial arithmetic plus explicit inequalities. Enumeration at finitely many lengths does not prove a theorem for all lengths. The limiting energy law also requires analytic perturbation and positivity of Perron eigenvectors, as stated in the proof. The supplied code uses exact arithmetic for polynomial identities and floating-point arithmetic only for displayed approximations. No independent external audit is asserted.
