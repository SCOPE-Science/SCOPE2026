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

## Reproducible verification
Run `python verify_grid.py` with Python 3; no external dependencies are needed. Actual execution returned:

```text
VERIFY_OK pointed rectangular grids: 204 instances (2<=m< n<=22)
```

For each pair, the code compares simultaneous one-dimensional Weisfeiler–Leman partitions at all rounds through \(m-1\), testing equal pointed colours at every smaller round and unequal colours at the claimed round. In parallel it iterates the graph adjacency on the degree-deficit function and checks that the pointed moment difference is zero for every \(k<m-2\) and exactly one when \(k=m-2\).

The unbounded claim does not rest on these finite tests. Its proof uses a coordinate-swap bijection of truncated quadrant walk unfoldings and an exact shortest-path enumeration; both cover every integer \(2\le m<n\). The standard correspondence with rank-bounded unary two-variable counting formulas is reconstructed within the proof. No independent audit or external formal certification was performed.
