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

Run `python3 verify.py` in the directory containing `verify.py`; no nonstandard Python modules are needed. The executed verifier printed `VERIFIED 2760 assertions`. Checks include exact-rational inclusion–exclusion computations over \(2\le m\le500\), independent exact polynomial integrations for a three-spacing simplex, exact truncated moments for thresholds \(2/5\) and \(3/5\), positive-definiteness of both marginal variances, and numerical diagnostics for the asymptotic expression.

The analytic argument in `RESULT.md` establishes the formulas for all allowed dimensions and thresholds, including breakpoints. Finite computations alone would not prove that infinite statement. No external independent audit or certification has been carried out.
