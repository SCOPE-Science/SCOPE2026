---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The standalone pure-Python `checker.py` has no third-party dependencies. Run it with `python3 checker.py`. Its checked finite fields have orders \(2\), \(4\), and \(8\), represented by irreducible binary reduction polynomials; field multiplication is independently implemented with polynomial reduction. The code enumerates all vertex vectors and all target edge-label vectors in 24 graph/field configurations. It derives the predicted fiber separately using nonzero-support components, root propagation, and independent-set enumeration. It also checks the claimed square-image cardinality through a distinct vertex-subset/bipartite-component count, and checks the identity fiber against the independent-set count. For small instances the actual group multiplication is evaluated directly, including all central coordinates.

Recorded execution result: `ALL_EXACT_SQUARE_FIBER_CHECKS_PASSED 24`.

Concrete triangle over \(\mathbb F_4\): actual targets with nonzero fibers number \(37\); the central square fibers have sizes \(640\) (the zero target), \(192\) on each of nine single-edge nonzero targets, and \(64\) on each of twenty-seven all-edge nonzero targets. Their weighted sum equals the group order \(4096\).

The checker is finite verification only. The proof separately establishes the square identity, exact support restrictions, multiplicative-kernel cardinalities for every connected graph in every even field, and disjointness of endpoint-support strata. Source comparisons are limited to inspected cited works and available searches; an unindexed equivalent statement remains possible. No independent mathematical audit has been performed.
