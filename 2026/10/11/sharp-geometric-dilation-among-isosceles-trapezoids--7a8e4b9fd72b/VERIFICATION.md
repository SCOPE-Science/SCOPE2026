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

Normalize an isosceles trapezoid to bases
\[
1-x,\qquad 1+x,
\]
height \(H\), and leg length
\[
S=\sqrt{x^2+H^2}.
\]
Its half-perimeter is \(1+S\).

Direct arc-length pairing gives the exact minimum halving distance
\[
h=
\min\left\{
H,\,
1+\frac{x^2}{S},\,
\sqrt{\frac{(S-x)(S+1)^2}{2S}}
\right\},
\]
with the third branch present exactly when
\[
1\le S\le1+2x.
\]

The checker symbolically verifies all three chord quadratics, the branch switch
\[
x_0(S)=\frac{2S+1-S^2}{2S},
\]
and the quintic
\[
11S^5-17S^4+6S^3-2S^2-5S-1.
\]
After the substitution \(S=1+y\), Descartes' rule gives one positive root because the coefficient signs have exactly one change.

The two fixed-\(S\) optimum branches are checked symbolically: the \(A=C\) branch has positive derivative, while the \(B=C\) branch satisfies a parametrization \(S(r)\) with negative derivative. Therefore their unique junction is the global optimum.

`verify.py` additionally reconstructs boundary points and directly samples halving chords for many trapezoids. These finite computations are regression checks only; the universal proof is the exact piecewise analysis above.
