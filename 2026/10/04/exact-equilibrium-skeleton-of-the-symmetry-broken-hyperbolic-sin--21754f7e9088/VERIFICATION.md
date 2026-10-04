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

The verification re-derives all displayed scalar thresholds from the printed asymmetric vector fields.

Checks performed:

1. The fold function
\[
M(q)=q\operatorname{arcosh}q-\sqrt{q^2-1}
\]
is bracketed at \(M(q)=0.01\), giving \(q=1.048351831276690\ldots\). Its derivative is \(\operatorname{arcosh}q>0\), so the fold root is unique.

2. The Case-C stability equation
\[
0.2x+x\cosh x-\sinh x=0.01
\]
is bracketed at its unique positive root. Its derivative is \(0.2+x\sinh x>0\) for \(x>0\).

3. The Case-D eliminated stability equation
\[
0.2x-x\cosh x+\sinh x=0.01
\]
is bracketed at the two roots belonging to the outer branches within the three-equilibrium interval, as well as the additional positive root whose parameter lies outside the plotted interval.

4. Every stability threshold is converted back with \(a=0.2-d\cosh x\), and the ordering
\[
a_L<a_R<a_{\mathrm{SN}}<-0.83
\]
is checked.

5. The characteristic polynomial
\[
\lambda^3+0.2\lambda^2+\lambda+k
\]
is checked against the cubic Routh--Hurwitz conditions: stable exactly for \(0<k<0.2\), one right-half-plane root for \(k<0\), and two right-half-plane roots for \(k>0.2\). At \(k=0.2\) it factors as
\[
(\lambda+0.2)(\lambda^2+1).
\]

The bundled `verify.py` uses only the Python standard library and prints `VERIFY_OK` when these checks pass.

Limits: the checker verifies scalar threshold arithmetic and branch ordering. It is not a numerical trajectory integration and does not establish nonlinear Hopf criticality, global basins, or attractor existence.
