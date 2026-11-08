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

First-reset distribution has defective masses f_k with total 1−p; independently restarted waits give a geometric number K of finite waits before escape, so L=sum_{j≤K} X_j<∞ a.s. and E[z^L]=pΣF(z)^K=p/(1−F(z)), with denominator bounded away from zero. Coupling last observed reset with ultimate reset yields ||U^{-t}rho_tU^t−sigma||_1≤2P(L>t). Eigenbasis multiplication multiplies off-diagonal rho_ij by G(u_j/u_i), and triangle bounds on 1−F give the sharp nonzero floor. Two-stage r0=q,r1=(1−p−q)/(1−q),r_n=0 afterwards exhaust [p/(2−p),1] at z=−1. Nonzero G for all phases proves convergence iff commuting; Cesàro averaging removes gaps. For r_n=(n+2)^−2, telescoping p=1/2, f_k=1/[2k(k+1)], E[K²]=3 gives P(L>t)≤3/t. Independent finite recurrence and direct transform truncation checks corroborate, not replace, these all-time arguments.

## originality

PASS

Prior discrete quantum reset work already has age renewal, last-reset propagation, and nonstationarity examples. The exact moving orbit filter, nonzero phase-independent coherence floor, complete fixed-escape attainable interval at opposite phase, iff convergence and reset-independent dephased Cesàro state are additional conclusions. Some may be implied by classical defective renewal theory but combined quantified quantum characterization not identified.

## value

PASS

The theorem distinguishes mere escape probability from residual observable quantum coherence and gives a sharp, attained obstruction to loss of off-diagonal information, with exact stationary/oscillatory dichotomy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
