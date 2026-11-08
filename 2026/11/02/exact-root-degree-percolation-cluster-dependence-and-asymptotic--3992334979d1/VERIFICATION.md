---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

From actual RESULT.md: increasing-tree root decomposition with F(x;u,z)=sum x^n E[u^R z^K]/n gives F_x=u(1-x)^(-z(1-p))(1-u+u(1-x)^p)^(-z). Direct parent/edge conditional expectations yield C_{n+1}=(1+p/n)C_n+p/n-p a_n/n^2; telescoping after dividing by a_n gives exact covariance and positivity for n>=3. L2-bounded R_n/a_n martingale and independent late root-attachment indicators after m_n=floor(exp(sqrt(log n))) establish joint Gaussian/Mittag-Leffler independence, not finite-n independence. Independently checked exact recurrence rationally for p=1/4,1/2,3/4 and n<=9 and checked actual verify.py code; bounded checks are corroborative only. Deterministic p=0,1 excluded from stated asymptotics.

## originality

PASS

The marked original root outdegree K_n and retained root cluster R_n joint generating function, covariance, and independent normalized joint limit are absent from the materially inspected 2023 marginal treatment; nearby published counts of fringe clusters or root degree versus leaves do not directly imply them. Qualified best-of-knowledge novelty, not priority certification.

## value

PASS

The exact finite dependence and simultaneous asymptotic independence are a meaningful structural distinction for a canonical growth/percolation model, rather than a routine scalar moment: the marked transform specifies every joint mixed moment and the covariance order differs from the normalized Gaussian limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
