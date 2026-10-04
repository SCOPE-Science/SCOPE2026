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
The packaged `verify.py` uses only the Python standard library and exact rational arithmetic.

For
\[
\dot x=-2y,\qquad
\dot y=x+z^2,\qquad
\dot z=1+y-2z,
\]
it verifies the polynomial generator identities
\[
L\left(\frac{y^2}{2}\right)=xy+yz^2,
\]
\[
L(xz)=-2yz+x+xy-2xz,
\]
and
\[
L(yz)=xz+z^3+y+y^2-2yz.
\]

Starting from
\[
\mathbb E[z]=\frac12,\qquad
\mathbb E[z^2]=\frac14+V,\qquad
2\mathbb E[z^3]=\mathbb E[z^2],
\]
the checker verifies exactly
\[
\mathbb E[(z-\tfrac12)^3]=-V,
\]
\[
\mathbb E[yz]=2V,
\]
\[
\mathbb E[xz]=-\frac18-\frac52V,
\]
\[
\mathbb E[y^2]=6V,
\]
and therefore
\[
\operatorname{Corr}(y,z)=\sqrt{\frac23}
\]
whenever \(V>0\).

It also verifies the unique equilibrium
\[
\left(-\frac14,0,\frac12\right).
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional laws use arbitrary one-variable antiderivative tests, and the deep-excursion conclusion additionally uses invariant-support tangency. Those analytic steps are not finite experiments.
