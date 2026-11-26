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

The proof covers every positive n and every even integer d>=6 (indeed, the estimates do not use evenness of d). For odd m, the reciprocal divisor tail after 1 is strictly below 2^(-d): after rescaling compare to the d=2 tail, and bound the latter by the strict convex midpoint integral over t>=1/2. For even m the divisor 2 forces at least 2^(-d). This and n^d<(n+1)^d rule out odd n. With u=2^(-d), v=3^(-d), the divisors 2 and 3 contribute exactly u and alpha(n)v to the difference of the two normalized sums. After those terms the tails are each in [0,1.8u^2] by the integral test. The log estimate therefore bounds the error in D=log(R_d(n)/R_d(n+1))=u+alpha v+eta by 3u^2, including alpha=0. At a collision D>0 and n=1/(exp(D/d)-1). For y>0, 0<1/y-1/(exp(y)-1)<1: the right inequality is immediate for y>=1, and for 0<y<1 follows from exp(y)<1/(1-y). Thus replacing n by d/D costs less than 1. Expanding the reciprocal once with its exact quadratic remainder gives the stated centers, with the normalized total error strictly less than 23449/5190<5 by monotone rational bounds at d=6. The count of candidates follows even if intervals overlap; no existence claim is made.

## originality

PASS

The identified neighbors are results on constant-run lengths, a separate weighted function built from the ordinary divisor sum, or low-exponent/low-factor-count problems. No examined source gives or implies the mod-3 refined, uniform O(d)-width localization in the asserted even-exponent regime. This is a bounded finding about existing coverage, not a priority certification.

## value

PASS

This is a height-independent reduction of an unbounded arithmetic collision problem to O(d) candidate integers per exponent. The mod-3 correction changes the center by an exponentially growing amount, so the narrow uniform windows are not a routine consequence of the leading d2^d estimate. The statement is useful for exact collision testing without asserting nonexistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
