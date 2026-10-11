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

Use Lebesgue measure on
\[
\Omega=[0,1]
\]
and scalar Hilbert spaces
\[
H=K=K_\omega=\mathbb C.
\]
Set
\[
\Lambda_\omega z=z
\]
for every \(\omega\), and set
\[
\Theta_0z=0,\qquad
\Theta_\omega z=-z
\]
for \(0<\omega\le1\).

The frame integrals are
\[
\int_0^1|\Lambda_\omega z|^2\,d\omega
=
|z|^2
\]
and
\[
\int_0^1|\Theta_\omega z|^2\,d\omega
=
|z|^2.
\]
Thus both families are Parseval.

In \(L^2([0,1])\),
\[
T_\Lambda^*h=[h],
\qquad
T_\Theta^*k=[-k],
\]
because the exceptional value of \(T_\Theta^*k\) at \(0\) is invisible to the \(L^2\)-class. Their ranges are therefore the same nonzero one-dimensional subspace.

For the combined family,
\[
\Gamma_0(h\oplus k)=h,
\qquad
\Gamma_\omega(h\oplus k)=h-k
\]
for \(0<\omega\le1\). Pointwise vanishing for every \(\omega\) forces
\[
h=k=0.
\]
But
\[
\Gamma_\omega(1\oplus1)=0
\]
for almost every \(\omega\), so
\[
T_\Gamma^*(1\oplus1)=0.
\]

This verifies both the false positive in the printed criterion and the exact repair: replacing pointwise vanishing by almost-everywhere vanishing makes the kernel condition equal to
\[
\ker T_\Gamma^*=\{0\},
\]
which is equivalent to weak disjointness.

The primary theorem, its complete proof, the coefficient-space definition, and the weak-equality convention were inspected directly in the open preprint, including rendered PDF pages of the theorem and proof.
