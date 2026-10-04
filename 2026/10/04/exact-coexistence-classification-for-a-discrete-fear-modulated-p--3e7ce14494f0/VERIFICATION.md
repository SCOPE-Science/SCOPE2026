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
The analytic verification reduces the positive fixed-point equations to \(v=q(bu+c)\) and \(P(u)=-KF(u)\), then checks the complete quadratic sign/discriminant classification.

`verify.py` uses exact rational arithmetic for both counterexamples. For the two-equilibrium case it verifies \(C_0=5001/5000\), \(C_1=-439/50\), \(C_2=1/2\), \(\Delta=9386/125\), and \(\log\lambda_u=-1/21\); it also substitutes both roots into the original exponential map numerically. For the zero-equilibrium case it verifies \(P(u)=6(u+1)^2/5\).

The finite substitutions are consistency checks only. The accepted equilibrium-count classification and the boundary-multiplier identity are established algebraically. No claim is made about local stability of both coexistence branches or global dynamics.
