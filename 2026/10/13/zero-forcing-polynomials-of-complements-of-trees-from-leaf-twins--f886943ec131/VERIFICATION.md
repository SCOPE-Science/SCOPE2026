---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independent proof reconstruction: for at least four white vertices, a first forcer v in the complement must have all the remaining whites in its tree neighborhood. Any other blue vertex has at most one tree neighbor in that remaining set (otherwise there is a four-cycle), so no second force is possible. For a nonstar there are no complement isolates; two whites fail precisely when their external tree neighborhoods coincide, which in a connected tree of this order means sibling leaves. A three-white set succeeds exactly if an external vertex sees two of the whites in the tree that are not both sibling leaves, and misses the third. Its witness count is the stated degree/leaf sum. Distinct witness centers use distinct pairs and form a five-vertex path with the white triple in alternating positions; three witnesses would form a subdivided triangle. Each unoriented four-edge path thus removes exactly one duplicate. A nonstar has adjacent internal vertices, giving a valid witness by choosing one more neighbor at one center and a third white outside its closed neighborhood, so a_T is positive. The isolated vertex of the star complement must be blue, and at most one clique vertex can be white. The path count uses a difference of squares over adjacency-list sums, giving O(n) arithmetic operations, not a bit bound. An independent bit-mask enumeration tested every white set for all 125 order-five and 1296 order-six labeled trees (4,000 and 82,944 trials); every coefficient agreed. The accompanying verify.py and verify_output.txt were inspected, not executed; the finite checks do not prove the all-orders assertion.

## originality

PASS

The supported distinct claim is the all-tree three-white classification and exact coefficient a_T (including its linear-arithmetic evaluation), not the already known minimum size, the upper coefficients implied by general formulas, the star formula, or the path specialization.

## value

PASS

The minimum-set count distinguishes tree complements that have identical order, degree multiset and minimum forcing size. The witness/overcount description gives a linear-arithmetic computation for the whole natural family, replacing subset enumeration and explaining why the four-edge path count appears.

The dated certificate retains the supplied scientific assessment, sources and limitations.
