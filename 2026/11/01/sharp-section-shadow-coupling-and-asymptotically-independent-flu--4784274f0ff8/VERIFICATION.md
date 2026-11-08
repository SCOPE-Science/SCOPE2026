---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The canonical regular simplex has facet volume sqrt(N-1)/(N-2)! and normal projections sqrt(N/(N-1)) U_i. Cauchy brightness formula gives Y=sqrt(N/(N-1)) sum |U_i|, while crossed edges give section vertices C=p(N-p). Equal positive/negative absolute masses a and unit norm imply 1/2<a²<=pq/N for generic N>=3 (upper equality for two-level sign classes), hence the entire half-open Y interval; connectedness of each sign chamber fills every intermediate value. The exact finite E[Y] and E[Y²] use spherical absolute-coordinate and correlated Gaussian pair moments. Represent U by centered iid Gaussians divided by their Euclidean norm. The sign-count influence psi=1_(G>0)-1/2-phi(0)G is odd and has variance s²; the brightness influence eta=|G|-sqrt(2/pi)-(sqrt(2/pi)/2)(G²-1) is even and has variance tau²=1-3/pi. Empirical moving-threshold/grid remainder and normalization errors are o_p(1), so iid bivariate CLT yields independent Gaussian limits, squaring sign count gives independent chi-square vertex deficit. Every all-N assertion is analytic, not extrapolated from finite simulations.

## originality

PASS

Best-of-knowledge comparison of exact conclusions and logical implications, not titles or equal parameter words. The section face-vector distribution, Cauchy brightness functional and Gaussian geometry were separately known, but neither prior RESULT.md gives their complete simultaneous feasible interval and independent joint weak limit under a single normal. A general Cauchy projection formula is sufficient to define Y but it does not give the sharp sign-split range or joint Gaussian-sign influence covariance. Known one-dimensional widths and section volumes are not a theorem about the same-direction codimension-one shadow with section vertices. Residual source-access risks and credited antecedents are explicit.

## value

PASS

A single hyperplane produces two intrinsic observables: discrete section complexity and continuous orthogonal shadow volume. The exact feasible joint domain and equality directions answer a natural inverse-geometric compatibility question, and the independent Gaussian/chi-square limit explains why a strong deterministic finite-N coupling disappears at fluctuation scales. These are genuinely additional joint facts beyond previously published section-only face counts and projection-only widths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
