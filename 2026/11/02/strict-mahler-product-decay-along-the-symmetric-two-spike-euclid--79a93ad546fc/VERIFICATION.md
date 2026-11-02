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

The proof uses direct polar constraints, exact meridian integration, differentiation, and strict reversed Chebyshev integral inequality. The formulas are universal in integer dimension \(d\ge2\). The accompanying `verify.py` checks independently computed meridian-volume integrals for five sample dimensions, decreasing products at 7 sampled spike values, a three-dimensional exact rational identity, and the double-cone asymptotic. Finite numerical checks cannot prove untested dimensions or parameters.

Run using Python 3 standard library: `python verify.py`.
