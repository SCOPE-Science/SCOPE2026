# The \(T_2^8(a,b)\) trialgebra family has three isomorphism strata

## Finding

Let \(K\) be a field of characteristic zero. Consider the two-dimensional associative trialgebra \(T_2^8(a,b)\) with basis \(\{e_1,e_2\}\) and nonzero products
\[
e_1\dashv e_1=a e_1,\qquad
e_2\dashv e_1=a e_2,
\]
\[
e_1\vdash e_1=a e_1,\qquad
e_1\vdash e_2=a e_2,
\]
and
\[
e_1\perp e_1=a e_1+b e_2.
\]

The parameter plane does not parametrize pairwise non-isomorphic trialgebras. It has exactly three isomorphism strata:
\[
\boxed{
a\ne0:\quad T_2^8(a,b)\cong T_2^8(1,0),
}
\]
\[
\boxed{
a=0,\ b\ne0:\quad T_2^8(0,b)\cong T_2^8(0,1),
}
\]
and
\[
\boxed{
a=b=0:\quad T_2^8(0,0)\text{ is the zero trialgebra}.
}
\]

The strata are pairwise distinct. If
\[
I_\dashv=\operatorname{span}\{x\dashv y:x,y\in T\},
\quad
I_\vdash=\operatorname{span}\{x\vdash y:x,y\in T\},
\quad
I_\perp=\operatorname{span}\{x\perp y:x,y\in T\},
\]
then the ordered triples of dimensions are
\[
(2,2,1),\qquad (0,0,1),\qquad (0,0,0)
\]
on the three strata.

The derivation and centroid spaces also jump across the same boundary. For the generic stratum,
\[
\boxed{
\operatorname{Der}(T_2^8(1,0))
=
\left\{
\begin{pmatrix}
0&0\\
0&d
\end{pmatrix}
:d\in K
\right\},
\qquad
\dim \operatorname{Der}=1,
}
\]
whereas on the nonzero \(a=0\) stratum,
\[
\boxed{
\operatorname{Der}(T_2^8(0,1))
=
\left\{
\begin{pmatrix}
r&0\\
w&2r
\end{pmatrix}
:r,w\in K
\right\},
\qquad
\dim \operatorname{Der}=2.
}
\]

For centroids,
\[
\boxed{
C(T_2^8(1,0))=K I_2,
\qquad
\dim C=1,
}
\]
but
\[
\boxed{
C(T_2^8(0,1))
=
\left\{
\begin{pmatrix}
\lambda&0\\
\mu&\lambda
\end{pmatrix}
:\lambda,\mu\in K
\right\},
\qquad
\dim C=2.
}
\]

At the zero point both the derivation space and centroid are all of
\[
M_2(K).
\]

The later tables in the same work therefore cannot represent the whole displayed \(T_2^8(a,b)\) family by one derivation row and one centroid row. The printed \(T_2^8\) derivation row agrees with the \(a=0,\ b\ne0\) stratum, while the printed scalar-centroid row agrees with the \(a\ne0\) stratum.

## Assumptions and scope

The source assumes characteristic zero. The isomorphism reduction itself works over an arbitrary field, but the statement above retains the source's characteristic-zero scope so that the displayed derivation formula with the coefficient \(2\) has its usual form.

The claim concerns only the displayed family \(T_2^8(a,b)\). It does not reclassify every two-, three-, or four-dimensional associative trialgebra in the source.

The assertion about the source is literal: Theorem 3.2 displays \(T_2^8\) with two parameters and no parameter restrictions or equivalence relation on the theorem page. The later derivation and centroid theorems each give only one \(T_2^8\) row.

## Proof

Suppose first that
\[
a\ne0.
\]
Set
\[
f_1=\frac1a e_1+\frac{b}{a^2}e_2,
\qquad
f_2=e_2.
\]
This is a basis because its change-of-basis determinant is \(a^{-1}\ne0\).

Direct substitution gives
\[
f_1\dashv f_1=f_1,\qquad
f_2\dashv f_1=f_2,
\]
\[
f_1\vdash f_1=f_1,\qquad
f_1\vdash f_2=f_2,
\]
and
\[
f_1\perp f_1=f_1.
\]
Every other basis product is zero. Hence
\[
T_2^8(a,b)\cong T_2^8(1,0).
\]

Now let
\[
a=0,\qquad b\ne0.
\]
Then only
\[
e_1\perp e_1=b e_2
\]
is nonzero. In the basis
\[
f_1=e_1,\qquad f_2=b e_2
\]
the sole nonzero product is
\[
f_1\perp f_1=f_2.
\]
Thus
\[
T_2^8(0,b)\cong T_2^8(0,1).
\]

If
\[
a=b=0,
\]
all three products vanish.

