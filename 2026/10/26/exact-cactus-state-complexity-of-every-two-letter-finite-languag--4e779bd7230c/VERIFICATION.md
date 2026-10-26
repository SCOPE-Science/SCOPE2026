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

# Mathematical verification

The main theorem is proved by the three-layer trimming lemma, a rectangle-cover lower bound, the cactus prohibition on three middle neighbors of one final state, and a cycle-disjoint pairing construction. The known Sperner antichain theorem yields the special inequality-language rank exactly.

Run `python verify_boolean_rank.py` with Python 3.9+ and no third-party modules. It exhausts all 15 nonempty two-by-two relations and all 511 nonempty three-by-three relations and verifies that the resulting automata accept exactly the prescribed length-two words, no words of other lengths through length four, and have a bipartite cactus underlying graph. It checks antichain-optimal constructions for inequality relations with 2–14 symbols. Expected terminal marker: `VERIFY_OK`.

The checker is not an exhaustive proof for arbitrary alphabet sizes; the symbolic arguments in `RESULT.md` supply that proof. Full-text inspection of the newest source remained incomplete, which is a literature-review risk rather than a mathematical-validation result. Independent audit was not performed.
