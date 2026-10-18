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

# Reproducibility and scope of verification

Run `python check.py` (Python 3 standard library, no third-party packages) to confirm the exact quadratic root and closed-form pole formulas using high-precision decimal arithmetic, the three alternating spectral errors, the admissible positive shift for a strictly positive-definite test matrix, and the sharp spacing inequality at 999 interior values of the exponential ratio. The same script checks 2,000 seeded random positive mixtures against the analytical three-point Jensen inequality and the exact three-point error floor.

The executed program reports:

```
algebraic extremizer, shifted SPD matrix and 999 q-cases: PASS
2000 independent positive-mixture checks: PASS
E_star = 0.051566846126417; shifted-SPD E_star = 0.039182329883356
```

These checks are finite and corroborative; the universal result is established by the algebraic and convexity proof in `RESULT.md`. External independent auditing has not been performed. Relevant inaccessible full manuscripts are identified as bibliographic limitations in `REVIEW.md` and `AUDIT.json`.
