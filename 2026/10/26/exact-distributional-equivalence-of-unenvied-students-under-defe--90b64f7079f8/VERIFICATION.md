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

PASS: Assumptions are n students/n unit-capacity schools, independent uniform complete strict preferences, independent uniform school priorities for student-proposing DA and uniform serial order for RSD. An earlier serial chooser cannot envy a later chooser. For marked RSD serial positions K, at time t each later chooser must prefer one of n-t+1 available schools to the a_t=|K∩{1,...,t-1}| previously selected marked schools, giving conditional probability (n-t+1)/(n-t+1+a_t). Identical hazard holds for first-appearance-ranked coupon types staying singletons until cover. Equality of all subset-inclusion probabilities implies joint indicator-vector equality by Boolean inclusion-exclusion; telescoping gives r!/product_{s=1}^r(n-k_s+s). DA has the already-known coupon singleton representation under the exact random market model, so full unenvied-count distributions agree. Pair covariance and variance follow from r=1,2, with harmonic asymptotics and factorial moments giving Exp(1) after log n normalization. Independent exhaustive RSD n=4 checked 331776 profiles, every one of 15 nonempty inclusion subsets, and full distribution (97,97,67,27)/288.

## originality

PASS

PASS, qualified: Ortega, Ziegler, Arribillaga and Zhao (2026) already obtain DA coupon singleton representation and equality of DA/RSD expectations H_n; Myers and Wilf give the coupon singleton distribution and Papanicolaou/Doumas the exponential coupon limit. The inspected original school-choice paper does not identify the full RSD serial-indicator joint law or DA/RSD finite-distribution equality. These are the novelty-bearing parts; no claim of new coupon distribution or known expectation is made.

## value

PASS

PASS: Matching an entire finite-market law, rather than a previously established first moment, and providing joint inclusion/covariance formulas yields a motivated distributional bridge for a natural market statistic. This is a nontrivial sharpening of known expectation identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
