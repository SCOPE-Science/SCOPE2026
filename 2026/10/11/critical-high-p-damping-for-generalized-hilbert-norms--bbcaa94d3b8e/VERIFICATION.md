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
x=\frac{\alpha+2}{p}.
\]
In the cited exact-norm range,
\[
0<x\le\frac12
\]
and
\[
x\|\mathcal H_b\|
=
\Gamma(1+x)
\frac{\Gamma(b+1-x)}{\Gamma(b+1)}.
\]

Taking logarithms,
\[
\log(x\|\mathcal H_b\|)
=
\log\Gamma(1+x)
+
\log\Gamma(b+1-x)
-
\log\Gamma(b+1).
\]
Taylor's theorem gives
\[
\log\Gamma(1+x)
=
-\gamma x+O(x^2),
\]
and
\[
\log\Gamma(b+1-x)-\log\Gamma(b+1)
=
-x\psi(b+1)
+
\frac{x^2}{2}\psi_1(b+1-\theta x)
\]
for some
\[
0<\theta<1.
\]
Since
\[
b+1-\theta x\ge1/2
\]
and
\[
\psi_1(1/2)=\pi^2/2,
\]
the remainder is bounded by an absolute constant times
\[
x^2
\]
uniformly for every
\[
b\ge0.
\]

Therefore
\[
\log(x\|\mathcal H_b\|)
=
-x(\gamma+\psi(b+1))
+
O(x^2).
\]

For
\[
b\to\infty,
\]
\[
\psi(b+1)=\log b+O(1/b).
\]
Hence at
\[
\log b
=
\frac{p}{\alpha+2}
(\log p+s+o(1)),
\]
one obtains
\[
x\|\mathcal H_b\|
=
p^{-1}e^{-s+o(1)}
\]
and thus
\[
\|\mathcal H_b\|
\to
\frac{e^{-s}}{\alpha+2}.
\]

The same formula gives divergence when the critical-window parameter tends to
\[
-\infty
\]
and convergence to zero when it tends to
\[
+\infty.
\]

For the classical case
\[
b=0,
\]
the identity
\[
B(x,1-x)=\pi/\sin(\pi x)
\]
gives
\[
x\|\mathcal H_0\|=1+O(x^2),
\]
consistent with the uniform formula because
\[
\gamma+\psi(1)=0.
\]

All estimates are analytic and uniform. Numerical beta-function evaluations were only consistency checks and are not used to justify any infinite or asymptotic statement.
