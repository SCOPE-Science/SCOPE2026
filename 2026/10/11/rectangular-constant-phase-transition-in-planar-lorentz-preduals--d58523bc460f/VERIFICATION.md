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

Set \(c=1+w\) and \(d=1-w\). The two candidate normalized triples are
\[
(x,y,t)=\left((1,w),(-c/2,c/2),2d/c\right)
\]
and
\[
(x,y,t)=\left((1,w),(0,-1),2w\right).
\]
Both satisfy \(x\perp_B y\), because at the vertex \((1,w)\) the first is annihilated by the slanted norming functional and the second by the axial norming functional. Their final vectors are respectively \((w,1)\) and \((1,-w)\), both of norm one. Their quotients are exactly \(1+2d/c\) and \(1+2w\).

For an arbitrary vertex and normalized orthogonal direction, sign and coordinate symmetries give \(x=(1,w)\) and either \(y=(-a,b)\) or \(y=(a,-b)\), where \(0\le a\le c/2\) and \(b=1\) for \(a\le w\), \(b=c-a\) otherwise. In the first sign case, the norm is bounded from below by the maximum of \(1+(b-a)t/c\) and \(w+bt\). These intersect at \(t=cd/(a+wb)\), where the true vector is a positive multiple of \((w,1)\). The ratio is maximized precisely there, and its value is
\[
R_+(a)=\frac{a+wb+1-w^2}{wa+b}.
\]
On the first piece its derivative equals \((1-w)^2(1+w)/(1+wa)^2>0\); on the second piece its derivative equals \(2dc/(c-da)^2>0\). Therefore the unique maximum is at \(a=c/2\).

In the opposite sign case the sharp affine lower bounds are \(1+at\) and \((d+(a+b)t)/c\). They intersect at \(t=2w/(b-wa)\) and the final vector is a positive multiple of \((1,-w)\). The exact maximum is
\[
R_-(a)=1+\frac{2w(1-a)}{b+wa}.
\]
Its derivatives are \(-2w(1+w)/(1+wa)^2<0\) on the first piece and \(-4w^2/(c-da)^2<0\) on the second, so its unique maximum occurs at \(a=0\).

In axial edge interiors one has an upper bound strictly below \(1+2w\); in diagonal edge interiors an upper bound strictly below \(1+2d/c\). Thus the two displayed types exhaust all normalized maximizers. The crossing condition \(w=d/c\) is the unique positive solution \(w=\sqrt2-1\).

The displayed rational derivatives and endpoint substitutions were checked symbolically from their algebraic definitions. A finite numerical optimization over representative parameters was used only for exploratory stress testing; neither that test nor an incomplete enumeration is used as proof. Independent external validation has not been performed.
