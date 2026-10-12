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
For a fixed cumulative level \(p\in(0,1)\), set
\[
b=1+\alpha,
\qquad
x=\alpha/Q_p(\alpha).
\]
Then
\[
p=
\left(1+\frac{x}{2b}\right)e^{-x},
\qquad
\frac{dx}{db}
=
-\frac{x}{b(2b+x-1)}.
\]

The hazard at that quantile is
\[
H_p(\alpha)
=
\frac{p}{1-p}
\frac{x^2(2b+x-1)}
{(b-1)(2b+x)}.
\]
Its logarithmic derivative is
\[
-
\frac{
4b^3+4b^2x-2b^2+bx^2-2b-2x+1
}{
b(b-1)(2b+x-1)^2
},
\]
which is strictly negative.

The included checker compares these analytic derivatives with finite differences across a parameter grid and confirms the strict sign.

For
\[
(\alpha_1,\alpha_2,p)=(1.5,0.7,0.4),
\]
it obtains
\[
H_p(\alpha_1)=0.4648096557\ldots,
\qquad
H_p(\alpha_2)=1.1177202352\ldots,
\]
so the stress increase produces a strictly upward jump.
