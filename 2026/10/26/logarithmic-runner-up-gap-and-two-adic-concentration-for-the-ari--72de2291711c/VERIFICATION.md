---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For odd m, sum_p v_p(m)/p <= log(m)/(3 log 3)=b log_2(m). Writing n=2^(k-t)m and x=m/2^t gives exact deficit (k/2)(1-x)+x(t/2-S(m)) >= ct+(k/2-ct)2^-t >=ct+bk2^-t, with c=1/2-b>0. Convex minimization yields c log_2 k+gamma. Competitor n=2^(k-t)(2^t-1), t=ceil(log_2 k), yields (log_2 k+2)/2. Each maximizing t and relative shortfall therefore satisfy explicit bounds. Independently computed D via smallest-prime recurrence for k=2..16; sample gaps k=2:3,k=8:384,k=12:7168,k=16:122880. Finite checks do not prove all-k bounds.

## originality

PASS

Earlier dyadic record results say D(2^k) is maximal and finite OEIS tables list record arguments; those do not quantify the next-best gap for unbounded k or localize every maximizer. Resultary semantic search returned a different arithmetic-derivative cototient gap, not this runner-up invariant.

## value

PASS

Quantitative behavior of the second-best value and valuation of every optimizer addresses a natural sharp near-record invariant, not a numerical one-off; asymptotic logarithmic scale was not implied by record status alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
