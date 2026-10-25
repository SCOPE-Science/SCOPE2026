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

## Exact mathematical checks

The standalone `check.py` was executed with Python 3 and SymPy. It verifies the defining identity under the proposed normalization coordinates, independently derives all four partial derivatives modulo two, and confirms the dehomogenized Jacobian ideals in both the triple-point and endpoint charts. The endpoint Gröbner basis gives three independent torsion classes, \(y,z,y^2\), annihilated by the singular-line parameter \(w\).

Exhaustive enumeration over \(\mathbb F_2,\mathbb F_4,\mathbb F_8\) gives respectively \(8,22,74\) rational surface points and \(7,13,25\) singular points. These finite checks independently corroborate the scheme-support formulas in small fields; they do not establish the universal or all-extension assertions. Those follow from the full proofs in `RESULT.md`. The ramification result follows from the exact rational function \(v+v^{-1}\), its derivative, and Riemann--Hurwitz.

Independent external examination was not performed.
