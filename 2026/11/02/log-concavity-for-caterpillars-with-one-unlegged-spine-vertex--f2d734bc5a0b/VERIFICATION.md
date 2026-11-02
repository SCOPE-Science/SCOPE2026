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

# Reproducibility and limits

Execute the enclosed `verify.py` using Python 3, without nonstandard packages:

```
python3 verify.py
```

Expected last four lines:

```
EXHAUSTIVE_OK 192
TREE_DP_OK 18045
MARGIN_OK 6400
VERIFY_OK
```

The program verifies the formula against literal subset enumeration on 192 instances, against a separately implemented three-state rooted domination dynamic program on 18,045 instances, and checks the exact algebraic log-concavity margin on all 6,400 adjacent block-parameter pairs with \(1\le a,c\le80\). The verifier tests its own input examples and reports assertion failures on discrepancies. It does not enumerate infinitely many caterpillars; the proof in `RESULT.md` proves the unbounded statement.

No independent audit or external formal certification has been performed.
