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

Execute with Python 3 (standard library only):

```
python3 verification/verify_descendants.py
python3 verification/verify_moments.py
```

The programs independently enumerate actual deletion vectors and residual multisets, then assert the proposed exact shape/histogram and rational moment expressions. They check 38,665 composition centers for the three-deletion distribution and 24,505 for moment identities. The exact inputs, loops, assertions and output are contained in these standalone files and their two output transcripts. Mathematical proof of unbounded cases is given in RESULT.md, including a hypergeometric CLT and a fourth-moment concentration argument for the variance asymptotic. No independent mathematical audit has been performed.
