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

## Reproducible check

Run `python3 verify_sierpinski2_limited.py` with standard Python 3. No external packages or data files are required.

Observed successful output:

`VERIFY_OK exhaustive_graph_cases=6 matrix_sizes=2..6 exact_counts=[(2, {1: 2}), (3, {1: 4, 2: 4}), (4, {1: 10, 2: 18, 3: 10}), (5, {1: 26, 2: 112, 3: 112, 4: 26}), (6, {1: 76, 2: 820, 3: 1760, 4: 820, 5: 76})]`

The program constructs the adjacency lists directly from the labelled graph definition. For every \(2\le m\le4\), and every \(1\le k<m\), it exhausts all vertex subsets of claimed minimum size and checks equality with all symmetric binary matrices of the prescribed row sum. For \(2\le m\le6\), it separately enumerates symmetric matrices, tests their domination constraints and validates the complementary-capacity, involution and row-sum-two formulas.

Finite enumeration does not prove an infinite claim. The general result follows instead from the rowwise lower bound, the explicit cyclic-offset constructions, and equality saturation at linking edges established in `RESULT.md`.
