---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

If a nonsingular binary A=BC over the nonnegative integers, all columns of B and rows of C are nonzero. Any entry ≥2 in either factor then contributes ≥2 to an entry of A, with no cancellation, so the factors are necessarily binary. This is the required reduction to a finite search. Independently, `python3 -B /workspace/reproduce_frozen.py 4` enumerates the three rank-one support rectangles for a possible binary product, requiring pairwise disjointness and rejecting the two unit-selector patterns. Empty rectangles are included, so this also supplies composite witnesses over the integers for every singular binary target. It gives 464 composites and exactly 42 remaining nonunits, split by row and column permutations into 36 shears and six complementary permutation matrices. Independent Leibniz determinants gave 338 singular matrices and precisely the six complementary permutations with absolute determinant two. The proof's support inequality also explains the two obstructions: nonsingular binary nonunits require at least four ones, and disjoint support of PQ, PV and UQ gives w(BC)≥w(B)+w(C)−3. This forbids a four-one shear product and forbids a six-one determinant-two product (one factor would already have six ones). The frozen verifier was inspected, not executed.

## originality

PASS

The supported contribution is the complete two-orbit classification for binary order-three targets in the full integer monoid, not the standard shear family or the definition of an atom. The matching-domain factorization literature examined does not give this census, and nearby Boolean, nonnegative-real and triangular results are not equivalent. This assessment is bounded by the identified full-text access risk.

## value

PASS

Order three is the first dimension permitting the complementary-permutation determinant-two obstruction, absent in the order-two binary problem. The classification does more than give 42: it distinguishes the familiar four-one shears from a second structural obstruction in ordinary integer multiplication and shows that these exhaust all binary targets. It is a sharp finite test case for studying nonnegative-integer square factorizations, not a claim for larger dimensions or for other semirings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
