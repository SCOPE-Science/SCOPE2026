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

The complete short-length classification is proved using a binary projection/support lemma and exhaustive finite bases on at most five symbols. Run `python3 verify_gapped_two_deck.py` to enumerate every relevant source word of lengths one through seven. The implementation independently computes each observed deck by a direct index-pair loop and by a streaming update, verifies all fibers have permitted cardinalities and symbol-support counts, and compares complete short binary/ternary collision lists.

The finite verification establishes the small-alphabet base. The extension to arbitrary finite alphabet sizes is mathematical (projection and a five-symbol support bound), not numerical extrapolation. No statement is made for lengths beyond seven. A separate independent mathematical audit has not been performed.
