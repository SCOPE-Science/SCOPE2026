---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Brunn–Minkowski gives the midpoint body area at least the common area, while inclusion in the equal-area middle body gives the reverse inequality. Equality therefore holds, so the two outer convex bodies are homothetic; equal area forces a translation, and equal-area inclusion identifies the middle body with the midpoint translate. An affine shear turns all three slices into copies of one body \(K\). For any nonhorizontal halfspace containing the middle centroid, its slice sections are nested parallel halfplanes; the middle one contains the centroid and therefore at least \(4/9\) of \(K\), and one outer section contains it and contributes at least another \(4/9\). Horizontal halfspaces contain at least two whole slices. Thus the captured mass is at least \(8a/9=(8/27)\cdot3a\).

## originality

PASS

Cheng–Basu prove the universal sharp \(2/9\) bound under the same midpoint inclusion, but their full v1 preprint contains no equal-area refinement or occurrence of \(8/27\). Their sharpness construction is explicitly unbalanced, with one slice area tending to zero and the other two near one half. Exact equal areas instead force equality in Brunn–Minkowski and translation rigidity, enabling a stronger two-slice centroid estimate not present in the source. Resultary returned only the assigned record as an exact match.

## value

PASS

The source's sharpness mechanism is maximally unbalanced, making exact balance a mathematically natural regime rather than an arbitrary slice. It forces a strong equality-case rigidity and improves the certified depth by one third relative to the universal \(2/9\) bound at a canonical explicit point, furnishing a useful benchmark for future balance-stability refinements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
