---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Seceleanu's coefficient triples at c=3 match the 21 frozen line equations, up to normalization. Independent evaluation of those normalized line triples on P²(F_7) confirms incidences 0:8, 3:28, 4:21 and selects exactly the off-conic points; intersections of two F_7 lines are automatically rational. The nonzero squares are 1,2,4 with sum zero, and −1 and −2 are nonsquares, proving the exact separation by G. The four lines y²=4x² or y²=2x² in the quartic T each give two distinct points on Q: on x=1 the complementary z² is respectively 2 or 4. The eight points therefore form the reduced complete intersection (Q,T) by Bézout. The Frobenius minors of the 2-by-3 coordinate/Frobenius matrix give the radical all-point ideal J, with Hilbert–Burch shifts 9 and 15. Since G is nonzero exactly on the conic points, the colon J:G is (Q,T). The multiplication sequence gives Hilbert numerator 1−3t^8+t^11+t^13. Independently I used normalized representatives (1,y,z),(0,1,z),(0,0,1), removed Q=0 and reduced the monomial evaluations modulo seven in each degree 0 through 11. Their ranks were 1,3,6,10,15,21,28,36,42,46,48,49. For d≥11 a linear form avoiding all 49 points after scalar extension propagates full rank by diagonal rescaling; base extension does not change rank. This proves equality with the candidate ideal in all degrees. The three independent octics and separating nonic are minimal, and Hilbert–Burch for the saturated reduced point ideal forces the asserted shifts 9,11,13.

## originality

PASS

The configuration, exceptional prime, octics, and need for further generators are documented already. The new supported content is identifying the extra generator as exactly one nonic, giving it explicitly, and proving that this gives the full minimal resolution. The strongest inspected same-object results stop at identifying the gap or studying different invariants; the standard residual argument only turns a justified separator and ideal comparison into the graded data.

## value

PASS

The missing presentation is a specific previously recognized obstruction in the exceptional Klein arrangement, not an arbitrary small finite-field example. The explicit polynomial makes the reduced ideal available for further exact algebra, and the resolution explains how the exceptional generator changes the nonexceptional picture. The incidence enumeration alone would not provide this contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
