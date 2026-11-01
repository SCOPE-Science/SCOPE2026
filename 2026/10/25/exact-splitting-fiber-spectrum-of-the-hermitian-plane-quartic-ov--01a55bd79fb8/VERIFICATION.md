---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The homogeneous quartic Y^3 Z+Y Z^3=X^4 has no singular projective points over characteristic three (partials -X^3,Z^3,Y^3), so genus three. The explicit quotient F3[t]/(t^6+t+2) is a field, as all 728 nonzero elements are invertible. Independent C++17 field and projective-line enumeration of the actual finite domain recovered 892 rational curve points, 532171 projective points/lines, exact line intersection histogram 0:158760,1:175420,2:158112,4:39879 and all 17 asserted exterior N(P) frequencies summing to 531279. It independently checked N=222 exactly on the 63 F9-rational exterior points; global table confirms exactly 63 such maximizers. No 3-secant occurs, and every exterior projection pencil is basepoint-free degree 4. This is a finite exhaustive computation, unlike extrapolating finite tests to infinitely many field sizes.

## originality

PASS

The 892-point arc completeness over F729 was already known by an earlier finite computation and is NOT a novelty claim. The complete 17-level exterior four-secant/split-projection-fiber distribution, minimum 25 and precise 63-point subfield maximum are strictly stronger arithmetic data not given by the inspected Hermitian arc completeness paper. Best of knowledge with a serious residual risk of unpublished original Magma output containing the census.

## value

PASS

Completely split fibers of degree-four projection maps of the canonical genus-three Hermitian quartic are a natural finite arithmetic statistic. The complete 17-valued exterior spectrum, sharp minimum 25 and exactly identified F9-rational maximizers refine a known yes/no completeness statement, producing exact data for projective arc theory and splitting properties. The finite one-field problem is mathematically motivated in its own right; a uniform q theorem is not required for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
