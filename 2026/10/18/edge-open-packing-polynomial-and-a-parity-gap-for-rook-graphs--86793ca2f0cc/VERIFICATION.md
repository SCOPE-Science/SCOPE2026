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

# Verification record

The standalone `verify.py` uses only Python's standard library. It constructs all rook edges explicitly, detects an incompatibility between a pair of selected edges by searching for an additional edge joining their endpoint sets, and enumerates admissible edge subsets recursively by including or excluding each candidate edge. Thus the direct counts do not assume the claimed three-component decomposition.

Command: `python3 verify.py`

Observed output:

```
VERIFICATION_OK direct_rectangles=21 enumerated_valid_edge_sets=852484 formula_max_rectangles=210
Examples: P_3,3=[(0, 1), (1, 18), (2, 45)]; P_4,4=[(0, 1), (1, 48), (2, 360), (3, 576), (4, 288)]
```

The 21 directly checked rectangles are every \(1\le m\le n\le6\). Each coefficient is compared with the explicit factorial expression, and each maximum with the parity rule. An additional formula-only sweep on every \(1\le m\le n\le20\) checks maxima and, for square boards, the separate number of optimizers. This last sweep checks algebraic consistency, not the combinatorial proof.

No finite computation proves the all-dimensions claim. Its infinite quantification rests on the induced-star equivalence, the exhaustive classification into row-column resource components, the labelled set count, and the sharp resource inequalities in `RESULT.md`.
