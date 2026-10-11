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
For an admissible unit pair, after changing the sign of \(y\) if necessary, put
\[
a=\|x+y\|\ge b=\|x-y\|,
\qquad
r=\frac ba.
\]
The analytic estimate is
\[
\Phi_X(x,y)
\le
\frac{1+r}{2}\bigl(2+a(1-r)\bigr)
\le
(1+r)(2-r)
=
\frac94-\left(r-\frac12\right)^2.
\]

Pointwise sharpness is explicit. In \(\ell_\infty^2\),
\[
x_r=(1,1-2r),
\qquad
y=(1,1)
\]
satisfies
\[
\|x_r+y\|_\infty=2,
\qquad
\|x_r-y\|_\infty=2r,
\]
and the normalized sum/difference vectors are
\[
(1,1-r)
\quad\text{and}\quad
(0,-1),
\]
whose distance is \(2-r\). Hence
\[
\Phi_{\ell_\infty^2}(x_r,y)=(1+r)(2-r)
\]
for every \(0<r\le1\).

For the global endpoint, equality in the quadratic maximum forces \(r=1/2\); equality in \(a\le2\) then forces \(a=2\) and \(b=1\); equality in the first triangle step is exactly \(\|3y-x\|=3\), after the chosen sign.

`verify.py` checks the sharpness family exactly over rational parameters with denominator at most \(80\) and checks the endpoint witness. The continuum theorem is proved analytically and does not depend on finite enumeration.

No independent audit or independent validation has been performed.
