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

# Reproduction

Run `python verify_joint.py` using NumPy and SciPy. The script executes direct Gaussian forward-query least-squares fits, including negative, zero, near-one and exact-one direction correlations, and checks the independent reference distribution for each row. It also uses explicit Gaussian small-ball importance sampling to compare finite-threshold joint-tail integrals with the proved limit for correlations \(0\), \(0.5\), and \(0.85\).

The recorded execution passed 2,759 assertions. Importance-sampling estimates remain random finite diagnostics. The general limits, constants, and alignment discontinuity are established analytically in RESULT.md; no finite simulation or output log constitutes an infinite proof. No external mathematical audit has been carried out.
