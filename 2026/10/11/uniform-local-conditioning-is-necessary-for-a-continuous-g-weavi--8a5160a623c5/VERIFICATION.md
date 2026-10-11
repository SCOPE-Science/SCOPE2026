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

For the first example, let
\[
\Lambda_n f=f_n
\]
on
\[
H=\ell^2(\mathbb N).
\]
Then
\[
\sum_n|\Lambda_nf|^2=\|f\|^2.
\]
The local one-point frame
\[
F_n(*)=\frac1n
\]
has exact frame bound \(1/n^2\). Since
\[
\Lambda_n^*F_n(*)=\frac1n e_n,
\]
the induced energy is
\[
\sum_n\frac{|f_n|^2}{n^2}.
\]
For \(f=e_N\), this equals \(1/N^2\), so no positive lower frame bound exists.

For the second example, let
\[
\Lambda_n f=\frac{f_n}{n}
\]
and use the local one-point frame
\[
F_n(*)=n.
\]
Then
\[
\Lambda_n^*F_n(*)=e_n,
\]
so the induced family is Parseval, while the outer energy is again
\[
\sum_n\frac{|f_n|^2}{n^2}
\]
and has no positive lower bound.

For the repair, the local inequalities
\[
a\|\Lambda_{\omega}f\|^2
\le
\int|\langle\Lambda_{\omega}f,F_{\omega}(x)\rangle|^2\,d\mu(x)
\le
b\|\Lambda_{\omega}f\|^2
\]
are integrated over the chosen outer weave. This gives
\[
aE_g(f)\le E_{\mathrm{vec}}(f)\le bE_g(f)
\]
without any approximation.

The 2020 theorem statement and relevant proof were inspected in a public full-text rendering. The later 2023 version-of-record PDF was inspected both as extracted text and as page images on printed pages 571--572, where the same infimum/supremum mechanism appears.
