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

Run `python verify.py` using Python 3. The program uses only exact Python integer arithmetic and the standard library. In the reviewed execution it printed:

```
PASS {'pair_cases': 16566, 'cut_checks': 32017, 'graph_cut_comparisons': 2641, 'contraction_partitions': 152, 'amplifying_partitions': 31}
```

The enumerated multipartite profiles are the unordered integer partitions of every order from two through eleven having at least two parts. Every nontrivial class-count cut is tested, and for orders at most eight the pair formula is also compared with a direct edge-by-edge derivative. Pair-inequality checks cover integers in the specified finite loops. The one-vertex strict witnesses and boundary examples are included. The mathematical proof, not enumeration, establishes the unbounded-in-order theorem. No formal proof assistant and no independent human validation were used.
