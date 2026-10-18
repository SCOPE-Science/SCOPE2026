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
# Reproducible exact checks

Run `python verify.py` with Python 3 and SymPy. It independently derives all five Cartier coefficients from the defining tenth-degree polynomial, verifies two simplified coefficient identities, validates an exact resultant in \(\mathbb F_{17}[a]\), and calculates five specialized polynomial gcds in \(\mathbb F_{17}[b]\). It separately checks the discriminant and complete Cartier ranks at all three exceptional smooth parameters. These polynomial identities are certificates for all algebraically closed-field parameters in characteristic \(17\); the final finite enumeration of prime-field pairs is only a corroborating sanity check.

The code verifies the algebraic identities used in the proof but does not attempt a scheme-theoretic classification of any finer moduli stratum, independently audit the science, or compute Jacobian \(p\)-ranks or Newton polygons. The group symmetry and Cartier–Manin formula are used as standard established mathematical facts, and the particular coefficient matrix is also derived afresh in the proof by its indices.
