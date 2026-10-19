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

# Verification

The mathematical certificate is the explicit finite-state conditional-drift calculation and bounded martingale in `RESULT.md`. No numerical extrapolation is used for the claims covering all \(N\ge2\).

Run `python3 neutral_coupled_traits_checker.py` using Python 3.9+; it uses only the standard library. The program enumerates four binary paired-label count classes for \(N=2,3,4,5,6\), derives all exact rational one-step probabilities for both conventions concerning self sampling, checks the proposed terminal probability is harmonic at 1,230 parameterized states, and independently solves rational absorption equations for 88 nonabsorbing states with \(N=2,3\). Expected final text: `PASS`.

The binary finite-state checker does not, by itself, establish the general-label or arbitrary-size theorem; these follow from the proof's arbitrary indicator choices and conditional algebra. It does not check payoff-dependent positive-selection dynamics. No external independent audit has been performed.
