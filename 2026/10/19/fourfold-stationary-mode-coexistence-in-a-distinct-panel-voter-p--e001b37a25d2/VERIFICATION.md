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
# Reproducibility and verification

Execute `python verify.py` with the exact listed SymPy version. The script tests the distinct-panel stationary probabilities from exact two-person combinatorial draw counts, checks the unique invariant distribution by positive detailed-balance ratios, symbolically factors the mode polynomial, and compares exact rational global maximizers for multiple finite populations. It checks finite Pell examples and verifies the replacement contrast using a separately computed squared-panel kernel.

Actual successful run: symbolic identities and 390 rational distribution/rate checks; Pell exponents 3, 5 and 7 checked by exact rational stationary distribution, and higher exponents 9 and 11 checked algebraically. The separately verified factorial stationary weight formula agrees with the birth–death ratios over an additional finite test range.

These checks verify code and finite arithmetic, not uniqueness in the mathematical literature or an infinite theorem by enumeration. The proof of the universal classification and infinite Pell family is in RESULT.md. No external or independent audit has been performed.
