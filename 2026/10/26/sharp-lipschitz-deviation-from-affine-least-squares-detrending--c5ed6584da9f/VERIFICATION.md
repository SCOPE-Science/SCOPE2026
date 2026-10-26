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

# Reproducible checks

Run `python3 checker.py` using the Python standard library. The exact-rational checker reports `PASS 12910 exact-rational assertions; analytical monotonicity is proved in RESULT.md` when executed successfully.

Its 12,910 assertions include exact algebraic verification of the derivative polynomial identity, 1,501 exact grid checks against independently integrated kernel expressions, and a rational grid test of kernel reflection. Endpoints, junction values, and sign geometry are also checked. Those finite arithmetic checks are not an exhaustive proof over the continuum.

The mathematical proof of the claimed infinite family of real and complex Lipschitz functions is the symbolic derivation of the kernel, its exact integration, global factor-sign analysis, and the equality characterization in `RESULT.md`.

No independent audit or independent validation was performed.
