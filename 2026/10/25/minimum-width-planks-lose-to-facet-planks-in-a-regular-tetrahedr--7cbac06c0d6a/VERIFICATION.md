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
# Verification notes

The proof is a symbolic identity valid in a continuous width parameter; the standalone `verify.py` checks its critical algebraic identities in the quadratic field \(\mathbb Q(\sqrt3)\). Tested directly from the actual package directory:

```text
python verify.py
PASS: coordinate frame, beta densities, exact integrals, factorization, roots, and boundary checks
W* = 1.8564064605510183
```

The source assumptions are the four explicit tetrahedron vertices, Euclidean widths \(0<W<2\), and uniform interior volume. The directional-width characterization uses the exact vertex frame operator and equality in the range–variance inequality. The beta distributions follow from uniform simplex barycentric coordinates, and interval translation optimality follows from monotonicity of the section density. Both exact integrals were checked and their symbolic difference factored. All roots and admissible domain restrictions are stated explicitly. The program does not search over all oblique directions or families of planks, and no conclusion about them is certified. Independent audit remains unperformed.
