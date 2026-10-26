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

# Reproducibility and limits

The derivation is analytic. The supplied `verify.py` recomputes three original recurrence updates and the transformed closed form independently. It checks the derivative via symmetric difference quotients over 5,000 seeded real parameter selections and verifies that initial releases strictly suppress the first two generations in those trials. It checks the critical-tangency equation and its sign neighborhoods for eight reproductive factors and six threshold multipliers (48 settings). It also checks the exact counterexample computationally; the proof of its sign is supplied directly in `RESULT.md`.

Reproduce with `python -m pip install -r requirements.txt` then `python verify.py` in the package directory. This does not require online services after dependencies are installed.

The general proof establishes the claims for all positive admissible real parameters. Floating-point tests are not exhaustive proof, and numerical differentiation cannot establish a sign everywhere. The model is deterministic, uses a single initial additive introduction, and only addresses the first three generation updates. External independent validation was not performed.
