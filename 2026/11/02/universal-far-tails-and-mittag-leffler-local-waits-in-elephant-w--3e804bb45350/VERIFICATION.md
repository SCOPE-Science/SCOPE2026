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

The accompanying `CHECK.py` is self-contained and uses Python's standard library. Execute `python CHECK.py`; it performs 609 finite checks using exact fractions for small activity paths and survival products. Its gamma-function coefficient comparisons and large-size conditional approximation checks are numerical consistency tests, not proofs of limits.

The infinite theorem follows from the complete derivation in `RESULT.md`: conditional hazard and gamma product; exact one- and two-activity histories; asymptotic comparison of a finite mixture; the tail-sum moment criterion; and the conditional Laplace argument. Bercu's already established almost-sure Mittag-Leffler activity limit (arXiv:2203.04196, Lemma 2.1) and the classical Mittag-Leffler large-argument asymptotic are external stated inputs, not independently derived here.

No independent audit, external certificate, or human validation is claimed. The fixed-time and macroscopic tail limits are deliberately separate, with no uniform joint scaling assertion.
