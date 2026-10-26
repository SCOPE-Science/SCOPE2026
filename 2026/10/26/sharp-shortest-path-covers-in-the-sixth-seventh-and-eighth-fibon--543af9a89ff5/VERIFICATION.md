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
# Verification notes

The complete witness file `geodesics.json` is part of this package. From the same directory run `python3 verify.py` with standard Python 3. No network or optimization program is needed.

Replayed finite checks:

```
n=6 vertices=21 edges=38 geodesics=8 union_edges=38 extreme_coordinate_edges=8
n=7 vertices=34 edges=71 geodesics=13 union_edges=71 extreme_coordinate_edges=13
n=8 vertices=55 edges=130 geodesics=21 union_edges=130 extreme_coordinate_edges=21
VERIFICATION_OK
```

The replay independently regenerates all valid strings and edges in the three graphs, checks every listed vertex and step, independently calculates shortest-path distances by breadth-first search, and compares the complete edge union to the regenerated edge set. This is exhaustive for the **claimed finite dimensions** and provides no verification for larger dimensions. The original mathematical argument supplies the lower bounds and the link from these edge covers to edge general position; computational output alone is not used as an infinite proof.
