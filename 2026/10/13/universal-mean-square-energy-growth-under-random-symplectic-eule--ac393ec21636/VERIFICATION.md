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

`verify.py` performs reproducible finite-dimensional symbolic computations using Python and SymPy. The exact matrix expansion independently reconstructs the transfer operator for all fourth-moment symbols. The factorization of \(\det(I-T)\), two-point identity, constant-step positive invariant form, and fixed rational witness are checked as polynomial identities rather than floating-point approximations. A further finite loop checks rational step distributions and initial-state quadratic updates using exact fractions.

The infinite-family theorem is established by the proof, not by finite enumeration. In particular, the spectral-radius inequality follows from the determinant sign, and the uniform lower bound for every deterministic initial state follows from a positive-definite adjoint eigenmatrix. The positive-map Perron--Frobenius existence statement is invoked as a standard finite-dimensional cone theorem, and its rank-one boundary case is explicitly eliminated in the proof.

No independent audit has been performed. The disclosed source-comparison residual risk is potential equivalent treatment in older random-products/symplectic-integration literature.
