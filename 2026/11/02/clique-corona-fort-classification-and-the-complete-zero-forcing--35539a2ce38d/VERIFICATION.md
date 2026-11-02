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

# Reproducible checks

Run `python3 VERIFY.py` with Python 3.10 or newer; it requires only the Python standard library. It reconstructs base adjacency from labeled edge-bit masks, attaches private complete graphs, enumerates vertex subsets and independently computes the forcing closure and minimal-fort predicates. It compares the exact complete coefficient distributions to the separate uniform/mixed generating-function formulas. The test includes all graphs of orders one through four, mixed clique sizes, uniform orders two and three, and seven examples with five original vertices.

Actual completed output:

```
VERIFY_OK: 104 graph-corona instances, 537504 direct vertex subsets; uniform and mixed clique sizes; all zero-forcing coefficients and all minimal-fort coefficients
```

The program checks formulas on a finite list only. The general result is proved in `RESULT.md` by graph-theoretic bijections and the fort-hitting equivalence. The checker does not determine whether an identical all-parameter theorem was published elsewhere; publication-priority uncertainty persists. The definition of standard zero forcing (unique white neighbor) matters, and sizes of attached cliques below two are outside the theorem.
