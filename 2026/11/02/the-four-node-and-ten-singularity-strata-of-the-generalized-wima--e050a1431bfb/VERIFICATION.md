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

Execute `python verify_symbolic.py` in a Python 3 environment with SymPy installed. The expected and observed terminal line is `SYMBOLIC_VERIFY_OK`. The script checks polynomial identities for coordinate squaring, the tangent cone, tangent-line factor, axis discriminant, and the previously published quotient resultant.

Execute `python verify_f25.py` with Python 3 and no third-party dependencies. The expected and observed line is `FINITE_F25_VERIFY_OK {'smooth_axis_parameters': 15, 'discriminant_parameters': 4, 'six_cusps_parameters': 1}`. The verifier enumerates all \(651\) projective points over \(\mathbb F_{25}\) for each \(\mathbb F_5\)-rational parameter pair satisfying the two nondegeneracy conditions. It checks singularities and Hessian ranks by a direct construction of \(\mathbb F_{25}\).

The all-characteristic classification is justified by the geometric argument in `RESULT.md`, independently of the finite-field witness count. Geometric connectedness follows from two independent Kummer squareclasses, not from observed finite cardinalities. The verifiers are arithmetic checks of explicit identities and a finite sample, not external audits or machine-checked formal proofs.
