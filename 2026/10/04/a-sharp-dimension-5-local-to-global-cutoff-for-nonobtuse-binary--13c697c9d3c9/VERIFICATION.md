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

Run `python3 verify.py` in the same directory as this file. The verifier uses only exact integer and rational arithmetic.

It checks the complete origin-normalized search spaces for dimensions \(3\), \(4\), and \(5\). For each candidate it tests every tetrahedral face by the inverse-Gram sign criterion, discards affine degeneracies exactly, and then tests the full simplex. The expected local counts are \(17\), \(150\), and \(1872\), with zero global failures. The corresponding unrestricted counts are \(34\), \(480\), and \(9984\).

For the dimension-six witness it checks the exact Gram matrix, determinant \(64\), exact inverse, failure of the global nonobtuse criterion, and nonobtuseness of all \(35\) tetrahedral faces. It also records the six positive off-diagonal inverse-Gram positions and the three negative row sums that witness obtuse incidences.

Successful replay ends with `VERIFY_OK`.

## Limits
The computation is exhaustive only for binary simplices in dimensions \(3\) through \(5\). Dimension \(6\) is not exhaustively classified; only the displayed counterexample is certified. The computation does not establish any claim in dimensions above \(6\).
