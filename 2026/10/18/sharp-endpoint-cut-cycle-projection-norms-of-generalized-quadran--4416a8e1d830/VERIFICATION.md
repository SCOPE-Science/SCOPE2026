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

# Mathematical and computational verification

## Exact symbolic steps
For an existing generalized quadrangle of order \(q,q\), with \(H=(q+1)^2(q^2+1)\), the root-centered Green-kernel steps are \(\Delta_i=(1-\sum_{j=0}^in_j/N)/m_i\). Their four explicitly listed rational values and the edge-rooted breadth-first two-tree decomposition yield the complete transfer-current column, not merely its first moments. The sum is \(1+6q^4/H\), the diagonal is \(2\Delta_0\), and the complementary column is \(8q^4/H\). Differentiation verifies strict monotonicity and the limits seven and eight. All-order conclusions rest on these algebraic and combinatorial steps.

## Executable checks
Run `python check.py`. Its implementation uses only the Python standard library and constructs the totally isotropic lines of \(W(3,q)\) from the standard symplectic form for \(q=2,3\). Independently from the analytic Green-kernel derivation, it forms the full graph Laplacian, inverts the grounded Laplacian with exact rational arithmetic, computes all transfer-current entries, and checks the expected diagonal, all absolute column sums of the cut projection, and all absolute column sums of the complementary cycle projection. Successful observed output:

```
q=2: 30 vertices, 45 edges, Q=47/15, C=128/45, all edge columns PASS
q=3: 80 vertices, 160 edges, Q=323/80, C=81/20, all edge columns PASS
ALL EXACT-RATIONAL CHECKS PASS
```

The 205 exact column checks are reproducibility evidence, not exhaustive evidence about every possible order. The theorem does not evaluate unrestricted minimum projection constants, other exponents, or nonexistent geometries.
