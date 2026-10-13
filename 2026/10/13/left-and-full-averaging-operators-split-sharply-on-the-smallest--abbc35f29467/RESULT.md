# Left and full averaging operators split sharply on the smallest non-Lie Leibniz algebra

## Finding

Let \(k\) be any field and let \(L\) be the two-dimensional left Leibniz algebra with basis \(e_1,e_2\) and sole nonzero bracket
\[
\{e_1,e_2\}=e_2.
\]
This is the smallest non-Lie hemisemidirect-product example: a one-dimensional abelian Lie algebra acts faithfully on a one-dimensional module.

Write
\[
P(e_1)=a e_1+b e_2,
\qquad
P(e_2)=c e_1+d e_2.
\]
Then \(P\) is a left averaging operator if and only if
\[
\boxed{c=0,\qquad ab=0.}
\]
Thus the left-averaging variety is the union of two affine planes.

The map \(P\) is an averaging operator in the full two-sided sense if and only if
\[
\boxed{c=0,\qquad ab=0,\qquad bd=0,\qquad d(d-a)=0.}
\]
Equivalently,
\[
\boxed{
\operatorname{Avg}(L)
=
\{aI:a\in k\}
\cup
\{aE_{11}:a\in k\}
\cup
\{bE_{21}:b\in k\}.
}
\]
The three lines meet only at the zero operator.

The automorphism group is
\[
\boxed{
\operatorname{Aut}(L)
=
\{\operatorname{diag}(1,s):s\in k^\times\}.
}
\]
Conjugation fixes \(a,d\) and sends
\[
b\longmapsto sb.
\]
Hence every full averaging orbit has a unique representative of exactly one of the following forms:
\[
\boxed{aI\quad(a\in k),}
\]
\[
\boxed{aE_{11}\quad(a\in k^\times),}
\]
or
\[
\boxed{E_{21}.}
\]
For left averaging operators, unique representatives are
\[
\boxed{P_{a,0,d}\quad((a,d)\in k^2)}
\]
and
\[
\boxed{P_{0,1,d}\quad(d\in k).}
\]

