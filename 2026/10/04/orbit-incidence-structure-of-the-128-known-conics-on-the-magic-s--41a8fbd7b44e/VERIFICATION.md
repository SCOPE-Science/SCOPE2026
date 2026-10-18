---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The Auel--Singer full arXiv HTML Sections 1.2,1.3,3.1 and Proposition 4.4 confirms automorphism subgroup S of order 256 and D4 factor 8, singular point orbits 128/64/64, and two 64-conic diagonal families with b^2+c^2=2a^2. For canonical C0=[a:b:c:c:a:b:b:c:a], sign stabilizer has 2^3/2=4 elements and S orbit 64; a square reflection interchanges diagonal families, yielding full 128-conic orbit and stabilizer 2048/128=16. Trivial all-squared-equal classes [1:±1:±1] yield exactly 4 points. Independently calculated 6x6 Jacobian minor from six source-derived quadrics via symbolic differentiation and determinant: -6^6 a^2 b^2 c^2. The only potentially singular positions are a=0,b=0,c=0, each giving two projective points; published node orbit patterns assign the split p3=2, p1=4, p2=0. Uniformity plus exact double count gives incidences 2,4,0,4 for the 256 trivial,128 p1,64 p2,64 p3 points. The conic claim does not assert all conics are known.

## originality

PASS

Auel--Singer provide the 128 conics, automorphism group, point-orbit data and discuss incidence of components of the larger nondistinct locus, including their intersections at trivial or singular points. The inspected Section 3.1 and Proposition 4.4 do not give this conic-transitivity/stabilizer theorem or the uniform per-point incidence multiplicities. The work is an additional explicit orbit-incidence computation from known ingredients, not the discovery of the conics.

## value

PASS

Converts a known finite collection of geometric curves into one transitive orbit with exact stabilizer and a uniform node/trivial-point incidence structure. These numbers are natural geometric incidence invariants, potentially useful in lattice, divisor or curve-intersection calculations; the result explicitly avoids claiming a census of all conics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
