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

The standalone `verify.py` reconstructs the monomial generator under rate-one probe-only Poisson jumps, computes the degree-two and degree-four stationary mixed moments, builds the closed two-time cubic-plus-linear observable generator, and verifies by exact symbolic algebra the positive initial derivative and the slow-mode residue. It reconstructs and checks all six quartic Routh–Hurwitz positivity certificates, the unique-root Descartes polynomial, and the signs of all denominator factors. Its finite numerical residue-sign samples do not replace the rigorous polynomial argument.

Run `python verify.py` with Python 3 and SymPy; no network access or source-paper files are needed. Assertions terminate on failure and the command prints `PASS` only after successful completion. The numerical threshold is reported as an approximation; its exact definition is the unique root of the displayed degree-eleven polynomial. The asymptotic sign at the critical cancellation point and intermediate-lag crossings below threshold are not established. Independent audit: not performed.
