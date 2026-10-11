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
Put
\[
r=\sqrt2-1.
\]
The regular-octagon norm has the eight norm-one support functionals
\[
\pm(1,0),\quad\pm(0,1),\quad
\pm(1,1)/\sqrt2,\quad\pm(1,-1)/\sqrt2.
\]
For every ordered pair \((f,g)\) from this set, the two dual norms
\[
\bigl(N_8^*(f+g),N_8^*(f-g)\bigr)
\]
belong to the exact five-element set
\[
\{(2,0),(0,2),(2,2r),(2r,2),(\sqrt2,\sqrt2)\}.
\]
Each produces an affine upper bound at most \(2+2rt\) on \(0\le t\le1\). This is the finite certificate behind the continuum chord estimate.

For
\[
u=(1,r),
\qquad
v=(-r,1),
\]
direct substitution gives
\[
N_8(u+t v)=N_8(u-t v)=1+rt
\]
for every \(0\le t\le1\). Hence the harmonic numerator is exactly \(1+rt\) on the sharp pair.

For \(1<p<\infty\) and conjugate \(q\), Hölder's inequality gives
\[
\frac{1+rt}{(1+t^p)^{1/p}}
\le
(1+r^q)^{1/q},
\]
with equality at
\[
t=r^{1/(p-1)}.
\]
The endpoint optimizers are \(t=0\) for \(p=1\) and \(t=1\) for \(p=\infty\).

`verify.py` enumerates all support pairs and checks representative exponent profiles from the actual packaged source. Its dense grids are reproducibility checks only; the finite support enumeration and Hölder equality above are the proof.

No independent audit or independent validation has been performed.
