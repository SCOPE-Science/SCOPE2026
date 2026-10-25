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

Run `python verify_huff.py` with SymPy installed. The script checks exact rational simplification, exact inverse roots, the exact maximizing exponent and share, and 5,000 seeded numeric tests across the three regimes. The observed output was:

```
PASS: exact rational inverse ambiguity, critical point and 5000 classifications
```

The complete proof does not depend on sampling: the derivative comparison is strictly monotone for every real \(\lambda>1\), the stated bounds include equality, and exact quadratic algebra verifies the explicit inverse example. Numerical tests do not validate the claim beyond the algebraic theorem. The work has not been independently audited. Historical priority remains subject to the literature-access limits explained in the scientific review.
