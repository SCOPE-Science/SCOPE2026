---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For connected allocations, Kirchhoff index N tr((L+11^T/N)^{-1})-N is strictly convex in individual edge conductances; symmetry plus uniqueness forces two edge-orbit weights per blade. Grounded blade Laplacian eigenvalues x and x+my give K=sum_j((N-m_j)/x_j+N(m_j-1)/(x_j+m_j*y_j)). Fixing blade spend E gives f_j(t)=[a_j+b_j(t-1)](A_j+C_j/t), t>=1, f_j prime=b_j*A_j-(a_j-b_j)*C_j/t^2; the support change is exactly Q_j/P_j=2N/M, including equality. Cauchy-Schwarz allocates E_j in sqrt(F_j) proportions and K*=Z^2/B, globally uniquely. Independent direct rational inversion of complete grounded Laplacian for blade sizes (2,3), spoke weights (3/2,7/3), peripheral weights (1/4,0) gave K=254/21, exactly the closed expression.

## originality

PASS

General inverse-resistance convex design and block Kirchhoff identities are prior results, as is the equal-price windmill/triangle special case. The assessed new part is an exact heterogeneous mixed-support allocation with independently chosen blade edge activation and coupled closed budget shares; general KKT marginal-price conditions do not state or directly specialize to this solution. Full-text comparison of an adjacent windmill-index paper remains outstanding.

## value

PASS

Sum of all-pairs resistance under a construction budget is a standard network-design objective; here a sharp price ratio decides whether to install entire internal-edge orbits and exact investment proportions solve a nontrivial all-edges problem. Heterogeneous mixed support is mathematically motivated and not merely a uniform-graph recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
