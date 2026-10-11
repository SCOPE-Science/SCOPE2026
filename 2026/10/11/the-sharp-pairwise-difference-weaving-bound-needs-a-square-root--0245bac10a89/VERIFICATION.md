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

Define
\[
E_i(J;f)
=
\int_J\|\Lambda_{\omega i}f\|^2\,d\mu(\omega)
\]
and
\[
D_{ij}(J;f)
=
\int_J\|(\Lambda_{\omega i}-\Lambda_{\omega j})f\|^2\,d\mu(\omega).
\]
The hypothesis gives
\[
D_{ij}(J;f)\le M E_j(J;f).
\]
Minkowski in the coefficient Hilbert space gives
\[
E_i(J;f)^{1/2}
\le
D_{ij}(J;f)^{1/2}+E_j(J;f)^{1/2}
\le
(1+\sqrt M)E_j(J;f)^{1/2}.
\]
Thus
\[
E_i(J;f)\le(1+\sqrt M)^2E_j(J;f).
\]

For a partition \(\{\sigma_j\}_{j=1}^m\),
\[
A\|K^*f\|^2
\le
\sum_{j=1}^m\sum_{i=1}^mE_i(\sigma_j;f)
\le
\left(1+(m-1)(1+\sqrt M)^2\right)
\sum_{j=1}^mE_j(\sigma_j;f).
\]
This proves the corrected lower bound.

For sharpness, take a one-point measure space, \(H=\mathbb C\), \(K=I\), and
\[
c=1+\sqrt M,\qquad
\Lambda_1=I,\qquad
\Lambda_i=cI\quad(2\le i\le m).
\]
The pairwise hypothesis holds because
\[
|c-1|^2=M
\]
and the smaller individual energy is \(1\). The summed exact lower bound is
\[
A=1+(m-1)c^2.
\]
A weave selecting family \(1\) has exact lower bound \(1\), and the corrected formula equals
\[
\frac{A}{1+(m-1)c^2}=1.
\]

The source formula instead equals
\[
1+
\frac{2(m-1)\sqrt M}
{1+(m-1)(M+1)},
\]
which is strictly larger than \(1\) for every \(m\ge2\) and \(M>0\).

The primary full text was inspected at Theorem 4 and its proof. The later 2022 comparison source was inspected at Theorem 3.6 and its proof. No numerical experiment or finite enumeration is used.
