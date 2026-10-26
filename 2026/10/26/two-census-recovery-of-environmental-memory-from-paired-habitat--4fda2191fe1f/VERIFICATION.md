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

The stationary model, parameter domain, cross-covariance and autocovariance definitions, and reconstruction are given in RESULT.md. Exact-rational checks using `verify.py` construct independent 8-state transition matrices for 12 parameter settings, verify their stationary laws, evaluate 48 independently obtained moment expressions, and check all 12 inverse reconstructions. Both positive and negative environmental memory, independent environmental states, no local copying, and coincident memory parameters are included. The one-date nonidentifiability example is checked by matching all four joint probabilities.

The general theorem is proved analytically and is not inferred from the finite test set. Only population-law identifiability is claimed: statistical uncertainty with finitely many field samples, observation errors, or an incorrect model is not quantified. A separate independent scientific audit has not been performed.
