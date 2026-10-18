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

The analytical proof in RESULT.md covers all integers \(d\ge2\) and all strictly positive feedback gains. The supplementary standalone `verify.py` was executed with Python 3 and SymPy; its exact-arithmetic output was:

```
VERIFY_OK 481 exact rational formula, monotonicity, endpoint and direct-matrix tests
```

The program calculates Walsh-spectral resolvent coefficients as rational numbers for dimensions two through eleven, checks exact inequalities for four gain pairs, verifies the closed-form near-antipodal differences, and compares the trace formula with explicit exact inverses of grounded matrices for dimensions two through four. No floating-point approximation, random Monte Carlo result, numerical root isolation, or unverified external data is used for these tests. Finite verification does not constitute the general proof; the heat-kernel ordering, potential maximum principle, and rank-two determinant expansion provide that proof. Results beyond the stated unit-edge and isotropic-noise scope are unproved.
