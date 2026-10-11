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
# Verification

The exact combinatorial input is the published sixteen-vertex K3 model generated from two facet seeds by an order-\(240\) permutation group.

The embedded `verify.py` performs exact binary arithmetic only. It reconstructs the group and all facets, verifies the face vector, computes both relevant boundary-map ranks, enumerates all four-vertex subsets, checks every tetrahedral-boundary cycle, reduces the cycles modulo \(\operatorname{im}\partial_3\), counts distinct classes and support multiplicities, recomputes the support and class orbits, and checks that the minimum-support classes span the full homology group.

A successful replay prints:

`VERIFY_OK group=240 f=16,120,560,720,288 H2dim=22 empty_tetrahedra=1100 min_support_classes=508 multiplicity=1:320,3:80,5:108 tetra_orbits=20,60,60,240,240,240,240 class_orbits=20,48,60,60,80,240 span=22`

The computation is exhaustive for this finite triangulation. It does not establish any statement about other K3 triangulations or integral minimum-support homology.
