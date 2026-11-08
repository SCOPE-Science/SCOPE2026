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

At rank-one sketches, RCGLS Algorithm 1 sets p_k proportional to the previous H-orthogonal projection of g_k. Exact line search makes e_k H-orthogonal to p_(k-1), so the scalar g_k^T H e_k cancels and each step removes the H-orthogonal component along w_k=P_(k-1)g_k. For d>=3, conditional w_k has full Gaussian density on a (d-1)-plane, and aligning with a fixed nonzero e_k is measure-zero; first step similarly nonterminating for d>=2. d=2 hyperplane dimension one forces termination at second step. With H=I, conditional normalized w_k is uniform on an m-sphere in dimension m=d initially, d-1 thereafter: exact squared surviving factor Beta((m-1)/2,1/2), independent of history and hence independent across k. Beta expectations and log-moment strong law yield stated mean and negative digamma exponent. Independent Gaussian simulations for d=3,4,7 with 20,000 paths showed first/second/third mean factors [0.663462,0.501726,0.499113], [0.747321,0.665344,0.667037], [0.857792,0.832789,0.834012], close to exact predictions. Infinite zero-termination and independence rely on the conditional measure proof, not simulation.

## originality

PASS

Zeng–Cai–Han–Xie (arXiv:2605.25034v1) Algorithm 1 exactly defines RCGLS and Theorem 2.4 establishes expected convergence inequality, not the exact product law. Sun–Han–Xie (arXiv:2505.20602v1) give a related projected-memory solver and full-memory finite termination at rank r (Remark 3.6); the d=2 finite-memory consequence is prior knowledge, not newly claimed. The surviving novel statement is the d>=3 almost-sure nontermination and the full independent beta-factor distribution plus exact exponential rate. No directly implying distribution theorem identified in topical searches, but unindexed randomized-projection analyses remain a risk.

## value

PASS

A full exact distribution and almost-sure rate for a contemporary randomized least-squares solver quantify reliability beyond expectation bounds. The sharp finite-termination dichotomy by dimension identifies a genuine algorithmic limit of one-direction memory, not a routine numerical inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
