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

The standalone `verify.py` artifact was read from its packaged path before replay.

It constructs the total dot product graph directly for
\[
q=2,3,4,5.
\]
Prime fields use modular arithmetic. The \(q=4\) implementation uses polynomial arithmetic in
\[
\mathbb F_2[\omega]/(\omega^2+\omega+1).
\]

For \(q=2,3,4\), every vertex subset is exhaustively tested for the zero forcing property, giving the complete polynomial. For \(q=5\), the direct component structure and predicted polynomial are checked without exhaustive subset enumeration.

For every tested field, connected components are reconstructed from the direct graph. A block real symmetric witness is built componentwise, its off-diagonal pattern is checked entry-by-entry, and exact rational row reduction verifies the claimed rank.

Exact replay output:

```text
q=2: |V|=3, components=[1, 2], polynomial={2: 2, 3: 1}, witness_rank=1
q=3: |V|=8, components=[4, 4], polynomial={4: 16, 5: 32, 6: 24, 7: 8, 8: 1}, witness_rank=4
q=4: |V|=15, components=[3, 6, 6], polynomial={10: 243, 11: 405, 12: 270, 13: 90, 14: 15, 15: 1}, witness_rank=5
q=5: |V|=24, components=[4, 4, 8, 8], predicted_polynomial={18: 4096, 19: 6144, 20: 3840, 21: 1280, 22: 240, 23: 24, 24: 1}, witness_rank=6
VERIFY_OK
```

The finite checks are corroborative only. The general theorem follows from the projective-line orthogonality involution and the componentwise proofs in `RESULT.md`.
