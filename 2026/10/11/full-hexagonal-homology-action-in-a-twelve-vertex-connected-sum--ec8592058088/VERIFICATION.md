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

`verify.py` contains the complete fifty-four-facet presentation and uses only the Python standard library.

It reconstructs the face vector, then collapses a star spanning tree at vertex \(1\) to obtain a \(55\)-coordinate integral graph-cycle lattice. Two explicit integral cocycles are checked against every facial triangle boundary. A fixed \(53\)-by-\(53\) relation minor is recomputed by Bareiss elimination and has determinant \(1\), proving a primitive rank-\(53\) boundary lattice and hence \(H_1\cong\mathbb Z^2\).

The verifier next enumerates the full simplicial automorphism group by backtracking over vertex permutations with triangle and tetrahedron status pruning. Exactly \(24\) automorphisms survive. Their induced actions on two certified homology basis cycles give twelve distinct integral matrices, each with multiplicity two.

The quadratic identity for \(q(x,y)=x^2+xy+y^2\) is checked coefficientwise for every action matrix. The full integral isometry group of \(q\) is independently exhausted: a norm-one column must have coordinates in \(\{-1,0,1\}\), leaving a finite search whose twelve isometries coincide exactly with the homology image. Reduction modulo \(2\) is then compared with all of \(GL(2,\mathbf F_2)\).

Exact successful output:

`VERIFY_OK f=12,66,108,54 aut=24 H1_Z=Z^2 boundary_minor_det=1 H1_image=O(x^2+xy+y^2,Z):12 action_multiplicity=2 kernel_Z=2 mod2_image=GL(2,2):6 kernel_F2=4`

The computation is exhaustive for every finite domain used in the claim.
