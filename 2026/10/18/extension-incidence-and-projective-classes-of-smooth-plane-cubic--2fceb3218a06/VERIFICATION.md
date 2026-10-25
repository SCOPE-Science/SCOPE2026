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

The geometric-smoothness test is exact: Euler identity for binary degree 3 implies F lies in its partial-derivative ideal; absence of projective common zeros of three quadratics is equivalent to height-3 complete intersection and surjectivity (S2)^3 -> S4, 15 rows, verified by bit-linear rank. Independently enumerated all 1023 nonzero ternary binary cubic masks and found 336 geometrically smooth. Canonical XOR triple enumeration gives 5544 distinct all-smooth binary pencils; extending by h outside a given pencil requires h,h+F,h+G,h+F+G smooth, with exactly four valid h per containing net, yielding extension histogram 1680,1848,1848,168 for e=0,1,2,3 and total 6048/7=864 nets. Independently computed rational base-point incidences and obtained all 12 nonzero joint cells exactly as stated. Constructed action of 168 invertible 3x3 F2 matrices on the 10 cubics, obtaining 37 pencil orbits and stabilizer distribution 31,1,3,2 at orders 1,2,3,4. This is a finite complete enumeration certified by the exact regular-sequence smoothness equivalence, not untested geometric point sampling.

## originality

PASS

Best-of-knowledge PASS for the full 5544-pencil extension-degree/rational-base joint distribution and the 37 projective pencil orbits. Known 336 smooth forms, 5544 pencils, 864 nets and prior eight net orbits are explicitly credited; no novelty is attached to broad smooth-family existence theorems.

## value

PASS

A complete projective classification of which small-field smooth plane-cubic pencils extend to smooth nets resolves a concrete finite algebraic-geometric incidence problem. Nonextendible pencils (1680) and max-three extensions (168) are meaningful structural boundary cases, and orbit representatives make the classification reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
