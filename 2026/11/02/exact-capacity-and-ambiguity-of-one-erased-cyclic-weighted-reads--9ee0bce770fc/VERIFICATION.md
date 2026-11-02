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

# Reproducible check

Run `python verify.py` with Python 3.8 or later; no third-party packages are required. The script implements the cyclic window sum afresh and groups observations independently of the symbolic proof. Its output includes:

```
Integer one-hole kernel checked in all coprime cases for 3 <= n <= 250
q=2 exhaustive up to length 15: PASS
q=3 exhaustive up to length 10: PASS
q=4 exhaustive up to length 8: PASS
q=5 exhaustive up to length 7: PASS
PASS: 163 exact parameter cases, 2409791 source instances
```

The exhaustive finite checks cover every permissible width for \(3\le n\le15\) with \(q=2\), \(n\le10\) with \(q=3\), \(n\le8\) with \(q=4\), and \(n\le7\) with \(q=5\). They verify both exact image cardinality and maximal list size in coprime cases, and equality of the full and erased inverse-fiber partitions (by fiber-size multisets and equal image sizes) in noncoprime cases. The primitive explicit kernel identity is additionally checked for every coprime pair with \(3\le n\le250\).

These computations do not exhaust all parameter values. The all-parameter guarantee is the self-contained proof in `RESULT.md`; no external scientific audit or machine proof has been performed.
