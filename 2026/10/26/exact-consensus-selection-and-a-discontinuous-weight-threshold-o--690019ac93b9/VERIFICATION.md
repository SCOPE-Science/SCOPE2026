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
The standalone `verify.py` requires Python’s standard library. Running `python verify.py` on the packaged file returned:

```
PASS: exact rational sensitivity examples, closed-form trajectories,
and independently evaluated weighted-median differential equations.
```

Checks include exact rational values at weights on both sides of the half-weight boundary and at equality, explicit multi-leaf trajectories, finite-difference residuals for the independent median-selection definition, and convergence of the closed forms. Finite checks do not prove the theorem for all star sizes; that proof appears in RESULT.md. No external independent audit or validation is asserted.
