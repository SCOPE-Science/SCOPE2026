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

# Verification and limits

The `checker.py` program uses Python 3 standard-library iteration over every anti-extensive map for \(m=1,2,3\) atomic types. It tests the exact total-class count, globally extinguishing count, the probability-one-half identity at **every** nonempty initial support, and the longest strict-update-chain census. It also independently evaluates the modal-depth-one support-indicator formula for a deterministic selection of maps. Execution command: `python3 checker.py`.

Expected and observed output:

```
m=1: maps=2, universal_extinguish=1, maximal_full_support_rounds=1; all nonempty starts extinct in exactly half
m=2: maps=16, universal_extinguish=3, maximal_full_support_rounds=4; all nonempty starts extinct in exactly half
m=3: maps=4096, universal_extinguish=189, maximal_full_support_rounds=384; all nonempty starts extinct in exactly half
ALL_CHECKS_OK
```

For \(m=4\), the value \(26{,}254{,}935\) is evaluated from the symbolic product, **not** from exhaustive enumeration of all \(2^{32}\) formula classes. The general proof uses type-support invariance, explicit definability, induction and an absolutely convergent expansion. The computation is a finite consistency check only. No independent mathematical audit or external certification is asserted.