These three representatives are pairwise non-isomorphic because an isomorphism preserves the dimensions of the three product-image subspaces. They are respectively
\[
(2,2,1),\qquad
(0,0,1),\qquad
(0,0,0).
\]

For derivations, write a general endomorphism as
\[
D(e_1)=r e_1+w e_2,\qquad
D(e_2)=s e_1+t e_2.
\]

For \(T_2^8(1,0)\), applying the derivation rule to
\[
e_1\dashv e_1=e_1
\]
forces
\[
r=0.
\]
Applying it to
\[
e_1\perp e_1=e_1
\]
then forces
\[
w=0.
\]
Finally, applying it to the zero product
\[
e_2\perp e_1=0
\]
forces
\[
s=0.
\]
The coefficient \(t\) is free, giving the one-dimensional displayed space.

For \(T_2^8(0,1)\), only
\[
e_1\perp e_1=e_2
\]
is nonzero. The derivation equation gives
\[
D(e_2)
=
D(e_1)\perp e_1+e_1\perp D(e_1)
=
2r e_2.
\]
Hence
\[
s=0,\qquad t=2r,
\]
while \(w\) is free.

For centroids, let
\[
\phi(e_1)=\lambda e_1+\mu e_2,
\qquad
\phi(e_2)=\nu e_1+\rho e_2.
\]

In \(T_2^8(1,0)\), the \(\dashv\)-identity
\[
\phi(x\dashv y)=x\dashv\phi(y)
\]
with \(y=e_1\) forces
\[
\phi(x)=\lambda x
\]
for every \(x\), so the centroid is scalar.

In \(T_2^8(0,1)\), the only nonzero condition comes from
\[
e_1\perp e_1=e_2.
\]
It yields
\[
\phi(e_2)=\lambda e_2,
\]
hence
\[
\nu=0,\qquad \rho=\lambda,
\]
with \(\mu\) free.

At \(T_2^8(0,0)\), every endomorphism is both a derivation and a centroid.

## Verification

The included exact symbolic checker performs four independent tasks.

First, it verifies all eleven associative-trialgebra identities symbolically for the displayed \(T_2^8(a,b)\) multiplication table.

Second, it verifies both change-of-basis normalizations exactly.

Third, it constructs the full linear derivation system from the definition and computes nullspaces for
\[
T_2^8(1,0),\qquad
T_2^8(0,1),\qquad
T_2^8(0,0).
\]
The dimensions are
\[
1,\qquad2,\qquad4.
\]

Fourth, it constructs the full centroid system and obtains dimensions
\[
1,\qquad2,\qquad4.
\]

The checker returns `VERIFY_OK`.

No finite experiment is used as a substitute for the symbolic proof.

## Relationship to prior work

Zahari, Mosbahi, and Basdouri's 2023 preprint states that any two-dimensional real associative trialgebra is either associative or isomorphic to one of eight displayed pairwise non-isomorphic entries. Its eighth entry is the parameterized family \(T_2^8(a,b)\) above, with no parameter restrictions or equivalence relation stated on the theorem page.

The same preprint later gives a single derivation row for \(T_2^8\),
\[
\begin{pmatrix}
\frac12 d&0\\
w&d
\end{pmatrix},
\]
which is exactly the derivation space of \(T_2^8(0,1)\) after writing \(r=d/2\). Its centroid theorem gives only scalar matrices for \(T_2^8\), which is instead the centroid of the generic \(a\ne0\) stratum.

The published 2025 version repeats the same \(T_2^8(a,b)\) table and the same single derivation and centroid rows. Thus the parameter issue was not removed in the later version.

Targeted searches for the labels \(T_2^8\), `Trias 8`, the exact multiplication table, parameter equivalences, and a correction or erratum did not locate a published normalization of this family.

## Limitations

The result does not determine whether other parameterized rows in the source require additional normalization.

The phrase “pairwise non-isomorphic” in the source may have been intended to distinguish the eight displayed labels rather than every parameter point. Even under that charitable reading, the later single derivation and centroid rows are incompatible with the displayed \(T_2^8(a,b)\) family because its invariant spaces change dimension across \(a=0\).

A separate unindexed correction may exist.

Failed searches do not prove novelty.

## References

1. A. Zahari, B. Mosbahi, and I. Basdouri, “Classification, Derivations and Centroids of Low-Dimensional Real Trialgebras,” arXiv:2304.04251v1, first public 9 April 2023. MSC 2020: 17A30, 17A32, 16D20, 16W25, 17B63.
2. B. Mosbahi, I. Basdouri, and A. Zahari Abdou Damdji, “Classification, derivations and centroids of low-dimensional associative trialgebras,” *Galois Journal of Algebra* 1 (2025), 118–136, DOI 10.65908/gja.2025.24974.
