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

# Computation and proof verification

The standalone `verify.py` program recomputes the quantum channels by exponentiating explicit Lindblad superoperator matrices constructed directly from the jump operators, without using the closed-form Bloch affine proof as input. It compares both cycle-section outputs, all three Pauli directions, the Choi operators and the predicted PPT transition at each nearest integer. Numerical evaluations also test the closed-form purity defect and the leading rapid-switching coefficients. `requirements.txt` specifies the Python dependencies. Execute `python verify.py` from the extracted package directory.

The delivered checker passed 196 individual finite assertions. Every assertion is explicitly constrained to finite test data. The all-dwell and all-cycle results rest on the separate algebraic proof in `RESULT.md`, not on extrapolation from these checks. No Lean certification, external expert assessment or independent audit has been performed.
