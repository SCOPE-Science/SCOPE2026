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

Conditioning on the first cycle gives the exact renewal denominator q_s+E[h_k(B_R);R<τ_L], strictly positive since P(R>0)>0 and the Brownian target can be reached by any positive deterministic time. The scale function gives h_k(x)→x/L on (0,L), with h_k=0 on the negative side. For a>0 the integrating factor e^(−ka²/(2D)) in the half-line mean hitting-time equation fixes m'_k(−a) in the positive distance coordinate: ∂_a m_k(−a)=sqrt(π/(2Dk)) erfcx(sqrt(k/(2D)) a). This is the actual mean: stop the candidate on the interval (0,M); the upper-exit correction is the candidate value at M (at most linear in M) times the scale-function exit probability, which vanishes as M→∞. For the positive-side interval a uniform exit-time supersolution is w(x)=(Lx−x²/2)/D, since w'≥0, w≥0 at the ends, and (D∂²−kx∂)w≤−1. Thus after multiplication by sqrt(k), only negative starts contribute. The bound erfcx≤1 and E|B_R|≤sqrt(2D ER) justify dominated convergence, and Eσ≤ER disposes of the search duration. In the filtration enlarged by R at time zero, σ=R∧τ_L gives an L²-bounded stopped martingale; E[B_σ]=0 gives A=E[(-B_R)_+;R<τ_L]=Lq_s+E[(B_R)_+;R<τ_L]=Lq_0. This proves the stated amplitude, including clock laws with atoms and with mass at zero. For k=0 negative starts have positive probability by the killed Brownian density at any positive search time and infinite mean return duration. Fresh iid cycles and q_s>0 preclude infinite sequences of instantaneous cycles before absorption with positive probability.

## originality

PASS

Credit the earlier arbitrary-clock renewal reduction, visible-target splitting and OU hitting-time ingredients. The distinct supported claim is the exact common leading mean coefficient over the full fixed finite-positive-mean iid clock class. The general renewal equations still contain two law-dependent quantities at leading order, and neither the generic renewal framework nor the exponential specialization forces their cancellation without the stopped-Brownian identity identifying their ratio. The inspected indexed moment hierarchy agrees for exponential clocks and the three-term law agrees for finite-second-moment clocks (with stronger asymptotics in those domains); neither supplies the full integrable-clock quantifier. This is a bounded claim-level comparison, not a priority certification.

## value

PASS

The weak-return limit is a physically and mathematically natural singular endpoint of an established search model. The result gives the exact leading divergence of physical elapsed time and shows why clock choice cannot change it at this order when the target stays visible. The identity relates two different features of the search/return decomposition and applies to non-Poisson clocks without requiring a second moment. This is information beyond deciding finiteness or estimating a coefficient for one clock.

The dated certificate retains the supplied scientific assessment, sources and limitations.
