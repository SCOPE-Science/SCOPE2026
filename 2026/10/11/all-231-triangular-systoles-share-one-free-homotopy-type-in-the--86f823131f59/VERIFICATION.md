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

`verify.py` reconstructs the complete ninety-tetrahedron complex and its one-skeleton. A lexicographic spanning tree leaves \(91\) edge generators for the standard edge presentation of the fundamental group.

`group_certificate.json` assigns those generators to words in two explicit degree-\(120\) permutations. The verifier checks all \(180\) triangular relators and enumerates the generated permutation group to exactly \(120\) elements. Two original edge generators map to the two permutation generators, so the representation is surjective. The published topology supplies \(|\pi_1|=120\), hence the representation is faithful.

The program then enumerates all \(411\) three-vertex cliques in the one-skeleton, subtracts the \(180\) facial triangles, and evaluates all \(231\) remaining triangular loops in the faithful group. It verifies order \(10\) for every image, computes a conjugacy class of size \(12\), checks all \(231\) images lie in it, and checks the class is inverse-stable.

Exact successful output:

`VERIFY_OK f=16,106,180,90 tree=15 edge_generators=91 perm_group=120 triangle_relators=180 cliques3=411 missing3=231 missing3_orders=10:231 conjugacy_class=12 inverse_stable=yes`

The finite group and loop computations are exhaustive. The only external mathematical premise used by the certificate replay is the independently published identification of the complex with the Poincaré homology sphere, whose fundamental group has order \(120\).
