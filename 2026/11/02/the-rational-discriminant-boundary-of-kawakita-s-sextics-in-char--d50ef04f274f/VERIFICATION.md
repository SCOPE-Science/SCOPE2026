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
# Verification and limitations

`verify_boundary.py` is a Python 3 script requiring `sympy`. It executes exact integer polynomial computations and verifies all displayed congruences modulo \(3\), including the linear coordinate rewrite, the axis cubic, the double-root equation at \(q=b/a\), the perpendicular derivative, and the parameter-boundary witness over \(\mathbf F_{27}\). Actual output:

```
KAWAKITA_CHAR3_BOUNDARY_SYMBOLIC_IDENTITIES_AND_NONEMPTY_WITNESS_PASS
```

The all-parameter statements about irreducibility, the ten singularities and rational normalization are proved in `RESULT.md`, not inferred from finite field tests. Crucially, the parity-of-valuations argument shows the fourfold Kummer extension is a field, and the tame Riemann–Hurwitz calculation is genuinely for every algebraically closed ground field of characteristic \(3\). Neither a formal verification project nor an independent external audit has been performed.
