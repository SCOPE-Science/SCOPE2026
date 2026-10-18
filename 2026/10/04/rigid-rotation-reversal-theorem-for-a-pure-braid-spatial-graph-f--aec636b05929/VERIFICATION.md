---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

At actual frozen source notebook commit 9a0f379..., cells 68–69 define A=(+1,+1), B=(+2,+2), braid body at x=k+t, s(t)=(1−cos pi t)/2, z=±0.32 sin pi t; the host 8 vertices, 12 edges, side spacer/couplings and nested closure polylines have symmetric x-margins ±1,±2,±3. Under (x,y,z)↦(2m−x,y,−z), reversing t swaps occupied lanes and over/under elevations while retaining a positive crossing, and the expanded generator list is blockwise reversed because every block consists of identical generators. Side and return edges pair or preserve. This is an orientation-preserving rigid half-turn ambient isotopy. Burnside counts (2^m+2^ceil(m/2))/2 reversal orbits, yielding only an upper bound on isotopy classes; not uniqueness across other orbits.

## originality

PASS

The original Akgün et al paper and frozen notebook give concrete constructor and finite reversal-invariant Yamada data, including AAB versus BAA, not an all-word 3D rigid-rotation proof. Exact source code for host geometry and closure was independently inspected. Resultary found only the assigned result as universal reversal isotopy; other knot/graph findings concern different objects.

## value

PASS

A structural all-length identification removes a natural reversal redundancy in a computational spatial-graph construction; explains observed invariant coincidences geometrically and provides a nontrivial exact family-size upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
