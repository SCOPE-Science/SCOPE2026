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

The standard-library verifier reconstructs the line configuration over the exact field \(\mathbf Q(\omega)\), not via floating point or finite-field specialization. It then exhaustively enumerates the sixers and automorphism action and checks every asserted profile and pair intersection.

Recorded replay:

```
lines=27 sixers=72 aut=648 orbit_sizes=18,54
profile_histogram=(0,3,3):18,(2,2,2):54
orbit18_blocks=6,6,6
cross_block_intersection=1 for all 108 pairs
within_each_block: intersection0=9 intersection3=6; disjoint_graph=triangular_prism; intersection3_graph=C6
orbit18_global_pair_intersections: 0=27 1=108 3=18
VERIFY_OK
```

The replay establishes the finite classification claimed here. It does not test any moduli-wide generalization, and it is not an independent audit.
