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

With y_i=x_i-xbar, A=sum W_i y_i and B=sum W_i y_i^2, the random centered weighted mean is A and the random weighted variance is B-A^2. Uniform Dirichlet monomial moments E(prod W_i^r_i)=prod(r_i!)/(N)_r give EAB=p3/[N(N+1)], EA^3=2p3/[N(N+1)(N+2)] and the required degree-four moments. Subtraction yields Cov(M,V)=N mu3/[(N+1)(N+2)] and Var(V)=N[((N+1)^2 mu4-(N^2-3)mu2^2)]/[(N+1)^2(N+2)(N+3)]. Checked center-translation invariance and the N=2/nonconstant or constant-data boundaries; claimed correlation only with nondegenerate denominators. Independent exact-fraction index-sum checks across 15 datasets N=2..6 support but do not replace general algebra.

## originality

PASS

Rubin 1981 defines Dirichlet Bayesian-bootstrap weights and illustrates the weighted mean; the inspected primary pages do not give the finite joint covariance and nonlinear weighted-variance uncertainty formula. Cheng 2014 treats asymptotic moment consistency for exchangeably weighted estimators, not these conditional fixed-data closed forms. A short derivation from standard Dirichlet moments remains plausible prior implicit coverage, recorded as a risk, but no searched directly equivalent statement was found.

## value

PASS

Weighted mean and weighted variance are jointly reported natural posterior functionals; the finite conditional joint covariance tells whether their uncertainty is positively or negatively coupled, with sign determined exactly by empirical skewness, and the fourth-moment variance formula permits joint uncertainty calculations without repeated Monte Carlo. It is more than a parameter renaming or a preexisting table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
