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

# Computational verification

Run `python3 verify.py` with the Python standard library. The script enumerates all Dyck words of semilengths 1 through 12, compares the greedy index against a separate explicit subsequence test through semilength 8, and checks the sharp height bound, complete near-maximal normal form, exact counts, and sharp witnesses.

Observed output:

```text
DYCK_UNIVERSALITY_PASS dyck_cases=290511 direct_subsequence_crosschecks=2055 semilengths=1..12 near_max_bijection=PASS sharp_height_bound=PASS
```

These are finite tests, not an infinite proof. The mathematical proof is in `RESULT.md`; there is no external or independent audit.
