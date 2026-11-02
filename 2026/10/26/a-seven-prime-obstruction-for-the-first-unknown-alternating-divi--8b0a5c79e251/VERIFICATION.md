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

PASS: For the multiplicative alternating divisor sum beta(p^e)=(p^(e+1)+(-1)^e)/(p+1), 4 beta(n)=n implies v2(n)>=2. If at most six distinct prime factors, n=2^a times at most five odd-prime powers. Each odd p contributes beta(p^e)/p^e >=(p-1)/p, minimized over five odd primes at 3,5,7,11,13 with product 384/1001. At a=2 the dyadic factor 3/4 yields 288/1001>1/4; at a=4 it is 11/16 yielding 264/1001>1/4; for a>=5 it is at least 21/32 yielding 252/1001>1/4. At a=3, beta(8)=5 is odd and v2(beta(n))=a-2=1, so exactly one odd prime has odd exponent. This factor is at least (p-1)/p, every remaining even-exponent prime factor at least p/(p+1). The minimum among five odd primes occurs with the exceptional odd exponent on p=3 and four other smallest possible odd primes 5,7,11,13, giving (5/8)(2/3)(5/6)(7/8)(11/12)(13/14)=3575/13824>1/4. Contradiction for all cases with omega(n)<=6. All fractions independently checked with exact rational arithmetic and original checker source inspected. No existence/sharpness claim.

## originality

PASS

PASS (qualified): Zhou–Zhu (2009) primary full paper Proposition 11 gives only omega(n)>=k−1, hence >=3 at k=4; Theorem 9 establishes >=18 only for odd k-imperfect n and cannot cover this necessarily even case. Tóth 2013/14 survey records the local beta identity and the absence of known examples for k>3, but not this seven-distinct-prime obstruction. The new conditional bound is a strict four-factor improvement and relies on 2-adic parity plus a targeted exact rational threshold. An unindexed equivalent restriction is possible; failed searches are not proof of historical novelty.

## value

PASS

PASS: k=4 is the first multiplier for which existence of alternating-divisor k-imperfect numbers is unknown; bounding the necessary number of distinct prime factors is a directly motivated structural constraint, not arbitrary finite computation. Raising the generic known support requirement from 3 to 7 via the critical a=3 parity mechanism excludes all hypothetical small-support examples and informs any future search. The result is exact and self-contained; it does not require proving existence or a general theorem about all k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
