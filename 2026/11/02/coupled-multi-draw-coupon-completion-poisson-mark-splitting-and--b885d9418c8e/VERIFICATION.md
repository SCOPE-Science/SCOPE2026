---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The number U of types not selected by an adaptive one-choice policy is a pure-death chain with exact death parameter q_(n,u)=1-binomial(n-u,d)/binomial(n,d), independent of tie breaking. The sum of geometric holding times from n to sqrt(n) concentrates around (n/d)log(n/sqrt(n))+n C_d, while the last sqrt(n) disappearances couple at o(n) error to independent exponential clocks, giving Pois(c_d e^-x) in the standard window. For disjoint tagged I,J, conditioning on avoiding I gives exactly the reduced n-a process and tagged factorial identity; inclusion-exclusion over J splits off already offered but unselected types. Mixed factorial moments yield independent Pois(e^-x),Pois((c_d-1)e^-x). Rare simultaneous draws of two still-unselected types permit the two independent pure-death limits across times, yielding joint Gumbel extrema. Integrating the difference of extrema gives F_D(z)=1/[1+(c_d-1)e^-z] for z>=0 with mass 1/c_d at zero. Exact finite tie probability convergence requires near-tie control; two independent continuous limiting maxima have zero tie probability, so ties come exactly from reversed final categories in the limit. d=1 yields identical policies. Independently computed seven sequential finite count-state distributions against labeled coupon-mask dynamics (n=5,d=2).

## originality

PASS

PASS, qualified: Doumas–Spektor study the exact same two multi-draw retention policies but accessible descriptions identify marginal means, variances and separate Gumbel limits, not their joint law under shared offered groups. Coupling, independent marked categories and a logistic lag with an atom are additional observables; general group-drawing Poisson results treat occupancy but may provide transferable machinery. Complete same-model primary full text remains inaccessible and priority risk is substantial, not treated as scientific failure.

## value

PASS

The coupling describes the sample-by-sample price of discarding offered coupons, a natural algorithmic comparison not determined by two marginal completion laws. Exact asymptotic chance of equal finishing round and a nontrivial limiting delay distribution are useful invariant statistics even for fixed d=2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
