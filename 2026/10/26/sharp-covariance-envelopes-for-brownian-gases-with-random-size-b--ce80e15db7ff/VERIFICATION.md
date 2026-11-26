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

Independently condition on the two backward ages, truncated at t for zero initialization. Write a=rq1 and b=rq2. For 0<s,u<t their joint survival is exp[-a(s+u)+b min(s,u)], since the overlap excludes the union of the two reset marks. Independent Brownian drivers give C(t)/(4D^2) as the double tail integral over [0,t]^2 of exp[-a(s+u)](exp[b min(s,u)]-1). This proves strict comparison at every t>0 and verifies the generator calculation: u'=2D-au, w'=4Du-(2a-b)w imply C'=-(2a-b)C+b u^2. At stationarity the double joint-survival integral is 2/[a(2a-b)] and a marginal age is Exp(a); Gaussian fourth moments give Var(X_i^2)=20D^2/a^2, verifying both normalizations. A two-sided Poisson construction and the probability bound N exp(-at) for a coordinate not yet reset give existence and uniqueness. For f(m)=m(m-1), the difference from the lower supporting line through k,k+1 is (m-k)(m-k-1), and the upper endpoint chord minus f(m) is (m-1)(N-m). Equality supports and the fixed mean force the stated unique laws (at integer means the lower law is a singleton); for mu=1,N only one law is feasible. Linear mixing of the endpoint laws and continuity give the entire range. At t=0 the range is {0} and all feasible laws attain it; strictness and optimizer uniqueness are at positive times or stationarity, as the proof specifies. The frozen checker was inspected, not run; its subset enumeration and finite quadrature are not the all-time proof.

## originality

PASS

Credit the known fixed-size transient and stationary correlations and the routine random-mark extension of the underlying generator. The supported contribution is the complete fixed-mean distributional envelope, not the fixed-size formula or a new convex-order method.

## value

PASS

At identical expected reset activity the marginal motion is unchanged, yet pair fluctuations can be tuned over a nontrivial sharp interval at every positive time. The optimizing protocols can be implemented directly, and the result distinguishes fixed-budget control from the known variation with deterministic size at fixed clock rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
