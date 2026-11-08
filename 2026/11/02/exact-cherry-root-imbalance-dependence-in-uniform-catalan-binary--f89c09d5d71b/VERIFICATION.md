---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n≥2 the uniform rooted ordered full binary tree root split has P(K=i)=C_i C_(n−1−i)/C_n. Cherry enumerator A(z)=z/sqrt(1−4z), Catalan F=1+zF². Extracting coefficients of (zF′)² and 2(zA′)(zF′), including n=2, yields Cov(X,B)=(n−2)4^(n−1)/[4(2n−1)C_n]; Q=(n−1)²−4B gives Cov(X,Q)=−(n−2)4^(n−1)/[(2n−1)C_n]. Bivariate cherry GF G=1+z(G²−1+u) gives Var(X)=n(n−2)(n−1)(n+1)/[2(2n−3)(2n−1)²] and Catalan split bulk asymptotics with endpoint truncation give Var(B)~sqrt(pi)n^(7/2)/32; combining gives Corr(X,Q)~−pi^(1/4)/sqrt(2)n^(−3/4) only for n≥3. Independently exhaustively enumerated plane full binary trees n=2..9, checking X,B,Q moments with exact rational arithmetic; no claim enumeration proves the all-n theorem.

## originality

PASS

Best-of-knowledge original exact mixed root-split/cherry covariance and asymptotic correlation for the uniform plane Catalan law, though the Catalan recurrence and marginal cherry statistics are well known.

## value

PASS

Cherries measure local branching, whereas squared root imbalance measures global top split. An exact sign for all n≥3 together with a decaying normalized correlation quantifies dependence of two standard tree-shape observables and gives the full conditional split regression; this is more than a textbook marginal count or arbitrary tiny case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
