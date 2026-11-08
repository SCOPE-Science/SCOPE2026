---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

On R_{m,n}=K_m□K_n, the unweighted Laplacian eigenspaces have eigenvalues 0,m,n,m+n and the last space of row/column-sum-zero matrices has dimension q=(m−1)(n−1), forcing ≥q coordinate actuators by PBH. At q actuators the unactuated cell set has m+n−1 edges in bipartite K_{m,n}; PBH on the high eigenspace means its oriented incidence kernel is zero, equivalent to a spanning tree. If m≠n, any forbidden nonzero row/column mode would force two complete rows/columns in a tree and hence a 4-cycle, impossible. If m=n=s the merged middle eigenspace X_ij=x_i+y_j vanishing on actuator graph U is controlled by its connected-component row/column count matrix. Failure iff h≥3 or h=2 with both components balanced, and the extremal edge bound with |U|=(s−1)^2 exhausts just the double stars and cross-plus-one trees, counts s² and s²(s−1)²; all other trees pass. Matrix-tree gives m^{n−1}n^{m−1}. A separate forcing argument gives Z=q+1 (context). An independently written exact modular PBH/tree enumerator verified full cases 3×3,3×4,4×3. Finite checks supplement all-size proof.

## originality

PASS

Best-of-knowledge originality PASS for the precise stated claim, not a priority certificate. Equivalent formulations include controllability of a Laplacian with coordinate leaders, PBH injectivity on each Kronecker eigenspace, and annihilator-support avoidance by bipartite tree flows. The existing general PBH/critical-set principles lead to the new classification only after the explicit square merged-eigenspace component analysis. Yuan et al. 2013 prove maximum eigenvalue multiplicity lower bounds (recover q only); Chapman et al. 2012 Cartesian-network construction handles constrained product spectra and fixed input configurations, not an all-minimum-set enumeration under repeated eigenvalue s=m=n. Rahmani 2009 equitable partitions provide obstructions, not a complete tree-complement sufficiency rule. Principal residual risk: An older specialized classification in graph leader selection / critical-set tables could already give the two exceptions.

## value

PASS

The result completely enumerates every sharp minimum independent-coordinate actuator placement for a natural two-parameter graph family and isolates two unexpected balanced-spectrum obstruction families, with an explicit construction and a one-actuator gap to strong zero forcing. This is an exact structural classification of useful controllability designs, not merely PBH restated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
