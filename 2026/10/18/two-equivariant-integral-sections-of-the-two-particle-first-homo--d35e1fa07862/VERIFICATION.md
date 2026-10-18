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
# Reproducible verification

Run `python verify.py` (requires `sympy`, see `requirements.txt`). The program enumerates the subdivided-graph cubical model directly, constructs its oriented integral square-boundary presentation, asserts the Smith invariant factors, computes the total-motion projection and the two symmetry generator actions over \(\mathbb F_2\), and solves all equivariance equations. The six input labels are not arbitrary graph instances: they describe this particular five-vertex complete graph. Its checks terminate as finite exact computations and neither prove general nonplanar graph cases nor establish novelty in unindexed literature.

Expected reported values: \(105\) zero-cells, \(260\) one-cells, \(150\) two-cells; Smith factors \(1^{149},2\); \(42\) variables and system rank \(41\); two exact equivariant sections. Assertions verify all values and equations. Any alteration to the cell structure or action must be checked afresh.
