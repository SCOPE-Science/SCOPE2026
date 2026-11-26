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

For a base-b pair with 1≤a≤M=b−1 and 0≤c≤M, subtracting a+c from ab+c makes the test a+c divides aM. The M pairs with c=0 all pass. For c>0 set g=gcd(a,a+c), (u,v)=(a/g,(a+c)/g). Then 1≤u<v and gcd(u,v)=1, so the test is exactly v divides M. Conversely each permitted u,v gives the distinct pairs (gu,g(v−u)) for positive g≤floor(M/max(u,v−u)), precisely the two digit bounds. There are always M−1 additional pairs with positive digits summing to M. If M=p≥3 is prime, v=p is the only option and max(u,p−u) lies between (p+1)/2 and p−1, so every summand is 1. If M is composite, a proper divisor 1<d<M gives the additional pair (1,d−1) outside the two guaranteed families. For b=2 only (1,0) works. For b=3 the pairs are (1,0),(1,1),(2,0),(2,2). The first family's proof notation (ab)_b should be read as the numeral with digits (a,0), of integer value ab; this is explicit elsewhere in the record. Reviewed VERIFICATION.md and verify.py: its check compares direct digit-pair counts and the formula for bases 2–300. An independent bounded check for 2–30 agreed as well, but the bijection and equality proof do not depend on enumeration.

## originality

PASS

The inspected all-length literature treats a fixed-base counting function, the OEIS material concerns decimal values or decimal length counts, and the closest indexed two-digit Harshad theorem fixes the integer and varies its base, rather than counting every two-digit integer per base. None of the available statements gives this exact divisor formula or the prime extremal criterion. The historical puzzle with a very close title remains an access risk, not evidence of coverage.

## value

PASS

The two-digit stratum is the first nontrivial finite stratum after all one-digit numbers and is a natural varying-base comparison. The result replaces scanning b(b−1) candidates with an exact primitive-ratio count determined by b−1, and identifies an arithmetic distinction invisible in decimal tables or fixed-base asymptotics: the two universal families are exhaustive precisely at prime b−1 from base four onward. This is a complete, usable exact classification of the lower-envelope cases, not an isolated finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
