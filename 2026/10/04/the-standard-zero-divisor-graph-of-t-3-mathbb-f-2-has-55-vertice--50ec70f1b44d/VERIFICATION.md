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

The standalone `verify.py` script reconstructs \(T_3(\mathbb F_2)\) from all six binary upper-triangular coordinates.

Checks performed:

- Enumerates exactly \(64\) ring elements.
- Finds units by brute-force two-sided inversion among all 64 matrices.
- Cross-checks the unit set against the diagonal criterion.
- Verifies every nonzero nonunit has a nonzero one-sided annihilator.
- Verifies no unit has a nonzero one-sided annihilator.
- Constructs the underlying simple graph using \(AB=0\) or \(BA=0\) for all \(1485\) unordered pairs.
- Runs exact breadth-first search from every vertex and checks connectivity.

Observed output:

```text
VERIFY_OK
ring_elements=64
units=8
nonzero_zero_divisors=55
underlying_simple_edges=420
diameter=2
```

Limits: this verifies the corrected standard host graph and its vertex/edge/diameter census. It does not compute the fault-tolerant metric dimension or edge metric dimension of the corrected graph.
