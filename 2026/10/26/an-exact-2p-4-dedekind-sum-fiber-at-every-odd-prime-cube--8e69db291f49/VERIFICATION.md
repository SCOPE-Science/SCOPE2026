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

Independently checked the three-term Rademacher–Dieter relation in the orientation S(A,B)=S(C,D)+S(R,Q)+(B²+D²+Q²)/(BDQ)−3, Q=AD−BC>0 and Bézout −CJ+DK=1. First taking (A,B,C,D)=(j+1,p,j,p) relates S(j,p), S(j+1,p), S(k,p). The bridge via H=p(p−1), CRT r≡j^−1 mod p and r≡−1 mod p−1, h=(r+1)/(p−1), yields a constant S(j,p)+S(r,H). The final (A,B,C,D)=(p−1+jp²,p³,j,p) gives the target, and inversion produces the second progression. For a candidate a matching witness c, Girstmair/Jabuka–Robins–Wang fractional congruence (a−c)(ac−1)≡0 mod p³ first forces a≡−1 mod p and then lifts to u≡±1 mod p when a=−1+pu: exactly 2p candidates. Four endpoints (two inversion pairs) are excluded by exact reciprocity with deviations ±(p²−1), leaving 2p−4; each candidate class is handled. Independently evaluated the original *sawtooth definition*, not a reciprocity-based checker, for every reduced a at p=3,5,7,11; entire computed fibers agree and have sizes 2,6,10,18. These finite cases corroborate rather than establish the every-prime proof.

## originality

PASS

Girstmair 2014 full primary arXiv:1404.4428v1 Corollary 2 classifies deeper prime-power strata r≥k/2, and explicitly notes the lack of analogous result at 1≤r<k/2. The current p³ r=1 fiber is in that shallower range, has a different target value and is not a rephrasing of the deep formula. Girstmair 2013 supplies congruence for *fractional part* coincidences, which is necessary but not sufficient for exact equality: four endpoints obey congruence yet differ by ±(p²−1). Girstmair 2021 provides the general three-term identity used, but not this fiber. Exact count 2p−4 has distinct content from a construction of pairs or from congruence counts. Qualified PASS given incomplete unindexed priority and older equality literature.

## value

PASS

Full equality fibers of normalized Dedekind sums at prime-power modulus are an established arithmetic classification problem. This gives one complete explicitly natural prime-cube equality fiber in the first shallower stratum beyond the known deep-layer theorem, with exact explicit progressions and exclusions for all odd primes. It is not an unmotivated finite special case, and it does not pretend to solve maximal multiplicity or classify every fiber.

The dated certificate retains the supplied scientific assessment, sources and limitations.
