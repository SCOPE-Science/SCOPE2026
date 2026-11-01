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

Execute `python3 verify_grassmann.py` from the directory containing this file. The checker requires Python 3 and no external packages. Its output in this package was:

```
ALGEBRAIC_PARAMETER_CASES_OK 37
INDEPENDENT_BINARY_SUBSPACE_GRAPH_OK 1395 68355
BINARY_6_3_CUTOFF 0.270530819610
ALL_CHECKS_OK
```

The checks comprise exact Fraction arithmetic for the Grassmann scheme recurrence over 37 field-order/dimension pairs, symbolic simplification of all three nonconstant eigenvalue triples (performed separately), positivity/bracketing checks, complete reduced-row-echelon enumeration of binary three-spaces in dimension six, 68,355 reconstructed adjacency edges, direct BFS/meeting-dimension distance comparison, intersection-number checks, and exact integer minimal-polynomial evaluations of the adjacency operator. Finite tests cannot prove the infinitely many field-order/dimension cases, which are established by the calculations and inequalities in `RESULT.md`. The numerical root is only an approximation. Neither independent historical originality certification nor external mathematical validation is asserted.
