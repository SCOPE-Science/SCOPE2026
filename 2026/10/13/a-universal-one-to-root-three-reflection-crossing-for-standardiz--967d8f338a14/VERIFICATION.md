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
The exact proof uses only the Gamma density formula, monotonicity of \(F(r)=\operatorname{artanh}(r)/r\), convergent power series on \(0<r<1\), and coefficient comparison.

The companion script `verify.py` checks three algebraic/numerical aspects without being used as proof:

1. symbolic simplification of the reflected-density log ratio;
2. the coefficient \(-12/5\) in the expansion of \(\kappa_\alpha^2\);
3. representative numerical roots, which satisfy \(1<\kappa_\alpha<\sqrt{3}\) and approach the displayed asymptotic.

The proof does **not** infer uniqueness, bounds, or asymptotics from those finite checks. The statement is restricted to the common reflected support \(0<z<\sqrt{\alpha}\); beyond that range the left reflected point is outside the Gamma support.
