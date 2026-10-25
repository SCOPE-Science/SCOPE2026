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

# Reproducible verification

The accompanying `verify.py` uses only Python standard-library exact rational arithmetic and an independent enumeration of fixed-composition binary words. Execute `python3 verify.py` with Python 3.9 or newer. The observed output was `PASS: 5648 exact rational and sign assertions; 16178 binary words enumerated`.

Enumeration covers all compositions with \(a,b\ge2\) and \(4\le a+b\le13\), checking exact means, mixed moments, unconditional covariance, every attainable conditioned covariance, and the strict three-run identity. Additional exact rational checks cover all \(2\le a,b\le49\). The checks exercise the formulas but do not certify the infinite family; the independent analytic proof is in `RESULT.md`. The uninspected older multiple-run papers remain historical-priority limitations, not computation errors.
