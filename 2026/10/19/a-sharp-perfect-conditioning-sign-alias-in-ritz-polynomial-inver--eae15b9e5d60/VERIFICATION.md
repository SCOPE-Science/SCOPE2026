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
# Reproducibility and verification

Execute `python verify.py` with Python 3, NumPy, and SymPy (see `requirements.txt`). The script reports `VERIFICATION_OK` with 169 checked assertions. Symbolic identities cover the interpolation polynomial, exact cubic factorization, Lanczos Hankel-moment determinant and projected eigenvalue moments, the visibility threshold polynomial, and the derivatives needed for the condition-number asymptotic.

Independent dense two-step Lanczos projections were computed for a range of strictly positive pilot amplitudes. They confirm the Ritz moments, the expected sign regime, and the actual one-step Arnoldi output; small-parameter checks compare the predicted first-order preconditioned conditioning. These finite checks are corroboration rather than proof of the identities for all positive parameters. The `RESULT.md` proof supplies the global algebraic and monotonicity arguments.

The reproducible test uses standard floating-point operations for its numerical examples and exact SymPy algebra for the critical polynomial identities. The analysis assumes exact arithmetic and does not quantify floating-point roundoff. The negative spectral sign is an input-polynomial branch condition, not a failure of a correctly evaluated principal inverse square root of the preconditioned matrix. Independent audit has not been performed.
