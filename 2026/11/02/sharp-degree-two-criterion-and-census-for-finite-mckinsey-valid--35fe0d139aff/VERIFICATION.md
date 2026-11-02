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

The proof uses standard Boolean Kripke semantics; its local splitting equivalence is checked directly against the truth conditions for the two modalities. The cardinality hypotheses (nonempty carrier, loops allowed, maximum outdegree two) are explicit. The count is obtained by a unique partition of rows according to successor-set size, and the asymptotic is bounded above and below using the same real critical point.

Run `python checker.py`: it enumerates all allowed relations and all valuations on one-, two-, three- and four-element carriers, compares the local criterion to actual modal truth, checks exact counts \(1,6,75,1612\), and verifies a separate maximum-outdegree-three counterexample. The performed run returned all assertions successfully. This is a bounded corroboration, not a computer proof of the arbitrary-\(n\) theorem.

References and originality comparisons are detailed in `RESULT.md`, `REVIEW.md`, and `AUDIT.json`. The inspected 2026 theorem concerns general computational hardness, while the 2024 weak-transitive characterisation overlaps qualitatively only on its restricted class. Independent external audit or historical-priority certification has not occurred.
