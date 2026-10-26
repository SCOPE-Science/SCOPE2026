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

# Verification and reproducibility

The proof is self-contained in `RESULT.md`. Its critical identities can be checked symbolically: \(t+t^{-1}=C/B\), \(g_i'(y_i^*)=t^2\), the conservation relation \(\sum_i(g_i(y_i^*)-y_i^*)=0\), and the exact tangent remainder
\[
 g_i(y_i^*)+t^2(z-y_i^*)-g_i(z)
 =\frac{t^2(r_i/K_i)(z-y_i^*)^2}{1+(r_i/K_i)z}.
\]
Summing this identity at a positive equilibrium gives the claimed deficit, while applying it to the vector of isolated carrying capacities proves the strict enhancement criterion. Positive-equilibrium existence and uniqueness are established by monotonic fixed-point bounds and strict subhomogeneity, not by testing.

Run `python3 verify.py` with Python 3 and the standard library; no downloaded data, extra modules, or credentials are required. The tested package produced:

```
PASS: exact Q(sqrt(5)) benchmark (all identities, maximum, conservation)
PASS: 780 deterministic random cases p=1..6 (existence convergence, unique optimum, exact deficit, strict heterogeneity)
```

The exact benchmark uses patch parameters \(K=(3,8)\), \(r=(3,8)\), the field \(\mathbb Q(\sqrt5)\), and optimum \((11+5\sqrt5)/2\). The seeded numerical cases test both random positive stochastic matrices and their prescribed rank-one optima, with numerical tolerances and an explicit convergence-iteration limit. Finite tests are diagnostic; no claim of exhaustive parameter enumeration, external certification, or independent validation is made.
