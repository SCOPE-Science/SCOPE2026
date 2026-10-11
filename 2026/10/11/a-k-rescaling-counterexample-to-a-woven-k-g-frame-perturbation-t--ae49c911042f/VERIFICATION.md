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
K=\frac14I_{\mathbb C^2}.
\]
Then
\[
\|K^*f\|^2=\frac1{16}\|f\|^2.
\]
For both coordinate families,
\[
\sum_{i=1}^2\|\Lambda_i f\|^2
=
\sum_{i=1}^2\|\Gamma_i f\|^2
=
\|f\|^2.
\]
Thus
\[
A_1=A_2=16,\qquad B_1=B_2=1
\]
are valid bounds.

For \(c=(c_1,c_2)\),
\[
(\Lambda_1^*-\Gamma_1^*)c_1=c_1(e_1-e_2)
\]
and
\[
(\Lambda_2^*-\Gamma_2^*)c_2=c_2(e_2-e_1).
\]
Therefore
\[
\left(
\sum_i\|(\Lambda_i^*-\Gamma_i^*)c_i\|^2
\right)^{1/2}
=
\sqrt2\,\|c\|.
\]
At
\[
\alpha=\beta=\mu=\frac34,
\]
the right side of the printed perturbation inequality is
\[
\frac94\|c\|,
\]
and the scalar smallness condition is
\[
\frac94
<
\frac{16}{2(1+1)}
=
4.
\]

For the weave using \(\Lambda_1\) and \(\Gamma_2\),
\[
|\Lambda_1e_2|^2+|\Gamma_2e_2|^2=0,
\]
while
\[
\|K^*e_2\|^2=\frac1{16}.
\]
Hence no positive lower \(K\)-\(g\)-frame bound exists.

The open publisher PDF was inspected at the theorem statement and proof. The proof explicitly introduces \(\|K^\dagger\|\) after the printed smallness hypothesis, consistent with the scale-dependence exposed by the example.
