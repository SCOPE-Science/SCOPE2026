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

The target preprint and published theorem were read at the statement and proof level. Both versions identify the transformed controlled-frame operator as \(WSW^*\), with \(W=U_1\otimes U_2\), and both infer invertibility of \(W\) from invertibility of \(WSW^*\) and \(S\). That inference is stronger than what the range relation provides.

For the explicit example, \(L\) is the backward shift on \(\ell^2(\mathbb N)\). It is surjective because \(L e_{m+1}=e_m\), and it is noninjective because \(Le_1=0\). The first-factor transformed atoms
\[
\frac{e_1}{\sqrt2},\quad-\frac{e_1}{\sqrt2},\quad e_2,\quad e_3,\ldots
\]
satisfy the exact Parseval identity
\[
\frac12|x_1|^2+\frac12|x_1|^2+\sum_{m\ge2}|x_m|^2=\|x\|^2.
\]
Tensoring with an orthonormal basis in the second factor preserves the Parseval identity. Thus the source's necessary invertibility condition fails even though no transformed tensor atom is zero.

For the repaired theorem, the lower bound follows from
\[
\langle WSW^*x,x\rangle\ge\alpha\|W^*x\|^2\ge\alpha m(W^*)^2\|x\|^2,
\]
and the upper bound follows from
\[
\langle WSW^*x,x\rangle\le\beta\|W\|^2\|x\|^2.
\]
The converse uses only
\[
R(WSW^*)\subseteq R(W).
\]
Therefore invertibility of \(WSW^*\) forces surjectivity, but not injectivity, of \(W\).

The verification does not remove the source theorem's commutation assumptions and does not claim novelty for the standard general fact that surjective bounded operators preserve the frame property.
