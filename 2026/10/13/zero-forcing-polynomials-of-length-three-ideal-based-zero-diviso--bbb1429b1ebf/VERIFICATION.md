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

It constructs representative ideal-based graphs directly from multiplication in
\[
\mathbb Z/(p^3)\times\mathbb Z/s\mathbb Z,
\]
exhaustively checks all forcing sets in the tested cases, verifies the rank-two witness by exact rational row reduction, and checks parameter recovery for several prime-power residue sizes.

Exact replay output:

```text
q=2, s=1: a=1, b=2, polynomial={1: 2, 2: 3, 3: 1}, witness_rank=2
q=2, s=2: a=2, b=4, polynomial={4: 8, 5: 6, 6: 1}, witness_rank=2
q=2, s=3: a=3, b=6, polynomial={7: 18, 8: 9, 9: 1}, witness_rank=2
q=3, s=1: a=2, b=6, polynomial={6: 12, 7: 8, 8: 1}, witness_rank=2
PARAMETER_RECOVERY_OK
VERIFY_OK
```

The finite checks corroborate the symbolic proof; they are not used as an infinite proof.
