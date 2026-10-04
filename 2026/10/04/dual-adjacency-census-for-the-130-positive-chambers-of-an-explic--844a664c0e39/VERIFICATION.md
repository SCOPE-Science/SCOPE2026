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

`artifacts/verify_dual_adjacency.py` independently reconstructs the intersection graph from the published Table-2 cyclic orders using only Python's standard library.

It checks:

- exactly 135 line-intersection vertices and 270 line-segment walls;
- every intersection-graph vertex has degree 4;
- exactly 10, 90, 30, and 0 induced cycles of lengths 3, 4, 5, and 6;
- every one of the 270 walls lies in exactly two of the 130 chamber boundaries;
- dual wall types are exactly 30 T--P, 120 Q--P, and 120 Q--Q;
- pentagon and quadrilateral neighbor profiles have the stated multiplicities;
- independent incidence handshakes sum to 270 dual edges.

Recorded output:

```
vertices=135
line_segment_walls=270
chambers=triangles:10 quadrilaterals:90 pentagons:30
wall_types=T-P:30 Q-P:120 Q-Q:120 others:0
pentagon_profile=30*(T:1,Q:4)
quadrilateral_profiles=20*(Q:4);20*(Q:3,P:1);50*(Q:2,P:2)
triangle_profile=10*(P:3)
VERIFY_OK
```

The verification proves the finite combinatorial claim for the embedded cyclic-order data. It does not prove that the same detailed profile is invariant throughout real cubic-surface moduli.
