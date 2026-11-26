---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks

Run `python3 verify_rank.py` with the Python 3 standard library. For each tested batch, the checker sorts actual residuals at both projected values, counts the transition events by rank, and computes the stationary risk using exact rational arithmetic. It checks the full risk ordering, including the strictly increasing part when some ranks are absorbing, and the optimal values for both sampling designs. The tested subset sizes are \(s=1,\ldots,g\) for \(2\le g\le6\) and \(1\le c<g\). For independent draws it tests \(s=1,\ldots,5\) for \(2\le g\le4\) and \(1\le c<g\).

The all-parameter proof is in `RESULT.md`; the executable checks are finite corroboration only. They do not address higher-dimensional models, unequal coefficients, or update rows drawn independently of the quantile batch.
