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

# Reproducible exact checks and scope

Run the companion Python 3 standard-library script from the same folder: `python3 check_path_choices.py`.

A successful replay completed 45,150 exact rational checks without assertion failures.

The first verification exhausts all connected visited intervals and current vertices for path orders two to twenty-one and substitutes the closed formulas into each minimizing Bellman equation. For every path of order at most five it checks every unvisited-versus-visited offered-neighbor conflict. The second method independently enumerates every stationary deterministic left-versus-right offered-neighbor preference for right-endpoint and either-endpoint hitting on each path with at most nine vertices, solves each exact finite Markov-chain linear system and compares the true rational minimum to the claimed formula. The exact six-vertex continuations \(833/81\), \(941/81\) and penalty \(4/3\) are checked explicitly.

Finite computation is not the infinite proof: correctness for arbitrary path orders follows from the Bellman identities, positive increments and endpoint decomposition documented in `RESULT.md`. No distributional cover-time optimality, independent external validation or historical-priority certification is claimed.
