---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For n≥3 distinct reports on any metric space with exactly n−1 open facilities, OPT is the closest-pair distance d*. Omission weighted by nearest-other distance^(−q) gives ratio (Σ y_i^(q−1))/(Σ y_i^q), y_i=d*/d_i, and a closest pair forces at least two y_i=1. For 0≤q<1 the real-line gap family 1,t,... gives unbounded ratio; q=1 approaches n/2. For q>1, maximizing g_R(y)=y^(q−1)−Ry^q at y=(q−1)/(qR) bounds Σg_R by 2(1−R)+(n−2)(q−1)^(q−1)/(q^q R^(q−1)), yielding the unique sharp root, attained by consecutive real-line gaps 1,t,t,... with t=qR/(q−1). The optimal root strictly decreases in q by a positive covariance/monotone weighted mean argument. On truthful (0,1,2) moving report 0 to −ε yields cost ε+(1−ε)/(1+2(1+ε)^q), with derivative 2(3−q)/9; all q>3 admit a profitable small deviation. The q=1 and q=2 theorems are explicitly treated as prior work. Finite program inspected, not used as universal proof.

## originality

PASS

Best-of-knowledge PASS limited to the all-real-exponent sharp welfare law and the q>3 incentive obstruction, not the known q=1 Escoffier or q=2 Chan–Lin–Wang cases.

## value

PASS

The distance-power exponent is a natural design choice trading aggregate facility cost against strategic robustness. A sharp full-exponent efficiency curve, q=1 unbounded/finite threshold, and explicit manipulation at q>3 resolve nontrivial infinite-family mechanism-design questions beyond the known q=1,2 instances; this does not solve incentives at 2<q≤3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
