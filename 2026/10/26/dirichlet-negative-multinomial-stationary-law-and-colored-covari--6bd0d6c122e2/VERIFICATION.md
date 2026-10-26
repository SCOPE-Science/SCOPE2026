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

# Reproducibility and checks

`verify.py` is fully standalone (Python 3 standard library). Running `python verify.py` performs 24,480 **exact rational** second-moment stationarity checks, plus matching first-moment identities, for integer chain lengths 1–8, numbers of colors 1–4 and rational shape parameters \(1/2,1,3/2,3\). It evaluates the original harmonic batch-transition generator at low degree using the exact jump factorial moments and verifies all first and second stationarity equations against the Dirichlet–negative-multinomial predictions. The tests also certify the two-species explicit example and Green-kernel identities. The verified test's assumptions are given in the code comments and in the RESULT.md proof.

The all-dimensional conclusion rests on the analytic chain of matching absorbing dualities, scalar hidden-parameter Dirichlet stationarity, moment determinacy, Foster recurrence and the displayed covariance algebra. No finite grid can independently prove the theorem outside the tested parameters. The scalar Dirichlet result and common absorbing dualities are cited established premises rather than newly proven lemmas. No independent audit has occurred.
