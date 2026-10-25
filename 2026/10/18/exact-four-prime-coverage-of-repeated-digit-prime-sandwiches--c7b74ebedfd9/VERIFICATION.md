---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For sandwich F(d,m,n)=dR_m 10^(t+m)+n10^m+dR_m, last digit instantly covers even d and d=5 by 2 or 5. For d in {1,3,7,9}, every prime 3,7,11,13 divides R6 and 10 has period dividing six, so F mod these primes depends only on m mod 6, t mod 6 and n mod 3003. This proves an exhaustive finite CRT decision, not a sample test. Independent direct-integer exhaustive calculation for all six length residue classes, all 3003 n residues and 24 (d,m) tests gives 273 multiples of 11 for each even t and odd classes {2499}, {231,420,759}, {651} for t=1,3,5 mod 6. Excluding 11-divisible n leaves one class per odd length. Exact counts of each odd-length decimal block give liminf 1/33033, limsup 10/33033 and logarithmic density 1/6006. Each covered sandwich exceeds its prime factor, so is composite.

## originality

PASS

Wu (2015) already introduced the sandwich problem, exhibited 231,420,759 and the even-length multiple-of-11 family and devised general repunit-factor coverage tests. This is acknowledged prior. The final claim is an exact classification of a motivated *fixed six-prime covering certificate*, including previously unlisted infinite odd-length congruence classes and sharp densities. A general finite algorithm does not by its bare statement supply the evaluated six-row residue classification, although the possibility that its tables or a straightforward specialization cover it remains a priority/value risk.

## value

PASS

The finite prime system is not chosen arbitrarily: 3,7,11,13 divide R6 and all four are necessary for the historic 231 covering; 2 and 5 handle terminal digits. Exact CRT evaluation promotes individual known exceptional cores to a positive-lower-density infinite certified family even excluding the easy 11 obstruction. This resolves the natural question of how much of the prime-sandwich obstruction these smallest repunit primes explain; it does not purport to classify every composite sandwich.

The dated certificate retains the supplied scientific assessment, sources and limitations.
