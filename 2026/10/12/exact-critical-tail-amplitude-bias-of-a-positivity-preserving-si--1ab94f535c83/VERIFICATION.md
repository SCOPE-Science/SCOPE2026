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

# Reproduction and limits

The source's BIM (12)–(13) yields the recurrence in `RESULT.md` after setting both diffusion coefficients to zero. Analytic verification uses three exact one-step formulas, domain invariance, asymptotic stability of scalar forced contractions, convergence of the ratio of susceptible deficit to infection, and Cesàro averaging of reciprocal infection increments. The continuous comparison uses an ODE variation-of-constants argument followed by the analogous reciprocal identity.

Run `python3 verify.py` with standard Python to check rational first-step and iterate identities, preservation of the domain, and a long finite numerical trajectory. Expected terminal string: `VERIFY_OK`. The code checks only the chosen finite instance; it does not certify all initial states, step sizes or infinitely many iterations. The stated theorem is proved by the textual argument.

Scientific limits: permitted zero-noise case, fixed positive step, exact invasion threshold, strictly positive initial infection; no claim about stochastic corrections. The full original source was read via its lawful open-access HTML publication. Independent audit: not performed.
