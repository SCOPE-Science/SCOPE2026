---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

The first t-1 draws are distinct, must include repeated label i and any t-2 others; their (t-1)! permutations give the exact joint law for every 2<=t<=m+1. Excluding pair i,j gives ratio (pi/pj)^2 (E_k+pj E_(k-1))/(E_k+pi E_(k-1)). Newton log-concavity yields strictly increasing E_(k-1)/E_k, including zero and infinity endpoints; hence odds strictly increase for pi<pj. Summing conditional pair differences yields the threshold-event ordering and declining E[p_R|T] except uniform vectors. Independent exhaustive rational first-repeat enumeration for m=4, p=(1,2,3,4)/10 matched every time-conditioned law, and checked endpoints. Includes edge m=2 and equal-probability equality.

## originality

PASS

Camarri–Pitman already develops complete first-repeat time and occupancy-set laws for arbitrary weights; the claim does not count those as new. Conditional pairwise LR ordering of the repeated label across every possible collision time, including strictness, is a distinct uniform inequality not observed in the inspected primary theorem.

## value

PASS

The repeated category given first collision time is a natural statistic for nonuniform birthday sampling. Its exact all-time rare-label shift, not merely marginal collision probability, offers a sharp pairwise stochastic-order classification over every alphabet size. A future probabilistic inference analysis can use this specific posterior ordering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
