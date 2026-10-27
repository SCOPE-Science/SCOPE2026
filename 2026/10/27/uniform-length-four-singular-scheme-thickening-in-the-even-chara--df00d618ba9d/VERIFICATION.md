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

For every even prime power \(q=2^m\) and \(k\in\mathbb F_q\), define \(\kappa^2=k\). On the chart \(x=1\), the exact derivatives are \(f_t=(1+ts^{q/2})^2\) and \(f_s=(t^{(q+2)/2}+s+\kappa)^2\). Since the homogeneous degree \(q+3\) is odd, Euler's identity shows that the hypersurface equation is in the derivative ideal. On \(x=0\), the derivatives \(F_z=y^{q+2}\) and \(F_x(0,0,1)=1\) rule out singular points.

Set \(r=q(q+2)/4\). Eliminating \(t\) gives \(s^{r+1}+\kappa s^r+1=0\), whose derivative is \(s^r\). Its constant term is one, so all \(r+1\) roots are distinct and nonzero. The determinant \(\det\partial(A,B)/\partial(t,s)=s^{q/2}\) is nonzero at those roots, so the completed Jacobian local algebra at every point is \(K[[A,B]]/(A^2,B^2)\), of length four. This proves the total \(4(r+1)=q(q+2)+4\).

As finite sanity checks only, exact polynomial differentiations modulo two were performed for \(q=2,4,8,16\) and matched the displayed formulas. Finite checks were not used as proof of the universally quantified statement. No assertion of independent audit, independent validation, or external certification is made.
