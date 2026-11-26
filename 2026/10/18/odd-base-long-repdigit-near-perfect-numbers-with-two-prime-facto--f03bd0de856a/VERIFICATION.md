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

Verified Ren–Chen Theorem 1.2's three classes and 40. With a=v2(N), their even forms have odd part q or q² and give N<2^(3a+2), including 40. For odd length, a=v2(d), so U_t<4d²<g^4 excludes every t≥5. For t=3, U_3 is odd, hence q or q², and g²<U_3<(g+1)² rules out a square. Then q>g>d forces d=2^a; the linear-exponent Ren–Chen forms have q<d or q<2d, the square form is impossible and 40 has odd part only 5. For t=2m≥6 the two factors U_m and g^m+1 have gcd dividing 2. For odd m, both U_m and the alternating quotient (g^m+1)/(g+1) are odd and greater than 1; for even m≥4, g^m+1 has 2-adic valuation 1 and an odd prime from g^(m/2)+1 divides U_m (it cannot divide g−1). Such a prime exists by valuation 1 for even m/2 or by the odd alternating quotient for odd m/2≥3. This gives two distinct odd primes plus 2. At t=4, gcd(g+1,g²+1) divides 2 and (g²+1)/2 is odd and >g, so g+1=2^s, s≥2. The odd part Q=(g²+1)/2 of U_4 is q or q²; no odd part can come from d by size in the prime case and exponent in the square case. Thus a≥s+1. The square form forces sqrt(Q)=2^(a+1)−1>g, impossible. For Q prime, Q≡1 mod 4 rules out the Mersenne form and forces k=1 in the remaining form. But Q+3 has valuation 2 with odd quotient >1 for s≥3, and equals 8<2^(a+1) at s=2. The sole witness has 40=1+3+9+27 and σ(40)=15·6=90; its redundancy 10 is proper and its prime support is {2,5}. No larger odd base can write 40 at length four. This is an analytic proof review; verify.py was inspected, not executed, and its bounded test is not needed for the infinite result.

## originality

PASS

Credit the earlier classification, the four-small-odd-base theorem and its already stated witness. The distinct result is the uniform exclusion in all remaining odd bases. The statement that Hasanalizade's formal Theorem 1.3 itself says fewer than three digits overpromotes wording in its discussion; the accessible preprint does omit the actual base-3 example from its small-base list.

## value

PASS

A complete classification across unbounded odd bases is a meaningful improvement over a fixed four-base sieve. The result separates the binary valuation and the odd-prime obstructions, yielding a uniform theorem rather than rechecking the known example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
