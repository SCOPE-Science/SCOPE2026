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

The exact proof is in `RESULT.md`. Reproduce the finite and symbolic checks with `python verify_fsbp.py` (Python 3 plus SymPy). The script runs matrix multiplication and exact polynomial-remainder tests for the exponential and trigonometric nodal identities, then explores a finite set of hyperbolic and trigonometric parameters. The checked invocation returned `VERIFICATION_OK 2862 checks`.

The all-parameter positivity classification follows analytically from the signs of the forced weights. The constant-mass strict inequality follows from the derivative identity for the explicit scalar function; the unique trigonometric normalization root follows from strict logarithmic monotonicity. Neither statement is inferred from numerical sweeps. The displayed decimal root is only an approximation.

No independent audit or external verification was performed.
