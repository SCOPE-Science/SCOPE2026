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

The accompanying `verify.py` uses no nonstandard Python packages. Run `python3 verify.py` in the directory containing the verifier. It computes complete three-decks by direct three-position enumeration through word length 12, separately computes them using a streaming subsequence recurrence through length 36, and compares the entire deck-class partition against the proposed two-word involution. It also calculates the correction term in two arithmetically different ways through length 140.

The finite execution returned: `THREE_DECK_WEIGHT3_PASS lengths=3..36 direct_deck_comparisons=715 enumerated_words=66045 series_coefficients=0..140 all_classes_at_most_two=True first_collision_length=7`.

These checks are finite consistency tests, not an exhaustive infinite proof. For the proof for all lengths, see `RESULT.md`, especially the complete-coordinate lemma and the unique nonzero root of the quadratic collision equation. Independent mathematical validation has not been performed.
