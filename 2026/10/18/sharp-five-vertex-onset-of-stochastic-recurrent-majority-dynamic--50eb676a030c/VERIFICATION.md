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

# Reproduction and scope

Run `python3 verify.py` in a directory containing this file and `verify.py`. Only the standard Python 3 library is required. It exhaustively enumerates all 728 connected labelled five-vertex graphs and all smaller connected labelled graphs with at least two vertices, reconstructing the binary synchronous random-tie majority transition relation exactly.

Each legal successor is checked by two separate routines: enumerating subsets of tied vertices, and exhaustive source/target state comparison. Each absorbing strong component is checked using two unrelated decompositions: Boolean transitive closure and Kosaraju's DFS. The expected distributions are verified through complete traversal and graph canonicalization over vertex permutations, not statistical sampling. The exact expected terminal output is reproduced in `RESULT.md`.

For the general balanced-hub construction, the proof in `RESULT.md` verifies a strict majority margin for each of the two flipping blocs and a simultaneous tie at the hub in both block phases. The finite program certifies the sharp order and classification, while this symbolic argument establishes the general construction; exhaustive five-site checks alone are not claimed to prove a theorem on all network orders.

The Markov chain's four-state communicating class has *temporal period two*. The four-state size is not a deterministic orbit period, and an independently performed scientific audit is not claimed.
