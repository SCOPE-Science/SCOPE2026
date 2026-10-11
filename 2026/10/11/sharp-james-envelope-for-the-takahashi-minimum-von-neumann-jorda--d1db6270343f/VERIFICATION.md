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
For the universal step, after normalization set
\[
c=J(X)-1,
\qquad
0\le r\le1.
\]
The proof obtains
\[
\min\{\|x+y\|,\|x-y\|\}\le1+cr.
\]
The scalar optimization is exact because
\[
(1+c^2)(1+r^2)-(1+cr)^2=(c-r)^2.
\]
Hence
\[
\frac{(1+cr)^2}{1+r^2}\le1+c^2.
\]

For the affine-regular hexagon, the analytic proof reduces the James estimate to four edge classes by two explicit isometries. The nontrivial edge formulas are
\[
A=\max\{1+c,1+a\},
\qquad
B=2-a-c,
\]
and
\[
A=1+a-b,
\qquad
B=\max\{1+b,2-a\}.
\]
Each pair forbids \(A>3/2\) and \(B>3/2\) simultaneously.

The exact Takahashi witness is
\[
p=(1,0),
\qquad
q=(-1/4,-1/2),
\]
for which
\[
N(p)=1,\quad N(q)=1/2,\quad N(p+q)=N(p-q)=5/4.
\]
Thus its quotient is exactly \(5/4\).

`verify.py` checks these formulas and witnesses with exact rational arithmetic on finite grids. The finite checks are supplementary only; the displayed identities and edge inequalities prove the continuum theorem.

No independent audit or independent validation has been performed.
