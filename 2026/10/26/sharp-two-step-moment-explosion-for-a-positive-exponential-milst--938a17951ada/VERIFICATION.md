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

# Verification of the numerical-moment frontier

Run `python verify.py` with Python 3, SymPy, and mpmath installed. The script reads no external files. Its current execution returned:

```
verification passed: symbolic identities; 176 numeric/exact-rational checks
```

The symbolic checks establish the factorization \(g=xf\), the exact formula for \(q=f'g\), the unique critical point \(x=2\), the maximum \(4\sigma^2/27\), the double-zero expansion with coefficient \(1/12\), and the support-minimum identity \(f^2/q=x+1\). High-precision Gaussian quadrature independently checks the conditional-moment expression at 48 subcritical parameter combinations. The remaining 128 exact-rational checks sample the global inequality for \(q\).

The infinite-moment conclusions are **not** inferred from finite tests. Their mathematical proof uses: (i) the standard Gaussian quadratic-exponential integral criterion; (ii) the fact that the first-step image has positive density in a neighborhood of the critical state; (iii) the nonintegrable \(\exp(c/(x-2)^2)\) singularity exactly at the boundary; and (iv) a uniform one-step conditional-moment lower bound for persistence. The numerical verifier supports the algebra but does not independently certify these measure-theoretic arguments.

The result assumes exact arithmetic and untruncated normal increments. For exact sample paths, the exponent remains finite almost surely and produces strictly positive output even when the mathematical expectation is infinite. Neither finite Monte Carlo nor floating-point overflow is evidence for divergence of the mathematical moment.
