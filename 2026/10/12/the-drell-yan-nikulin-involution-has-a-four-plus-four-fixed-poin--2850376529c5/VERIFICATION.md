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
The included `verify.py` uses exact arithmetic in \(\mathbf Q(\sqrt5)\). It reconstructs the quartic of Proposition 4.13, checks that \(t=1\) and \(t=-1\) are not bad fibers, specializes the source involution coefficients, verifies the exact factorization and separability of \(F_1\), and checks the finite fixed-point value on \(t=-1\).

The two infinity points on the \(t=-1\) weighted quartic are checked from the leading homogeneous equation \(-Y^2=X^4\) and the weighted scaling rule. The checker supports the algebraic substitutions; exhaustiveness comes from the base action \(t\mapsto1/t\) and the geometric compactification argument.
