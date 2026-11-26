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

The frozen deterministic area intervals and threshold are correct, but the claimed positive Haar measure at each fixed interior q is false and the boundary counts are underspecified. The complete repaired RESULT and diagnostic classify this boundary and distinguish positive arc length, zero Haar area on the exact fiber, and positive Haar area in open q-neighborhoods of either strict chamber. Re-audit: Cauchy's facet sum gives max(a+b+c,2c) for sorted nonnegative unit-normal coordinates. Central symmetry permits centering the inball, and polarity makes r^{-1} the greatest norm on the central cube section. Intersecting the section with the cube edges yields q=(a+b)/c in the dominant chamber and q=(c−a)/b in the triangle chamber (the two displayed cross-products establish the latter ratio is greatest). The continuous parameter intervals are exhaustive. The quadrilateral area decreases with its imbalance, giving Q_− and Q_+; the triangle area has derivative sign q²−q−2t+2, maximum at 1+(q²−q)/2 and smaller endpoint at t=1−q. The cross-band squared difference Q_−²−H_+² has numerator 2(1−2q²−q⁴); the other squared comparisons order the exterior endpoints. Equality is at q=r=√(√2−1), area 2^(3/4). The two orientations at q=0 give the asserted two areas (up to symmetry). The projected relation a p_1+b p_2+c p_3=0 proves which points are extreme; at q=1 one signed pair lies on the diamond boundary and the remaining four points are extreme, including the coincident-pair endpoint. Smooth one-dimensional q-fibers establish the corrected Haar statement. The changed diagnostic explicitly uses the dominant formula at equality and tests the symmetric boundary normal; the proof is independent of this diagnostic.

## originality

PASS

The prior two-branch pointwise radius formula and classical brightness formula are explicit inputs, not claimed as new. The closest earlier computed area law conditions on the size of the largest absolute normal coordinate; the same-day cube-shadow joint law changes both observables. Neither computes the fixed-inradius extrema or the exact boundary-overlap polynomial. Finch gives, in addition to marginals, a mixed area–perimeter moment, not the claimed area–inradius feasible set. The repaired literature paragraph accurately credits this. The surviving content is the evaluated pair of area ranges and exact classification transition, not the availability of a coordinate representation from which one can optimize them.

## value

PASS

The exact joint constraints answer a natural inverse question about identifying a silhouette with two Euclidean measurements. A genuine forbidden interval and its sharp contact give a simple limit to identification; beyond the contact, both polygon types realize the same measurements. This requires the full attainable set, not a conjectured bound, separate moments or a few arbitrary fibers. The repaired Haar clarification does not add an unproved probabilistic contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
