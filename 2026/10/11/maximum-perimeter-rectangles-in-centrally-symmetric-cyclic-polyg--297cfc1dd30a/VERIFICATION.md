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

# Verification and proof boundaries

The proof in `RESULT.md` establishes the assertion for every centrally symmetric cyclic convex polygon with at least four vertices. Its critical facts are: centralization by averaging a rectangle with its reflection; a separately convex half-diagonal perimeter functional; equal-length vertex radii, which turn extremal vertex pairs into actual rectangles; strict positive Hessian for noncollinear half-diagonals, implying all corners are vertices; and the chord/angle identity reducing the exact optimum to two projective-circle directions nearest perpendicularity. The off-center equality case is excluded by summing the squares of opposite translated vertices in the circumdisk.

Reproduce the finite numerical diagnostics with `python3 verify_rectangle.py`, using the Python standard library only. Recorded standard output:

```
VERIFY_OK regular_cases=300 cyclic_polygons=104 interior_rectangle_checks=26000
```

The test script performs direct Euclidean vector calculations for every even regular polygon order from 4 through 602, 104 fixed-seed centrally symmetric cyclic examples, independent quadratic and two-pointer angle searches, and radial halfspace tests of 26,000 feasible centered random rectangles. The random examples are reproducible but do not exhaust cyclic polygons or establish any statement over an infinite domain. No external independent audit has been performed. Numeric tolerances are explicit in the script.

Analytic checks also handle the four-sided case, both residue classes modulo four, and the limit of the cosine deficit. For arbitrary noncyclic or nonsymmetric polygons, the vertex-feasibility reduction is unavailable and no conclusion is asserted.
