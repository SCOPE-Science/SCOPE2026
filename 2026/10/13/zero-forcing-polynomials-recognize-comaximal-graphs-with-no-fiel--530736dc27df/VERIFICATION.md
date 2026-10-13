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

It verifies the unit-pattern quotient rank exactly through five local factors, exhausts every at-most-one-white type profile through four factors, and exhaustively enumerates all vertex subsets for \(\mathbb Z/4\), \(\mathbb Z/9\), and \(\mathbb Z/4\times\mathbb Z/4\).

It also checks the mixed unit-pattern weights for \(\mathbb Z/4\times\mathbb Z/9\) and replays the parameter-recovery algorithm on examples with repeated residue-field orders and multiple factors of residue-field order \(2\).

Exact replay output:

```text
quotient r=1: rank=2
quotient r=2: rank=4
quotient r=3: rank=8
quotient r=4: rank=16
quotient r=5: rank=32
profiles r=1: 4 forcing profiles
profiles r=2: 16 forcing profiles
profiles r=3: 256 forcing profiles
profiles r=4: 65536 forcing profiles
q=(2,), s=(2,): weights=[2, 2], N=4, Z=2, min_sets=4
q=(3,), s=(3,): weights=[3, 6], N=9, Z=7, min_sets=18
q=(2, 2), s=(2, 2): weights=[4, 4, 4, 4], N=16, Z=12, min_sets=256
mixed q=(2, 3), s=(2, 3): weights=[6, 6, 12, 12], predicted_Z=32
recover q=(2,), S=2 -> q=(2,), S=2
recover q=(2, 3), S=6 -> q=(2, 3), S=6
recover q=(2, 2, 5), S=40 -> q=(2, 2, 5), S=40
recover q=(3, 4, 7), S=168 -> q=(3, 4, 7), S=168
recover q=(2, 3, 3, 5), S=270 -> q=(2, 3, 3, 5), S=270
VERIFY_OK
```

The computations are finite corroboration. The arbitrary-factor theorem is established by the symbolic forcing, rank, and multiset-reconstruction arguments in `RESULT.md`.
