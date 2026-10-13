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

It implements \(Q_{4n}\) directly from its presentation multiplication law. For each tested pair it generates the subgroup and independently checks cyclicity. For \(n=2,3,4,5\), the graph is compared edge-for-edge with the claimed decomposition. For \(n=2,3,4\), every vertex subset is exhaustively tested for zero forcing and the full polynomial is reproduced. The Gram matrix pattern and rank are checked exactly. For every \(2\le n\le10\), all at-most-one-white type profiles are tested, with exactly the all-class profile failing.

Exact replay output:

```text
Q_8: N=8, Z=5, min_sets=32, polynomial={5: 32, 6: 24, 7: 8, 8: 1}, witness_rank=3
Q_12: N=12, Z=8, min_sets=144, polynomial={8: 144, 9: 128, 10: 56, 11: 12, 12: 1}, witness_rank=4
Q_16: N=16, Z=11, min_sets=512, polynomial={11: 512, 12: 560, 13: 320, 14: 100, 15: 16, 16: 1}, witness_rank=5
Q_20: N=20, predicted_Z=14, min_sets=1600, witness_rank=6
PROFILE_CLASSIFICATION_OK
VERIFY_OK
```

The finite checks are corroborative; the arbitrary-\(n\) theorem is proved symbolically in `RESULT.md`.
