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

For sorted x<=y<=z and 6/7<q<1, x is 2 or 3. Bounding the two remaining terms by 2/y leaves only (x,y)=(2,3),(2,4),(2,5),(3,3); using the two strict inequalities gives respectively z=7..41, 5..9, 5..6 and 4..5. In the first branch cancellation of both negative valuations in 5/6+1/z requires z=6k with gcd(k,6)=1 and then 5k+1 divisible by 6. This needs k=1 mod 6, impossible for 2<=k<=6. In the second branch cancellation at 2 requires v2(z)=2 and no z in range qualifies. The last two branches give only 9/10, 13/15 and 11/12. Conversely any totient ratio >6/7 has all prime factors of n at least 11 by the product formula; its reduced denominator divides rad(n) and is prime to 6, excluding all four branches. A ratio of exactly 6/7 requires 7|n by the reduced denominator, and the factor for 7 already equals 6/7, excluding any other prime factor. The witness 1/2+1/3+1/42 works for every 7^k and disproves the weak-threshold implication for every c<=6/7. Thus the set is (6/7,1] with unattained infimum. The n>=2 restriction is necessary, and the exhaustion permits repeated denominators.

## originality

PASS

The supported distinct contribution is the exact all-integer threshold, using a denominator obstruction that applies to composite prime supports as well as prime powers. The displayed equality representation is credited to Mandal; the equality locus is then a short, necessary Euler-product argument. No inspected statement or documented implication covers all n with the same threshold. This is a best-of-knowledge judgment, not a priority certification.

## value

PASS

This is a natural exact cutoff in the three-term totient-ratio problem: it decides the strongest uniform exclusion, distinguishes the attained endpoint from the strict exclusion interval, and gives a residue-based obstruction independent of the size of n. The uniform passage from prime powers to arbitrary prime support is substantively useful; the equality witness by itself would not be.

The dated certificate retains the supplied scientific assessment, sources and limitations.
