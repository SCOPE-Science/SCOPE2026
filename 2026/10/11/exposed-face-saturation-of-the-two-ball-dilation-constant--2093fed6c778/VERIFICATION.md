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

# Verification and scientific limits

The accompanying `verify.py` is self-contained (Python 3 standard library only). Run `python3 verify.py` in the extracted directory. The observed result was `VERIFY_OK`. It checks the rational strip witness at \(a=4/5\), the exact rational intermediate example \(a=15/16\), the clipping inequalities and radial formulas, equality witness distances and polygon norm calculations for selected even \(N\) through \(80\).

The code is finite and includes floating-point trigonometric comparisons; it does not certify the claims for arbitrary dimensions, continuous parameter values or infinitely many polygons. Those parts follow instead from the fully stated compactness/duality, exposed-face classification, and monotonicity arguments in `RESULT.md`. Both endpoint equalities and strictness are included in the proof. No external or independent validation is asserted.
