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
For a smooth complete-intersection threefold of codimension \(c\) and multidegree \(\mathbf d\), put
\[
m=\sum_i d_i-c-4>0.
\]
The proof uses
\[
p_g
=
1+
\frac{m}{48}
\left(\prod_i d_i\right)
\left(
m^2+\sum_i d_i^2-c-4
\right).
\]

The bundled checker verifies this expression independently against the degree-\(m\) coefficient of the complete-intersection Hilbert series
\[
\frac{\prod_i(1-t^{d_i})}{(1-t)^{c+4}},
\]
which equals \(h^0(K_X)\).

For a balancing move
\[
(a,b)\mapsto(a+1,b-1),
\qquad
b-a\ge2,
\]
the proof factors the change as
\[
\frac{mP\delta}{48}
\left(
R-2ab-2\delta
\right),
\]
where \(P\) is the product of the untouched degrees and \(\delta=b-a-1\). Writing
\[
r=c-2,\qquad u=a-2,\qquad t=b-a-2,
\]
and the untouched degrees as \(2+w_j\), the last factor is exactly
\[
\begin{aligned}
&(r-1)(r+4)
+4u(r+u+t)
+2t(r+t+1)\\
&\quad
+2W(r+2u+t+2)
+W^2
+\sum_j w_j^2,
\end{aligned}
\]
with \(W=\sum_jw_j\).

This identity proves nonnegativity in the general-type range and leaves exactly three equality types. The checker replays these identities and the resulting fixed-sum extrema over a bounded grid as regression evidence; no finite enumeration is used to infer the infinite theorem.

Limits: smooth ordinary projective complete intersections, complex dimension three, and the general-type range only.
