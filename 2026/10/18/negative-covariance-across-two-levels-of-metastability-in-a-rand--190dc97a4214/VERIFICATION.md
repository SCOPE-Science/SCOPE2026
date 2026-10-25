---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

A block flip changes energy only on two boundary bonds. A wall must be a radius-k strict minimum of iid bond strengths, and all such minima are separated; even wall subsets give exactly 2^(M_k) stable configurations, accounting for ring spin parity and global spin reversal. For k=1,2, local overlap integrals under the probability-integral transform give p11(2)=2/15,p12(2)=1/18,p12(3)=8/105,p22(3)=1/20,p22(4)=2/45. Independently recomputed exact SymPy integrals produce those values, and cyclic displacement sums for n>=11 yield Var(M1)/n=2/45, Cov(M1,M2)/n=-1/315, Var(M2)/n=13/450. The bounded 4-dependent vector indicator process and Cramer–Wold give the joint Gaussian limit, with cyclic cut changes O(1) only. The finite-n restriction avoids cyclic window collision. These analytical steps, not saved verifier logs, support all n>=11.

## originality

PASS

Newman–Stein develop metastable-state structure and known one-spin typical scale; Masui-Southern-Jacobs examine one-spin finite-chain distributions. Their available results do not imply the joint disorder covariance across one- and two-spin stability levels, which can be negative despite S2<=S1. The inaccessible 1989 full text remains a named priority risk, not automatic rejection.

## value

PASS

The exact negative cross-covariance is a counterintuitive fluctuation effect across nested physically meaningful metastability notions; the universal rational covariance matrix and joint CLT permit quantitative comparisons rather than mere marginal state-count asymptotics. Natural object and invariant, not a manufactured statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
