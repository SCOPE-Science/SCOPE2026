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

The exact two-round recurrence encodes all 3 equality comparisons and all 27 relational multiplication atoms over the ordered tuple (identity, first pebble, second pebble). For each first pebble it stores the set of second-pebble atomic diagrams; for each structure it stores the set of first-pebble types. Equality of these root sets is exactly a two-round EF win.

`dihedral_rank2.cpp` was executed across n=3..200 and gave precisely 13 root types. `cyclic_rank2.cpp` was executed across n=1..110. A distinct Python cyclic pointed-profile implementation evaluated all widths up to 144. The recorded C++ output `dihedral_rank2.out` is included, and the boundary classifications were checked against the analytic case split. The proofs of the finite exceptions rely on exact enumeration, not numerical approximations. The infinite argument and the cited dihedral transfer are necessary; the finite output by itself has no infinite scope.

Self-review only; independent audit has not been performed.
