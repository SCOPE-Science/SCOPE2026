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
H=H_{\overline\psi}
\]
be nonzero, finite rank, and SRKT.

Because \(H\) is compact and normalized Hardy kernels are weakly null at the boundary,
\[
\|Hk_a\|_2\longrightarrow0
\qquad
(|a|\to1).
\]
Hence there is
\[
a\in\mathbb D
\]
with
\[
\|Hk_a\|_2=\|H\|.
\]

Finite-rank Kronecker theory makes \(\psi\) bounded and rational. Define
\[
\phi_a(z)=\frac{a-z}{1-\overline a z},
\qquad
g=\psi\circ\phi_a-\psi(a).
\]
Boundary composition by \(\phi_a\) preserves the
\[
L^\infty/H^\infty
\]
quotient distance, so
\[
\|g\|_*=\|\psi\|_*.
\]
Harmonic measure gives
\[
\|g\|_2^2
=
\mathcal P(|\psi|^2)(a)-|\psi(a)|^2
=
\|Hk_a\|_2^2.
\]
Thus
\[
\|g\|_2=\|g\|_*.
\]

The checked minimal-norm theorem implies
\[
\|g\|_*=\|g\|_\infty.
\]
Therefore
\[
\|g\|_2=\|g\|_\infty,
\]
so \(|g|\) is constant almost everywhere on the unit circle. Rationality gives
\[
g=CI
\]
with \(I\) finite Blaschke. Undoing \(\phi_a\) and using \(\psi(0)=0\) gives
\[
\psi=C(B-B(0))
\]
for a finite Blaschke product \(B\).

Conversely, for
\[
\psi=C(B-B(0)),
\]
the Bonsall identity reduces to
\[
\|H_{\overline\psi}k_a\|_2^2
=
|C|^2(1-|B(a)|^2).
\]
At a zero of \(B\) this is
\[
|C|^2.
\]
The quotient-distance formula gives
\[
\|\psi\|_*\le|C|,
\]
so
\[
\|\psi\|_G=\|\psi\|_*=|C|.
\]

The kernel is
\[
BH^2,
\]
hence
\[
\operatorname{rank}H_{\overline\psi}
=
\dim(H^2\ominus BH^2)
=
\deg B.
\]
The kernel-testing formula shows that the norming reproducing kernels are exactly the zeros of \(B\).

Finally, because
\[
B(\mathbb T)=\mathbb T,
\]
\[
\|\psi\|_\infty
=
|C|(1+|B(0)|).
\]
Thus \(B(0)\ne0\) gives the strict bounded examples requested in the fresh paper.

No numerical experiment or finite enumeration is used.
