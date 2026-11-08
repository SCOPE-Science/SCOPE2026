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

Run `python3 records_descents_verify.py` with the standard library. Expected output:

```text
PASS 248 exact comparisons, exhaustive permutations through n=9
PASS 528 total checks including exact matching-site shielding
```

These checks enumerate all permutations through \(n=9\), and all nonconsecutive index-set conditioning tests through \(n=7\); they are finite consistency tests. The all-size mathematical justification is the adjacent-swap group action and two conditional expectation calculations in `RESULT.md`. No independent audit is claimed.
