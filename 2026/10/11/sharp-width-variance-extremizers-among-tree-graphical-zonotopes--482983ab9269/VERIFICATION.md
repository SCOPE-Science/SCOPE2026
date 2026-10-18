---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For connected simple unweighted G on n≥3 vertices and d=n-1, the centered zonotope support sum gives W_G(U)=Σ_{e={i,j}}|U_i-U_j|. Gaussian polar decomposition g=RU in H has E R²=d and E|<e_i-e_j,U>|=sqrt(2)c_d. For distinct root vectors, normalized correlations are 0 (disjoint edges) or ±1/2 (incident edges). Independently applied exact bivariate normal kernel E|XY|=(2/π)(sqrt(1-ρ²)+ρ arcsinρ) to get off-diagonal spherical moments 4/(πd) and (2sqrt3/π+1/3)/d; expansion of W² yields (2m+8 binom(m,2)/π+2δq(G))/d with δ=1/3+(2sqrt3-4)/π>0. For trees, excess degrees a_v=deg(v)-1≥0 sum n-2; sum binom(a_v+1,2) uniquely minimized by all a_v in {0,1} (path), maximized by concentration (star); exact gap δ(n-2)(n-3)/(n-1) follows. Tree incidence maximal minors all ±1, hence Gram determinant n and Euclidean volume sqrt(n), and full-rank tree zonotope is a parallelotope/cube. Gamma-ratio expansion confirms path finite asymptotic 2+2δ-6/π and star variance/n→δ. These are analytic proofs, with finite Prüfer tests and Monte Carlo only diagnostic.

## originality

PASS

Best-of-knowledge PASS: classical Gaussian absolute moments and standard extremal degree sequences are acknowledged ingredients, but the natural graphical-zonotope directional-width variance formula and complete tree path/star extremizers are not shown as consequences of inspected graph zonotope face/volume papers. An unindexed generic zonoid-width correlation theorem remains a named possible partial antecedent.

## value

PASS

The second moment of width is a natural intrinsic stochastic geometric statistic. Among all n-vertex tree zonotopes, identical Euclidean volume, combinatorial cube structure, and mean width nevertheless conceal a sharp, strictly branch-sensitive variance, classified uniquely by paths and stars with explicit finite-n gap and scaling limits. That geometric distinction is a motivated exact result a zonotope or random geometry researcher could directly use, not an arbitrary graph slice or known face-count recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
