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

The complete proof is included in `RESULT.md`. Execute `python3 verify_central_belts.py` using Python 3 standard library; it has no third-party dependencies. It was executed from the delivered source file and produced:

```
constant_sections 6 12 sides 6 normals 1000
constant_sections 12 24 sides 8 normals 720
constant_sections 30 60 sides 12 normals 960
cube_witness 4 6
VERIFICATION_OK
```

The program uses exact elements of \(\mathbb Z[\sqrt5]\), constructs all twenty triangular icosahedron facets by exhaustive supporting-plane tests, rectifies the icosahedron and octahedron, and groups the resulting edges by their unique plane through the origin. Every group is checked to be a connected degree-two cycle of the requisite size; the code then checks the vertex-sign edge-crossing count for the displayed integer normals. The cube examples give genuinely nondegenerate four- and six-sided central sections. No floating-point approximation is required.

The general if-and-only-if assertion is not certified by finite computations: it follows from a vertex-wall jump formula, a complete two-dimensional sign-imbalance lemma, and a planar convexity argument proving that matched edge pairs form full equatorial polygon cycles. The theorem assumes central symmetry and dimension three. The origin-plane genericity convention excludes directions orthogonal to original vertices. This is reproducible self-review, not an independent mathematical audit or a claim of historical priority.
