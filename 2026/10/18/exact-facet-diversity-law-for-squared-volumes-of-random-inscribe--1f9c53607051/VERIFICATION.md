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

Barycentric point on facet i has E[r_j r_k]=(1+1_{j=k})/[d(d+1)] for j,k!=i and zero otherwise (Dirichlet(1,..,1)). For m=d+1, c=1/[dm], B=sum_i t_i A_i/c=T(I+11^T)-t1^T-1t^T. It acts as T on the common orthogonal complement of 1,t, and direct rank-two determinant gives det(sum t_i A_i)=c^m m T^(m-2)(T²-sum t_i²). The squarefree coefficient [prod t_i] is E(det R_strat)^2=C_d=m!/[m^(m-1)d^m]. For iid mixture A_pi, E det(R)^2=m! det(A_pi)=C_d(1-sum pi_i²). Cauchy-Schwarz yields unique uniform pi maximizer. Independent direct two-permutation rational second-moment checks: 12 cases, d=2,3,4 stratified + iid, including degenerate pi. Finite checks corroborate analytic rank-two proof.

## originality

PASS

Best-of-knowledge: targeted published finding search and primary-source theorem comparison did not identify a prior result implying the entire final claim; known components are explicitly credited, not counted as novel. Sharp shape-independent second moments for a natural one-point-per-facet stratification and an independently labelled iid facet-mixture, with optimal facet-diversity comparison in every dimension. Unindexed-equivalent risk retained.

## value

PASS

One independent point from EACH facet is a natural sampling design distinct from iid boundary mixtures. Exact second moments and a strict sharp design advantage are nontrivial, shape-invariant benchmarks for high-dimensional inscribed simplex sampling; the iid covariance identity is classical and is not claimed itself to be new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
