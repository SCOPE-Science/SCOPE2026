---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

With n≥2 iid Uniform[0,1] and S²=(ΣX_i²−(ΣX_i)²/n)/(n−1), conditioning on X_(k)=x splits other observations into independent k−1 Uniform[0,x] and n−k Uniform[x,1] groups. The resulting conditional E[S²|x] is quadratic; integrating x times that polynomial against Beta(k,n+1−k) moments yields Cov(X_(k),S²)=k(n+1−k)(2k−n−1)/[6n(n−1)(n+1)(n+3)]. Independent SymPy symbolic reduction of those conditional moments gave exact zero difference for symbolic n,k. Uniform Var(S²)=(2n+3)/[360n(n−1)] and Beta order variance give the stated correlation; the squared bulk limit is (5/4)z²(1−z²) with z=2u−1 and maximum 5/16. Symmetry and the median-zero boundary follow directly. For Uniform[a,b], covariance scales (b−a)^3, correlation invariant. Source exact-rational checker was inspected; finite n≤1000 tests do not prove the universal identity.

## originality

PASS

The precise same-sample rank-by-rank mixed covariance/correlation curve, exact median sign law and sharp bulk-correlation peak are distinguished from classical single/product order-statistic moments and bounds on expected ranges. Bekçi has directly relevant moment recurrences, but its full text was inaccessible; an equivalent formula could be derivable and remains a named residual risk, not automatic scientific failure.

## value

PASS

Exact dependence between an individual sample quantile and the same-sample dispersion estimate, including sign transition and nontrivial bulk correlation maximum, is an interpretable finite-sample statistical invariant. It could be used in joint quantile-variance inference; not just a beta marginal identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
