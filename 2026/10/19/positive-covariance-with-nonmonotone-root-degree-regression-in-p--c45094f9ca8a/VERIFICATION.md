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

Run `python verify.py` in the directory containing this document and the checker. The script requires only Python 3 and built-in modules. It enumerates all individual attachment histories through nine vertices with their exact rational probabilities, rather than assuming a precomputed joint law. It checks the degree-one and degree-two root masses, conditional leaf-count means, covariance, and both marginal first/second moments. It also compares direct rational moment recurrences through 79 vertices and tests numerical approach to the asymptotic coefficients at 100001 vertices. The executed script reported 397 passed assertions. These finite checks are separate from the analytic proof and cannot establish historical originality or a theorem for all sizes on their own.

The full theorem proof appears in `RESULT.md`. No independent scientific audit or external formal proof certification has been performed.
