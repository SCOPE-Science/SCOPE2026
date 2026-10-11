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

`verify.py` embeds the complete forty-eight-facet presentation and uses only the Python standard library.

It reconstructs the face vector \((12,60,120,120,48)\) and the six antipodal missing edges. It enumerates all three-vertex cliques, obtaining exactly \(40\) nonfacial triangles, and verifies that every one is nonzero in the one-dimensional mod-two first homology.

For the integral certificate, the script checks the displayed integer one-cocycle on all \(120\) facial triangles and obtains zero every time. It then evaluates the same cocycle on every increasing nonfacial triangle and obtains exactly \(+1\) in all \(40\) cases.

Finally, because every simplicial automorphism must preserve the missing-edge matching, the script exhausts all \(2^6\cdot6!\) pair-preserving vertex permutations, retains exactly \(24\) automorphisms, and recomputes the three carrier orbits.

Exact successful output:

`VERIFY_OK f=12,60,120,120,48 H1_F2_dim=1 empty3=40 all_empty3_nonzero=yes integral_pairings=+1:40 aut=24 carrier_orbits=4,12,24 reps=159|138|148 carrier_vertex_degree=10`

The only external mathematical input to the integral identification is the published topological type \(S^3\times S^1\), hence \(H_1\cong\mathbb Z\).
