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

The proof reduces the original FISTA recurrence on an invariant quadratic eigendirection to four explicit scalar points. The key identities are
\[
x_3=r^2A(r)x_0,\qquad
x_4=r^3B(r)x_0,
\]
with
\[
A(r)=(1+\beta_2)r-\beta_2,\qquad
B(r)=(1+\beta_3)A(r)-\beta_3.
\]
The fourth-point objective increases exactly when
\[
(rB(r)-A(r))(rB(r)+A(r))>0.
\]
The two factor sign changes are proved algebraically in `RESULT.md`.

`check.py` uses Python's standard-library `decimal` arithmetic at 80-digit precision. It reconstructs \(t_2,t_3,t_4\), \(\beta_2,\beta_3\), \(r_-\), \(r_0\), and \(r_+\); verifies the numerical constants; checks the exact polynomial-factor identities to high precision; confirms the sign pattern on the four resulting intervals; and replays the first four iterates at representative parameter values. At the resonance it verifies \(A(r_0)=0\) to working precision and \(B(r_0)=-\beta_3\), hence \(x_3=0\) and \(x_4\ne0\).

Numerical replay supports the displayed algebra; it is not used as a substitute for the all-parameter proof. Independent audit has not been performed.
