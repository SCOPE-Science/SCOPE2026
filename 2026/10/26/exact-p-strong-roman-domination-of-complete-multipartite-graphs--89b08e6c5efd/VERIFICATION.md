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

# Verification

Run `python3 verify.py` in the same directory as `verify_output.txt`. This is a standalone Python standard-library-only checker. It directly reconstructs the complete multipartite adjacency relation and the exact neighbor-zero threshold, then compares the closed formula with two independent finite enumerators. The zero-profile enumerator examines all possible sets of defending parts, rather than imposing the main proof's two-defender reduction. The direct checker enumerates all labeled functions on small graphs with the full permitted label range.

The recorded run gives `ZERO_PROFILE_CHECKS=844`, `DIRECT_LABEL_CHECKS=90`, `GRAPH_PROFILES=187`, `CONGRUENCE_EXAMPLES=4`, and `VERIFY_OK`. Four special examples are checked at moderately larger orders.

These computations do not prove statements for unbounded part sizes or parameters; the universally quantified result follows from the proof in `RESULT.md`. No independent mathematical audit has been performed.
