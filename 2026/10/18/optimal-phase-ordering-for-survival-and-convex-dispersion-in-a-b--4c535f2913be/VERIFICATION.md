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

Run `python3 verify.py` with Python 3 standard library; stdout matches `verification_certificate.json` byte for byte including its terminating newline.

The program performs 1,024 adjacent-swap comparisons using exact fractions; 360 four-phase permutation comparisons; 3,917 exact assertions including five integer stop-loss thresholds for each tested schedule; and eight forward-uniformization checks with an independently propagated 111-state population distribution. The latter check has numerical truncation and Poisson-series approximation bounds inferred from the large state cap and tail; its output is used only as corroboration. The analytical proof in RESULT.md is unrestricted in number of phases and number of initial ancestors.

Critical limits: no general proof rests on finite experiments; branching independence, strictly positive birth/death rates, deterministic durations and terminal-horizon comparisons are essential. The historical general time-dependent-process paper (Kendall, 1948) could not be inspected in full, and bibliographic originality has not been independently validated. Scientific results were checked as presented; no independent audit has been performed.
