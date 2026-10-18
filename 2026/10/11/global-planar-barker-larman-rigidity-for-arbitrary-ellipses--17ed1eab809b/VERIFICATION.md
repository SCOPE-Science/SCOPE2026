---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Derived line–ellipse length from affine disk chord: L²/4=det(Q)[q(u)−(r−c·u)²]/q(u)², q=uᵀQu, r>0. Exact antipodal odd part isolates det(Q)(c·u)/q². For both nonzero centers, homogeneous degree-five identity and irreducibility of positive binary quadratics in R[x,y] force q2=kq1, then determinant scale gives centers equal and full even part k=1; centered case uses separate nonround/round argument, and one zero center forces the other zero. Strict inner-disc containment ensures all radicands positive. Independent symbolic algebra and inspect actual verify.py examples; finite samples explicitly not universal proof.

## originality

PASS

Yaskin–Zhang formulate one-inner-ball data determination as open for general bodies, their planar positive result uses TWO disks. Makai–Martini prove local determination under small perturbations and describe centered circles and polygons, not freely translated ellipses. Resultary contains narrower same-day centered-ellipse result, which does not settle unknown center. Free-center arbitrary positive quadratic matrices require new odd/even polynomial factorization. Primary 2001 Barker–Larman complete article inaccessible, retained as historical overlap risk.

## value

PASS

Global determination of an arbitrary five-parameter plane ellipse from one disk’s tangent-chord function is a natural complete smooth-quadratic subclass of the open Barker–Larman tomography question; center, orientation and semiaxes all reconstructed with rigorous parity/UFD mechanism. Meaningful structural rigidity beyond known concentric or polygon cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
