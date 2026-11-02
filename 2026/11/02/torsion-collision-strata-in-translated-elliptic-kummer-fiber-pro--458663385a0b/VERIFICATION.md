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

# Verification

Run `python verify.py` with Python 3 and SymPy. In the checked environment, it printed `VERIFY_OK: translation, valuation kernels, inertia, and genus examples`.

The checker calculates the three-term elliptic translation product exactly modulo \(y^2-x^3+1\), checks the valuation-matrix determinant, exhaustively computes modular kernel vectors for the three orbit-occupancy possibilities for \(m=5,7,11,13,17,19\), checks local inertia, and confirms several genus/component examples.

The general proof is the symbolic divisor/Kummer/Riemann--Hurwitz argument in RESULT.md; checks for finitely many \(m\) do not certify all \(m\). Full independent validation, positive-characteristic extensions, and composite indices divisible by two or three are not claimed.
