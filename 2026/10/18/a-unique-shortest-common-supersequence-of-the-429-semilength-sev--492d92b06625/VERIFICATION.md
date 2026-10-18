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

# Reproducibility checks

Compile the two attached C++17 sources with `g++ -O3 -std=c++17`. Execute `./verify_exhaustive` and `./verify_bfs 7 3000000`. The first explicitly enumerates all binary hosts of lengths 21 and 22, constructs 429 Dyck targets, finds respectively zero and one universal hosts, and checks counts before successful exit. The second independently builds a greedy-progress BFS and finds min=22, optimal_host_words=1, reachable_states=1690893, expanded=919290. Both print `(()(()()()()()()())())` as the witness. The literal source files are sufficient to reproduce the finite computation, with no external packages.

The proof of exhaustiveness relies on inspecting the loop bounds, recursion and subsequence greedy lemma, not merely on the outputs. No result for larger semilengths, independent external validation, or complete search of all possible unpublished literature is claimed.
