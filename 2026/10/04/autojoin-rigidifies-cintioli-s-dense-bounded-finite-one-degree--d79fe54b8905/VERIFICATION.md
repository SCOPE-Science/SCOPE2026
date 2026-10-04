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

Assume the source's scalar calculus:
\[
S_q\le_1S_r
\iff
q\le r,
\]
\[
S_q\oplus S_r\equiv_1S_{q+r},
\]
for positive dyadic \(q,r\), with every internal one-one degree represented by one \(S_q\).

These formulas make
\[
[S_q]_1\mapsto q
\]
an ordered-semigroup isomorphism.

For the automorphism calculation, let \(F\) be any additive bijection of positive dyadics and set
\[
c=F(1).
\]
Then
\[
2^eF(2^{-e})=F(1)=c,
\]
so
\[
F(2^{-e})=c2^{-e}.
\]
Additivity gives
\[
F(m2^{-e})=cm2^{-e}
\]
for every positive dyadic.

Thus \(F\) is multiplication by \(c\). It is onto exactly when \(1/c\) is also dyadic. The positive units of \(\mathbb Z[1/2]\) are precisely
\[
2^z,
\qquad
z\in\mathbb Z.
\]
Hence the automorphism group is infinite cyclic.

The group-completion calculation is exact because every element of \(\mathbb Z[1/2]\) is a difference of two positive dyadics.

## Limits

The primary arXiv PDF was inaccessible through the attempted routes. The accessible primary abstract confirms the tower and autojoin exhaustivity, while the exact scalar laws were cross-checked through a detailed source-focused review.

No computational sampling is used.
