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

The standalone script `verify.py` uses exact rational arithmetic for the competing-exponential renewal kernel and floating-point consistency tests for stable one-jump rates, Pareto excess, the normal-exponential mixture, and the successful-excursion inverse-rate limit. Running `python verify.py` produces a count of successful assertions. It does not sample full stable paths or certify asymptotic probability limits; the proof rests on the small-time marked-exit lemma, geometric regeneration, and the random-index characteristic-function argument. Numerical tolerance checks are finite and thus cannot establish originality.
