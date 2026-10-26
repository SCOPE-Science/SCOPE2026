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
# Reproduction notes

Run `python verify.py` in a directory containing that standalone file, using standard Python 3 only. The program deterministically writes one compact JSON object to standard output. The exact expected output appears in `certificate.json` (the latter also ends in one newline).

The finite verifier checks independent edge-subsets, not simulated infection outcomes: each subset is weighted by its exact rational Bernoulli probability. It tests all source vertices for selected broom shapes, rational probabilities, algebraic adjacent-difference identities, and finitely many ordered root brackets. Analytic completeness for arbitrary positive integer sizes and every real probability strictly between zero and one is furnished by the inequalities in RESULT.md; no finite checker could establish those universal claims alone.

Independent external validation has not been performed.
