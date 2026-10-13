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

# Reproducible verification
Run `python3 artifacts/verify.py` from the finding directory with Python 3 and only its standard library. The checked input maps are reconstructed directly from their definitions. A forward breadth-first search over all reachable subsets from the complete state set independently computes the shortest reset length, including the nonsynchronizing case, for each integer \(2\le n\le19\). An independent forward image evaluation checks each displayed odd-order witness through \(n=151\). Direct set-comprehension inverse images are compared to the cyclic-interval inverse formula, and all potential inequalities are checked for odd sizes \(5\le n\le101\).

Successful invocation of the embedded file yielded:

```
VERIFY_OK bfs_n=2..19 bfs_cases=18 witness_odd_n=3..151_count=75 inverse_potential_edges=347214
```

These calculations are finite. The proof of unbounded validity is the symbolic one-step potential inequality, plus the explicit witness word, not this finite enumeration. The test does not independently certify scientific priority; that evaluation is documented separately.
