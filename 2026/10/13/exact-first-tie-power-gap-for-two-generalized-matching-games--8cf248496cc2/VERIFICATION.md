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

## Reproduction
Run `python3 verification.py` using standard Python 3. The exact-arithmetic verifier checks the fixed-point inclusion-exclusion formula, the two-stage mixture representation, the likelihood-ratio polynomial identity, exact likelihood ordering, and the power-loss profile at 32 rational sample-size/skill combinations, as well as selected sparse-intensity checks.

## Analytic limits
The finite suite cannot verify all real skills or all sample sizes. Those claims use positive-coefficient polynomial identities and the Neyman–Pearson lemma in `RESULT.md`. The sparse-intensity coefficient uses the classical derangement-to-Poisson limit and an elementary exponential limit. Independent examination of the mathematics and publication priority remains unperformed.
