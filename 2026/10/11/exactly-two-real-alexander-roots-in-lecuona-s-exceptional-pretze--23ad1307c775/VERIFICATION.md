---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For odd a≥3 set m=(a+1)/2≥2; the representative polynomial is monic reciprocal degree 2a. On t=(1+u)/(1-u)>0, |u|<1, Saurabh’s exact Cayley transform gives D_m(u)=E_m(u)^2-u²(1−u²)^(2m−2)(u²+4m²−1). Since E_m(u)>=1+m(2m−1)u² and (1+A r)^2>=4A r>4m²r for m≥2, D_m>0 on all positive t. On t=−e^(2v), the exact hyperbolic reduction is [sinh(2mv)/sinh(v)]²−1−4m²cosh²v. For v>0 the difference between 2Σ_{j=1}^m cosh((2j−1)v) and 2m cosh v is strictly increasing from zero, while the sum is positive increasing, so exactly one simple root appears below −1. Reciprocity gives the unique simple partner in (−1,0), and Δ(−1)=−1 excludes the middle. Infinite-family argument uses strict inequalities, not finite samples.

## originality

PASS

The published residual-family theorem DOES COVER exactly-two-negative-simple-reciprocal roots when m≥3 is odd; no priority claimed for that portion. Its statement does not apply to even m, and it does not rule out positive real roots. Saurabh’s full paper provides polynomial, Cayley transformation and a positivity lemma for an auxiliary Q in odd-m case; it does not classify all real Alexander roots for all odd a. The present all-m>=2 real-axis classification is therefore a strictly broader complete statement, albeit an algebraically straightforward extension of the prior negative-axis proof.

## value

PASS

Alexander real-root counts are natural topological polynomial invariants for the entire exceptional three-strand pretzel family. Completing the real-axis spectrum for every odd a≥3, including the previously omitted even m and explicitly excluding all positive roots, is a precise, potentially reusable family-wide classification beyond residual odd-m negative-root asymptotics. It does not claim a new sliceness obstruction or progress on nonreal root distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
