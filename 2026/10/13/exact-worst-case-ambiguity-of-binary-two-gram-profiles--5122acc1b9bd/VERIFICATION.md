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

# Reproducible checks and limits

The mathematical argument is in `RESULT.md`. Its core run-composition identity and strict ratio comparisons prove the claim for every binary word length \(n\ge3\). There is no finite-only inference of the infinite result.

Run the attached programs with Python 3 from the directory containing this file:

```
python3 verify_bruteforce.py
python3 verify_profiles.py
```

The first checks by explicit binary word enumeration every length from 3 through 18, including the complete set of maximizing profiles and partition-size sum. The second checks all nonnegative four-count vectors for lengths 3 through 80, using the independent composition-count formula and again checking the exact mode set and that total fiber size is \(2^n\). Both printed `PASS` when executed from extracted package files.

No independently performed audit has been supplied. The computations do not establish originality and do not replace the symbolic all-length proof; inaccessible historical literature remains a residual originality risk.
