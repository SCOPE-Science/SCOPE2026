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

# Mathematical verification

The exact determinant of the equilibrium Jacobian is \(\lambda(\lambda^2-Q)\), and the critical profile derivative is \(B'_a(u)=2(A(u)-a)/u^2\). Differentiating \(A\) yields the single interior critical coordinate \(u_*\); the sign analysis in RESULT.md proves every quantifier and endpoint of the count.

Run `python verify.py` with Python 3 and SymPy. The script validates the two exact Jacobian characteristic polynomials, Cayley–Hamilton cubic identities, the two branch derivatives, the derivative of \(A\), numerical location of the unique cusp, sign witnesses for the four-point region, and sampled root counts at six parameter pairs. The six finite root samples are diagnostics and are **not** offered as a proof that no other zeros exist. The infinite parameter theorem instead follows from the explicit derivative-sign argument.

Boundary conventions: \(a=a_*\), including \(b=b_*\), has two distinct neutral points per punctured circle (the lower point is a triple zero at the cusp). With \(a>a_*\), equality with either fold produces three distinct points (including one double lower zero), while strict inclusion produces four. At the common origin the absolute-value vector field has no smooth Jacobian; it has been omitted throughout. Other nonlinear stability properties have not been proved.

Self-review: passed. Independent audit: not yet performed.
