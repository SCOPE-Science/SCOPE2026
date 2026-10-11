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

For
\[
N(s,t)=\max\{|s|,|t|,|s-t|\},
\]
the six vertices of the unit ball are
\[
(1,1),\ (1,0),\ (0,-1),\ (-1,-1),\ (-1,0),\ (0,1).
\]
The displayed linear coordinate transformations preserve \(N\) and move any vertex to any other vertex.

At
\[
v=(1,1),
\]
the norming functionals form the segment joining the two coordinate functionals. Therefore
\[
v\perp_B(w_1,w_2)
\]
exactly when
\[
w_1w_2\le0.
\]
After scaling and coordinate interchange, every non-axis direction is
\[
w=(q,-1),\qquad q\ge1.
\]

For \(u,t\ge0\),
\[
N(v-u w)=
\begin{cases}
1+u,&0\le u\le q^{-1},\\
(q+1)u,&u\ge q^{-1},
\end{cases}
\]
and
\[
N(v+t w)=
\begin{cases}
1+qt,&0\le t\le1,\\
(q+1)t,&t\ge1.
\end{cases}
\]
Solving the two sides at a common norm level and taking the midpoint parameter gives
\[
m(v,w)=1+\frac{q-1}{2q^2}.
\]
The derivative is
\[
\frac{2-q}{2q^3},
\]
so the unique maximum for \(q\ge1\) occurs at \(q=2\), with value \(9/8\). The checked two-dimensional frame theorem therefore gives
\[
DW(X)=2\cdot\frac98=\frac94.
\]

Finally,
\[
x=(-1,-2),\qquad y=(-1,0)
\]
satisfy
\[
N(x)=2,\quad N(y)=1,\quad N(x-y)=2,
\]
and
\[
N\!\left(\frac{x}{N(x)}-\frac{y}{N(y)}\right)=\frac32.
\]
Thus the original quotient is exactly
\[
\frac32\cdot\frac32=\frac94.
\]

No numerical optimization, finite enumeration, or external certificate is used as proof.
