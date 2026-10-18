---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Schwab–Thompson Proposition 1.1 supplies an iff sorted-prefix test for sums of distinct divisor-aliquot values. For composite n, each distinct prime divisor contributes one weight s(p)=1, other composite divisors have s(d)>=3. Exhausting the exponent partitions of Omega(n) in {2,3,4} constrains possible p^a and p^a q^b forms, leaving n=12,24,36,60,84,90,100,126,198. Checking the exact sorted positive weights excludes all except 60; s(60) multiset sorted is [1,1,1,3,6,8,9,16,22,42,108] and satisfies every prefix inequality. No unbounded enumeration cutoff is used. Independent factorization/subset-prefix check through n=100000 corroborated the symbolic partition proof.

## originality

PASS

Best-of-knowledge new natural first composite prime-factor-multiplicity classification: Omega(n)>=4, equality iff 60. Full founding paper and OEIS do not entail it; 2026 thesis inaccessible and risk documented.

## value

PASS

The first attainable composite Omega-layer is a mathematically natural structural invariant in the recognized s-practical number sequence. The sharp uniqueness theorem is unbounded, rules out all lower multiplicity patterns, and gives future searches a rigorous base case; it is not equivalent to a finite table or arbitrary small cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
