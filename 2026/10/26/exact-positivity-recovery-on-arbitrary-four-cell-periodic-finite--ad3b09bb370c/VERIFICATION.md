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

The file `verify.py` exactly constructs the mass and stiffness matrices of the theorem and checks the coefficients of all 16 entries of the cleared-denominator adjugate numerator as polynomials in four independent positive symbols. It establishes the diagonal, neighboring and opposite-node monomial-sign pattern used in the proof and specializes all opposite quadratics to the previously known alternating formula. Command: `python verify.py`; dependency: SymPy.

An exact-rational four-length example separately demonstrates direction-dependent sign failure and recovery. These calculations are reproducible algebraic identities, not a numerical sample offered as proof of the infinite family. No independent audit was performed. The full literature search cannot exclude unavailable specialized work.
