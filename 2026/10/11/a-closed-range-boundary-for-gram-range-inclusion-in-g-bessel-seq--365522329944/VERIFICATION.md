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

For
\[
\Lambda_nx=\frac{x_n}{n}
\]
on \(\ell^2(\mathbb N)\),
\[
\sum_n\|\Lambda_nx\|^2
=
\sum_n\frac{|x_n|^2}{n^2}
\le
\|x\|^2.
\]
Thus the family is \(g\)-Bessel.

The synthesis operator and Gram operator are
\[
T(c_n)=\left(\frac{c_n}{n}\right),
\qquad
G(c_n)=\left(\frac{c_n}{n^2}\right).
\]
Because \(T=T^*\), let
\[
x=(1/n)_{n\ge1}\in\ell^2
\]
and
\[
y=Tx=(1/n^2)_{n\ge1}.
\]
Then
\[
y\in R(T^*).
\]
If
\[
y=Gz,
\]
then coordinatewise
\[
z_n=1
\]
for every \(n\), contradicting \(z\in\ell^2\). Hence
\[
R(T^*)\not\subseteq R(G).
\]

For the exact repair, the inclusion
\[
R(T^*T)\subseteq R(T^*)
\]
always holds. Closed range of \(T\) gives the reverse inclusion by decomposing the preimage of \(T^*\) along
\[
R(T)\oplus N(T^*).
\]
Conversely, Douglas factorization turns
\[
R(T^*)\subseteq R(T^*T)
\]
into
\[
T^*T\le\lambda(T^*T)^2.
\]
The spectrum of \(T^*T\) away from zero is therefore bounded below by \(\lambda^{-1}\), so \(T\) has closed range.

The complete discrete and continuous lemmas and their proofs were materially inspected in the published full texts. No numerical approximation, truncation, or finite experimental inference is used.
