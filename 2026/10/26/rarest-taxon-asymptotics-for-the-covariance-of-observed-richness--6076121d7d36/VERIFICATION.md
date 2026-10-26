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

# Reproducibility

Run `python verify.py` alongside `certificate.json` with Python 3.10 or later. This re-enumerates five rational categorical distributions for sample sizes 2 through 9, validates the leave-one-taxon covariance identity coefficient by coefficient in the formal linear span of logarithms of positive integers, and compares against the supplied certificate. It also computes numerical large-sample checks (not proofs) for the asymptotic leading constant and first correction. The 180 exact coefficient identities were all checked. The asymptotic theorem rests on the stated analytic binomial Taylor expansion and rarest-species argument, not on finite enumerations.

The certification scope is only numerical and exact finite consistency. No independent auditing or external certification has been performed. This model assumes IID with-replacement sampling and fixed finite positive category probabilities; application to spatially structured ecological field data requires further work.
