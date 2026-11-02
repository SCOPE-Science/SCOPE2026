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

The included `ladder11_tree.json` encodes a complete binary edge-query tree of depth seven for perfect matchings of \(L_{11}\). Query names `v1`–`v11` mean rung membership and `h1`–`h10` mean top-horizontal-edge membership; each terminal `tiling` integer is a bitmask of horizontal-dimer start positions, indexed from the first column.

Run both standalone Python 3 programs in the directory containing the witness:

```bash
python3 verify_witness.py
python3 finite_recurrence.py
```

The graph-based checker independently enumerates all perfect matchings of the \(22\)-vertex ladder from the adjacency lists, confirms the \(144\) matching count and the one-to-one correspondence with \(10\)-bit dimer-start signatures, then recursively checks every query branch and all terminal matching witnesses. Expected verified output includes:

```text
LADDER11_TREE_CERTIFICATE_PASS graph_matchings=144 internal_nodes=127 distinct_leaves=128 depth=7
LADDER11_LITTLESTONE_EXACT_PASS value=7 entropy_upper=7
FINITE_ONLINE_RECURRENCE_PASS ((1, 0), (2, 1), (3, 1), (5, 2), (8, 3), (13, 3), (21, 4), (34, 5), (55, 5), (89, 6), (144, 7))
```

The second program computes a separate exhaustive minimax recurrence over all finite version spaces at widths one through eleven, corroborating the explicit witness. The upper bound of seven follows mathematically from \(144<256\) possible matching concepts. The universal static VC theorem and the block-product online lower bound are proved in `RESULT.md`, not inferred from experiments. No verification covers an exact adaptive dimension formula at general width, and no independent external scientific audit is claimed.
