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

Given the censored clock history at s=(log K)/4, the residuals of surviving clocks are independent rate-one exponentials. A late root must lie in an all-surviving triple. Its conditional probability there is p=e^{-x}K^{-1/4}; the number S of surviving triples has mean K^{1/4} and variance K times (q^3-q^6)+2(q^4-q^6)+2(q^5-q^6), with q=K^{-1/4}. Thus E|pS-e^{-x}|=O_x(K^{-1/8}). The conditional dependency graph has radius two, and conditional b1 is at most 5p^2 S. Neighboring valleys exclude one another; for distance two both centers being late forces all five clocks to exceed t. Independently, transforming the residual ranks to uniforms gives the two-valley probability 2∫_0^1 (v-v^2/2)(1-v)^2 dv=2/15, yielding E b2=O_x(K^{-2/3}). Chen–Stein and the Lipschitz bound for the exponential give the stated continuous-clock conditional error for fixed x and eventually t>s. Roots seen by s can be identified exactly from the history. The expected number of missed roots is K^{1/4}/3, and each insertion changes a fixed gap count by at most two. The event of no early root has probability e^{-Ks}. Hence the early and final fixed-coordinate profiles differ by o_P(1) after normalization. Testing a bounded function of the early profile against a last-arrival threshold factors its expectation with the stated error. Matijasevick's Theorem B supplies the marginal Gaussian process, with the submitted coordinate cutoff eventually identical in each coordinate; marginal tightness gives joint tightness and finite-coordinate laws determine the product-space limit. The same early approximation works for root count using its known CLT (its radius-two indicators also give variance per site 1/3(2/3)+2(0-1/9)+2(2/15-1/9)=2/45). Finally P(tau>log K)≤1/(3K^2), and the rate-K Poisson martingale satisfies Doob's bound 4K log K on the squared supremum up to log K. This suffices for Slutsky on the K scale without assuming independence of the martingale and tau. Neither a discrete-step conditional error nor a growing-gap result follows from this review.

## originality

PASS

The two marginal laws and the unconditional dependency-neighborhood method have clear prior coverage. The supported distinct contribution is the quantitative conditioning on an expanding first-arrival history and its use to prove the last-root-time/entire-final-gap-profile product limit, not either marginal or a general new Poisson approximation theorem.

## value

PASS

The time at which the last spatial root forms and the fluctuations of the final spatial gaps are natural observables of the same experiment. Their asymptotic independence cannot be inferred from the two marginal laws. The quantitative early-history bound captures what can still be predicted after most roots have formed and yields decoupling of the complete Gaussian profile without asserting independence among its coordinates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
