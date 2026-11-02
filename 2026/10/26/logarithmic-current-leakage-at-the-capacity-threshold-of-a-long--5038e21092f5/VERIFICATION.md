---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

At fixed q>1, N=M, M/L→η∈(0,∞), and L≥3, the imported exact stationary product weight gives W_k=binom(L,k)q^{-k(k+1)/2}[M choose k]_{1/q} and exact ratio R_k=((L-k)/(k+1))q^{-(k+1)}(1-q^{-(M-k)})/(1-q^{-(k+1)}). Every prefactor is decreasing, giving R_{k+1}<q^{-1}R_k. Its mode m satisfies (log q)m+log m=log L+O(1), so m=[log L-loglog L+log(log q)]/log q+O(1); uniform supergeometric tails give E K=m+O_q(1), Var K=O_q(1), and E K²=O_q((log L)²). Conditional ring exchangeability gives per-bond signed J=(h_f-h_b)E[K(L-K)]/[L(L-1)], yielding stated log/loglog expansion. Complement occupations maps N to L+M-N and q to 1/q, preserving signed ring current. Independently recomputed exact canonical weights and consecutive ratios at (L,M,q)=(7,5,2),(11,9,3),(13,9,1.5), and inspected finite Markov-generator verifier. The infinite limit follows from the analytic mode/tail proof, not from those tests. Hypotheses strictly fixed q≠1, η>0 finite; no q→1 uniformity, time fluctuations or spectral gaps claimed.

## originality

PASS

The exact one-side-branch stationary measure and current identity are already due to Ishiguro–Ando, as are qualitative blocked regimes. The inspected 2026 primary paper's §III.3/§IV.2 does not explicitly identify the capacity-matched growing-L logarithmic leakage, negative loglog correction or bounded-fluctuation window. The novel candidate is a sharp asymptotic consequence of the published canonical formula, not a new stationary measure. No searched publication or Resultary record demonstrably states or dominates this precise joint asymptotic; generic canonical saddle techniques may yield an implicit equivalent, recorded as a residual priority risk.

## value

PASS

The occupation fluctuation scale and −loglog correction quantify a physically meaningful singular capacity boundary between macroscopic current and almost trapping. Exact power/log correction can calibrate finite rings; proving a tight order-one variance, not just exponent, is substantive. A sharp asymptotic boundary of a natural model is independently useful even when its finite-size distribution was known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
