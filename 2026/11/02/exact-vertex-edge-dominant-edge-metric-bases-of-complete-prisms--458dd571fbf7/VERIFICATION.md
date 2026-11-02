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

# Verification protocol

Run `python3 verification/check_basis.py` in the directory containing RESULT.md. The script requires only the Python 3 standard library. It constructs each graph from edges rather than using the symbolic proof's edge-distance formula. For every \(2\le n\le11\), it computes graph distances by breadth-first search, compares each pair of distinct edges, requires one selected vertex within distance one of each edge, and enumerates **every** vertex subset of the theorem's asserted minimum size. Each candidate is compared with the structural classification before exact counts are checked.

The resulting output is:

```
n=2: minimum=2, bases=4, checked=6
n=3: minimum=3, bases=14, checked=20
n=4: minimum=4, bases=50, checked=70
n=5: minimum=5, bases=182, checked=252
n=6: minimum=6, bases=532, checked=924
n=7: minimum=6, bases=140, checked=3003
n=8: minimum=7, bases=560, checked=11440
n=9: minimum=8, bases=1638, checked=43758
n=10: minimum=9, bases=4200, checked=167960
n=11: minimum=10, bases=10032, checked=646646
VERIFY_OK: full candidate-space verification at minimum sizes n=2..11; graph-theoretic BFS and independent edge comparisons
```

The proof that smaller sets cannot qualify is structural: every edge resolver must meet all but at most one matched column, and the local collision conditions exclude every size-\(n-1\) candidate when \(n\le6\). Finite enumeration is not used as an infinite proof. No independent mathematical audit has been performed.
