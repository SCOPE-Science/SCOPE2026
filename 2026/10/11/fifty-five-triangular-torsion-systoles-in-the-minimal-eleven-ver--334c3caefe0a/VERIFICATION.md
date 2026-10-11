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

`verify.py` is standalone and uses only Python's standard library.

It reconstructs all faces from the forty tetrahedra, verifies the four missing edges and the face vector \((11,51,80,40)\), and enumerates all \(135\) three-vertex cliques. Exact mod-two chain reduction gives triangle-boundary rank \(40\) inside a graph cycle space of dimension \(41\), and it checks all \(55\) nonfacial triangular cycles are nonzero.

For an independent integral check, the star at vertex \(1\) is used as a spanning tree. Projection to \(41\) cotree-edge coordinates identifies the integral graph cycle lattice with \(\mathbb Z^{41}\). A fixed set of \(41\) facial triangle boundaries has determinant \(2\), verified by fraction-free Bareiss elimination. Thus the full boundary lattice has index dividing \(2\); the nonzero mod-two quotient forces the index to equal \(2\).

Graph degrees split vertices as \(6+4+1\). The verifier exhausts all \(6!\,4!=17{,}280\) permutations preserving these degree blocks, retains exactly \(48\) simplicial automorphisms, and computes all five orbits on the \(55\) shortest carriers.

Exact successful output:

`VERIFY_OK f=11,51,80,40 missing_edges=4 H1_Z=Z/2 cliques3=135 facial3=80 essential3=55 aut=48 vertex_orbits=6,4,1 systole_orbits=3,4,12,12,24`

The verification is exhaustive for every finite set used in the claim.
