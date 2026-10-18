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

`checker.py` is a standalone Python 3 standard-library program. `checks.txt` captures its exact stdout. The program compares all six algebraic formulas to dynamic programming over the matched subsequence prefix, for every \(0\le A,B\le14\), and then independently compares the DP to explicit whole-word enumeration for \(A+B\le11\). It reports 67,500 formula/DP cells and 4,758 independent enumeration/DP cells, all matching.

The all-parameter claim rests on the direct disjoint run-form proofs in `RESULT.md`. Machine tests are finite, not a universal proof. The Gaussian-binomial denominator is justified by an area-preserving partition bijection, and the zero-letter boundary is handled separately. Research-literature comparison remains limited by unavailable full text in one particularly relevant source.
