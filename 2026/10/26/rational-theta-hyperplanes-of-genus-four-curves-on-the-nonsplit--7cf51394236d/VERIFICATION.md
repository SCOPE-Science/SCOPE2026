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

The fixed nonsplit quadric Q in P3/F2 has exactly 5 rational points, 120 automorphisms permuting them, and a 16-dimensional cubic-section quotient (65535 nonzero classes). The full group orbit census gives 683 orbits. For every representative, the exact Jacobian-ideal Groebner unit test on four affine charts detects geometrically smooth complete intersections over the algebraic closure, not merely F2 or F4 rational smoothness; 254 smooth orbits of total weight 27060. Fifteen rational hyperplane sections consist of 10 smooth conics and 5 conjugate-line tangent conics; restriction to a conic yields a binary sextic, even-divisor iff odd exponents vanish (3 linear syndrome conditions), while tangent conics have analogous three-bit extension-field syndromes with a vertex parity condition. An independent implementation rebuilt group generators, reduced cubic action, 15 linear syndromes, exact Groebner smoothness and full weighted orbit census, reproducing bins 5680,13580,7020,320,460 and the 7 extremal orbits with weights 120,30,60,60,10,60,120. The independent implementation did not use the source certificate JSON, so the enumeration is supported by independent exact finite computation. Smoothness over Fbar is certified by algebraic ideal tests; small-extension point tests alone would not suffice.

## originality

PASS

Xarles 2020 already enumerates abstract genus-four F2 curves, split/nonsplit quadric models, source-coordinate automorphism orbits, and point counts: this prior curve enumeration is fully credited. Pacini-Testa 2020 supply characteristic-two even-divisor theta-hyperplane definitions and general geometric theory. Neither inspected relevant full-text theorem/tabulation supplies the 15 rational-hyperplane syndrome counts or the seven fixed-nonsplit extremal incidence orbits. The new claim is the extra theta incidence statistic in an explicitly fixed equation-weighted quotient, not existence or total classification of genus-four curves. An indirect calculation from Xarles' curve list is possible and is an explicit residual priority risk.

## value

PASS

The theta-hyperplane incidence profile refines the established small-field genus-four census by a natural canonical divisor invariant, giving all rational even-section multiplicities and the sharp extremal classes. The complete exact list and split of smooth versus tangent quadric sections are independently useful arithmetic-geometric data, not an arbitrary single numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
