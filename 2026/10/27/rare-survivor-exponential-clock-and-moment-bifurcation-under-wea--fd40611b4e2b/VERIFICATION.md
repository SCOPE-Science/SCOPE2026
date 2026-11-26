---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Each recruit has a defective success delay: it is τ if it survives to τ, and infinity otherwise. The count of successful immigrant arrivals by t is Poisson with mean βε J_{δε}(t). Its first-arrival time is independent of the initial searcher and equals the system completion time on initial failure. On u=εt>0, εJ_{δε}(u/ε) tends to u by bounded convergence, the initial-failure factor divided by ε tends to δm, and the light bare tail is o(ε). This proves both normalized survival and the conditional clock, including for bare laws with atoms. The coupling agrees up to τ if no birth or initial death occurs before τ, giving the TV bound. For moments the S(t) part is dominated by the bare moment integral. In the rescaled failure term, g_{δε}/ε≤δm and J_{δε}(t)≥c(t−M)_+ for fixed M with P(τ≤M)>0 and c>0 uniform for small ε. This dominates by a constant times u^{q−1}exp(−βcu), integrable for every q>0. Integrating gives δmΓ(q+1)/β^q with prefactor ε^{1−q}; the bounded bare part supplies the q<1 and q=1 limits. At q=2 the bounded squared mean is negligible, giving 2δ/[m(β+δ)^2] for ε times squared CV.

## originality

PASS

This is a close extension of a known same-model, same-regime analysis. The exact survival formula, first-moment discontinuity and qualitative rare-mortality/long-wait mechanism are prior. The existing weak-rate survival expansion also essentially supplies the macroscopic profile once its error is controlled at t=u/ε. Credit the joint quantified result, particularly the conditioning on initial failure and the real-order transition with sharp constants and uniform control of the moment integrals, not rediscovery of the mechanism or a new solution of the finite-rate survival problem.

## value

PASS

Typical completion times and risk-sensitive summaries can behave differently even with a light-tailed bare passage law: O(ε) of the mass survives on an O(1/ε) time scale. Quantifying that tail and proving the entire positive-moment transition distinguishes small changes in the distribution from variance divergence and gives usable leading constants, not just a first-moment discontinuity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
