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

Run `python3 verify.py` beside `certificate.json`.

The verifier implements reversal and reversal-complement closure directly. It breadth-first enumerates every distinct closure output of length at most \(15\), using all four choices of appended bit and antimorphism at every node. Strict length increase proves that this finite traversal is exhaustive for the stated range.

Minimum string-attractor sizes are then recomputed in two ways. The first converts each factor to the union of positions occupied by all its occurrences and solves the resulting finite hitting-set instance by increasing cardinality. The second tests candidate sets directly against factor occurrences. The engines agree for every reached word.

The replay checks all level counts and attractor-size histograms, verifies that no length at most \(14\) word needs four positions, identifies exactly the two complementary length-\(15\) witnesses, reconstructs their directives, and checks the displayed minimum attractor by both success of the four-set and failure of every three-set.

Independent audit has not been performed.
