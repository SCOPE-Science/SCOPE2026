# Two omitted classes in the two-dimensional associative quasi-centroid table

## Finding

Let \(A\) be a two-dimensional complex associative algebra and define its quasi-centroid by
\[
QC(A)=
\left\{
\phi\in\operatorname{End}_{\mathbb C}(A):
\phi(x)y=x\phi(y)\ \text{for all }x,y\in A
\right\}.
\]

Theorem 5.1 of Fiidow--Zahari--Mosbahi is presented as the quasi-centroid classification of all two-dimensional complex associative algebras, but its table has only five isomorphism-class rows. A complete two-dimensional associative classification has seven pairwise non-isomorphic classes. The two missing classes are the zero algebra and the decomposable algebra with a one-dimensional idempotent factor and a one-dimensional zero factor.

Using a basis \(\{e_1,e_2\}\), the complete list may be written as follows.

\[
A_0:\quad xy=0\ \text{for all }x,y.
\]

\[
A_e:\quad e_1e_1=e_1.
\]

\[
A_n:\quad e_1e_1=e_2.
\]

\[
A_L:\quad e_1e_1=e_1,\qquad e_1e_2=e_2.
\]

\[
A_R:\quad e_1e_1=e_1,\qquad e_2e_1=e_2.
\]

\[
A_D:\quad
e_1e_1=e_1,\qquad
e_1e_2=e_2e_1=e_2.
\]

\[
A_S:\quad
e_1e_1=e_1,\qquad
e_2e_2=e_2.
\]

With the convention that the columns of a matrix are the coordinates of \(\phi(e_1)\) and \(\phi(e_2)\), their quasi-centroids are

\[
\boxed{QC(A_0)=M_2(\mathbb C),\qquad \dim QC(A_0)=4,}
\]

\[
\boxed{
QC(A_e)=
\left\{
\begin{pmatrix}
a&0\\
b&d
\end{pmatrix}
:a,b,d\in\mathbb C
\right\},
\qquad
\dim QC(A_e)=3,
}
\]

\[
\boxed{
QC(A_n)=
\left\{
\begin{pmatrix}
a&0\\
b&d
\end{pmatrix}
:a,b,d\in\mathbb C
\right\},
\qquad
\dim QC(A_n)=3,
}
\]

\[
\boxed{QC(A_L)=QC(A_R)=\mathbb C I_2,\qquad \dim=1,}
\]

\[
\boxed{
QC(A_D)=
\left\{
\begin{pmatrix}
a&0\\
b&a
\end{pmatrix}
:a,b\in\mathbb C
\right\},
\qquad
\dim QC(A_D)=2,
}
\]

and

\[
\boxed{
QC(A_S)=
\left\{
\begin{pmatrix}
a&0\\
0&d
\end{pmatrix}
:a,d\in\mathbb C
\right\},
\qquad
\dim QC(A_S)=2.
}
\]

Thus the corrected multiset of quasi-centroid dimensions is
\[
\boxed{\{4,3,3,2,2,1,1\}.}
\]

The five matrices printed in Theorem 5.1 have dimensions \(3,1,1,2,2\). The theorem therefore omits exactly the dimension-\(4\) zero-algebra row and one additional dimension-\(3\) row, \(A_e\). The source's own proof identifies its first row with \(A_n\), so the missing dimension-\(3\) row cannot be hidden there.

## Assumptions and scope

The result concerns complex associative algebras without an assumed identity, matching the scope of the cited low-dimensional classifications.

The completeness of the seven algebra isomorphism classes is taken from the published classification theorem of Rikhsiboev--Rakhimov--Basri, whose Theorem 4.1 explicitly lists all seven pairwise non-isomorphic two-dimensional complex associative algebras. The quasi-centroid calculations are reconstructed directly from the defining equation and do not depend on the quasi-centroid table being corrected.

No claim is made here about dimensions three or four.

The result is a correction of completeness, not a claim that every matrix displayed in the five printed rows is wrong.

## Proof

Write
\[
\phi(e_1)=a e_1+b e_2,\qquad
\phi(e_2)=c e_1+d e_2.
\]

For each multiplication table, impose
\[
\phi(e_i)e_j=e_i\phi(e_j)
\qquad
(i,j\in\{1,2\}).
\]

For \(A_0\), both sides are always zero, so there is no restriction:
\[
QC(A_0)=M_2(\mathbb C).
\]

