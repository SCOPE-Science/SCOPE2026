---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For all nondegenerate parallelograms K and any P in its closed body, polar integration of rays gives exactly pi M_K(P)=∫_K |x-P|^{-1} dx. A layer-cake identity coupled with Brunn–Minkowski for K=-K yields potential maximal at its center, strictly if P≠center, even on the boundary. A sheared centered parallelogram has horizontal slices of length a centered at sy/h; rearranging every slice toward 0 only increases inverse-distance potential and removes the shear while decreasing perimeter, with strictness unless shear 0. The rectangle potential equals 2[a asinh(h/a)+h asinh(a/h)]. As asinh is strictly concave, weighted Jensen with weights a/(a+h), h/(a+h) and arguments h/a,a/h gives upper p asinh(1), with equality exactly a=h; dividing pi yields the sharp mean chord coefficient. The proof is for uniform orientation of a chord through fixed P, not random affine-line chord sampling. Independent quadrature/identity comparisons passed 20 rectangles; the proof holds for arbitrary real sizes and shear.

## originality

PASS

Compared direct equivalences, stronger implications, exact tables, and the original papers; no decisive prior coverage identified for the same final statement. Residual priority and access risks separately recorded.

## value

PASS

The angular mean length of the chord through a chosen point in a parallelogram is a natural localized integral-geometric invariant. Optimizing its ratio to perimeter over all shapes and points with an exact unique equality configuration answers a clear sharp extremal question; the proof uses several natural but nontrivial reductions. Even if techniques are classical, the shape comparison is not a mere constant substitution in the triangle result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
