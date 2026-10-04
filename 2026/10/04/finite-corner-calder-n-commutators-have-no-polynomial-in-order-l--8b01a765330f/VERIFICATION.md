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

Let
\[
\mathbb R=I_1\cup\cdots\cup I_N
\]
up to the finitely many breakpoints, with \(A\) affine on each \(I_j\) and
\[
L=\|A'\|_\infty.
\]

For a diagonal block, the divided difference equals the local slope \(s_j\), hence
\[
\|\mathbf1_{I_j}T_{A,n}\mathbf1_{I_j}\|_{2\to2}
\le
\pi |s_j|^n
\le
\pi L^n.
\]

For two different intervals, Lipschitz continuity gives
\[
|K_n(x,y)|\le L^n|x-y|^{-1}.
\]
If a point \(c\) separates the intervals and
\[
u=x-c,
\qquad
v=c-y,
\]
then
\[
|x-y|=u+v.
\]
The positive majorant is therefore a restriction of the Carleman operator. With
\[
\phi(u)=u^{-1/2},
\]
one has
\[
\int_0^\infty\frac{\phi(v)}{u+v}\,dv
=
\pi\phi(u),
\]
and the symmetric identity in the other variable. The weighted Schur test gives norm at most \(\pi\).

Thus every one of the \(N^2\) blocks has norm at most \(\pi L^n\). The operator norm of the resulting finite block matrix is at most
\[
\pi N L^n.
\]

The proof is exact and uses no numerical experiment, finite truncation, or unproved asymptotic assumption.
