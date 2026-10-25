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

# Reproduction and evidence

The proof of the infinite statement is the leaf-core/Prüfer calculation in `RESULT.md`. The included `verify.py` independently enumerates all \(n^{n-2}\) labelled trees by Prüfer words for each \(3\le n\le8\), reconstructs adjacency lists, and computes actual leaf and sibling-pair counts. It separately evaluates the claimed generating polynomial through integer allocations, checks full distributions, validates normalization and first two conditional factorial moments, and compares the exact support.

Command: `python3 verify.py` (Python 3 standard library only). Executed result: 

```text
n=3 trees=3 leaf/cherry-cells=1 PASS
n=4 trees=16 leaf/cherry-cells=2 PASS
n=5 trees=125 leaf/cherry-cells=3 PASS
n=6 trees=1296 leaf/cherry-cells=6 PASS
n=7 trees=16807 leaf/cherry-cells=9 PASS
n=8 trees=262144 leaf/cherry-cells=15 PASS
PASS: 90 independent exact table, moment, and support checks
```

The script tests finitely many sizes and does not independently verify historical novelty or an asymptotic statement; it does not replace the all-size combinatorial proof. The printed checker counts refer only to the specified finite computations. No independent audit has been performed.
