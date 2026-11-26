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

In {e,R}, cancellation reduces nontrivial atoms on e,x,y to equality, x²=e, y²=e, x²=y, y²=x, or xy=e (equivalently yx=e). A two-round back-and-forth therefore compares sets of achievable second-move signatures at each first move, and then the sets of those profiles. The special second values e,x,x^{-1},x² depend on the stated order categories. For n>=5 the coordinate flips and positive three-cycles provide the two generic nonsquare-root signatures outside all special values; an order-three x has a nonspecial root -I x^{-1}, and all roots of other nonidentity orders lie outside the special values. Square status is visible by the existence of y²=x. Squaring negative cycles of odd length removes their sign; doubling a cycle of even length splits it into two equal signed types, and interlacing pairs reverses that operation (cycle signs can first be normalized by diagonal conjugation). Thus an order-four square needs two negative 2-cycles or two positive 4-cycles; in degree at most four the only exceptional paired types fitting are length-one negative pairs and length-two pairs, with remaining positive odd cycles of length at most three, so no square has order at least five there. The witnesses in the table attain all eight signatures by degree five and persist upon adding positive fixed coordinates. The four separating sentences have rank at most two even when there are two independently bound inner variables, so all five classes are distinct. An independent NumPy replay on the full action on signed letters, with every ordered pair of elements at n<=5 and no conjugacy reduction, found distinct profile-set sizes 2,4,6,7,8 and the stated categories at five. The all-degree argument is structural.

## originality

PASS

Credit the signed-cycle square criterion as known: Kundu–Mondal Proposition 4.3 for prime powers in G wreath S_n yields it verbatim at G=C_2 and exponent 2. Related work also gives the same eight candidate profile types for symmetric groups. The distinct supported result is their exact realization and resulting five-class threshold in B_n with the stated signature; no inspected result covers that family theorem.

## value

PASS

The family is a classical Weyl-group series. The result gives the exact low-rank logical stabilization and tells which sharply different relabeling-invariant element types a two-move game detects. The signed order-four square is a concrete reason the threshold differs from symmetric groups, rather than a restatement of the known signed-cycle square lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
