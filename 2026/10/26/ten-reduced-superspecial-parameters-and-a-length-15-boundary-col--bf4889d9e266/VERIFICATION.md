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
Run `python3 verify.py` (Python 3, SymPy) in the extracted package. The checker expands the characteristic-eleven Cartesian coefficients \(A\) and \(B\) from \(q(T)^5\), compares every coefficient with the displayed formulas, recomputes the degree-twenty-five resultant, verifies the eight simple projected roots, the \(u=2\) common factor, transverse Jacobians \(8\) at \((2,3)\) and \((2,4)\), and boundary restrictions. The script reports `VERIFY_OK` on success.

The step from the exact resultant to a geometric classification uses finiteness of the monic-in-\(v\) projection, lack of projective intersection at infinity, and local intersection multiplicities. These arguments, not a finite field-point search, prove the result over an algebraically closed field. The excluded boundary point is not claimed to carry a smooth genus-two Jacobian. Two distinct abstract isomorphism classes of superspecial genus-two curves in characteristic eleven are known: this result counts ten **marked parameters**, not ten classes.

Independent audit is not performed, and older alternate-coordinate classification tables may contain equivalent numerical statements.
