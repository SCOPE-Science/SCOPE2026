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

The source presentation is
\[
F_m=\langle x,y,a\mid (yx)^m y (yx)^{-m}x^{-1}=1,\ (x^{-1}ax)a^{-1}x^{-1}(yay^{-1})=1\rangle.
\]
The meridian constraint is \(x=\sigma\) for the \(B\)-family and \(a=\sigma\) for the \(G\)-family, with \(\sigma=(15432)\in A_5\).

The verifier constructs \(A_5\) as the sixty even permutations of five letters. It independently computes the set of element orders as \(\{1,2,3,5}\), hence the exponent as \(30\). This proves exact period \(30\) divisibility for the parameter-dependent word.

For each of the thirty residues, it checks all \(60^2\) assignments of the two unconstrained generators on each side. The resulting certificate has
\[
(N_B,N_G)=(6,1)
\]
for the ten residues \(1,4,7,\ldots,28\), and
\[
(N_B,N_G)=(1,1)
\]
for the other twenty residues. It then recomputes a shifted full period and the source's printed cases \(m=1\) and \(m=61\).

The replay output is:

`VERIFY_OK A5_size=60 exponent=30 residues=30 distinguished=10 pattern=m_mod_3_eq_1 source_case=true`

The finite enumeration is exhaustive because exact group periodicity has already reduced the unbounded integer parameter to these thirty cases.

The independent-audit channel has not been performed.
