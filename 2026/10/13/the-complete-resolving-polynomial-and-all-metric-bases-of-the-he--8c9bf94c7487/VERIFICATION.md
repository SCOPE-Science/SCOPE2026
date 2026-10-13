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
# Reproducible finite verification

Execute `python3 verify.py` (standard library only). The script constructs all seven lines of the Fano plane, verifies its point-pair and point-degree axioms, obtains the fourteen-vertex incidence graph and all shortest-path distances, and builds the 42 distinct eight-vertex equidistance masks by incidence. It then tests the forbidden-set condition and a separate direct distance-signature predicate on each of the 16,384 vertex subsets; all agree. The exact resolving cardinality coefficients and the 168 minimum bases are recovered. Geometry tests reconstruct the 84 three-point/two-line bases, its dual 84 sets, all 168 Fano collineations, a polarity, 336 full graph automorphisms, and the unique orbit of bases.

Expected final lines:

```text
VERIFY_OK Heawood vertices=14 edges=21 42_equidistance_8_sets
VERIFY_OK all_masks=16384 nonresolving=4796 resolving=11588
VERIFY_OK polynomial=5:168,6:1890,7:3096,8:2961,9:2002,10:1001,11:364,12:91,13:14,14:1
VERIFY_OK metric_dimension=5 bases=168 split=84+84 full_automorphism_group=336 base_orbits=1
```

Limits: This is a complete finite enumeration for this fixed fourteen-vertex graph, not a proof for an infinite graph family. The verification script is independently implementable, but no third-party mathematical audit or external certification is asserted.
