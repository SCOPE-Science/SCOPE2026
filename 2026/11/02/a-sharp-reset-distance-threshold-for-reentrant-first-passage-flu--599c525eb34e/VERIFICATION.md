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

First-reset renewal gives survival Laplace transform [1−exp(−a sqrt((s+r)/D))]/[s+r exp(−b sqrt((s+r)/D))]. Differentiating at s=0 yields both passage-time moments and CV²−1=[e^(−t)/(1−e^(−t))](2−Hq(t)). Hq rises from 1 to infinity for 0<q≤1. For q≥1, differentiation gives (log Hq)″≤−1/t²+1/[4sinh²(t/2)]<0; for q>1 its unique maximum strictly decreases from >2 near q=1 to <2 by q=2. This proves precisely one, two, tangential one, or zero CV=1 crossings, with unique q_c≈1.228631400481950585 and t_c≈4.133452638304952835. Domain: fixed a,b,D,r>0 and absorbing Brownian halfline.

## originality

PASS

The underlying first-passage survival transform is explicitly known in two-site resetting literature; the asserted extra result is the four-regime CV crossing classification and strict shape lemma, not a new transform. Source with averaged starting/reset distributions is not the same ensemble.

## value

PASS

A global sharp reset-distance bifurcation in first-passage dispersion, including a two-crossing reentrant phase and universal exact tangency, supplies a practically relevant regime map beyond mean-optimal resetting and avoids extrapolating CV=1 optimal-restart folklore to mismatched starts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
