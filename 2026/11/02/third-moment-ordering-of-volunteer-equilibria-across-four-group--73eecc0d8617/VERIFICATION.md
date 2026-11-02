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

# Mathematical and computational verification

The exact payoff difference is derived directly from the one-volunteer rule. The proof of the all-parameter comparison relies on the rank-three four-node moment matrix and the strict sign of a third divided difference of an exponential in the group size. The two explicit examples use rational group-size weights and have been evaluated algebraically. The independent study of historical priority is not part of this verification.

To replay the computational evidence, run `python check.py` with Python 3.9+ and no external packages. Expected output:

```
PASS: 2330 exact-rational assertions; 210 ordered four-size support choices; two explicit sharp examples.
```

The script checks barycentric identities, sample strict generating-function inequalities, all stated moment identities, and the exact four- and five-size crossing examples. Only the analytic proof establishes universal support spacing, every interior frequency and every permitted benefit–cost ratio; finite sampling cannot do so. Source limitations and alternative formulations are recorded in `REVIEW.md` and `AUDIT.json`.
