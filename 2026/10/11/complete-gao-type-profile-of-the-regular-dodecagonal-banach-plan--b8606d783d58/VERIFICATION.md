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
The verification target is the complete formula for
\[
c_{\mathrm{NJ}}^{(p)}(X_{12})
=
\inf_{x,y\in S_{X_{12}}}
\frac{N_{12}(x+y)^p+N_{12}(x-y)^p}{2^p}.
\]

`verify.py` uses exact symbolic arithmetic in \(\mathbb Q(\sqrt3)\). It reconstructs the twelve regular-dodecagon vertices and the twelve signed supporting facets, verifies all edge incidences, and checks the five dihedral nonincident-edge support certificates whose smallest value is \(4-2\sqrt3>1/2\). This is the finite input needed to reduce the small-difference case to equal or adjacent edges.

The checker verifies the adjacent-edge algebraic identities, including
\[
(2-\sqrt3)(2+\sqrt3)=1,
\qquad
4(2-\sqrt3)=1+(2-\sqrt3)^2,
\]
and the exact one-parameter extremizer family
\[
x=\bigl(1,r(1-2t)\bigr),
\qquad
y=\bigl(1-rt,r+\sqrt3rt\bigr),
\]
for which
\[
N_{12}(x-y)=t,
\qquad
N_{12}(x+y)=2-rt.
\]
It also verifies the balanced coordinate pair used for \(p\ge2\).

The minimization in the real exponent \(p\) is proved analytically in `RESULT.md`: strict calculus on the adjacent-edge line for \(1<p\le2\), concavity on the quadratic boundary for the complementary subquadratic region, and the power-mean inequality for \(p\ge2\). Finite sampling is not used as an infinite proof. No independent audit or independent validation has been performed.
