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

`verify.py` reconstructs the triangulation solely from the six published facet-orbit representatives and the affine action \(x\mapsto ax+b\) on \(\mathbf F_{13}\), with \(a\in\{1,3,9\}\). It checks the six orbit sizes, disjointness, the complete face vector, and the two-facet incidence of every ridge.

For each of the 533 tetrahedra, it constructs the complete link and verifies that the link graph is a connected two-regular cycle. It then checks the exact link-length distribution, all three affine orbits of short-link tetrahedra, the representative link triangles, and the \(2\text{-}(13,4,1)\) pair-incidence condition of the 13-block orbit.

For each bistellar index \(i\in\{1,2,3,4,5\}\), the script exhausts every \(5-i\)-simplex \(A\), computes its full link, and tests the exact condition \(\operatorname{lk}_K(A)=\partial B\) for an absent \(i\)-simplex \(B\). Each index has zero legal centers. Index zero is intentionally excluded because it is the facet subdivision that introduces a new vertex.

The verified terminal record is:

`VERIFY_OK f=13,78,286,533,468,156 facet_orbits=39,39,39,13,13,13 tet_link_spectrum=3:91,4:195,5:195,6:52 short_orbits=13,39,39 pg23_blocks=13 pair_lambda=1 short_reps=1-2-3-10|1-2-4-8|1-2-5-7 short_links=5-6-8|3-5-13|9-12-13 positive_bistellar_moves=1:0,2:0,3:0,4:0,5:0`

The computation proves only the finite statements encoded above. No unbounded search, global uniqueness claim, or statement about sequences beginning with vertex addition is inferred from these checks.
