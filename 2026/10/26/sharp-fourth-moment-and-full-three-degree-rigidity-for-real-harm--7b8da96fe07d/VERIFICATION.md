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

Run `python check_harmonic_quadratic.py` with Python 3, SymPy, and NumPy installed. The code derives normalized disk monomial moments exactly, checks the full second- and fourth-moment expansions, verifies the maximizing one-variable rational expression and its derivative, isolates the unique positive quartic root, and verifies the three two-degree constants. It separately compares 100 deterministic random real harmonic quadratics against independent tensor-product Gauss quadrature over squared radius and angle. This execution passed all assertions.

# Proof boundaries

The finite numerical comparisons are **not** used to infer the optimal constant or to certify that no other maximizers exist. Those global statements follow analytically from the phase-sign reduction, the strictly unimodal linear-energy quotient for every nonnegative quadratic ratio, Descartes' sign rule, and strict comparison with the constant-free boundary. The exact algebraic definition of the constant does not depend on floating-point approximations. Independent audit has not been performed.
