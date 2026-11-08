---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For each coupon, occurrence frequency is Bin(t,p), p=s/n; conditioning on another coupon absent in every packet changes its per-round inclusion probability to s/(n-1). Summing n(n-1) ordered distinct-coupon pairs gives E[U M_r] and exact Cov=n² q^t binom(t,r)p^r q^(t-r)(R_r-1) with R_r=(n/(n-1))^(t-1)((n-s-1)/(n-s))^(t-r). For s<=n-2, R_1<1<R_t and R_{r+1}/R_r>1; equality at intermediate r would equate powers with reduced numerators n and n-s and is impossible. For s=n-1 only r=t is positive. Logarithmic root gives j, and packet-width monotonicity follows monotonic (n-s-1)/(n-s). Dense regime logs ratio tends 1-rho; ceiling/t→0. Independent exact enumeration for n=4,s=2,t=3 (216 ordered packet sequences) reproduced every r=1..3 covariance. Exact fraction evaluations reproduced 120475/839808 and -160256/820125 for the claimed s=1,2 sign reversal at n=6,t=5,r=2. Boundary 0^0 exponent convention checked.

## originality

PASS

Mahmoud–Smythe Proposition 1 already provides the generalized full covariance matrix and is prior for the finite second moment. The assessed new statement is the uniform strict one-transition sign pattern, impossibility of zero ties, monotonic packet width, explicit width reversal and dense asymptotic threshold. Closest published occupancy-richness sign switch uses iid single draws, i.e. a subcase not this dependent fixed-size packet model.

## value

PASS

Fixed-size group sampling is natural in coupon and species occupancy models. An exact all-frequency sign boundary, strict nonzero covariance and packet-width reversal predict qualitative dependence not visible from a covariance formula alone; the value lies in this complete phase characterization, not in recomputing an old moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
