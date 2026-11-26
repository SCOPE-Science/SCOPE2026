---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The multiplicity convention gives complete additivity of S. For t≥2, induction under t=ab with a,b≥2 proves S(t)≤a+b≤ab=t, with prime cases immediate; S(1)=0. If composite m=ab satisfies S(m)=m−1, then (a−1)(b−1)≤2, so 2≤a≤b leaves only (2,2),(2,3). The first gives S(4)=4, the second S(6)=5. If n+1 is prime then S(n+1)=n+1>S(n), even at n=1. Otherwise a prime member must be n, and the lemma forces n+1=6, with S(5)=S(6)=5. This works for neighbors of arbitrary factorization complexity. The smallest-prime-factor checker ranges only through 2000000; the two finite predicates corroborate but do not establish exhaustiveness over all m or n. No fresh execution or formal verification is claimed.

## originality

PASS

The strongest catalogue comparison gives uniqueness only under a two-sided Ω≤2 restriction; the closest inspected low-component primary theorem uses a different function and different quantifiers. The exact OEIS comments record the ingredient S(m)≤m and list (5,6) via start 5, but do not state the unrestricted prime-member result or the sharp one-below equality in the passages inspected. Historical coverage is not ruled out by the unresolved access gaps.

## value

PASS

This is the complete minimal prime-factor layer on either side of a standard consecutive-factor-sum equation. Unlike a census or the different two-sided low-Ω problem, it rules out every composite neighbor of arbitrary complexity except the lone witness. Its exact one-below lemma isolates the obstruction and is independently reusable when comparing S(m) to a nearby prime, without making a claim about infinitude or higher-complexity pairs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
