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

The mathematical proof is in `RESULT.md`. `verify_sparse_anchor.py` is a reproducible auxiliary checker that requires Python 3, SymPy, and SciPy.

Command: `python3 verify_sparse_anchor.py`

Actual checks: expansion by the \(SU(2)\) fusion product against the closed fourth-moment polynomial for each integer \(n\) from 1 through 60; exact radical identities for both parity limits; numerical optimization at 14 distinct indices from 9 through 800, compared with the predicted scaled norm gain and low-mode amplitude; additionally, 12 independent Weyl-Haar class-angle quadratures with complex coefficients at six small weights. The output from the execution used for this package is in `verification_output.txt`.

A finite checker cannot establish a uniform all-integer theorem, uniqueness of asymptotic critical points, or a bibliographic originality assertion. Those mathematical conclusions instead rely on the product expansion, one-variable maximization, and uniform stationary-point argument given in `RESULT.md`. Numeric optimizer tolerances do not constitute formal error certificates.
