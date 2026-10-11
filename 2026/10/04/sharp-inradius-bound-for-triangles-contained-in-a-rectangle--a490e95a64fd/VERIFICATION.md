---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The standard boundary-enlargement reduction takes a contained triangle to a corner triangle without decreasing its inradius. For the normalized rectangle, the submitted quotient \(r=(h-xy)/P\) is correct. At any interior critical point, the second derivative in direction \((1,-1)\) is positive because \(A P''<2P\), excluding an interior maximum. The four boundary families reduce by convexity or direct differentiation to explicit one-variable values, and the long-side-base value \(h/(1+\sqrt{1+4h^2})\) dominates the other three for \(0<h\le1\). Rescaling gives the claimed formula and the midpoint-apex triangle attains it. An independent random containment check at five aspect ratios found no violation and approached the stated extremal value.

## originality

PASS

Abi-Khuzam--Barbara's complete primary article proves the sharp square case and develops the same kind of corner reduction, but it fixes aspect ratio one. The exact rectangular profile is not obtainable by anisotropic scaling because Euclidean inradii are not affine invariant. Targeted literature and Resultary searches for the rectangle formula returned the submitted record as the direct exact hit and no earlier rectangular theorem implying it.

## value

PASS

This is the sharp aspect-ratio completion of a published extremal square problem, with an explicit extremizer for every rectangle. The problem is a natural geometric invariant and the result is an all-parameter theorem rather than an isolated numerical case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
