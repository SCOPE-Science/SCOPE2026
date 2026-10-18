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

# Exact computational verification

Run `python3 CHECK.py` from the directory containing this file. No third-party dependencies, non-deterministic choices, external data or network access are required. `CHECK_OUTPUT.json` records output from a completed run.

The standalone checker independently builds the multipath face set twice over all 4096 arc masks, by directed source/target collision plus directed-cycle detection, and by union-find testing of selected undirected multiedges. Both enumerations agree exactly and give face numbers \((1,12,42,48,12)\), including the empty simplex. For the 114 nonempty faces, the explicit twelve-coordinate discrete-Morse rule gives 53 pairs and critical counts \((1,1,6,0)\) in dimensions 0–3; exhaustive topological sorting covers all 276 nonempty Hasse incidences without a directed cycle. The program reconstructs every exact integer Morse boundary by signed gradient projection and checks that all are zero. Mod-two boundary ranks \((11,30,12)\) give a separate homology comparison.

For the symmetry character, the checker constructs a four-term integral one-cycle paired primitively with a cocycle. It checks the cocycle identity on every two-simplex, then evaluates all 24 induced signed simplicial permutations. It verifies the twelve class-trace pairs and decomposes the character algebraically using the three irreducible characters of \(S_3\).

The mathematical conclusion also uses the standard discrete-Morse CW-homotopy theorem and the classification of maps \(S^1\to S^1\) by degree; those are stated separately from finite enumeration in `RESULT.md`. No claim is made that this output constitutes independent validation, a proof for larger graphs, or a classification of all bidirected theta graphs.
