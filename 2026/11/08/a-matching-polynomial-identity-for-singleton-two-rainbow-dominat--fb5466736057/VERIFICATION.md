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

# Reproducibility and verification

Run `python3 artifacts/verify.py` from the extracted package root using the Python 3 standard library. The checker constructs the definition's ordered trinary labelings from scratch and checks all \(3^n\) assignments for each \(3\le n\le12\). It then reconstructs a nine-state transfer automaton independently and checks the complete polynomial coefficientwise for every \(3\le n\le60\). Finally it constructs the matching-trace/Lucas recurrence and checks both algebraic polynomial and minimum-count identities for every \(3\le n\le150\).

On the packaged source, the final lines are:

```
INDEPENDENT_NINE_STATE_TRANSFER_OK n=3..60
LUCAS_RECURRENCE_AND_MINIMUM_COUNTS_OK n=3..150
VERIFY_OK
```

No external dependencies or data files are required. These finite checks detect many indexing or algebra mistakes, but they do not establish the universal quantifier; the combinatorial count in `RESULT.md` does so. No independent external validation was performed.
