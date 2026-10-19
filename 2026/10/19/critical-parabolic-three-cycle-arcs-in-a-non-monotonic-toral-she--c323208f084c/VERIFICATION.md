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

# Reproducible checks

Run `python3 checker.py` from this package directory. It has no external dependencies, carries out every calculation in exact fractions, subdivides the square into convex affine cells at each of three steps and exhaustively solves the third-iterate torus fixed equations. It verifies that the cell areas at each step sum to one, that all isolated candidates and positive-length solutions lie in the stated set, and that all designated orbit representatives satisfy the direct exact third-iterate equations.

The observed result was:

```
PASS: 7/32/128 rational polygons partition the unit square
PASS: 32 point representatives and 12 exact rank-one segments all classified
PASS: exactly two fixed points, two isolated three-cycles, two interval families
PASS: all claimed families and their boundary points are periodic
```

The 32 point representatives include exact duplicates arising from the square's edges and from separate affine polygon pieces. The 12 segments likewise form subpieces of the six geometric periodic arcs. This is an exhaustive rational affine certificate: interior solutions solve invertible linear systems and singular solutions are intersected with closed polygons by exact half-plane arithmetic. Completeness includes shared faces because the map is continuous on the torus and the closed cells cover the square. The exact length formula and smooth-interior multiplier identities also have explicit hand derivations in RESULT.md. This verification is not an independent external audit, is specific to the stated critical shear parameter, and says nothing about higher periods.
