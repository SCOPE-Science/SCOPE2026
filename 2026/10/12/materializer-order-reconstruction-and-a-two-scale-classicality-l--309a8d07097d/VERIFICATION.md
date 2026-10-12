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

The embedded `verify_materializers.py` constructs the finite lattice with Boolean elements represented by bit masks and newly adjoined upper chain points represented by successive integers. It computes implication by enumerating the elements \(z\) with \(x\wedge z\le y\) and locating their unique greatest element, not by reusing the derived implication-case formulas. It separately compares each resulting materializer to the claimed set, verifies all claimed inclusions and strict inclusions, checks the number of distinct materializers and compares the exhaustive number of failures against the closed formula.

Replayed from the standalone code at its actual package path using `python3 verify_materializers.py`:

```
VERIFY_OK cases 30 material_implication_pairs 11243 materializer_orders_checked 30
```

Checked every \(n\in\{1,2,3,4,5\}\), \(k\in\{1,2,3,4,5,6\}\). This finite experiment does not certify the formulas for arbitrary parameters; the general proof is the exhaustive implication-case argument in `RESULT.md`. No independent audit or external verification is claimed.
