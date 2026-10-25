---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The source treats real nonnegative p×q arrays (p,q>=2) of total mass 1 satisfying the adjacent Monge (submodular) inequality, explicitly excluding transportation polytopes and inverse Monge. For p<=q, source vertex/facet classification (Erickson–Kretschmann Proposition 5.1, Theorem 5.3) gives all coordinate and adjacent-cut facets; corner-rectangle normalized vertices maximize each cut slack at 1/w_ij with w_ij=min(i(q-j),(p-i)j). The proposed unnormalized Y=J/p+sum_{cuts}V_ij has total mass T=q+(p-1)(q-1)=p(q-1)+1 and exactly max cut slack at each cut. For a coordinate requiring a larger bound than 1/p, the rectangle at a corresponding cut appears with appropriate full or half coefficient; the tie argument uses r(p-r)>=p-1 and area >=p/2 to show J/p plus the half term suffices. Thus Y/T meets each primal facet reflection bound with h=T-1. Dual grid coefficients lambda_rs=1+w_rs-w_r,s-1-w_r-1,s+w_r-1,s-1 are >=0, because w_ij=i(q-j)-(iq-pj)_+ and the rectangular mixed second difference of the positive part is nonpositive. The exact mass decomposition ΣZ=Σlambda Z+Σ w_ij h_ij(Z) makes any center satisfy h+1>=q+(p-1)(q-1); transpose yields s=min(p,q)(max(p,q)-1). Independently reconstructed exact-rational primal center values, all coordinates and cut slacks, and dual positivity for all p=2..5 and p<=q<=6, beyond merely trusting the supplied verifier. This finite test is supplementary, not an infinite proof.

## originality

PASS

Two highly relevant papers on the identical normalized Monge polytope were compared at the level of their theorems. The earlier supplies the complete extremal geometry, while the later computes volume/Ehrhart. Neither examined statement gives a Minkowski asymmetry formula, matching optimal center and dual certificate. General symmetry results for other 0/1 or transportation polytopes are not automatically applicable to Monge inequalities and different mass constraints. This is qualified by a possible earlier submodular-grid dual formula.

## value

PASS

The normalized Monge cost-matrix polytope is a mathematically natural convex body arising from transportation/assignment inequalities; its exact Minkowski asymmetry is a separate affine invariant from its already-studied volume and face lattice. The result solves an unrestricted two-integer-parameter classification, supplies an explicit optimal center and a nonnegative dual mass-slack identity, and quantifies the exact defect from the simplex bound. The cut-area formulas and tied-cut constraints give substantive geometric content beyond a routine determinant computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
