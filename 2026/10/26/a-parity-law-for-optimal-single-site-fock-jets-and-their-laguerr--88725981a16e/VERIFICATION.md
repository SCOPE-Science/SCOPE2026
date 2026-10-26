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

The self-contained program `CHECK.py` uses only Python's standard library. Run `python3 CHECK.py` to reproduce 42 exact polynomial-identity checks, finite Laguerre-root candidate and comparison tests for six jet orders, 18 central-limit comparisons, 36 independent coherent-polynomial coefficient comparisons, and 45 finite-difference derivative comparisons. The program printed `ALL CHECKS PASSED` on the packaged source.

Mathematical verification rests on the Fock Weyl-unitarity calculation, explicit Charlier coefficient extraction, the telescoping derivative identity, the positive simple zero theorem for associated Laguerre polynomials, Stirling and Charlier asymptotics with global tail exclusion, and the strict monotonicity of the Hermite oscillator's Sonin energy. The exact polynomial checks are not a universal proof for all integers. No independent audit has occurred.
