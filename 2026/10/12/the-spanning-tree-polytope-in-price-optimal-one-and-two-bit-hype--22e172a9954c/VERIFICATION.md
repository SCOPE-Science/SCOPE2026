---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Every nonconstant Walsh character has squared norm N on the vertex space; each sign-crossing undirected edge contributes 4w to its energy. Parity and the mean singleton quotient give the two unrestricted upper bounds 4W1/N and 4(W1+2W2)/(dN). For t<2 their crossing is the unique maximum of their minimum under W1+tW2=1, giving the asserted totals and value; for t≥2 the mean singleton bound is at most 4/(dN), strictly smaller if t>2 and W2>0. Uniform conductance c=4/[Nd(2+(d−1)t)] on both shells attains the lower-price bound because the Walsh eigenvalue of weight k is 2c k(d−k+1)≥2cd; uniform ordinary cube edges attain the high-price bound. Above t=2 equality forces every singleton to be a minimum eigenvector on the mean-zero space, giving 2 w_{x,x+e_i}=Γ at each vertex and hence edgewise uniqueness. In the invariant subclass, Walsh eigenvalues are twice the cut weights of the coordinate graph with auxiliary vertex 0, edge weights w_0i=b_i and w_ij=a_ij. Equality at singleton cuts yields b_i+Σ_j a_ij=q=Γ/2; eliminating b_i makes λ_S=2q(|S|−Σ_{ij⊂S}z_ij) for z_ij=2a_ij/q. Thus cut lower bounds give exactly the subset forest inequalities, and b_i≥0 gives degree bounds. These induced-subset inequalities also give the graphic-matroid rank inequalities for any edge subset by summing over its connected components. Parity equality fixes total z=d−1 below the threshold, giving budget Nq[2+(d−1)t]/4=1; at t=2 the budget is automatic from singleton equalities and total z need only be ≤d−1. A path on [d] gives a cycle on the augmented graph via its two endpoint edges to 0; all its d+1 classes are positive and attain the gap. Independent python3 /workspace/reproductions/2.py verifies 72 exact cut spectra and budgets, including a fractional slack forest at t=2 and prices on both sides. This tests designs and boundaries, not arbitrary-parameter optimality or a classification of nonsymmetric optimizers at t≤2.

## originality

PASS

The supported distinct claim is the solved price-dependent two-shell continuous-time problem and the tree/forest equality family, not the general FMMP optimization framework or the fixed unweighted square-cube spectrum. Closest indexed statements are distinguished by traceable objective, support, and optimizer comparisons. Historical risk remains for uninspected spectral/majorization work.

## value

PASS

A single threshold settles when distance-two links help across an arbitrary-dimensional natural design family. The explicit tree/forest face gives more than the optimum value: it explains and certifies very sparse and fully dense exact solutions within the same price-normalized class. Above the threshold edgewise rigidity holds without a symmetry assumption. These distinctions are usable for design and are not just a change of parameters in the general SDP.

The dated certificate retains the supplied scientific assessment, sources and limitations.
