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

Let \(S\) be the unilateral shift on \(\ell^2(\mathbb N)\):
\[
S(x_1,x_2,\ldots)=(0,x_1,x_2,\ldots).
\]
Then
\[
S^*S=I,
\qquad
SS^*=I-P_{\operatorname{span}\{e_1\}}.
\]

For the standard coordinate \(g\)-frame
\[
\Lambda_jx=\Gamma_jx=x_j,
\]
choose
\[
O_1=O_2=S^*.
\]
The published exact hypothesis is satisfied:
\[
O_2O_1^*=S^*S=I.
\]
The transformed coefficients are
\[
\Lambda_jO_1x=\Gamma_jO_2x=x_{j+1},
\]
so
\[
\sum_j|\Lambda_jO_1x|^2
=
\|x\|^2-|x_1|^2.
\]
At \(e_1\) this is zero, proving failure of the lower frame bound.

Independently, the synthesis identity is
\[
T_{\Lambda O_1}=O_1^*T_\Lambda,
\qquad
T_{\Gamma O_2}=O_2^*T_\Gamma.
\]
For an original dual pair,
\[
T_\Gamma T_\Lambda^*=I,
\]
and therefore
\[
T_{\Gamma O_2}T_{\Lambda O_1}^*=O_2^*O_1.
\]
This proves the corrected exact criterion and, by taking operator-norm distance from the identity, the corrected approximate criterion.

The complete source theorem and proof were inspected in the open-access version of record. No numerical approximation, finite truncation, or experimental extrapolation is used.
