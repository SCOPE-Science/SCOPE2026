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

# Verification of the maximal-clique gap theorem

Run with the Python standard library:

```bash
python verify.py
```

The checker constructs the complete quinary unit-transfer graphs for lengths 8, 9, 10, 11, 12, 15, and 20 and examines every lower and upper clique via exact rational arithmetic. It also checks every potentially nonzero one-corner boundary pattern and the exact corner-mass formula. Expected final marker: `VERIFY_OK`.

Observed checks, using code packaged with this result: `SYMBOLIC_PATTERN_CHECK_OK`; all seven finite lengths passed; final marker `VERIFY_OK`. The proof in RESULT.md establishes uniform validity for all integers \(n\ge8\), including those not enumerated. The published integer independence theorem is separately cited; the checker verifies only the new fractional-point construction and the elementary numerical separation, not that earlier theorem. No independent audit or external certification has been performed.
