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

For a>b>c>0, the restriction of Q=diag(a^-2,b^-2,c^-2) to u-perpendicular has positive eigenvalues and smooth perimeter P(sigma_1^-1/2,sigma_2^-1/2), with strictly negative spectral derivatives. The tangent derivative vanishes exactly when Qu is proportional to u, so the ONLY stationary normals are the six signed coordinate axes, with critical perimeters P(b,c)<P(a,c)<P(a,b). At ±e_b the exact Taylor Hessian is diag(-mu,nu), mu=a(a²-b²)P1(a,c)/b²>0 and nu=c(b²-c²)P2(a,c)/b²>0. A normalized spherical pushforward of t=(nu z²-mu x²)/2 has 2 log(1/|t|)/sqrt(mu nu) local delta coefficient; accounting for both antipodes and 1/(4pi) gives 1/(pi sqrt(mu nu)). At the two extrema the analogous positive/negative definite Hessians give the exact one-sided limits 1/sqrt(alpha1 alpha2), 1/sqrt(beta1 beta2). Smoothness/coarea elsewhere, nondegenerate Morse charts, compactness and monotone P prove no other singularities or atoms. Independently calculated axes (3,2,1): ell*=13.364893220555, mu=14.0532082185, nu=1.59174498432, log coefficient 0.0673016391598 and second finite-difference Hessians. Monte Carlo and the packaged numeric script do not establish the global analytic claim.

## originality

PASS

The substantive claim is NOT the general saddle-logarithm lemma or deterministic ellipsoid-section semiaxes. It is the exhaustive six-normal critical-value classification for the Euclidean perimeter, with an explicit two-sided density coefficient and both endpoint constants, for central sections and all strict triaxial axes. Full text of the 2014 offset-section filamentarity study was read; its random experiment and observables are not equal to this single scalar random perimeter. Best-of-knowledge PASS with older stereological-tabulation risk.

## value

PASS

The central-section perimeter is a natural stereological and geometric probability observable. The exact location and strength of its sole density blowup distinguish the middle semiaxis saddle from endpoint extrema, and provide sharp checkable parameters for identifying triaxial shapes from sampled sections. The explicit coefficient and endpoint laws require real geometry beyond generic Morse theory, and are useful even without the full smooth density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
