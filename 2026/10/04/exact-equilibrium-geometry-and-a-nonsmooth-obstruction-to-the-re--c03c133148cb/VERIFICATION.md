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

The exact checker `verify.py` evaluates the algebra in \(\mathbb{Q}(\sqrt{230})\) without floating-point dependence for the identities that determine the threshold. It verifies
\[
197x_H^2-20x_H-10=0,
\]
\[
c_H=x_H^2-\frac15x_H
=\frac{1776}{38809}+\frac{291\sqrt{230}}{194045},
\]
and
\[
\frac1{10}\left(1+\frac3{10}x_H^2\right)-x_H\left(2x_H-\frac15\right)=0.
\]
It also checks the two exact endpoint inequalities used to establish stability of the larger positive branch and checks that the computed decimal value of \(c_H\) lies in a narrow stated interval. A successful replay prints `VERIFY_OK`.

The origin instability is not delegated to computation. For the left smooth extension, \(p_-(0)=-c<0\) and \(p_-(\lambda)\to+\infty\) as \(\lambda\to+\infty\), so there is a positive real eigenvalue for every \(c>0\). The associated one-dimensional unstable manifold has a branch in \(x<0\), where the extension coincides with the original vector field. This proves Lyapunov instability of the nonsmooth origin.

Limits: the checker does not establish a first Lyapunov coefficient, a periodic orbit, chaos, or multistability, and the scientific claim does not assert any of those conclusions.
