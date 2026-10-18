---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For U=X_i/sigma,V=X_(i+1)/sigma and L=S_n/sigma, the Gaussian exponential-tilt identity gives Cov(1_{UV<0},L^2)=[rho(a^2+b^2)-2ab]/(pi sqrt(1-rho^2)), with a,b the covariance row sums. Summing yields F_n=Sum_{i=1}^{n-1}[rho(b_i^2+b_(i+1)^2)-2b_i b_(i+1)] and the exact closed polynomial-rational expression using t=rho^n. Independent rational arithmetic matched the two expressions for n=2..15 and five rho values. Uniform regimes are stated for FIXED c>0: rho=-1+c/sqrt(n) gives 1/2-c^2; even n at -1+c/n^2 gives n^3 F -> c^2(c-12)/6; odd n gives n F ->2c. The even c=5,c=20 small layer and c=1 square-root layer prove negative-positive-negative and at least two distinct roots for large even n. No exact number of zeros or critical c behavior claimed.

## originality

PASS

The primary Kratz survey covers general Gaussian level-crossing moment theory and chaos expansions, while Sinn–Keller focuses on covariances among zero-crossing indicators or counts at lags. Neither accessible statement directly provides this mixed Cov(sign-crossing count, square of the GLOBAL sum) or the separate n^{-1/2} and n^{-2} negative-unit-root boundary layers with parity and two sign reversals. Full Sinn–Keller text was inaccessible, so this is best-of-knowledge with genuine priority risk, not a whole-text NOT_COVERING conclusion.

## value

PASS

The covariance between sign changes and a global quadratic statistic is a natural dependence diagnostic for finite Gaussian time series near a negative unit root. Its endpoint behavior is qualitatively nonuniform: odd/even parity and two n-dependent scales give nonmonotonic sign changes and at least two roots in the even case. These exact structural boundary facts go beyond a routine closed covariance formula or arbitrary finite parameter scan and could inform asymptotic statistical analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
