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

Fix the priority order and the designated positions. The first-appearance order from each student's independent uniform label stream has the required ranking law (prefix a forced s and use only other labels for a designated student's tail). RSD reads through the first available label, so each school's first occurrence assigns it and a later occurrence in a different student's read prefix witnesses incoming envy; earlier students cannot envy a later assignment. Thus the unenvied count equals the singleton count. With no designations the fresh draws together are iid uniforms, stopped on complete collection. With one designation, conditioning on that student's top school leaves the law of the count invariant by school relabeling. With at least two, the first designated move allocates s if it is not already allocated, so s is not last; both designated students probe s and it cannot be a singleton. Generate each ordinary probe by an independent flag (output s with probability 1/n), and on non-s probes draw the next label from a common independent iid uniform reservoir on the other schools. A designated probe is either its forced s or the next reservoir label; this realizes the same conditional transition laws at every revealed history. The reservoir is read exactly up to the first discovery of all its labels, because s is not last, and multiplicities of the non-s labels are unchanged. This proves the fixed-priority claim for all n, including n=2, r=2 with S_1=1. Independent rate-one Poisson clocks give the stated density integral: choose the last type and j−1 already seen exactly once, with the other types seen at least twice at its first-arrival time. For the mean, for any type and maximum T of the other first arrival times, its singleton probability is E[(1+T)e^(−T)]=H_m/m (for m=1 take T=0).

## originality

PASS

Pass the supported distinct claim: two or more forced common-first rankings lower the effective coupon alphabet by one, with the entire fixed-priority unenvied-count law independent of r in that range. The coupon law, independent-preferences baseline, and single-designation relabeling consequence do not constitute new results here.

## value

PASS

A popular school with a guaranteed group of first choices is a natural elementary demand concentration in RSD. The result identifies the exact threshold at two and gives the full unenvied-count law, not just its mean; once the threshold is crossed, every additional designated student leaves the law unchanged. The reduction permits exact probability computations for arbitrary n without enumerating preference profiles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
