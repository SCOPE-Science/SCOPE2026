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
The bundled checker uses exact symbolic arithmetic.

It reconstructs
\[
E_0=\left(\frac{B}{\eta},0,0\right),
\qquad
\lambda_I=\frac{MB}{\eta}-(\mu+\eta),
\]
and verifies the endemic equation
\[
k\gamma I^2+(k-B\gamma)I+B\left(\frac1{\mathcal R}-1\right)=0.
\]

For
\[
B=\eta=\mu=\alpha=M=1,\qquad \gamma=10,
\]
it verifies
\[
\mathcal R=\frac12,\qquad
I_-=\frac16,\qquad I_+=\frac25,
\]
the full equilibrium coordinates, and the characteristic polynomials
\[
(\lambda+1)^2(\lambda+2),
\]
\[
\frac{(\lambda+1)(36\lambda^2+43\lambda-42)}{36},
\]
and
\[
\frac{(\lambda+1)(5\lambda^2+12\lambda+14)}5.
\]

It also verifies the algebraic subthreshold saddle-node boundary. No numerical trajectory simulation is used.
