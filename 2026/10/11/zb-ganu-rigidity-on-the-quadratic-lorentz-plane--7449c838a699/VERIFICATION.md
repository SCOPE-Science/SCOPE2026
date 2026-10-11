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
N_\omega(u,v)^2
=
\max\{u^2+\omega v^2,\omega u^2+v^2\},
\]
one has
\[
\frac{1+\omega}{2}(u^2+v^2)
\le
N_\omega(u,v)^2
\le
u^2+v^2.
\]
Lower equality holds exactly when \(|u|=|v|\); nonzero upper equality holds exactly when \(uv=0\).

With
\[
p=x+y,\qquad q=x-y,
\]
the exact comparison chain is
\[
N_\omega(p)N_\omega(q)
\le
E(p)E(q)
\le
\frac{E(p)^2+E(q)^2}{2}
=
E(x)^2+E(y)^2
\le
\frac{2}{1+\omega}
\bigl(N_\omega(x)^2+N_\omega(y)^2\bigr).
\]
The pair
\[
x=(1,1),\qquad y=(1,-1)
\]
attains the resulting bound.

If equality holds, \(p\) and \(q\) are nonzero axis vectors, their Euclidean lengths are equal, and both \(x\) and \(y\) lie on diagonal rays. The axis vectors must use distinct axes, so after the natural symmetries
\[
p=(2r,0),\qquad q=(0,2r),
\]
which gives
\[
x=r(1,1),\qquad y=r(1,-1).
\]
This proves both the value and the complete equality classification.

No numerical experiment, finite enumeration, or external certificate is used as proof.
