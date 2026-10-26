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

# Reproducibility and verification

Run `python3 verify.py` using Python 3.10 or later with no third-party dependencies. The program forms exact rational Euler beta integrals and an independently implemented finite Markov first-event recurrence, agreeing for 196 parameter sets (all opposed-majority initial counts when each odd part has size 3, 5, 7, or 9). It tests 16 exactly fair opposite-full-polarization cases, an exact-rational globally negative-majority example with positive-consensus probability 0.978685744676395 approximately, and three finite-size critical-window approximations. The test code is self-contained. The asymptotic result is proved by the survivor-binomial CLT and delta method, not by finite checks. The program and its outputs are not an independent scientific audit.
