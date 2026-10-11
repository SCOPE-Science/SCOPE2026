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

The packaged `verify.py` reconstructs the ten-vertex complex from the five published facet representatives and two published permutations. It checks the face vector, chain-complex identities, a unimodular rank certificate for each critical boundary map, the integral cocycle used to normalize the generator of \(H_2\), every four-vertex support, all \(35\) missing tetrahedra, and the complete \(A_4\)-orbit decomposition.

The rank argument is exact: the \(36\)-minor of \(\partial_2\) has determinant \(1\), while \(\partial_1\partial_2=0\) and the complete one-skeleton gives the matching upper bound. The \(73\)-minor of \(\partial_3\) has determinant \(-1\); the explicit cocycle evaluates to \(1\) on a \(2\)-cycle outside \(\operatorname{im}\partial_3\), giving the matching upper bound. The unimodular \(\partial_3\) minor makes its image primitive in \(C_2\), so the resulting rank-one \(H_2\) is torsion-free.

The four-vertex support argument is also exhaustive. On fewer than four vertices there is no nonzero simplicial \(2\)-cycle. On four vertices, a nonzero cycle exists only when all four triangles are present and is then the tetrahedral boundary; it is null-homologous exactly when the tetrahedron is a face. The verifier directly checks these conditions for every four-set.

Expected terminal line:

`VERIFY_OK f=10,45,110,120,48 H2=Z missing_tetrahedra=35 primitive=34 double=1 diagonal=x11-x22-x33-x44 orbits=1,4,6,12,12 primitive_orbits=4,6,12,12`

Limit: the checker proves only the stated finite theorem for this exact complex; it does not enumerate cycles with support larger than four.
