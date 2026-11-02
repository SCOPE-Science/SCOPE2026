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
# Verification and limits

Run `python3 projective_check.py` and `python3 affine_check.py` from this directory, with no third-party packages. Each program builds an exact complete projective plane of order three, enumerates all \(715\) candidate four-point sets and \(234\) valid ovals, calculates all distances by exhaustive breadth-first search, and asserts the exact blocker/detour equivalence over all \(27,261\) unordered pairs. The first implementation uses homogeneous coordinates and determinants, the second nine affine points plus four infinity points and bit-mask incidence.

Recorded results of both executions: `PROJECTIVE_DETERMINANT_ALL_PAIRS_PASS` and `AFFINE_INCIDENCE_BITSET_ALL_PAIRS_PASS`. Both assert \(1404\) edges, degree \(12\), diameter \(4\), distance spheres \((1,12,60,114,47)\), six exceptional partners indexed by common point pairs and eight indexed by common singletons, and the full \((|A\cap B|,d(A,B))\) multiplicity table in the result.

The result is finite, exhaustive and reproducible, but not a theorem for arbitrary field orders. A self-review does not constitute independent scholarly validation; no such validation was performed. Published static classifications of arcs and blocking sets are not reproduced as new results.
