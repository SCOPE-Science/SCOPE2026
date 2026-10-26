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

Run `python verify.py` in an environment with Python 3 and SymPy. The checker does polynomial computations over the prime field of characteristic two using `sympy.Poly(..., modulus=2)` and a direct binary elimination for the seven-point cubic evaluation matrix.

It verifies the Cayley cubic coordinate change; all four derivatives in the new frame; reduction of the polar map to the three binary cubic forms modulo the defining equation; all seven Fano points as reduced base points via local Jacobian rank two; rank seven of their cubic evaluation conditions; and three cleared-denominator function-field identities. The local valuation nonsquare arguments and the transcendence-degree-two \(p\)-basis theorem proving the generic degree and exponent are written out in RESULT.md and are not substituted by the finite computation.

Observed execution on the packaged source was successful, producing two `VERIFY_OK` messages. These checks are self-review reproducibility only, not an independent audit.
