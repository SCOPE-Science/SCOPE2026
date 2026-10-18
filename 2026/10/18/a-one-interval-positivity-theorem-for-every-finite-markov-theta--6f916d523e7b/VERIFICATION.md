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

Run `python3 verify.py` using the Python 3 standard library. The checker performs exact-rational inversions and verifies algebraic update identities, stochasticity, off-diagonal signs, and the reduction to diagonal resolvent inequalities for 197 constructed directed generators, six parameter settings, and five rational timesteps. It checks strictly ordered resolvent diagonal samples for each positive-exit state, exact horizon signs in the three-state pure-birth example, and return-resolvent invariance under stationary time reversal in one nonreversible chain.

These finite cases do not imply a theorem for all generators. The universal strict monotonicity and endpoint classification are proved in `RESULT.md` from renewal at return times; the script is a reproducibility check of critical algebra and representative boundary cases. It does not calculate floating-point roots or inspect external sources. Mathematical limits: finite conservative generators with bounded finite entries and completed theta steps only.
