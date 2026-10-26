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
# Verification and limits

The all-dimensional theorem is proved in RESULT.md by the exact generalized-eigenvalue pencil, convexity of spectral log moments and the generalized Courant–Fischer principle. The nuclear-norm consequence additionally uses positive-semidefinite Nyström residuals and Löwner–Heinz. The sharpness family has exact symbolic eigenvalues and its asymptotic ratio follows by polynomial division and square-root expansion.

Run `python verify.py` after `pip install -r requirements.txt`; the script uses NumPy and SymPy. At preparation time it printed `VERIFY_OK symbolic identities, sharp gap, and 1728 random matrix comparisons`. These calculations cover several sample dimensions, sketch ranks, integer iterations and fractional/superlinear exponents, and check the explicit two-dimensional algebra. They cannot establish an infinite-dimensional or all-input statement; only the displayed proof establishes the universal finite-dimensional quantifiers. No independently commissioned scientific audit has been performed.
