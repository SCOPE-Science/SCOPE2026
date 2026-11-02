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

# Reproduction and limits

Run the packaged file `bridge_peak_verifier.py` with Python 3 in the same directory. The program uses only standard-library exact integers and rational arithmetic. During the reported execution it printed:

```
PASS: exact assertions = 3707
PASS: enumerated bridges = 66196
PASS: all prescribed-return subsets through n=7; unconditional and conditional moments through n=9; closed-form identities through n=80
```

The theorem covers every integer \(n\ge2\); the tests cover only the stated finite values. Its unbounded correctness relies on the explicit block-conditioning and generating-function proof in `RESULT.md`. No independent validation has been conducted, and no claim of machine verification for all \(n\) is made.
