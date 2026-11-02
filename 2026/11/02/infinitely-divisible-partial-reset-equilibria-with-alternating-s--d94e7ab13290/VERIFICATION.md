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

# Verification scope
Run `python3 verify.py` with the Python standard library. The checker independently verifies eight exact rational moment/cumulant identities (through sixteenth moment), nine direct Lévy integral/characteristic exponent comparisons, six non-self-decomposability derivative witnesses, and twenty-five resonant cancellations. It does not establish the theorem for an infinite parameter family: that is the role of the proof's uniform analytic inequalities and the Lévy-measure characterization.

The proof assumes only finite mean refractory duration. The checker uses selected numerical and rational parameters as reproducible diagnostics and makes no claim of independent expert or formal certification.
