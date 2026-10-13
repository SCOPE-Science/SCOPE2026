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
The exact raw moment is
\[
\mu_r'
=
(1-p)\alpha\beta
\int_0^\infty
\frac{
y^{\beta-1}e^{-r y-\alpha y^\beta}
}{
[1-p+p e^{-\alpha y^\beta}]^2
}\,dy.
\]

For
\[
\alpha=\beta=1,\qquad p=1/2,\qquad r=1,
\]
direct integration gives
\[
\mu_1'=2\log2-1.
\]
The source's printed Eq. (5.9) instead reduces to
\[
(1-p)\sum_{i\ge0}p^iH_{i+1}
=
-\frac{\log(1-p)}{p},
\]
which equals \(2\log2\) at \(p=1/2\).

On the slice \(\beta=1\),
\[
\mu_r'
=
\frac{
{}_2F_1\!\left(
2,1+r/\alpha;
2+r/\alpha;
-p/(1-p)
\right)
}{
(1-p)(1+r/\alpha)
}.
\]
The standalone checker compares this formula with direct quadrature for several parameter values and verifies the elementary special case
\[
\alpha=2,\qquad p=1/2,\qquad r=1,
\]
where
\[
\mu_1'=\pi/2-1.
\]

Finite computation is used only as a consistency check; the counterexample and corrected formulas are analytic.
