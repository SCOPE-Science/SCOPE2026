---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

An as-yet-unseen initial complement label is never in the current r-packet, so the next incoming uniform draw, conditional on complete history and eviction, hits each of k unseen labels with probability 1/m. This makes the cumulative-seen-set Markov transition kernel exactly the coupon collector kernel, independent of the eviction policy; waiting times yield 1+mH_m, variance m²H_m^(2)-mH_m, and inclusion-exclusion CDF. For independent packets, J newly hit among k missing has hypergeometric expectation rk/n. V(k)=(n/r)H_k has conditional decrement >= (n/r)J/k and hence expected at least 1, strictly >1 from initial state when r,m>=2 because P(J>=2)>0; optional stopping of finite positive expected cover time gives E(T_iid)<1+(n/r)H_m<=1+mH_m. If r=1, direct harmonic subtraction is H_(n−1)>0; if m=1, replacement needs one move whereas iid succeeds geometrically at rate r/n. Separately derived exact rational iid expectation dynamic recurrence for all 105 pairs 2<=n<=15; all signs match. No stochastic-order comparison for entire distributions is claimed.

## originality

PASS

The independent packet inclusion-exclusion formula is prior Adler–Ross; the assessed new result is the full adaptive replacement coupon-law identity and complete strict finite (n,r) sign reversal. Closely related Johnson-walk conjectures and iid subset collectors do not state these additional results in the inspected material.

## value

PASS

The dependent Johnson-graph individual-label cover process was explicitly raised as a natural case in existing work. Its complete distribution under arbitrary nonanticipating eviction and the exact sign boundary comparing it to iid packets are a useful all-parameter solution, revealing a nontrivial reversal at both extreme packet sizes rather than a tiny numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
