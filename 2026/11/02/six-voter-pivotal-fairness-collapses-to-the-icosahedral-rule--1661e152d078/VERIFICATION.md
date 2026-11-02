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

# Verification record

The proof in `RESULT.md` gives the universal structural classification for all monotone, candidate-neutral six-voter rules, including every boundary case with zero to five winning two-voter coalitions and the three-edge triangle possibility. It is a finite exact theorem, not a probabilistic experiment.

`verify.py` uses only Python's standard library and exact integers. It enumerates all \(192\) pairwise-intersecting winning-pair patterns and their admissible complementary winning-triple orientations, yielding \(2640\) non-dictatorial monotone neutral rules. It independently evaluates swing counts from losing-to-winning predecessor coalitions, rather than reusing the algebraic fairness formula in the proof. Results: exactly \(12\) Shapley–Shubik-fair and exactly \(12\) Banzhaf-fair rules, identical sets; each has exactly ten winning triples and a two-regular graph on the other five vertices; all twelve are one relabeling orbit with automorphism group size \(60\).

The six possible dictatorships are omitted by the verifier's search but excluded by the elementary singleton-winning argument. The code exhaustively checks all other rules; it does not assert independent publication priority, and an independent audit has not been performed. The historical literature-access limitations are described in `REVIEW.md`.
