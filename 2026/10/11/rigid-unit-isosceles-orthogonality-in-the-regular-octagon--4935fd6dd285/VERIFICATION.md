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
r=\sqrt2-1,
\qquad
d=2-\sqrt2,
\]
and parametrize the reference edge by
\[
x(a)=(1-da,r+da),
\qquad
0\le a\le1.
\]
The quarter-turn map is
\[
R(s,t)=(-t,s).
\]
The exact edge identities are
\[
E_2(a)=R(x(a)),
\qquad
E_6(a)=-R(x(a)).
\]

The analytic proof establishes the following zero table for
\[
F(x,y)=N_8(x+y)-N_8(x-y):
\]
\[
\begin{array}{c|c}
\text{relative edge}&F=0\\
\hline
E_0&\varnothing\\
E_1&(a,b)=(0,1)\\
E_2&a=b\\
E_3&(a,b)=(1,0)\\
E_4&\varnothing\\
E_5&(a,b)=(0,1)\\
E_6&a=b\\
E_7&(a,b)=(1,0).
\end{array}
\]
The isolated endpoint zeros are shared endpoints of the \(E_2\) and \(E_6\) families, so the global equality set is exactly
\[
y=\pm Rx.
\]

The bundled `verify.py` replays all eight edge classes in exact arithmetic in \(\mathbb Q(\sqrt2)\) on a rational parameter grid and checks the exact quarter-turn identities and common chord value. The grid is supplementary; the continuum sign proof is contained in `RESULT.md`.

No independent audit or independent validation has been performed.
