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

# Reproducible verification

Run `python3 fan_rainbow_verify.py` using a standard Python 3 interpreter. No external package, repository access, or auxiliary input is needed. The program constructs the actual fan edges, builds diamond-conflict pairs from the defining cross-edge criterion and four-cycle conflicts by a separate enumeration, and verifies their agreement for fan orders two through eight. It then compares full conflict-graph completion counts (after fixing spoke labels) with both the inclusion-exclusion sum and an independently coded state dynamic program in 20 parameter cases, and compares inclusion-exclusion against the state dynamic program in another 42 cases. Explicit minimum-palette constructions are checked at 75 fan orders. The count assertions for the first five orders in the infinite family are also tested.

Observed execution output:

`VERIFY_OK independent_cases=62 explicit_constructions=75`

The exact polynomial and infinite palette classification are proved symbolically in `RESULT.md`. Finite tests do not claim an exhaustive search over all orders or an independent mathematical audit. The relevant source date is the first arXiv submission of the motivating D-colouring paper, 2026-06-05, not its later revision date.
