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
# Exact verification
Run `python check.py` with `sympy>=1.11`. The certificate constructs every one of the 90 possible arrangements, recurses on inversion count with the exact exponential race probabilities, and proves the stated rational formula and derivative by symbolic identity. It checks positive coefficients, the parameter-inversion symmetry, both limits, and the example at \(x=2\). The output PASS is a reproducibility summary; the definitions, first-step equation, source code and exact polynomial identities jointly constitute the mathematical verification.

The exhaustive computation is finite and complete for six particles; it is not an extrapolation to larger sorting systems. Independent scientific audit and independent publication-priority validation have not been carried out.
