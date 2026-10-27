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

# Verification and limits

The full mathematical proof uses rational generating functions and dominant-pole Fourier averages; it does not rely on numerical enumeration for an infinite claim. The included `verify_renewal.py` was actually run with `verification_output.txt` recorded; it uses exact `Fraction` arithmetic for four finite-support laws, including two with no unit interarrival probability. It checks both strict signs in a finite window. Such checks cannot certify infinite sign densities, and no outside independent validation has occurred.
