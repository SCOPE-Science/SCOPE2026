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

Run `python3 verify_graphic_horn.py` in a Python 3 environment. The script uses only the standard library, reconstructs the graphic-matroid closure from connected components via union-find, derives chordless cycles independently from induced subgraphs, searches simple paths independently by DFS, and enumerates the pseudo-intents from the defining recursion. It checks the exact canonical premises, their forward-chaining completeness, direct one-pass completeness of all-cycle rules, and directness threshold for the canonical collection. Tested instances: all simple graphs with 3, 4 or 5 vertices; 24 seeded order-6 graphs; complete graphs of orders 3 through 6; and wheels with rim sizes 3 through 7. The final expected output is:

`VERIFY_OK small_graphs 1120 subsets_checked 77117 pseudo_intent_subset_candidates 77117 wheel=3..7 complete=3..6`

The finite exhaustive scope does not establish the theorem beyond its tested graphs. For all graphs, the proof rests on: closure of proper rooted-induced-path subsets; chord splitting; the pseudo-intent recursion; forced antecedents in sound bases; and elementary cycle counting. No external proof assistant or independently commissioned audit was used.
