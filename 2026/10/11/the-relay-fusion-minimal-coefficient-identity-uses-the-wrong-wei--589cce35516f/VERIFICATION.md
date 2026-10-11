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

For the one-block relay system
\[
H=K_1=V_{11}=W_1=\mathbb C,\qquad
\Lambda_1=I,\qquad
v_{11}=2,
\]
the relay energy is
\[
4|f|^2,
\]
so
\[
S_{\mathcal R}=4I
\]
and
\[
\widehat\Lambda_1=\frac14I.
\]

At \(f=1\), the hypothesis of Theorem 3.14 forces
\[
g_{11}=\frac14.
\]
The asserted left side is
\[
\left|\frac14\right|^2=\frac1{16}.
\]
The first right-side term is
\[
4\left|\frac14\right|^2=\frac14,
\]
and the residual term is
\[
\left|\frac14-4\frac14\right|^2=\frac9{16}.
\]
Thus the asserted equality fails exactly.

For the repair, let
\[
a_{ij}=A_{ij}S_{\mathcal R}^{-1}f.
\]
The source's own inner-product calculation gives
\[
\sum_{i,j}v_{ij}^2\|a_{ij}\|^2
=
\sum_{i,j}v_{ij}^2\langle g_{ij},a_{ij}\rangle.
\]
Hence
\[
\sum_{i,j}v_{ij}^2
\langle g_{ij}-a_{ij},a_{ij}\rangle=0.
\]
Applying Pythagoras in the weighted coefficient inner product yields the corrected identity.

As a second check, define
\[
h_{ij}=v_{ij}g_{ij}.
\]
Then the reconstruction constraint is precisely
\[
T_{\mathcal R}^*h=f,
\]
and the canonical minimum-norm coefficient vector is
\[
T_{\mathcal R}S_{\mathcal R}^{-1}f
=
\{v_{ij}a_{ij}\}_{i,j}.
\]
Its ordinary direct-sum norm is exactly the weighted \(g\)-norm in the repaired formula.

The primary source was inspected at the definitions of the representation space, analysis and synthesis operators, the canonical dual, the theorem statement, and its complete proof. All checks are symbolic.
