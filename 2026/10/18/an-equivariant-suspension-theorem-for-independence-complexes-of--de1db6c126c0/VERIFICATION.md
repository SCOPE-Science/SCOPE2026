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

# Finite replay and mathematical boundaries

Run `python3 verify.py` with Python 3 (standard library only). The checker enumerates every independent face for each of 64 simple graphs on four labeled vertices and for cycles of lengths five and seven. It verifies the face-union condition and equivariant simplicial retraction; it also calculates signed reduced Lefschetz numbers for every four-vertex graph automorphism and the dihedral symmetries of the two cycles. Expected final line: `VERIFY_OK four_vertex_graphs=64 cycle_examples=2`.

The general proof is not finite enumeration. Its essential facts are: the shadow projection is a \(\Gamma\)-equivariant simplicial retraction contiguous to the identity; the shadow simplex contracts equivariantly to its invariant barycenter; the apex link is the old independence complex; and collapsing a \(\Gamma\)-contractible invariant cofibration yields a weak equivalence on every subgroup fixed-point space. These steps apply to every finite nonempty simple graph and every inherited automorphism subgroup. No external audit has been performed.
