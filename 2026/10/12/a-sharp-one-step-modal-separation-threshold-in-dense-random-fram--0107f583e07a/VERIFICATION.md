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
# Reproducibility

Execute `python3 verify.py` using standard Python 3. The program exhaustively verifies the depth-one type criterion across every simple labeled undirected graph on at most four vertices and all color maps to alphabets of size two or three: 6,519 configurations. It compares each vertex pair's color/neighbor-palette signature against an independently constructed family of Boolean color-union formulas and their diamonds. Six small exact computations check the identity for the expected number of missing vertex/color incidences at edge probability one-half. Nine seeded examples report the number of distinct depth-one signatures and neighborhood-saturated vertices.

An observed successful replay printed:

```
EXHAUSTIVE_DEPTH1_OK 6519
EXACT_MISSING_COLOR_MEANS_OK 6
SEEDED_EXAMPLES [(300, 0.22, 12, 12, 300), (300, 0.75, 39, 187, 138), (300, 1.55, 82, 300, 0), (650, 0.22, 22, 22, 650), (650, 0.75, 75, 468, 230), (650, 1.55, 156, 650, 0), (1100, 0.22, 35, 35, 1100), (1100, 0.75, 118, 863, 282), (1100, 1.55, 243, 1100, 0)]
VERIFY_OK
```

The asymptotic zero-one threshold is proved analytically using occupancy Poissonization and a union bound. Finite simulation alone cannot establish an infinite limiting statement. The theorem makes no claim about the critical limit or unrestricted modal-depth behavior in the low-alphabet regime.
