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

`python3 artifacts/verify_grid_game.py` regenerates graph edges, BFS distances, forbidden geodesic triples and exact minimax values for the two starting conventions. It checks every corner's maximal-pair count, exact triple count, and impossibility of extending a corner-rooted feasible triple. It does not assume the geodesic antichain characterization used in the proof.

The checker ran successfully on 18 graph instances, testing 20,504 recursive minimax states and 72 rooted classifications. Its final line was:

```
VERIFICATION_OK graph_cases=18 total_minimax_states=20504 corner_classifications=72
```

The file `artifacts/verify_grid_game_output.txt` contains the full recorded per-instance results; the code runs with the Python standard library. The 18 finite tests are not an exhaustive search over all grid orders. The infinite theorem is established analytically by the proof of the corner-rooted classification and matching two-player strategies. Independent audit and independent scientific validation have not been performed.
