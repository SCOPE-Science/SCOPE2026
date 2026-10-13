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

# Verification notes

Run `python3 verify.py` from the directory containing this file. It uses only the Python standard library. The output is `VERIFY_OK exact_rational_allocation_cases=3261 checked_probe_values=15198 geometric_cases=108`.

The exact-rational checks independently recompute all feasible allocation MSEs on monotone spectral-weight profiles, verify the finite-difference and increment identities, check the optimizer and tie rules, and test finite geometric thresholds by exact fraction arithmetic. The package's proof, not finite testing, establishes the statements for all sizes and real spectra. This verification does not test randomized Nyström implementation error, Lanczos quadrature, wall-clock cost, or originality beyond the separately documented literature comparison.
