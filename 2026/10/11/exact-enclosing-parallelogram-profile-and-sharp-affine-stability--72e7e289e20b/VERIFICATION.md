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

For nonzero independent \(u,v\), the tight containing parallelogram has the exact area
\[
|Q(u,v)|=\frac{4h_P(u)h_P(v)}{|\det(u,v)|}.
\]
On each polygonal normal-fan cone, \(h_P\) is a linear functional. With the second normal held fixed, the quotient of support function to determinant is a linear-fractional expression with denominator of fixed sign. Its value inside the cone cannot be less than all values at the cone's extreme rays. Parallel-normal boundary rays give infinite area. Thus a minimizing first normal can be a hexagon edge normal, then likewise the second; this analytic step covers every orientation and is not inferred from computations.

In the basis of generators \(a,b\), the third generator has coordinate magnitudes \(Y/X,Z/X\). Hence the tight parallelogram for those two directions has area
\[
4X(1+Y/X)(1+Z/X)=4(T+XYZ/X^2).
\]
Cyclically permuting the generators proves
\[
q(P)=4(T+XYZ/M^2).
\]

For \(0<r\le s\le1\), the normalized ratio is
\[
\frac{q(P)}{|P|}=1+\frac{rs}{1+r+s}.
\]
This increases in \(s\), giving its sharp upper bound at \(s=1\). The family of generators
\[
a=(1,0),\quad b=(0,1),\quad c=(-1,r)\]
realizes determinant magnitudes \((1,1,r)\) for every \(r\in(0,1]\), hence equality in the stated sharp stability envelope.

The included exact-rational checker verifies these symbolic formulas and several representative polygon areas. It does not replace the all-orientation normal-fan argument or serve as proof of an infinite parameter result.
