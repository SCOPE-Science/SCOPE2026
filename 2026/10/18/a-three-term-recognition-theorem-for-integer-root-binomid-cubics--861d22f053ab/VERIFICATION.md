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

If the cubic sequence is binomid, k=1 yields integral f2/f1 and f3/f1. For ordered nonnegative integer a<=b<=c, u_t=(t+2)/(t+1) strictly decreases. Bounding 1<u_a u_b u_c excludes a>=3 and b outside 0..3,1..5,2..3. Solving exact integer m=f2/f1 via c+1=K/(m-K), K=u_a u_b, gives exactly twelve admissible triples and no unbounded c escapes. Independently enumerated all candidates using rational arithmetic and checked f3/f1, leaving exactly (0,0,0),(0,0,1),(0,1,2). Their sequences n³,2n·C2(n),6C3(n) are products/scalings of binomid integer n and Pascal columns; Shapiro’s integer determinant gives all generalized binomial coefficients integral. The package’s larger finite checks are corroboration, not an infinity argument. Carefully limited to cubic split-root shifts.

## originality

PASS

Shapiro published Theorem 26 classifies degrees at most two and Open Problem 27 explicitly asks for cubic classification (full primary journal PDF and page image inspected); it provides Pascal-column sufficiency but no exclusion of other integral shifts. Caalim–Tanaka studies binomid index extension/valuations, not complete shift triples. The theorem solves the natural integer-root subfamily with a two-coefficient test and does not claim the whole open problem.

## value

PASS

This is a genuinely complete natural three-parameter subclass of the published open cubic-polynomial binomid question. A short two-ratio certificate decides infinitely many divisibility constraints by a uniform exact reduction; classifying the excluded root multiplicities is substantive beyond known Pascal-column examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
