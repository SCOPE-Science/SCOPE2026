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

# Reproducing the finite calculation

Place `check.py` and `certificate.json` together and run `python3 check.py` (standard Python 3 only). The independent certificate check verifies that every listed function signature is derived by an allowed operation from earlier entries and that the resulting full sets are closed under all allowed operations. It then recomputes the nonmodal and one-modal-depth closures by a distinct enumeration routine.

Expected output:

```
EXACT_CLOSURE box 60 all_derivations_and_operations_valid
EXACT_CLOSURE diamond 342 all_derivations_and_operations_valid
GODEL_ONE_WORLD_FRAGMENTS_EXACT_OK 60 342
DEPTH_ONE_NORMAL_FORM box 6 60 sharp
DEPTH_ONE_NORMAL_FORM diamond 6 342 sharp
```

All numbers and identity checks use exact integer coordinates, not floating point. The complete eleven-case reduction is proved in `RESULT.md`; the attached enumeration certifies its finite consequences. This is a self-review finite verification only, not independent expert or formal-methods validation. No claim is made for unrestricted multiworld models.
