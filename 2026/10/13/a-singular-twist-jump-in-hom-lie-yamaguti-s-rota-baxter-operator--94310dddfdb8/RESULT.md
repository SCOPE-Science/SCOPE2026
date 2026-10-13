# A singular-twist jump in Hom–Lie–Yamaguti s-Rota–Baxter operators

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2,3,
\]
and let \(L_k\) be the two-dimensional Hom–Lie–Yamaguti algebra from Teng–Jin–Long Example 3.4:
\[
[u_1,u_2]=u_1,
\qquad
\{u_1,u_2,u_2\}=u_1,
\]
\[
\alpha(u_1)=ku_1,
\qquad
\alpha(u_2)=u_2.
\]
Fix
\[
k\ne1
\]
and an integer \(s\ge0\).

In the standard column convention, the complete \(s\)-Rota–Baxter locus is
\[
\boxed{
R=\operatorname{diag}(a,d),
\qquad
k^s a^2=0,
}
\]
where \(k^0=1\).

Because \(K\) is a field, this gives a sharp phase diagram:
\[
\boxed{
\operatorname{RB}_s(L_k)
=
\{\operatorname{diag}(0,d):d\in K\}
}
\]
whenever \(s=0\) or \(k\ne0,1\), whereas
\[
\boxed{
\operatorname{RB}_s(L_0)
=
\{\operatorname{diag}(a,d):a,d\in K\}
}
\]
for every \(s\ge1\).

Thus the one-parameter family
\[
\operatorname{diag}(0,d)
\]
printed in Example 3.4 is complete for every nonidentity nonzero twist and for order \(s=0\), but the singular twist \(k=0\) has an extra affine direction at every positive order.

The descendant operations of any such operator are
\[
\boxed{
[u_1,u_2]_R=du_1,
\qquad
\{u_1,u_2,u_2\}_R=d^2u_1.
}
\]
They are independent of the exceptional parameter \(a\). Hence the new affine direction at \(k=0\), \(s\ge1\), changes the operator moduli without creating new descendant isomorphism types.

When \(d=0\), the descendant binary and ternary products are both zero. When \(d\ne0\), the change of basis
\[
u_1\mapsto u_1,
\qquad
u_2\mapsto d^{-1}u_2
\]
identifies the descendant with the original \(L_0\).

Over a finite field \(\mathbf F_q\) of characteristic greater than \(3\), the exceptional case \(k=0\), \(s\ge1\) has
\[
\boxed{q^2}
\]
operators with matrix-rank profile
\[
\boxed{(1,\ 2(q-1),\ (q-1)^2)}.
\]
Exactly \(q\) of them induce the zero descendant, and \(q(q-1)\) induce a nonzero descendant isomorphic to \(L_0\).

Every other case with \(k\ne1\) has
\[
\boxed{q}
\]
operators with rank profile
\[
\boxed{(1,\ q-1,\ 0)}.
\]
Exactly one induces the zero descendant.

For fixed \(q\), the extension-field counts are respectively \(q^{2m}\) and \(q^m\). Therefore the reduced zeta functions are
\[
\boxed{Z_{\mathrm{sing}}(T)=\frac{1}{1-q^2T}}
\]
and
\[
\boxed{Z_{\mathrm{generic}}(T)=\frac{1}{1-qT}}.
\]

## Assumptions and scope

Teng, Jin, and Long introduce \(s\)-Rota–Baxter operators on Hom–Lie–Yamaguti algebras and give the exact two-dimensional family above as Example 3.4. Their Example states that \(\operatorname{diag}(0,k_2)\) is an \(s\)-Rota–Baxter operator; it does not claim exhaustiveness.

The author-posted preprint was publicly available on 4 October 2022. The journal paper lists \(17B38\) first among its 2020 Mathematics Subject Classification codes.

The paper assumes an algebraically closed field of characteristic different from \(2\) and \(3\). The proof here only uses field arithmetic after the displayed identities, but the theorem retains the source's characteristic assumptions.

The identity-twist boundary \(k=1\) is deliberately excluded. There the commutant is larger and the problem becomes the ordinary Lie–Yamaguti Rota–Baxter classification rather than the nonidentity Hom phase studied here.

## Proof

Write
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
\]
The twist is
\[
\alpha=\operatorname{diag}(k,1).
\]
The condition
\[
R\alpha=\alpha R
\]
gives
\[
(k-1)b=0,
\qquad
(k-1)c=0.
\]
Since \(k\ne1\),
\[
b=c=0.
\]
Thus every possible \(s\)-Rota–Baxter operator is diagonal.

