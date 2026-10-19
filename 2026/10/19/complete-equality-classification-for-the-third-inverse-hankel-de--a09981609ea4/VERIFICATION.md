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

# Exact algebraic verification

Run `python3 verify_inverse_hankel.py` using Python 3. Only the standard library is needed. The program generates and checks exact rational coefficient identities and tensor Bernstein forms. It checks 60 nonnegative source-envelope coefficients and the 12 strictly positive leading coefficients, a coefficientwise complex-phase Laurent identity, 40 strictly positive defect coefficients on the two subrectangles, and the rational inverse-Hankel determinant identity for arbitrary two-pole parameters. It ends with `CERTIFICATE PASS` only if every asserted identity holds.

This is a finite symbolic proof check of particular polynomial steps. The starlikeness proof, the Carathéodory boundary representation, and the logical necessity/sufficiency argument are mathematical reasoning in `RESULT.md`. No independent mathematical audit or infinity-wide enumeration is claimed.
