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
The verification target is
\[
\left\{
N_8(x+y):
x,y\in S_{X_8},\ x\perp_B y
\right\}
=
\left[
\frac{3\sqrt2}{2}-1,\
1+\frac1{\sqrt2}
\right].
\]

`verify.py` uses exact rational-pair arithmetic in \(\mathbb Q(\sqrt2)\). It reconstructs the eight signed supporting facets of
\[
N_8(s,t)=
\max\left\{
|s|,\ |t|,\ \frac{|s|+|t|}{\sqrt2}
\right\}.
\]

The checker verifies the active supports at the representative edge and vertex. It then certifies each one-parameter norm formula from the proof by endpoint inequalities against every signed facet. Since each difference between a candidate active affine value and a facet value is affine in the segment parameter, nonnegativity at both endpoints proves the inequality on the full segment; an active facet with equality at both endpoints proves exactness.

Finally, the checker verifies the two endpoint Birkhoff witnesses and
\[
\delta_B(X_8)=\frac{2-\sqrt2}{4},
\qquad
\rho_B(X_8)=\frac{3(2-\sqrt2)}{4}.
\]
No finite sample is used as a substitute for a continuum proof. No independent audit or independent validation has been performed.
