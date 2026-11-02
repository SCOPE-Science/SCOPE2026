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

# Reproducibility

Run all three packaged scripts locally; no external input, network, or nonstandard Python packages are required.

`python3 verify_rank4_connectedness.py` exhaustively enumerates integer partitions with parts at least three and total between six and seventeen, computes exact adjacency/equality quantifier-extension signatures of order four, and checks all disconnected types against representatives \(C_3,\ldots,C_{11}\). It also checks six two-component identities. The actual recorded output is in `verify_rank4_connectedness.out`.

Compile `verify_rank4_connectedness.cpp` with `g++ -std=c++17 -O3` and execute it. This independent implementation uses integer type interning and ordered tuple loops. Its recorded output is `verify_rank4_connectedness_cpp.out`.

`python3 ef_game_independent.py` computes the full four-round adversarial Ehrenfeucht–Fraïssé game on \(C_9\sqcup C_9\) and \(C_{11}\), independently of the type recursion; its actual output is `ef_game_independent.out`. It normalizes the first selected vertex to vertex zero by vertex transitivity of each graph, then checks both Spoiler move directions and every available response.

The finite checks do not themselves establish the infinite family. That conclusion additionally relies on Brown–Hoshino's published single-cycle theorem at rank four and the elementary Ehrenfeucht–Fraïssé compatibility of disjoint unions. The proof in `RESULT.md` states these steps explicitly. For the sharp bound, exactly 105 disconnected graphs below eighteen vertices are exhausted; no assumptions about larger disconnected graphs are needed.
