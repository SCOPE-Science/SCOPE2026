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

PASS: IID scaled exponential spacings yield Dirichlet(1,...,1) shares Z_j. Express G_n=Σ((j-1)/n) Z_j and the top-k share as Σmin(1,k/(n-j+1)) Z_j. Dirichlet covariance gives k[(n+1)(H_n-H_k)-(n-k)]/[2n²(n+1)]; positivity follows strict rearrangement for k<n. Subtraction yields Δ=(n+1)(H_n-H_k)-2(n-k), single sign switch by Δ(k+1)-Δ(k)=2-(n+1)/(k+1), with equality producing exactly a two-way tie. Harmonic asymptotics locate alpha*= -W0(-2e^-2)/2 and limit alpha*(1-alpha*)/2. Rates and all n≥2 boundary conditions consistent.

## originality

PASS

PASS best of knowledge: published exponential Gini and sample-Lorenz tests, population Lorenz curves, and Dirichlet spacing laws are credited. The inspected primary bibliographic and accessible material did not provide the all-(n,k) mixed covariance, its exact maximizing upper rank, or Lambert-W limit. The classical Dirichlet trick supplies premises but leaves explicit mixed covariances and maximizer proof. Full historic tests remain an indirect-coverage risk.

## value

PASS

PASS: Finite-sample dependence of an income-inequality index on the largest k exponential incomes is a natural statistical question. Exact all-rank covariance and sharp optimal share fraction about 0.203 provide useful nontrivial quantification beyond mean Gini or deterministic sample Lorenz identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
