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

The cited full text gives
\[
DW(X)=2\sup_{p\in S_X}M(p)
\]
and reduces the two-dimensional calculation to extreme points.

For
\[
p_a=(a,b),\qquad q_a=(b,-a),\qquad
a^2+b^2=1,\qquad\frac1{\sqrt2}<a<1,
\]
the source proves:
\[
m(p_a,q_a)=\frac1a<\sqrt2
\]
when \(a\le2b\), and
\[
m(p_a,q_a)<a+b<\sqrt2
\]
when \(a>2b\). For the nonsmooth corner \(w=(1,-1)\),
\[
m(w,p_a)=a(a+b)<\sqrt2.
\]
The diagonal and axis endpoints give \(m=1\) by direct equal-level evaluation.

Thus no frame/extreme-point contribution equals \(\sqrt2\). The frame reduction therefore rules out equality in the unit-sphere Dunkl--Williams quotient.

For sharpness, choose \(a\downarrow1/\sqrt2\), let \(b=\sqrt{1-a^2}\), and take
\[
\mu\ge\frac{a+b}{a-b},
\qquad
\lambda=-\mu+\frac{2b}{a},
\qquad
r=\mu a-b.
\]
With
\[
u=\frac{p_a+\lambda q_a}{r},
\qquad
v=\frac{p_a+\mu q_a}{r},
\]
the source's equal-level formulas give
\[
\|u\|=\|v\|=1,
\]
the minimum norm on the joining segment is \(1/r\), and
\[
\|u+v\|=\frac{2}{ar}.
\]
Hence the exact quotient is
\[
\frac2a\longrightarrow2\sqrt2.
\]

No numerical sampling, finite enumeration, or external certificate is used as proof.