Put
\[
m=k^s,
\]
with \(m=1\) at \(s=0\). Then
\[
\alpha^sR=\operatorname{diag}(ma,d).
\]
Evaluate the binary \(s\)-Rota–Baxter equation on \((u_1,u_2)\):
\[
[Ru_1,Ru_2]
=
R([\alpha^sRu_1,u_2]+[u_1,\alpha^sRu_2]).
\]
The left side is
\[
ad\,u_1,
\]
while the right side is
\[
a(ma+d)u_1.
\]
Hence
\[
ma^2=0.
\]

The ternary equation on \((u_1,u_2,u_2)\) gives
\[
ad^2u_1
=
a(2mad+d^2)u_1,
\]
which is already implied by \(ma^2=0\). Direct basis expansion shows that every other binary and ternary basis equation is either zero or a scalar multiple of the same condition. Therefore
\[
R\text{ is }s\text{-Rota–Baxter}
\iff
R=\operatorname{diag}(a,d),\quad k^sa^2=0.
\]

Over a field, \(k^sa^2=0\) allows \(a\ne0\) exactly when \(k=0\) and \(s\ge1\). This proves the phase diagram.

For the descendant operations, Corollary 3.6 with the \(\alpha^s\)-adjoint representation gives
\[
[u_1,u_2]_R=(ma+d)u_1
\]
and
\[
\{u_1,u_2,u_2\}_R=(2mad+d^2)u_1.
\]
On the solution locus, either \(a=0\) or \(m=0\), so these reduce to
\[
[u_1,u_2]_R=du_1,
\qquad
\{u_1,u_2,u_2\}_R=d^2u_1.
\]
The stated descendant classification follows.

The finite-field counts are then the point counts of an affine line or affine plane, and the rank profiles are the elementary diagonal-matrix counts.

## Verification

The included `artifacts/verify.py` reconstructs the source multiplication, ternary operation, and twist. It first checks all Hom–Lie–Yamaguti identities on basis elements for symbolic \(k\).

It reconstructs the complete binary and ternary \(s\)-Rota–Baxter defects for a symbolic matrix and verifies that, after \(k\ne1\) forces \(b=c=0\), the complete system is generated by
\[
k^sa^2=0.
\]

The checker independently derives the descendant coefficients
\[
k^sa+d
\]
and
\[
2k^sad+d^2.
\]

It then exhaustively tests every \(2\times2\) matrix over
\[
\mathbf F_5,\quad\mathbf F_7,\quad\mathbf F_{11}
\]
for representative cases \(k=0\) and \(k=2\), at orders \(s=0,1,2\). It obtains exactly \(q\) operators in the generic cases and \(q^2\) operators for \(k=0\), \(s\ge1\).

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field phase diagram is proved symbolically.

## Relationship to prior work

The primary source defines \(s\)-Rota–Baxter operators and gives this exact two-dimensional Hom–Lie–Yamaguti example, but only exhibits the line \(\operatorname{diag}(0,k_2)\). The inspected full text does not classify all operators on the example or separate the singular twist \(k=0\).

At \(k=1\), the problem reduces to the ordinary Lie–Yamaguti Rota–Baxter case and has a larger solution set; that boundary is prior-covered and is not part of the novelty claim here.

Targeted searches for Example 3.4, the parameter \(k_1=0\), complete \(s\)-Rota–Baxter classifications, and the singular-twist phase jump did not locate a covering theorem. Later Hom–Lie–Yamaguti and Hom–Lie triple operator papers cite the general framework but do not state this exceptional plane in the sources inspected.

## Limitations

The theorem excludes the identity twist \(k=1\).

It treats one explicit two-dimensional Hom–Lie–Yamaguti family rather than all such algebras.

The source works in characteristic different from \(2\) and \(3\), and that assumption is retained.

Failed searches do not prove absolute novelty.

## References

1. W. Teng, J. Jin, and F. Long, “Relative Rota-Baxter operators on Hom-Lie-Yamaguti algebras,” author-posted preprint DOI `10.13140/RG.2.2.33626.00961`, first public 4 October 2022; *Journal of Mathematical Research with Applications* 43 (2023), 648–664, DOI `10.3770/j.issn:2095-2651.2023.06.002`.
