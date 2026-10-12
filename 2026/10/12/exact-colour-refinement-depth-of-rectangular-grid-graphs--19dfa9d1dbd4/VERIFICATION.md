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

# Reproducibility and boundaries

The pure-Python companion \(\texttt{grid_depth_check.py}\) requires Python 3.9 or later and only its standard library. Invoke \(\texttt{python3\ grid_depth_check.py}\). Expected output:

```
GRID_DEPTH_VERIFIED 539 cases, 147224 total tested vertices
WALK_MOMENT_ORBIT_VERIFIED 539 cases
Parameters: 2 <= m <= 23 and m <= n <= 36
```

The checker constructs all four-neighbour grids in the indicated parameter rectangle, performs the refinement partition sequence from the uniform colour, checks the least stable round and complete reflection/axis-swap orbit classes, and independently computes exact adjacency-walk-count signatures through the predicted round. It does not assume the theorem in its refinement algorithm (the predicted formula is checked against the independently computed stopping round). All counts are integer and there are no random seeds or floating-point tolerances.

The formal proof in RESULT.md treats arbitrary grid dimensions; finite enumeration supports but does not replace it. No independent external audit has been performed.
