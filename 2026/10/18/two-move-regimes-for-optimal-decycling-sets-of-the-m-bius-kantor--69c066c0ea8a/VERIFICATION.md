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
# Reproduction and boundaries

Run both programs with an ordinary Python 3 interpreter from this directory:

```
python3 verify_masks.py > masks_replay.out
python3 verify_forests.py > forests_replay.out
cmp masks_replay.out forests_replay.out
cmp masks_replay.out verify_masks.out
```

Both programs enumerate the full \(\binom{16}{5}=4368\) deletion domain or, equivalently, its eleven-vertex complements. The first checks acyclicity via union-find on retained edges, the second via component DFS and the forest Euler identity. Both independently build every legal jump and slide exchange, execute BFS from every one of the \(672\) valid states, and emit complete degree, eccentricity, and pairwise-distance distributions. Each prints `VERIFY_OK`. A replay that exits without this marker is not a successful check. The canonical state/edge fingerprints match the sorted lists in `certificate.json`.

The minimum cardinality also follows without computation from \(|E(G-S)|=24-3|S|+|E(G[S])|\le15-|S|\), while the displayed explicit five-set witnesses attain it. The exhaustive finite checks do not establish any analogous assertion for other generalized Petersen graphs, or prove bibliographic novelty. Literature overlap review and computational replay remain conceptually distinct.
