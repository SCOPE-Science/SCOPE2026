---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Every cubic through the 15 rational points is an alternating Frobenius cubic; smoothness of a (3,4) complete intersection forces its 4x4 alternating matrix full rank, hence 28 possible cubics and Sp4(F2) stabilizer of order720 for a fixed one. Quartic vanishing sections modulo G times linear forms form F2^16. Independently built 35-monomial evaluation kernel, dimension20, quotient dimension16, and traversed all 65536 classes via 15 symplectic transvections: 128 orbits, 288 classes smooth at all rational points in exactly two size-144 orbits, reps 13387 and 13394. Exact four-chart Groebner ideals in characteristic2 show 13394 geometrically smooth and 13387 singular; the packaged degree-five singular point further witnesses exclusion. Thus 28*144=4032 smooth embedded ideals in one orbit; stabilizer order720/144=5 cyclic. Independent symbolic reduction verified G and F vanish at all 15 rational points, A of order5 preserves G and F modulo G. Its irreducible degree4 characteristic polynomial Φ5 gives four fixed eigenlines; homogeneous eigenvalue scaling forces their incidence with C. Tame RH with genus19 and four totally ramified points gives quotient genus3. Exhaustive finite computations cover the precisely finite domain; not all fields or all types.

## originality

PASS

PASS for unique projective class and cyclic projective automorphism/quotient structure, while explicitly crediting the original minimal-degree construction and earlier count of 144 smooth quartic sections on one cubic. Neither a count of smooth sections nor an existence example alone implies transitivity or ramification.

## value

PASS

Complete classification of minimal-degree binary projective complete-intersection space-filling curves is a natural finite moduli problem. An exact unique orbit, its C5 stabilizer and genus-three quotient give structural geometry beyond a known finite tally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
