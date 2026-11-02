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

# Reproducible checks and proof boundaries

The analytic proof in `RESULT.md` derives the exact rank-one Nyström residual and active-plane generalized eigenvalues. It then algebraically factors the condition-number comparison, solves its unique positive quadratic root, and integrates the Haar-normal squared-coordinate distribution. The exact \(L=2\) rational-orientation witness is separate from sampling tests.

Run `python verify_nystrom.py` with NumPy and SymPy installed as declared in `requirements.txt`. The completed verification printed:

`VERIFY_OK symbolic identities=6, exact example=3, sampled Gaussian sketches=160, dimension-two cases=20`

`L=2 probability of harm: 0.17117806242279432`

`L=2 witness condition number: 2.1684763386382304`

The checks evaluate several exact symbolic identities and finite samples of Gaussian sketches, as well as rank-one/full-rank controls. Only the analytic arguments prove the continuum of \(L>1\) values, the exact probability, and the asymptotic order. No finite sample is used as a novelty certificate; external independent validation remains unperformed.
