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

Set
\[
K=\frac12I_{\mathbb R^2},
\qquad
K^\dagger=2I_{\mathbb R^2}.
\]
For both source families use
\[
\Lambda_{i1}=P_{\operatorname{span}\{e_1\}},
\qquad
\Lambda_{i2}=P_{\operatorname{span}\{e_2\}},
\]
with unit weights and full fusion subspaces.

Every full weave contains one copy of each coordinate projection, so
\[
E(f)=|f_1|^2+|f_2|^2=\|f\|^2.
\]
Since
\[
\|K^*f\|^2=\frac14\|f\|^2,
\]
the constants \(A=B=3\) are valid:
\[
3\|K^*f\|^2
=
\frac34\|f\|^2
\le
E(f)
\le
3\|f\|^2.
\]

For deletion set \(I=\{1\}\),
\[
C=
\sum_{i=1}^{2}\|\Lambda_{i1}\|^2
=
2.
\]
The printed condition is satisfied because
\[
2<3\cdot4=12.
\]
The printed lower bound would be
\[
A-C=1.
\]

After deletion, the energy is
\[
E_{\mathrm{del}}(f)=|f_2|^2.
\]
At \(f=e_1\),
\[
E_{\mathrm{del}}(e_1)=0,
\qquad
\|K^*e_1\|^2=\frac14,
\]
so no positive \(K\)-lower bound exists.

For the corrected estimate, extend a partition of the retained indices to the full index set. The removed contribution is at most
\[
C\|f\|^2
\le
C\|K^\dagger\|^2\|K^*f\|^2.
\]
Subtracting from the full lower frame inequality yields
\[
E_{\mathrm{del}}(f)
\ge
\left(A-C\|K^\dagger\|^2\right)\|K^*f\|^2.
\]
Hence
\[
C\|K^\dagger\|^2<A
\]
is a sufficient deletion condition.

The primary theorem and its proof were inspected directly in the publisher PDF and as page images. The counterexample is exact; no numerical approximation is used.
