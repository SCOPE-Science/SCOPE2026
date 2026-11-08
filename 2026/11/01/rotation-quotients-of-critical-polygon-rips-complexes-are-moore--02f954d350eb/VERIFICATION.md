---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. Checked exhaustive clique-type dichotomy: a cyclic-distance-k clique either sits in an interval of length k or equals one of k equilateral triangles {j,j+k,j+2k}. For arc complex A_d the new faces are uniquely indexed by their length-d endpoint edge; cone matching on interior vertex i+1 pairs every such face, has no cyclic-orbit stabilizer (n=3k>=3d), and descends as a free equivariant collapse A_k/C_n to A_1/C_n ≃ S¹. The k exceptional triangles form one rotation orbit, each with order-three stabilizer acting geometrically by an orientation-preserving triangle rotation, so contributes one disk with rim boundary 3-to-1 relative to original triangle. The original equilateral boundary traverses the full n-edge cycle once via interval faces; after the degree-n rim covering, attaching degree is n/3=k. Thus a CW circle with one 2-cell attached by k has π1 and H1=Z/k and no higher reduced homology. Independent barycentric face-flag orbit chain complexes for k=2,3 and characteristics 2,3,5 reproduce predicted Betti patterns; finite checks only test, do not replace, the all-k equivariant collapse.

## originality

PASS

PASS best knowledge. Adamaszek Corollary 6.7 computes the unquotiented Cl(C_{3k}^k) ≃ wedge^{k−1}S², not its geometric rotation orbit. Other circle Rips classifications and metric quotient comparison theorems address different invariants/scales; metric vertex orbit is one point and cannot imply this Moore-space topology. No equal/dominating ordinary-rotation-orbit theorem was retrieved from indexed literature. Unindexed treatments remain risk.

## value

PASS

PASS. Distinguishing the true geometric orbit from the Rips complex of an orbit metric yields a uniform sharp topological phenomenon: full cyclic symmetry creates arbitrarily large integral H1 torsion and nontrivial fundamental groups from previously known simply-connected sphere wedges. This is a natural critical family with an explicit CW attachment, not an arbitrary finite homology computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
