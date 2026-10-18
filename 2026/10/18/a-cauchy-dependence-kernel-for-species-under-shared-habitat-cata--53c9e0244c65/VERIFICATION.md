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

`python verify.py` uses exact rational arithmetic to solve a four-state Markov stationary system and independently reproduce the age-mixture covariance formula. It checks 360 rate quintuples, 1,080 exact marginal/joint comparisons, 360 half-correlation inequalities, 3,801 Cauchy-minor identities and associated rank tests, and 54 derivative-shape cases. Its checked output is recorded in `certificate.json`. The unbounded sharpness family and universal results are proved analytically in `RESULT.md`, not inferred from these finite tests. No independent scientific audit has been performed.
