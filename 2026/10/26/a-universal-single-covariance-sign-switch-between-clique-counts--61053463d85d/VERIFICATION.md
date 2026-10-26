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

## Reproducibility

Run `python3 check.py` from this directory using Python 3. The script enumerates small labelled graphs, calculates both sides of the claimed covariance identity independently, and compares rational results. Observed output: `PASS 168 exact covariance identities`; it also prints two pairs of opposite-sign, exact-rational motif covariances.

## Scope and limits

The script is a finite consistency test, not an exhaustive check of the theorem's infinite parameter domain. In particular it does not verify the single-crossing conclusion at infinitely many graph sizes or clique orders. Those statements rely on the conditional expectation and strict-derivative proof in `RESULT.md`. Scientific priority remains subject to external assessment. Independent audit has not been performed.
