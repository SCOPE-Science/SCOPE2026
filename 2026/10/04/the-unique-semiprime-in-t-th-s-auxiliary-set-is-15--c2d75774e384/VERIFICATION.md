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

The equation is σ(n)/n=2x/(x+1), with the right side strictly increasing for positive integral x. For distinct odd primes p<q, the left side is (1+1/p)(1+1/q), strictly greater than 1 and bounded above by (1+1/3)(1+1/5)=8/5, with equality only at (3,5). This gives x∈{2,3,4} and settles x=4 directly. At x=3 one would have 2σ(n)=3n, impossible for odd n. At x=2 the frozen factorization (p−3)(q−3)=12 has positive even factors and only the ordered pair (2,6), giving q=9. For n=p², p=3 gives σ/(2n−σ)=13/5; for p≥5, σ/n=1+1/p+1/p² lies strictly between 1 and 4/3, so cannot equal 2x/(x+1). Finally 15 has σ=24 and x=4. Thus both possible multiplicity-two cases are exhausted without an upper bound on n. The certificate is a summary of the branches; the script checks finite divisions and inequalities and a regression through 200000, not the unbounded quantifier. No fresh script execution or formal verification is claimed.

## originality

PASS

Tóth and the exact sequence database establish membership of 15 but do not establish its uniqueness at Ω=2. The nearby published shifted-equation family and restrictions on factors of spoof odd perfect numbers concern different hypotheses. The distinction is between a bounded observed example and an unbounded theorem that also rules out prime squares.

## value

PASS

Tóth's motivating study computes this very set and seeks structural alternatives to brute force. Semiprimes are its entire first composite factor-count layer, not an arbitrary cutoff. Ruling out that infinite layer except for 15, including all prime squares, gives a concrete necessary factor-count condition for any other composite member. The novelty and utility are the complete exclusion, not the already-tabulated witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