Over \(k=\mathbf F_q\), the two notions therefore differ sharply:
\[
\boxed{\#\operatorname{LAvg}(L)=2q^2-q,\qquad
\#(\operatorname{LAvg}(L)/\operatorname{Aut}(L))=q^2+q,}
\]
whereas
\[
\boxed{\#\operatorname{Avg}(L)=3q-2,\qquad
\#(\operatorname{Avg}(L)/\operatorname{Aut}(L))=2q.}
\]
All full-averaging orbits are singleton except the single nonzero \(E_{21}\)-orbit, whose size is \(q-1\).

Finally, the full averaging operators induce exactly four isomorphism types of di-Leibniz structures:

1. the zero structure, from \(P=0\);
2. both operations equal to a nonzero scalar multiple of the original bracket, from \(P=aI\) with \(a\ne0\);
3. \(\dashv=0\) and \(\vdash\) a nonzero scalar multiple of the original bracket, from \(P=aE_{11}\) with \(a\ne0\);
4. \(\vdash=0\) and the sole nonzero product \(\{e_1,e_1\}_{\dashv}=e_2\), up to isomorphism, from \(P=bE_{21}\) with \(b\ne0\).

Thus passing from left averaging to full averaging collapses a quadratic-size finite-field family to a linear-size one, and the resulting full descendant structures collapse further to only four isomorphism types.

## Assumptions and scope

The bracket convention is the left Leibniz identity used in the source on averaging operators. A left averaging operator satisfies
\[
\{P(x),P(y)\}=P\{P(x),y\},
\]
while a full averaging operator also satisfies
\[
\{P(x),P(y)\}=P\{x,P(y)\}.
\]

The theorem holds in every characteristic. The finite counts require a finite coefficient field.

The classification concerns this canonical two-dimensional non-Lie Leibniz algebra only. It does not classify averaging operators on all two-dimensional Leibniz algebras.

## Proof

For vectors
\[
x=x_1e_1+x_2e_2,
\qquad
y=y_1e_1+y_2e_2,
\]
the bracket is
\[
\{x,y\}=x_1y_2e_2.
\]

Write
\[
P(e_1)=a e_1+b e_2,
\qquad
P(e_2)=c e_1+d e_2.
\]
The left averaging identity on the four ordered basis pairs gives
\[
ab=0,
\qquad
ac=0,
\qquad
bc=0,
\qquad
c^2=0.
\]
Because \(k\) is a field,
\[
c=0,
\]
and the left averaging condition reduces exactly to
\[
ab=0.
\]

For the full averaging identity, the second equality contributes
\[
bd=0,
\qquad
d^2=ad.
\]
Thus
\[
c=0,
\qquad
ab=0,
\qquad
bd=0,
\qquad
d(d-a)=0.
\]
If \(a\ne0\), then \(b=0\) and either \(d=0\) or \(d=a\), giving the \(aE_{11}\) and \(aI\) lines. If \(a=0\), then \(d=0\) and \(b\) is arbitrary, giving the \(bE_{21}\) line.

Now let \(\phi\) be an automorphism. Since
\[
\{e_1,e_1\}=0,
\qquad
\{e_1,e_2\}=e_2,
\]
a direct product-preservation calculation forces
\[
\phi(e_1)=e_1,
\qquad
\phi(e_2)=s e_2,
\qquad
s\in k^\times.
\]
Hence
\[
\operatorname{Aut}(L)=\{\operatorname{diag}(1,s):s\in k^\times\}.
\]
For
\[
P=\begin{pmatrix}a&0\\ b&d\end{pmatrix},
\]
conjugation gives
\[
\operatorname{diag}(1,s)P\operatorname{diag}(1,s)^{-1}
=
\begin{pmatrix}a&0\\ sb&d\end{pmatrix}.
\]
The orbit representatives follow immediately.

Over \(\mathbf F_q\), the left averaging set is the union of the planes \(a=0\) and \(b=0\), which intersect in the line \(a=b=0\). Inclusion--exclusion gives
\[
q^2+q^2-q=2q^2-q.
\]
There are \(q^2\) singleton orbits with \(b=0\), and for each \(d\in\mathbf F_q\) the \(q-1\) maps with \(a=0\), \(b\ne0\) form one orbit. Hence there are
\[
q^2+q
\]
left-averaging orbits.

The full averaging set is the union of three lines meeting only at zero, so
\[
3q-2
\]
operators occur. The scalar line contributes \(q\) singleton orbits, the nonzero \(E_{11}\)-line contributes \(q-1\) singleton orbits, and all \(q-1\) nonzero multiples of \(E_{21}\) form one orbit. Thus the full orbit count is
\[
q+(q-1)+1=2q.
\]

For a full averaging operator, the source's induced di-Leibniz operations are
\[
\{x,y\}_{\dashv}=\{x,P(y)\},
\qquad
\{x,y\}_{\vdash}=\{P(x),y\}.
\]
Substitution of the three full-averaging lines gives the four listed descendant types. Nonzero scalar coefficients are removed by a diagonal change of basis, while the pattern of which operation vanishes distinguishes the nonzero types.

## Verification

The included checker exhaustively treats
\[
q\in\{2,3,5,7\}.
\]
It enumerates all linear maps, checks the left and full averaging identities directly on all ordered basis pairs, independently computes the full automorphism group, constructs every conjugacy orbit, and verifies the closed counts.

It also verifies the rank distribution of the full averaging set:
\[
1
\]
operator of rank \(0\),
\[
2q-2
\]
operators of rank \(1\), and
\[
q-1
\]
operators of rank \(2\).
There are exactly three idempotent full averaging operators and exactly \(q\) square-zero full averaging operators.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem.

## Relationship to prior work

Das introduces left averaging operators and full averaging operators on Leibniz algebras and proves that full averaging operators induce di-Leibniz structures. The definitions distinguish the one-sided identity
\[
\{P(x),P(y)\}=P\{P(x),y\}
\]
from the full pair of averaging identities.

The source does not contain a two-dimensional classification and has no occurrence of “two-dimensional” or “classification” in its searchable full text. The theorem above supplies an exact model on the canonical two-dimensional hemisemidirect Leibniz algebra and quantifies how much stricter the full notion is.

Focused semantic-database and literature searches for two-dimensional Leibniz averaging operators, the bracket \(\{e_1,e_2\}=e_2\), automorphism normal forms, and finite-field counts did not locate the displayed classification. The closest database result concerns averaging operators on a nilpotent two-dimensional pre-Lie algebra with product \(e_1\cdot e_1=e_2\); that is a different algebra and a different operator identity.

## Limitations

The result is a complete classification for one canonical two-dimensional non-Lie Leibniz algebra, not a classification for all low-dimensional Leibniz algebras.

The equations are elementary once the averaging identities are written down. Their value lies in the sharp structural comparison between the newly introduced left and full notions, the exact moduli under automorphisms, and the collapse to four descendant di-Leibniz types.

An equivalent computation may exist in unindexed notes or under embedding-tensor terminology.

Failed searches do not prove novelty.

## References

1. A. Das, “Averaging operators on groups, racks and Leibniz algebras,” arXiv:2403.06250v1, first public version 10 March 2024, DOI 10.48550/arXiv.2403.06250. MSC 2020: 17B40, 22E60, 16T05, 17A32.
