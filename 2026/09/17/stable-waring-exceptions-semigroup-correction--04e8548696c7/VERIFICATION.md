---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The semigroup equivalence is exact by subtracting 1 from each summand and padding a finite semigroup representation with 1^k terms. The generated monoid is numerical because the gcd of all a^k-1 is 1. For q=p^e with e<=k and lambda(q)|k, each generator is 0 or -1 mod q; an element congruent to -r therefore needs at least r p-divisible-base generators, each at least p^k-1, yielding exactly r(p^k/q)-1 forced gaps in that residue class. Summation gives the stated bound. The extra residue-zero gaps under q(q-1)<2^k-1 are below the smallest positive generator. For p=3, S_2=<3,8,...> has exactly the seven gaps {1,2,4,5,7,10,13}, contradicting the published bound 9. The p=5 and p>=7 repairs are arithmetically consistent.

## originality

PASS

The primary paper itself contains the inconsistency: Table 2 gives |B^2|=7 while Theorem 10.7 states the universal odd-prime lower bound, which gives 9 at p=3. Targeted searches found no published correction or the prime-power Carmichael extension. General numerical-semigroup literature located in search results concerns other generator families and does not cover this Waring-offset semigroup theorem.

## value

PASS

The result corrects a concrete false theorem in a recent paper while preserving its important p=11 corollary, and the prime-power formulation turns the repair into a reusable structural obstruction. This is substantively motivated and not merely a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
