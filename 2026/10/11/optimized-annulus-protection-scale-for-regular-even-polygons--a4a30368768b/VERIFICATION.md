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

Let
\[
s=\sin^2\frac{\pi}{N},
\qquad
u=
\frac{3-2s-2\sqrt2(1-s)}
{1+4s-4s^2}.
\]
The exact active-bound equation is
\[
(1+4s-4s^2)u^2+(4s-6)u+1=0.
\]
Its discriminant is
\[
32(1-s)^2.
\]

For a regular even polygon of minimal width \(1\),
\[
c=\tan\frac{\pi}{N},
\]
so the two active source bounds are
\[
A(\lambda)=(1-\lambda)s
\]
and
\[
B(\lambda)=
\frac12\left(1-\sqrt{1-\lambda^2\tan^2\frac{\pi}{N}}\right).
\]
The checker confirms symbolically that \(\lambda=1-u\) makes \(A=B=su\).

It also verifies the limiting identity
\[
\lim_{s\downarrow0}u=3-2\sqrt2,
\]
which, together with \(\sin(\pi/N)\sim\pi/N\), gives the stated asymptotic.

The finite numerical sweep over even \(6\le N\le400\) checks the branch choice, the inactivity of the fourth source bound, and the global one-parameter optimization. These checks are supplementary; the proof for all even \(N\ge6\) is analytic.
