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
\varphi(x)=\forall y\,\forall z\,([x,y,z]=1).
\]

The source gives
\[
G=B(3,3)=F_{\mathcal V_3}(x,y,z),
\qquad
a=[x,y],
\qquad
A=\langle a,z\rangle.
\]
It also gives
\[
a\ne1.
\]

For every exponent-three extension
\[
H\ge G
\]
and every \(b,c\in H\),
\[
[a,b,c]=[[x,y],b,c]=1.
\]
Embedding \(G\) into a model \(M_0\models T_3^*\) therefore gives
\[
M_0\models\varphi(a).
\]

In
\[
B=A*_{\mathcal V_3}F_{\mathcal V_3}(v,w),
\]
Example 5.1 gives
\[
[a,v,w]\ne1.
\]
Embedding \(B\) into a model \(M_1\models T_3^*\) therefore gives
\[
M_1\models\neg\varphi(a).
\]

Both copies of \(a\) are nonidentity elements of order \(3\). A parameter-free one-variable group term reduces to \(x^m\), so an atomic one-variable equation reduces to
\[
x^{m-n}=1.
\]
Its truth on a nonidentity exponent-three element depends only on divisibility of \(m-n\) by \(3\). Hence the two copies of \(a\) have identical parameter-free quantifier-free one-types.

Therefore \(\varphi\) is not equivalent modulo \(T_3^*\) to any quantifier-free formula. Quantifier elimination fails.

Because \(T_3\) is universal, a model completion of \(T_3\) would eliminate quantifiers. Thus \(T_3^*\) is not a model completion.

## Limits

The argument is for the pure group language and makes no claim about expanded languages.

No computation or finite enumeration is used.
