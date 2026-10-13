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

# Reproduction and limitations

The mathematical proof of the all-order statement and constant-vertex diameter equality is in RESULT.md; no experiment is substituted for those proofs.

With a C++17 compiler run:

```sh
g++ -std=c++17 -O3 verify_fault_profile.cpp -o verify_fault_profile
./verify_fault_profile
```

The program builds every vertex-deleted directed binary de Bruijn graph of orders 2 through 10. It computes breadth-first distances from every surviving starting vertex, rejects a survivor digraph as disconnected on finding any unreachable endpoint, and otherwise records its directed diameter. For each order it checks the entire table with exact integer comparisons. Expected success marker: `PROFILE_VERIFIED`.

With Python 3 and the standard library run:

```sh
python3 verify_scc_independent.py
```

The program independently uses string-indexed arcs, a two-pass DFS strongly-connected-component decomposition, and all-surviving-ordered-pair BFS through order seven. It checks the sizes of the three SCCs at every exceptional fault and reproduces the small profile independently. Expected success marker: `INDEPENDENT_VERIFIED`.

Programs use no external datasets and all finite loops have explicit bounds. The verification does not prove a closed formula for every larger order, and does not provide independent outside review.
