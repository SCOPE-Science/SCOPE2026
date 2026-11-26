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

Condition on the first core infection. Memorylessness leaves one independent seed clock of each type for the second core, and n−2 independent two-edge paths that must both transmit at the first type's rate before they can beat the opposing seed. Their joint survival gives the displayed integral, including n=2 (the empty product), its finite sum, and strict monotonicity. One type has only its seed precisely when the core does not split. For u=alpha t, h(u)=log(1+u)−u is at most −u²/4 on [0,1] and at most −(1−log 2)u on [1,infinity). These bounds justify discarding the tail after s=√n u exceeds n^(1/12). On the remaining interval the scaled density exponent is −s²/2+n^(-1/2)(s³/3−(1+beta/alpha)s), with an integrable order-n^(-1) error after expansion. Writing rho=beta/alpha, the weighted leading factors exchange q and 1−q and sum to one; the weighted quadratic factors sum to rho+rho^(-1)−1, yielding the stated second coefficient. The conditional lag is on the n^(-1/2) scale, and conditioning each two-edge path to survive gives first-edge completion probability alpha t/(1+alpha t). Thus only o(n) peripheral vertices are claimed before the split; fresh independent hub races then yield the claimed conditional fractions. Bounded normalized minority size gives moment convergence; the unsplit contribution 1 is negligible for r≥1. This is an analytic proof, not an inference from the frozen checker, which was inspected but not executed.

## originality

PASS

The inspected work does not cover the fixed two-hub, two-peripheral-seed split probability, its two asymptotic terms, or its resulting minority moments. The infection paradigm and winner-takes-all-but-one phenomenon themselves are not new.

## value

PASS

The deterministic two-hub graph isolates a mechanism for nearly certain singleton loss that nevertheless gives a diverging mean minority size. The universal leading coefficient and the rate-sensitive correction quantify that mechanism, and the conditional limit distinguishes rare macroscopic coexistence from a merely non-singleton loser. This is a useful exact benchmark for competing-growth models, not a new claim of qualitative winner-takes-all behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
