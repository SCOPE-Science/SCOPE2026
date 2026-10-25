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

Run `python verify_tournament.py` using Python 3 standard library. This program independently constructs every tournament orientation on n=3,...,7 vertices, computes vertex-0 outdegree and rooted cyclic triangle count directly, and then checks the exact joint probability formula, posterior means, every upper-tail stochastic inequality with strictness boundary, and every conditional variance comparison using exact integer and Fraction arithmetic.

Observed successful output: 681 exact assertion groups across n=3,...,7, including 2,097,152 tournaments at n=7. Exhaustive enumeration is finite and does not establish the theorem for unbounded n. The universal proof is the independent fair-edge conditional binomial law and monotone likelihood-ratio calculation in RESULT.md; its assumptions do not apply to dependent edge orientations or biased tournaments.

No independent audit has been performed.
