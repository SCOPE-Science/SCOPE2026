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

The proof uses the elementary equivalence between a nonresolving set and a subset of a distance bisector, plus the independent per-coordinate three-atom distribution. The single-coordinate, binary-pair, and ternary-support equality cases are classified explicitly; all infinite-parameter assertions depend on this proof, not finite extrapolation.

Reproduction: from the directory containing `verify_bisectors.py`, execute `python3 verify_bisectors.py`. The program requires only the Python standard library. It directly enumerates all vertex pairs of each listed finite Cartesian product, independently recomputes pairwise distances, obtains distinct largest bisectors as integer bit masks, and verifies both their cardinality and their count. Its final success line is `VERIFY_OK`; failures raise an assertion.

Test scope: all one-factor orders \(2\) through \(7\); all two-factor combinations of sizes \(2\) through \(6\); 22 specified mixed products with three to five factors. This test suite does not enumerate arbitrarily many dimensions and is not an independent external audit. Scientific limitations and related literature are described in the result and review.
