---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

In characteristic 2, gradient of F equals products of three other coordinates, forcing >=2 zero coordinates; on a coordinate edge Q=0 has ratio roots ω,ω², giving precisely 12 nodes and locally uv+w²=0. For any line outside coordinate planes, restrictions of four coordinates are nonzero linear forms and the divisor of their product is even since it equals Q²; they must form two proportional pairs. Coefficient comparison then forces both ratios to solve a²+a+1=0. There are 3 pairings×4 choices=12 such lines, plus 2 conic-factor lines in each of 4 coordinate planes. This proves algebraic-closure completeness, not inferred from GF4 sampling. Independent GF4 enumeration exhausts 85 projective points, 357 lines, finds exactly 20 contained; every 190 line pair checked giving 72 nodal and 22 smooth intersections, every node belongs to 4 lines, all 20 lines swapped by Frobenius. Because geometric line set is finite, its reduced Hilbert scheme over perfect F2 is finite étale with ten degree-two closed points. These results apply to reduced scheme only; no claim about nonreduced tangent structure.

## originality

PASS

Exact claims were contrasted with primary mathematical results, aliases, stronger scope, and published semantic records; no inspected source logically implies the final exact claim, subject to explicitly logged residual risks.

## value

PASS

Complete line configuration, incidence and Frobenius arithmetic of an explicit twelve-nodal quartic is a natural exact surface-geometry invariant, distinct from merely counting singularities. Full geometric classification and Galois orbit census can serve as a reproducible finite-field benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
