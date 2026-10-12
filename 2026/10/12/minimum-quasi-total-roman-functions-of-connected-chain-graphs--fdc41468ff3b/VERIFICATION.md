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
# Verification

The verifier generates every canonical connected chain graph of total order \(4\) through \(8\) whose two bipartition classes both have order at least \(2\). Canonical twin-class sizes range over all positive compositions compatible with a common number of classes.

For every graph, the checker enumerates every labeling
\[
f:V(G)\to\{0,1,2\},
\]
tests both quasi-total Roman conditions directly at every vertex, computes the true minimum weight, collects every minimum function, and compares the result with the four-family classification and the formula
\[
uv+\mathbf 1_{s=2}ut+\mathbf 1_{t=2}vs+\mathbf 1_{s=t=2}.
\]

Recorded output:

```text
VERIFY_OK
connected_chain_graph_types_checked = 114
orders_checked = 4..8
types_by_order = {4: 2, 5: 6, 6: 14, 7: 30, 8: 62}
ternary_labelings_checked = 484218
minimum_functions_checked = 633
all minima had weight 4 and matched the four-family classification
all minimum-function counts matched u*v + [s=2]u*t + [t=2]v*s + [s=t=2]
half_graph_H3_published_endpoint_pattern_x3_y3 = invalid
half_graph_H3_universal_pair_x3_y1 = valid
```

The checker covers \(114\) connected canonical chain-graph types and \(484{,}218\) ternary labelings. It also directly tests the three-by-three half graph construction used in the prior-work comparison.

The finite computation is corroborative only. The theorem for arbitrary connected chain graphs follows from the exhaustive symbolic classification of weight-four label multisets in the proof.
