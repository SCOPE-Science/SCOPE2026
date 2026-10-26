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

# Verification and reproducibility

Run `python check.py` using Python 3. The standalone checker has no third-party dependencies and reproduces the numerical entries in `checks.txt` from the exact radial Laplace transform. It checks the exact constants, the limiting saddle and crossing, and coexistence points at three small positive inner radii. It does not prove the quantified uniform asymptotics, the global rate-selection argument or publication priority; those are addressed by the written proof and literature comparison. The prior numerical fits are reported as prior literature rather than treated as exact conclusions. Independent audit has not been performed.
