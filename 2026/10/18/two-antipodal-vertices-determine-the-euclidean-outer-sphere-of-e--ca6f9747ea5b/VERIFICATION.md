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

# Computational and analytic verification

The proof uses the normalized path-average formula, complete coherent-path enumeration, and an exact convex maximization over a bounded ordered simplex. It proves the universal theorem for real strictly increasing positive coefficients; the checker below is an independent implementation of the finite instances, not an infinite certificate.

Run `python verify_signohedron.py` with the standard Python library. The script recomputes every vertex as a sum of trapezoid contributions over strictly increasing projection heights; it does not use the simplified squared-norm formula from the proof as its starting point. It verifies zero projection height, the radius inequality, the exactly two antipodal contacts, and the quantitative gap for paths containing multiple intermediate vertices.

Observed complete run:
```
PASS: profiles 597
PASS: exact coherent vertices 198294
PASS: multi-intermediate vertices and quantitative clearance 193860
PASS: unique antipodal contact pair and zero projection for every vertex
```

These tests range over strictly ordered positive rational height profiles in dimensions 2--9; dimension two is a consistency check outside the stated dimension range. The universal statements for arbitrary real heights and unbounded dimension follow from the analytic convexity proof, not from an exhaustive finite sweep. No independent mathematical audit has been performed.
