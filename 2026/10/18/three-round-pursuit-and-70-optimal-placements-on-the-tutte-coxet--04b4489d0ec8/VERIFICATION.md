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

# Finite-state verification

Run from the directory containing this file:

```
python3 verify_game.py
python3 verify_dual.py
```

Both programs use Python 3 standard-library modules only. They construct all 15 nonzero binary four-vectors and 15 isotropic two-dimensional subspaces, generate the 30-vertex incidence graph, and independently evaluate the game dynamic programming on cop multisets and robber positions. The first implements the cops' winning recurrence; the second implements the complementary robber's evasion recurrence. Both enumerate all 4,960 three-cop placements with repeats allowed and classify exactly 70 optimal placements, including all 35 point triples and all 35 line triples. `optimal_starts.csv` records the lexicographically sorted winning configurations, one three-label tuple per line, with the label convention defined in `RESULT.md`.

`verify_game.out` and `verify_dual.out` are outputs of actual local runs of the respective packaged source files. An ordered-list checksum is printed and checked: `422e6ea22043c57643838985dc011c76221708a837c123f32282bb65c4d9353d`. `verify_game.py` independently checks all graph distances, girth eight, degree three, and all two-ball coverage obstructions needed for the short lower-bound argument.

The computational proof is finite and exhaustive for the specified graph. It does not claim formal verification in another theorem prover, a noncomputational classification of all optimal starts, or validation by any external reviewer. The source-comparison caveats are described in `REVIEW.md` and `RESULT.md`.
