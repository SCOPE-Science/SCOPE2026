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

# Reproduction and verified boundaries

Run `python3 verify_stationary.py` using Python 3.9+ and the standard library only. The program independently constructs and solves exact finite-state Markov stationarity systems; checks exact joint hub marginals; and evaluates finite-size critical-window means against closed chi and independently integrated weak-bias predictions. The run reported 80 exact-rational stationary states, 16 exact-rational hub-marginal identities, 12 chi-mean approximations, and 8 biased-mean approximations, with all assertions passed. A finite sample of cases is **not** an exhaustive proof of the theorem. The general Gaussian-window statement is proved analytically in RESULT.md by exact canonical reduction, a geometric local central limit theorem, and explicit tail bounds. No independent audit or external certification has been performed.
