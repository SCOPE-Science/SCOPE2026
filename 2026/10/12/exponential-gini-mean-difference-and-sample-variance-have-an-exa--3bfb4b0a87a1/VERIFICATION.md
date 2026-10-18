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

For iid Exp(lambda), n>=2, G_n and unbiased S_n^2 are normalized degree-two U-statistics with kernels h(x,y)=|x-y| and q=(x-y)^2/2. From index-overlap counts Cov= [2 c2 + 4(n-2)c1]/[n(n-1)]. Standard exp |X-Y|~Exp(1); same-pair c2=2. Independent SymPy integrations confirm conditional kernels a(x)=x-1+2e^-x and b(x)=x²/2-x+1 satisfy Ea=Eb=1, Eab=7/4 so c1=3/4, Var(a)=1/3, Var(b)=2. Same-pair kernel variances 1 and 5 yield exact Cov=(3n-2)/[n(n-1)lambda^3], Var(G)=2(2n-1)/[3n(n-1)lambda²], Var(S²)=2(4n-3)/[n(n-1)lambda^4]. Divide to obtain rho=sqrt(3)(3n-2)/(2sqrt((2n-1)(4n-3))), increasing because independent SymPy factorization rho²(n+1)-rho²(n)=3(6n²-4n-1)/[4(2n-1)(2n+1)(4n-3)(4n+1)]>0; limit 3sqrt6/8. Only unnormalized pairwise Gini mean difference, not mean-normalized Gini coefficient; ordinary iid sample, no general-law universality.

## originality

PASS

Čiginas–Pumputis 2014 full open HTML develops Gini mean difference and empirical variance as separate U-statistics and variance decompositions; inspecting relevant definitions, covariance notation and proof context did not show exponential SAME-SAMPLE cross-covariance or closed rho(n). Hoeffding overlap counting is classical and explicitly credited; evaluating mixed conditional projection 3/4 and exact exponential law is new claimed special-case invariant. Resultary hit nearby exponential sample range–variance harmonic covariance (different first statistic), not this Gini-versus-variance pair. Older specialised Gini/exponential-statistics sources may already contain cross-moment, residual risk.

## value

PASS

Gini mean difference and sample variance are natural robust/order and quadratic scale statistics; their exact finite-sample correlation under a canonical skew exponential model quantitatively answers whether those competing estimators become redundant. Strict growth and nonunit asymptotic limit are precise reusable statistical comparisons beyond univariate marginal variances. Standard U-statistic overlap formula alone does not determine distribution-specific cross-projection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
