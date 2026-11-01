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

# Reproducibility

Run `python check.py` with SymPy installed. The checker reconstructs the numerator polynomial from finite power-series identities, recomputes five exact reciprocal resultants, the discriminant, the critical factorization, and the derivative of squared modulus at the two unit-circle crossings. It also tests a finite sample of numerical roots on both sides of the critical exponent; those checks are not a proof of root counts over an unbounded parameter range.

The global claim follows from the analytically established positivity of resultant factors for \(b\ge1\), the exact crossing derivative, root-count continuity where the resultant is nonzero, and the discriminant. These checks require no downloaded external data or third-party paper text. Scientific priority has not been independently established. Independent mathematical audit and validation have not been performed.
