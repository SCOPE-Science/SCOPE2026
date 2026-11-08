---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For uniform-parent rooted recursive trees let F_(n,r)=∑_v binom(L_v,r) for the number L_v of terminal children. Conditioned on the tree, increment drift is [F_(n,r-1)-r F_(n,r)]/n (F_0=n), because adding the new leaf increases its chosen parent's binomial count while a previously terminal chosen parent ceases to be a terminal child. This gives E F_(n,r)=n/(r+1)! for n≥r+1. For X=F_1, Y=F_2, Z=F_3, exact conditional increments are E∆X=1-X/n, E∆Y=(X-2Y)/n, E(∆X∆Y)=X/n, E(∆Y)^2=(X+4Y+6Z)/n. Product recurrence and true small n initial conditions give E X=n/2, E Y=n/6, E X²=n²/4+n/12, E XY=n²/12+n/8, E Y²=n²/36+59n/180. Thus for n≥5 Cov=n[[1/12,1/8],[1/8,59/180]], determinant 101n²/8640 and correlation 3sqrt(15)/(2sqrt59). Independently enumerated complete labeled parent-choice sets n≤8 and checked moments; induction proves general n. Rooted terminal children differ from unrooted graph-degree-one leaves.

## originality

PASS

Qualified PASS: Hartle–Krapivsky 2025 studies marginal degree-one leaf-neighbor distributions (unrooted) and fluctuations, while present full cross-covariance of rooted terminal-leaf count with unordered sibling pairs needs overlapping local descendant dependencies. Earlier recursive-tree fringe-motif covariance theory could potentially subsume when represented as an additive pattern mixture but no same statement or direct theorem implication was identified; any existing mean hierarchy is credited.

## value

PASS

Closed exact joint second-order law for two dependent classical growth-tree statistics, including nontrivial overlap corrections and all-n positive definite correlation; directly informs asymptotic fluctuations and local clustering without assuming independent leaf pairs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
