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

# Reproduction and exact scope

The required verification artifacts are the standalone Python 3 files `finite_types.py` and `ef_game.py`. From the directory containing these files, run `python3 finite_types.py` and `python3 ef_game.py`. Both commands were actually executed successfully, and their recorded stdout appears in `finite_types_output.txt` and `ef_game_output.txt` respectively. No third-party Python modules, data downloads, randomization, or precomputed packages are used.

`finite_types.py` exhaustively constructs the adjacency/equality diagrams of all ordered four-tuples (repeats allowed) for \(H_n\), \(1\le n\le15\), then computes the complete sets of possible child types through rank four. It maintains a common interning dictionary across all sizes. An assertion checks the precise identifier sequence \((0,1,2,3,4,5,6,6,6,6,6,6,6,6,6)\). Further assertions separately compute ranks one through three.

`ef_game.py` independently solves each of four actual four-round games, using only the adjacency matrices and minimax with memoization, not the tuple-type table. It confirms inequivalence for sizes \(4,5\), \(5,6\), and \(6,7\), and equivalence for \(7,8\). Selected positions of Spoiler can be repeated, but they are never helpful: their unique legal matched responses are already fixed, so the algorithm omits those redundant moves.

The separate mathematical infinite-tail lemma converts a four-round Duplicator strategy on length-\(n\) linear orders into one on their half-graphs, retaining the A/B tags; all orders of length at least fifteen are four-round equivalent by the interval-splitting induction. Consequently the finite check through fifteen covers **all** larger sizes. The programs by themselves do not constitute an infinite proof.

No independent mathematical audit is asserted or simulated. Historical priority is not exhaustively established; no proof-assistant verification is claimed.
