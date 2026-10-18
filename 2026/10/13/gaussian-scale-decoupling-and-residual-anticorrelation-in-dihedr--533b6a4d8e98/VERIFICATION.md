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

Represent a/b as Y=+/-1. The global-memory drift is E[Y_{n+1}|F_n]=qW_n/n, so W_n/A_n is L2-bounded for q>1/2, giving W_n/n^q->L_q. The alternating predictor Z_n converges in L2 and almost surely for q<1 by pairing a summable martingale transform and k^{q-2} drift. S_n-Z_n is a bounded-increment martingale with quadratic variation n-o(n). Conditional martingale FCLT for every finite prefix, followed by L1 approximation of bounded full-history observables, gives the mixing Brownian limit independent of both limiting memory variables. The cross-covariance reduces to a convergent alternating sum with b_k=E[W_k^2]/(k A_k), b1=b2, b_{k+1}<b_k for k>=2; consequently Cov(L_q,Z_inf)<0. The exact recurrence and sign monotonicity were independently checked with rational q=3/5,2/3,4/5,9/10 over 50 terms. The infinite sign follows from the proved recurrence, not the finite partial sums.

## originality

PASS

Best-of-knowledge: Mukherjee–Talukdar prove marginal dihedral Brownian FCLT and correction convergence. They do not establish joint independence from the full-history superdiffusive limit or strict negative covariance within memory variables. Shibata’s alternation has independent parity-specific histories, so does not cover this model.

## value

PASS

A joint two-scale invariance principle and an exact negative sign for residual memory covariance identify dependence unavailable from a marginal Gaussian limit. This distinguishes independence of diffusive noise from the nontrivially dependent superdiffusive memory and its correction on a standard nonabelian walk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
