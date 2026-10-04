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
The proof reconstructs the two Bernoulli branch matrices of classic error feedback on a scalar quadratic.

`verify.py` uses exact rational arithmetic to check the branch-averaged three-moment recursion, the characteristic coefficients, all four cubic Jury expressions, the geometric waiting-time cycle factor and its optimizer, and the no-memory comparison.

The executable checks do not replace the infinite-time proof. Schur stability follows from the complete symbolic Jury factorization in `RESULT.md`, and necessity for the standard zero-residual initialization follows independently from the renewal calculation.
