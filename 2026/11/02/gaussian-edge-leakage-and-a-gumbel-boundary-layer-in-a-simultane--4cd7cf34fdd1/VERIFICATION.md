---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Under stationary common rate-r Poisson resets, age A~Exp(r) and conditional particle positions iid N(0,σ²(1−exp(−2µA))) with σ²=D/µ. S=exp(−2µA) has exact Beta(β,1) density βs^(β−1), β=r/(2µ); V=(logN)S has density β(logN)^(−β) v^(β−1) on (0,logN). Independently derived exact conditional max threshold q_N(v,x)=1−Φ((u_N+x/u_N)/sqrt(1−v/logN))^N, u_N=Φ^−1(1−1/N). At fixed v Gaussian max Gumbel scaling shifts x→x+v; Mills tail-ratio upper bound q_N≤exp(−v/4) for large v yields an integrable beta-weighted envelope for every β>0 and fixed x. Dominated convergence gives Kβ(x)=β∫v^(β−1)Q(x+v)dv=E(G−x)_+^β. Normalization gives the conditional V mark and −log age-offset distribution. At uncorrected threshold sqrt(2logN), N Gaussian tail ~exp(−v)/sqrt(4π logN), another dominated convergence yields scaled leakage Γ(β+1)/sqrt(4π) and distinct β+1/2 exponent. Independent direct 1D Gaussian-mixture quadrature for β=.5,1,2 and logN=16,40,80 corroborated approach to both exact limits (not a substitute for proof). Claims are fixed x and fixed µ,D,r, stationarity, not finite-N uniform bounds.

## originality

PASS

Qualified PASS as a refinement. The exact conditional-Gaussian stationary mixture and bounded-support leading maximum law are established by de Mauro–Majumdar–Schehr (arXiv:2606.31634, accepted Phys Rev E 2026-11-03); no originality is attributed to them. The present theorem computes sharp vanishing exceedance probability on the corrected Gumbel boundary, conditional rare reset-age selection and the extra +1/2 power at the uncorrected edge. The closest primary abstract/accepted-paper landing was checked; full arXiv text was inaccessible in this run, while previous source manuscript describes Sec VI.1.1's approximate O(1/logN) cutoff. This creates material risk that Eq (129)–(136) or appendix already implies a coefficient more directly. Published Resultary related OU sensor and pinned bridge Gumbel results involve different source/mixing variables. Best-of-knowledge claim remains qualified, not a declaration that the original full paper lacks the result.

## value

PASS

The leading compact-support weak maximum law leaves vanishing beyond-edge probabilities completely unresolved. Computing Kβ(x), a conditional reset-age law, and Γ(β+1)/sqrt(4π) leakage rate provides natural exact finite-population extreme-event observables, including a physically interpretable distinction between rare old common resets and Gaussian fluctuations. This is a substantive asymptotic boundary refinement of an established model, not rediscovery of the stationary mixture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
