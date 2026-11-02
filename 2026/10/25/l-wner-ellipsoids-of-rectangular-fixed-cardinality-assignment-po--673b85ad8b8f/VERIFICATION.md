---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For 2<=m<=n,1<=k<=m, the complete-bipartite k-matching vertex orbit has center k/(mn)11^T. Frobenius-orthogonal modes R=F_m YH_n, Q=H_m YF_n, I=F_m YF_n have covariance eigenvalues lambda_R=k(m-k)/(mn(m-1)), lambda_Q=k(n-k)/(mn(n-1)), lambda_I=k((m-1)(n-1)+k-1)/(mn(m-1)(n-1)). The positive eigenspace range equals the true affine hull, with dimensions mn-1, m(n-1), (n-1)^2 in the three boundary regimes. Each vertex has deterministic projected squared energy r_T lambda_T, so is on the ellipsoid of squared semiaxes d lambda_T. For arbitrary enclosing ellipsoid center c and shape A, averaged containment gives tr(A^-1 Sigma)+(C-c)^T A^-1(C-c)<=1, and matrix AM-GM yields det A>=d^d det Sigma, with equality only at c=C and A=d Sigma: uniqueness global, not just symmetric ansatz. Comparing modes gives squared-axis anisotropy [((m-1)(n-1)+k-1)/((n-1)(m-k))] for k<m, n/(n-m) at k=m<n, 1 at m=n=k. All last-step increase/decrease/equality integer cases follow by direct inequalities. Independently checked exact rational energies and anisotropy for 2<=m<=4, m<=n<=5, all allowed k; those finite checks do not replace the universal determinant proof.

## originality

PASS

The general uniform-vertex covariance to Löwner ellipsoid principle is a classical orbit-transitive optimization argument, explicitly not novel. Gill–Linusson's exact same k-assignment polytope covers facets and combinatorics; Torres extends normality/H-description. Published SCOPE same-object work gives inscribed John ellipsoid and inscribed balls (different optimization), and partial permutohedron Löwner work concerns different polytopes. Neither an inscribed John shape nor an outer circumsphere determines the entire intrinsic Frobenius covariance spectrum, determinant, or changing-rank saturation reversal. Qualified PASS for rectangular three-mode formulas and complete sharp transition classification, with matrix-design literature priority risk.

## value

PASS

The fixed-cardinality matching polytope is a natural combinatorial convex body. The explicit intrinsic ellipsoid, all-vertex contact, and nonmonotonic anisotropy at saturation give a meaningful geometric phase change and exact benchmark across rectangular aspect ratios and dimension drops, not a cosmetic reformulation of the standard covariance principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