For \(A_e\), the sole nonzero product is \(e_1e_1=e_1\). The pair \((e_1,e_2)\) gives
\[
0=e_1\phi(e_2)=c e_1,
\]
so
\[
c=0.
\]
The other ordered pairs add no condition. Hence
\[
QC(A_e)=
\left\{
\begin{pmatrix}
a&0\\
b&d
\end{pmatrix}
\right\}.
\]

For \(A_n\), where \(e_1e_1=e_2\), the same mixed-pair calculation forces
\[
c=0
\]
and no other coefficient is constrained, so the quasi-centroid is again the full lower-triangular matrix algebra.

For \(A_L\), use the products
\[
e_1e_1=e_1,\qquad e_1e_2=e_2.
\]
The quasi-centroid equations force
\[
b=c=0,\qquad d=a,
\]
hence only scalar matrices occur. The opposite algebra \(A_R\) gives the same quasi-centroid.

For \(A_D\), the unit is \(e_1\). Applying the quasi-centroid identity with \(x=e_1\) yields
\[
\phi(e_1)y=\phi(y)
\]
for every \(y\), so \(\phi\) is left multiplication by \(\phi(e_1)=a e_1+b e_2\). In the chosen basis this is
\[
\begin{pmatrix}
a&0\\
b&a
\end{pmatrix}.
\]

For \(A_S=\mathbb C\times\mathbb C\), applying the identity to the orthogonal idempotents \(e_1,e_2\) kills both off-diagonal coefficients:
\[
b=c=0.
\]
The diagonal coefficients are independent.

This gives the seven quasi-centroids and their dimensions.

The seven underlying algebras are pairwise non-isomorphic by the cited complete classification. They can also be separated by elementary invariants: the zero algebra has \(A^2=0\); \(A_n\) is nilpotent with \(A^3=0\); \(A_e\) has \(A^2=A^3\ne0\) and a nonzero annihilator; \(A_L\) and \(A_R\) are distinguished by left versus right annihilator dimensions; \(A_D\) is commutative, unital, and has nonzero nilpotent radical; and \(A_S\) is commutative semisimple.

## Verification

The included program `artifacts/verify.py` encodes all seven multiplication tables over the rational numbers, constructs the linear system for
\[
\phi(e_i)e_j=e_i\phi(e_j),
\]
and computes the exact nullspace.

It obtains quasi-centroid dimensions
\[
4,\ 3,\ 3,\ 1,\ 1,\ 2,\ 2
\]
in the order
\[
A_0,A_e,A_n,A_L,A_R,A_D,A_S.
\]

It separately checks the claimed matrix bases and prints `VERIFY_OK`.

The computation is exact linear algebra; no numerical approximation is used.

## Relationship to prior work

Fiidow--Zahari--Mosbahi state that they compute quasi-centroids for all two-, three-, and four-dimensional associative algebras. Their Theorem 5.1 contains five rows in dimension two, of dimensions \(3,1,1,2,2\), and their proof identifies the first row with the nilpotent algebra \(e_1e_1=e_2\).

The classification paper they cite as a source for low-dimensional associative algebras explicitly says that its displayed tables contain only indecomposable algebras. Its two-dimensional table therefore cannot by itself support a complete theorem covering decomposable algebras.

A separate published classification theorem by Rikhsiboev--Rakhimov--Basri explicitly lists seven pairwise non-isomorphic two-dimensional complex associative algebras, including the zero algebra and the algebra with sole product \(e_1e_1=e_1\). Those are exactly the two classes missing from the five-row quasi-centroid table.

Focused searches for a correction, erratum, or later complete seven-row quasi-centroid table did not locate one.

## Limitations

This correction addresses only Theorem 5.1 in dimension two.

The quasi-centroid table for dimensions three and four was not re-audited here.

The cited preprint may acquire a later revision or an unindexed correction.

Failed searches do not prove that no independent correction exists.

## References

1. M. A. Fiidow, A. Zahari, and B. Mosbahi, “Quasi-Centroids and Quasi-Derivations of Low Dimensional Associative Algebras,” arXiv:2306.14331v1, first public 25 June 2023. The first page gives 2010 MSC \(16D70\).
2. I. M. Rikhsiboev, I. S. Rakhimov, and W. Basri, “Classification of 3-Dimensional Complex Diassociative Algebras,” *Malaysian Journal of Mathematical Sciences* 4(2) (2010), 241–254. Theorem 4.1 lists the seven pairwise non-isomorphic two-dimensional complex associative algebras.
3. I. S. Rakhimov, I. M. Rikhsiboev, and W. Basri, “Complete lists of low dimensional complex associative algebras,” arXiv:0910.0932v2. Its table section explicitly notes that only indecomposable algebras are tabulated.
