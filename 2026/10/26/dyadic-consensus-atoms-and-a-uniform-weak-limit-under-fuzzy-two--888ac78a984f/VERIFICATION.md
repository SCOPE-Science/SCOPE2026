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

The accompanying `verify.py` uses only the Python standard library. It builds an independent exact-rational transition tree for several stage-dependent probabilities and compares every terminal dyadic atom against the claimed closed product law. It also checks mean, variance and expected calendar rounds via rational arithmetic, and assesses the asymptotic expected-time prefactor numerically for a specified logistic parameter example. It does not replace the general proof.

The analytic proof establishes countable support, almost-sure finite stopping, distributional convergence to continuous uniform, the total-variation discontinuity, and the exponential-time constant. Exact-rational tests cover selected finite trees only. No empirical or independent validation has been performed.
