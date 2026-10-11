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

Set
\[
\alpha=a-\frac\pi2,
\qquad
\beta=b-\frac\pi4,
\qquad
M=m+n.
\]
The exact phase vector field checked is
\[
a'=-\cos a\bigl(n\sin a\cos b+m\sin b\bigr),
\]
\[
b'=\sin b\cos b\bigl(\cos b-\sin a\sin b\bigr).
\]

Symbolic expansion gives
\[
\alpha'
=
\frac{M}{\sqrt2}\alpha
+
\frac{m-n}{\sqrt2}\alpha\beta
+
O\!\left(\|(\alpha,\beta)\|^3\right),
\]
and
\[
\beta'
=
-\frac{\beta}{\sqrt2}
+
\frac{\alpha^2}{4\sqrt2}
+
O\!\left(\|(\alpha,\beta)\|^3\right).
\]
Substituting
\[
\beta=c\alpha^2+O(|\alpha|^3)
\]
in the invariant-manifold equation yields
\[
c=\frac1{4(2M+1)}.
\]

The checker then verifies
\[
\csc\left(\frac\pi2+\alpha\right)-1
=
\frac{\alpha^2}{2}+O(\alpha^4)
\]
and
\[
\tan\left(\frac\pi4+c\alpha^2+O(\alpha^3)\right)-1
=
2c\alpha^2+O(\alpha^3),
\]
so their leading-coefficient ratio is exactly
\[
2M+1.
\]

The final step is analytic rather than computational. With
\[
w=\frac yx-1,
\]
the identity \(y=x(1+w)\) gives
\[
xw'=\frac{dy}{dx}-\frac yx.
\]
The verified ratio expansion therefore implies
\[
xw'=2Mw+O(w^{3/2}).
\]
As \(x\downarrow0\) on the classified nontrivial end, asymptotic integration gives
\[
w=Cx^{2M}(1+o(1))
\]
for some \(C>0\), and hence
\[
y=x+C x^{2M+1}+o(x^{2M+1}).
\]

No finite enumeration or numerical experiment is used to infer the infinite family.
