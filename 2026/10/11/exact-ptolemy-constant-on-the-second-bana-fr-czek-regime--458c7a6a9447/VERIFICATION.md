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

For \(\lambda>\sqrt2\), set
\[
c=\frac{\lambda^2}{2},
\qquad
d=\frac{\lambda^2}{2(\lambda^2-1)},
\qquad
H(v)^2=cv_1^2+dv_2^2.
\]
If \(F(v)=\lambda|v_1|\ge E(v)\), then
\[
v_2^2\le(\lambda^2-1)v_1^2
\]
and
\[
H(v)^2\le\lambda^2v_1^2=F(v)^2.
\]
If \(E(v)\ge F(v)\), then
\[
v_2^2\ge(\lambda^2-1)v_1^2
\]
and
\[
H(v)^2-E(v)^2
\le
\left[
\frac{\lambda^2-2}{2}
-
\frac{\lambda^2-2}{2}
\right]v_1^2
=0.
\]
Hence \(H\le N_\lambda\) globally.

For a mixed active pair,
\[
E(a)F(b)
\le
\frac{\lambda}{\sqrt{cd}}H(a)H(b)
=
2\sqrt{1-\lambda^{-2}}\,H(a)H(b).
\]
Hilbert Ptolemy then gives the claimed global upper bound for all mixed numerator cases. Same-branch cases have factor \(1\).

With
\[
t_\lambda=\sqrt{\lambda^2-1},
\]
the triple
\[
x=(1,t_\lambda),\qquad
y=(1,-t_\lambda),\qquad
z=(2,0)
\]
satisfies
\[
N_\lambda(x)=N_\lambda(y)
=
N_\lambda(x-z)=N_\lambda(z-y)=\lambda,
\]
\[
N_\lambda(x-y)=2t_\lambda,
\qquad
N_\lambda(z)=2\lambda.
\]
Its ratio is therefore
\[
2\sqrt{1-\lambda^{-2}}.
\]

No finite enumeration, numerical optimization, or unproved computation is used. The only unresolved scientific scope is the generalized \(p\)-family and bibliographic coverage outside the checked sources.
