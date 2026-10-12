# Scalar Rota–Baxter operators force the two side products to coincide

## Finding

Let
\[
(A,\dashv,\vdash,\perp,\alpha,\beta)
\]
be a BiHom-associative trialgebra over a field \(K\), and use the Rota–Baxter definition in which a weight-\(\lambda\) operator \(R\) satisfies
\[
R(x)\vdash R(y)
=
R\bigl(R(x)\dashv y+x\dashv R(y)+\lambda(x\dashv y)\bigr),
\]
\[
R(x)\dashv R(y)
=
R\bigl(R(x)\vdash y+x\vdash R(y)+\lambda(x\vdash y)\bigr),
\]
and
\[
R(x)\perp R(y)
=
R\bigl(R(x)\perp y+x\perp R(y)+\lambda(x\perp y)\bigr).
\]

For the scalar map
\[
R=-\lambda I_A,
\]
commutation with \(\alpha\) and \(\beta\) is automatic. The three Rota–Baxter identities reduce to
\[
\lambda^2(x\vdash y)=\lambda^2(x\dashv y),
\]
\[
\lambda^2(x\dashv y)=\lambda^2(x\vdash y),
\]
and an identity that is automatically true for \(\perp\).

Therefore
\[
\boxed{
\lambda\ne0
\quad\Longrightarrow\quad
R=-\lambda I_A\text{ is Rota--Baxter of weight }\lambda
\iff
\dashv=\vdash.
}
\]
For \(\lambda=0\), the scalar map is the zero map and is always a weight-zero Rota–Baxter operator.

This gives an immediate correction to Example 2.10 of Zahari--Mosbahi--Basdouri. The displayed two-dimensional example has
\[
e_2\dashv e_1=e_1
\]
but no listed nonzero product \(e_2\vdash e_1\), hence
\[
e_2\vdash e_1=0.
\]
For \(x=e_2\) and \(y=e_1\), the first Rota–Baxter identity for \(R=-\lambda I\) therefore reads
\[
0=\lambda^2e_1.
\]
Over the characteristic-zero field assumed by the source, this fails for every
\[
\lambda\ne0.
\]
Thus the displayed operator in Example 2.10 is a Rota–Baxter operator only at weight \(0\), unless the multiplication table is altered so that \(\dashv=\vdash\).

## Assumptions and scope

The universal scalar criterion is valid over any field. The correction to Example 2.10 is stated in the source's characteristic-zero setting.

The convention used for the example is the standard multiplication-table convention that unlisted products are zero. The contradiction itself does not depend on the unspecified values of \(\alpha(e_1)\) or \(\beta(e_1)\), because a scalar map commutes with all linear maps and the Rota–Baxter defect used above involves only \(\dashv\) and \(\vdash\).

The claim concerns Definition 2.9 exactly as printed, where the first two Rota–Baxter equations cross the two side products. It does not assert that this cross-coupled definition is the only possible convention in the literature.

## Proof

Set
\[
R(x)=-\lambda x.
\]
For the first defining identity, bilinearity gives
\[
R(x)\vdash R(y)=\lambda^2(x\vdash y).
\]
The argument of \(R\) on the right is
\[
(-\lambda x)\dashv y+x\dashv(-\lambda y)+\lambda(x\dashv y)
=-\lambda(x\dashv y),
\]
so the right side is
\[
R\bigl(-\lambda(x\dashv y)\bigr)=\lambda^2(x\dashv y).
\]
Hence the first identity is equivalent to
\[
\lambda^2(x\vdash y-x\dashv y)=0
\]
for all \(x,y\).

The second identity gives the same condition with the two terms interchanged.

For the middle product,
\[
R(x)\perp R(y)=\lambda^2(x\perp y),
\]
while the argument on the right again equals
\[
-\lambda(x\perp y),
\]
so its image under \(R\) is exactly
\[
\lambda^2(x\perp y).
\]
Thus the third identity imposes no extra condition.

If \(\lambda\ne0\), the field property allows division by \(\lambda^2\), yielding
\[
x\dashv y=x\vdash y
\]
for every \(x,y\). Conversely, if the two side products agree, all three equations hold. If \(\lambda=0\), then \(R=0\) and every defining equation is zero on both sides.

For Example 2.10, substituting
\[
x=e_2,
\qquad
y=e_1
\]
uses
\[
e_2\dashv e_1=e_1,
\qquad
e_2\vdash e_1=0.
\]
The first defect is therefore
\[
-\lambda^2e_1,
\]
which is nonzero for every nonzero \(\lambda\) in characteristic zero.

## Verification

The packaged checker `artifacts/verify.py` symbolically introduces independent structure constants for \(\dashv\), \(\vdash\), and \(\perp\) on a two-dimensional vector space and substitutes \(R=-\lambda I\) into all three defining equations. It verifies coefficient-by-coefficient that the first defect is
\[
\lambda^2(\vdash-\dashv),
\]
the second is its negative, and the third is identically zero.

It then instantiates the exact multiplication table of Example 2.10 and checks all ordered basis pairs. The pair \((e_2,e_1)\) produces the nonzero first defect
\[
-\lambda^2e_1.
\]
The checker also verifies that setting \(\lambda=0\) annihilates every defect. It returns `VERIFY_OK`.

The symbolic computation is a replay of the algebraic proof, not finite experimental evidence for an infinite statement.

## Relationship to prior work

The primary source defines the cross-coupled Rota–Baxter identities in Definition 2.9 and immediately follows them with Example 2.10, where the displayed scalar map is \(R(e_i)=-\lambda e_i\). The same example has unequal left and right side products, because \(e_2\dashv e_1=e_1\) while \(e_2\vdash e_1\) is zero.

Targeted semantic searches for the exact arXiv identifier, Example 2.10, the scalar operator \(-\lambda I\), and the condition \(\dashv=\vdash\) did not locate a correction or an equivalent scalar criterion. Web searches likewise returned the preprint itself and later papers that cite it, but no erratum or repaired version of the example.

The scalar criterion is stronger than the single counterexample: it identifies exactly when the source's natural scalar ansatz can work under its printed definition.

## Limitations

The result corrects one Rota–Baxter example and proves a scalar-operator criterion. It does not classify all Rota–Baxter operators on BiHom-associative trialgebras.

If the authors intended Example 2.10 only for \(\lambda=0\), then the displayed operator is the trivial zero operator and the example is correct in that restricted interpretation; no such restriction is stated next to the example in the inspected text.

A later unindexed correction or author note may exist. Failed searches do not prove absolute novelty.

## References

1. A. Zahari, B. Mosbahi, and I. Basdouri, “Classification, Derivations and Centroids of Low-Dimensional Complex BiHom-Trialgebras,” arXiv:2304.06781v1, first public 13 April 2023. MSC 2020: 17A30, 17A32, 16D20, 16W25, 17B63.
