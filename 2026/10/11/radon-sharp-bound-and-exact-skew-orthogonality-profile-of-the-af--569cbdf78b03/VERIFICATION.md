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
The structural inequality is analytic. If \(x\perp_B y\) and \(y\perp_B x\), then
\[
\|\beta x-\alpha y\|
\ge
\beta
\quad\text{and}\quad
\|\beta x-\alpha y\|
\ge
\alpha.
\]
Together with
\[
\|\alpha x+\beta y\|\le\alpha+\beta,
\]
this yields
\[
B_{\alpha-\beta}(X)
\le
\min\left\{1,\frac{\beta}{\alpha}\right\}.
\]

`verify.py` checks the affine-regular hexagonal model
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
It verifies that the six signed facet functionals and the two stated linear isometries preserve the unit hexagon. It then symbolically checks the norming-functional certificates
\[
t-us,\qquad us-t,\qquad s-vt
\]
used to prove symmetric Birkhoff orthogonality in the canonical edge and vertex cases.

Finally, the script verifies the equality pair
\[
x=(1,0),\qquad y=(0,-1)
\]
for rational parameter samples in both regimes \(\alpha\le\beta\) and \(\beta\le\alpha\). These samples are reproducibility checks only; the all-parameter equality is the exact algebraic identity
\[
N(\alpha,-\beta)=\alpha+\beta,
\qquad
N(\beta,\alpha)=\max\{\alpha,\beta\}.
\]

No independent audit or independent validation has been performed.
