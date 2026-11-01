---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The projective-F2 rational point ideal is generated in degree three by six Frobenius binomials. Its 24 linear multiples have degree-four rank20, while multiples of G by four independent linear forms reduce the quartic-section quotient to 16 dimensions. A fresh independent bitset implementation enumerated all 65536 quotient masks and tested all 15 F2 points: exactly 288 have transverse gradients at every rational point. For those 288, independently computed exact Gröbner bases over F2 for all four affine charts of the complete-intersection Jacobian ideals give 144 geometrically smooth and 144 singular cases; five disjoint replay slices had smooth counts 28,28,28,28,32. An independent Cech cohomology computation forms the 19-dimensional kernel of multiplication by G on H^3(P3,O(-7)); multiplying Frobenius by GF gives rank19 on this kernel for every one of the 144 independently smooth masks (and images preserve the kernel). Thus all are ordinary. Degree=3*4=12, adjunction gives genus19, and smooth connected complete intersections are geometrically integral. Exhaustive finite algebra over F2 plus the Jacobian criterion proves the classification over the algebraic closure; finite-extension point sampling alone would not.

## originality

PASS

The specific binary symplectic cubic and construction of smooth space-filling (3,4) complete intersections are published by Campbell et al. That existence is not assessed as new. The additional all-class 144 census, the 288 rational-smooth filtering figure, and the uniform maximal Hasse–Witt rank for this entire finite linear system were not supplied by the closely relevant full primary article inspected.

## value

PASS

The complete 65536-class search in the natural binary quartic linear system fixes the exact smooth count and establishes a uniform arithmetic invariant, ordinary genus19, on every geometrically smooth member; this is a motivated finite classification, not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
