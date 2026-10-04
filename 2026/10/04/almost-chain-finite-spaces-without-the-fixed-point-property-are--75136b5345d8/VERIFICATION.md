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

The proof is symbolic and does not depend on computation. The critical steps checked were: (1) monotone iteration in a finite poset forces a fixed point whenever a point is comparable with its image; (2) under incomparability degree at most one, a fixed-point-free map must equal the unique mate involution; (3) monotonicity of that involution makes the quotient by mate pairs a total order; and (4) the converse swap map is order-preserving.

`verify.py` is a dependency-free corroborative checker. It enumerates all labeled posets on at most four points, filters to the stated incomparability hypothesis, enumerates all self-maps, and compares actual fixed-point-free monotone maps with the theorem. It also brute-forces the canonical ordinal sums with one, two, and three two-point levels. Its recorded output is:

```text
GENERAL [(1, 1, 1, 0), (2, 3, 3, 1), (3, 19, 12, 0), (4, 219, 66, 6)]
CANONICAL [(1, 2, 1), (2, 4, 1), (3, 6, 1)]
VERIFY_OK
```

The computation is not an infinite proof and is not used to justify the all-cardinality theorem. The degree statement is verified mathematically by identifying the order complex with the boundary of the cross-polytope and the mate swap with the restriction of central inversion.
