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

# Reproduction and limits

The formulas are derived directly from the neutral inverse-branch recurrence, not from a finite sum experiment. Reproduce the Abel coefficients by putting \(z=x^\gamma\), \(b=2^\gamma\), \(\widehat f(z)=z(1+bz)^\gamma\) and equating the constant, linear and quadratic coefficients in \(\widehat A(\widehat f(z))-\widehat A(z)+1\). They yield
\[
c_{-1}=\frac1{\gamma b},\qquad c_\ell=-\frac{\gamma+1}{2\gamma},\qquad c_1=\frac{(\gamma+1)(2\gamma+1)b}{12\gamma}.
\]
Independently, differentiate \(W(s)=-q(A^{-1}(s))(A^{-1})'(s)\) and use the integral tail of its fourth derivative to justify the stated Euler--Maclaurin remainder. The algebraic \(x^\gamma\) coefficient is
\[
-\frac{(\gamma+1)(2\gamma+1)b}{12}q_0+\frac{(\gamma+1)b}{12}q_0=-\frac{\gamma(\gamma+1)b}{6}q_0.
\]
A separate symbolic Taylor expansion of the Abel defect through \(z^2\) returned zero for these coefficients. A direct finite inverse-branch numerical sum agreed in sign and scale with the subprincipal prediction at tested small inputs; the numerical tail is not a certified infinity and is not used for correctness. Only the finite-parameter \(0<\gamma<1\) asymptotics are established; no claims of parameter-uniform constants or external certification are made.
