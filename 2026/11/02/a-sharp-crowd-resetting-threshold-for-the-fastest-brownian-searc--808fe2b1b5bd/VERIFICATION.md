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

The reflection-principle hitting law gives density sqrt(t0/pi) h^(-3/2) exp(-t0/h) and its exponential discount gives q_N=N^(-2 sqrt(a)). The time substitution h=t0 z/log N exposes the constrained rate inf_{0<z<=y}(1/z+a z). The moving cutoff beyond a^(-1/2) contains the unique saddle, so the truncated probability divided by q_N tends to one. I checked the second-moment bound: under a pair of prescribed starts s<u, the earlier discounted success event is cut off no later than u, and its reset data use only the interval before u; the later event uses independent data after u. Brownian excursion marks are independent. The earlier marginal probability is bounded by q_N(delta) and the later is q_N(delta). Integrating ordered reset pairs and pairs with the initial start gives (r_N w)^2+2r_N w times q_N(delta)^2. Thus the count bounds do not assume unconditionally independent successful starts. Below threshold, N multiplying the first-attempt lower bound and the O(log N) multiple upper bound separates y below and above the smaller root of 1/y+a y=1. At a=1/4, y<2 has rate >1; y>2 allows a cutoff c in (2,y), true success probability asymptotic to 1/N, and order log N starts, with negligible pair correction. Above threshold at t=z/(Nr_Nq_N), take any cutoff c t0/log N with c>a^(-1/2); it is negligible relative to t and the pair correction is O(N^(-2)). Hence N p_N(t) tends to z and survival tends to exp(-z). At a=0 the first-attempt bounds coincide. Scope is fixed a with independent resetting; the script's finite checks are supplementary and were read, not run.

## originality

PASS

The finite-N identical-model renewal formula and the single-walker frequent-reset exponential law are prior results. An indexed same-day synchronized-reset theorem also recovers the same leading supercritical normalization and exponential law on a>1, but its common-clock dependence, transition at a=1, and critical normalization differ. The supported distinct claim is the joint three-regime independent-clock theorem, especially the critical value and the entire supercritical range a>1/4. This is a bounded determination, not a priority certificate.

## value

PASS

The threshold separates a fastest time shrinking as 1/log N from a fastest time growing polynomially despite the increasing number of independent searchers. The exact critical constant shows where the saturated one-attempt saddle and the number of fresh attempts must be treated jointly rather than extrapolating either regime. It is a motivated nonuniform limit for the standard independent-reset model, not an optimization claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
