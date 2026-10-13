# Six product-structure orbits on the nontrivial three-dimensional \(3\)-Lie algebra

## Finding

Let \(K\) be a field of characteristic different from \(2\), and let \(L_K\) be the three-dimensional \(3\)-Lie algebra with basis
\[
\{e_1,e_2,e_3\}
\]
and sole independent nonzero bracket
\[
[e_1,e_2,e_3]=e_1.
\]

A product structure is an endomorphism \(E\) with
\[
E^2=I,\qquad E\ne\pm I,
\]
satisfying the Nijenhuis integrability condition. On this particular \(3\)-Lie algebra every endomorphism is Nijenhuis. Consequently every nonscalar involution is a product structure.

The full automorphism group is
\[
\boxed{
\operatorname{Aut}(L_K)
=
\left\{
\begin{pmatrix}
\lambda&r&s\\
0&a&b\\
0&c&d
\end{pmatrix}
:
\lambda\in K^\times,\quad ad-bc=1
\right\}.
}
\]

Up to conjugation by \(\operatorname{Aut}(L_K)\), there are exactly six product structures. Three representatives with two-dimensional \(+1\)-eigenspace are
\[
\boxed{
E_{\mathrm{s}}
=
\operatorname{diag}(1,1,-1),
}
\]
\[
\boxed{
E_{\mathrm{p}}
=
\operatorname{diag}(-1,1,1),
}
\]
and
\[
\boxed{
E_{\mathrm{g}}
=
\begin{pmatrix}
-1&0&0\\
-2&1&0\\
0&0&1
\end{pmatrix}.
}
\]
The remaining three representatives are their negatives.

Let
\[
D=[L_K,L_K,L_K]=Ke_1.
\]
For each of the two possible dimensions of the \(+1\)-eigenspace, the three orbits are distinguished exactly by
\[
D\subseteq L_+,\qquad
D\subseteq L_-,\qquad
D\not\subseteq L_+\cup L_-,
\]
where
\[
L_\pm=\ker(E\mp I).
\]

More intrinsically, there are three geometric types, each with a sign-paired companion:

- **strong abelian:** \(D\) is contained in the two-dimensional eigenspace;
- **perfect:** \(D\) is the one-dimensional eigenspace;
- **generic abelian:** \(D\) lies in neither eigenspace.

All six are abelian product structures because every proper subspace of this three-dimensional alternating algebra is an abelian \(3\)-Lie subalgebra.

Over every odd finite field \(\mathbf F_q\), the exact number of product structures is
\[
\boxed{
2q^2(q^2+q+1).
}
\]
The six automorphism-orbit sizes are
\[
\boxed{
q^2,\quad q^2,\quad
q^2(q+1),\quad q^2(q+1),\quad
q^2(q^2-1),\quad q^2(q^2-1).
}
\]

## Assumptions and scope

The characteristic restriction
\[
\operatorname{char}K\ne2
\]
is essential to the eigenspace argument: an involution then diagonalizes with eigenvalues \(+1\) and \(-1\).

The algebra is the unique nontrivial three-dimensional \(3\)-Lie algebra appearing in the cited product-structure literature.

The equivalence relation is conjugacy by automorphisms of the fixed \(3\)-Lie algebra:
\[
E\sim \phi E\phi^{-1}.
\]

The scalar involutions \(I\) and \(-I\) are excluded because the standard definition of an almost product structure requires
\[
E\ne\pm I.
\]

No classification in characteristic \(2\) is claimed.

## Proof

The bracket has the determinant form
\[
[x,y,z]
=
\det(x,y,z)e_1
\]
for column vectors in the ordered basis \((e_1,e_2,e_3)\).

The cited later paper records that every linear transformation of this algebra is Nijenhuis. The accompanying verification reconstructs this directly from the Nijenhuis identity, so the product-structure problem reduces exactly to classifying nonscalar involutions.

Because
\[
\operatorname{char}K\ne2,
\]
every involution \(E\) is diagonalizable:
\[
L_K=L_+\oplus L_-.
\]
Since \(E\ne\pm I\), both eigenspaces are nonzero, hence their dimensions are \(1\) and \(2\). Every one- or two-dimensional subspace is an abelian \(3\)-Lie subalgebra because an alternating ternary bracket vanishes on any subspace of dimension at most \(2\). The decomposition criterion for product structures therefore applies to every nonscalar involution.

Next determine the automorphism group. For an invertible matrix \(P\),
\[
[P x,P y,P z]
=
\det(P)\det(x,y,z)e_1.
\]
Thus \(P\) is an automorphism precisely when
\[
P e_1=\det(P)e_1.
\]
Writing
\[
P=
\begin{pmatrix}
\lambda&r&s\\
0&a&b\\
0&c&d
\end{pmatrix},
\]
one has
\[
\det(P)=\lambda(ad-bc).
\]
The condition \(Pe_1=\det(P)e_1\) is therefore equivalent to
\[
ad-bc=1,
\]
with \(\lambda\ne0\). This gives the displayed automorphism group.

The derived line
\[
D=Ke_1
\]
is characteristic, so every automorphism preserves it. Consequently the dimension of \(L_+\) and the incidence type of \(D\) with the two eigenspaces are conjugacy invariants.

There are exactly three incidence types for each fixed eigenspace dimension:

\[
D\subseteq L_+,
\]
\[
D\subseteq L_-,
\]
or
\[
D\not\subseteq L_+\cup L_-.
\]

The automorphism group is transitive on each type. This can be seen from its action on the quotient
\[
L_K/D\cong K^2,
\]
where the lower-right block ranges through
\[
\operatorname{SL}_2(K),
\]
together with the free top-row shears \(r,s\). The \(\operatorname{SL}_2(K)\)-action normalizes the one- and two-dimensional quotient data, while the shears normalize the lift of the complementary line. Thus the six displayed representatives form a complete transversal.

For the generic representative
\[
E_{\mathrm g}
=
\begin{pmatrix}
-1&0&0\\
-2&1&0\\
0&0&1
\end{pmatrix},
\]
one has
\[
L_+=\operatorname{span}\{e_2,e_3\},
\qquad
L_-=\operatorname{span}\{e_1+e_2\},
\]
so \(D\) lies in neither eigenspace. The negative representative exchanges \(L_+\) and \(L_-\).

The strong/perfect distinction follows from the mixed-bracket identities. Take a basis of the two-dimensional eigenspace together with a generator of the complementary one-dimensional eigenspace. Their bracket is a nonzero multiple of \(e_1\). Hence the strong condition holds exactly when \(D\) belongs to the two-dimensional eigenspace, while the perfect condition holds exactly when \(D\) is the one-dimensional eigenspace. If \(D\) lies in neither, neither stronger condition holds.

For the finite-field count, fix odd \(q\). An involution with one-dimensional \(+1\)-eigenspace is equivalent to an ordered direct-sum decomposition
\[
\mathbf F_q^3=U\oplus W,
\qquad
\dim U=1,\quad \dim W=2.
\]
There are
\[
q^2+q+1
\]
choices for \(U\), and each line has exactly
\[
q^2
\]
complementary planes. Thus there are
\[
q^2(q^2+q+1)
\]
such involutions. The same number has two-dimensional \(+1\)-eigenspace, giving
\[
2q^2(q^2+q+1)
\]
product structures.

For a fixed sign choice, the three orbit sizes are obtained by counting decompositions according to the position of \(D\):

- if \(D\) is the one-dimensional eigenspace, there are
  \[
  q^2
  \]
  complementary planes;

- if \(D\) lies in the two-dimensional eigenspace, there are
  \[
  q^2(q+1)
  \]
  decompositions;

- if \(D\) lies in neither eigenspace, there are
  \[
  q^2(q^2-1)
  \]
  decompositions.

Repeating these three sizes for the negative sign gives the six stated orbit sizes.

## Verification

The included program `artifacts/verify.py` performs three independent checks.

First, it represents the bracket by
\[
[x,y,z]=\det(x,y,z)e_1
\]
and symbolically substitutes a completely general \(3\times3\) endomorphism into the \(3\)-Lie Nijenhuis identity. Every coefficient of the defect vanishes identically.

Second, it verifies the automorphism condition
\[
Pe_1=\det(P)e_1
\]
and checks each of the six normal forms directly:
\[
E^2=I,\qquad E\ne\pm I.
\]
It also tests the product, abelian, strong, and perfect identities on all ordered basis triples and reproduces the three-type classification.

Third, over \(\mathbf F_3\) it exhaustively enumerates all \(3^9\) matrices, finds exactly
\[
234
\]
product structures, constructs the full automorphism group of order
\[
432,
\]
and obtains exactly six orbits of sizes
\[
9,\ 9,\ 36,\ 36,\ 72,\ 72.
\]
Including the two excluded scalar involutions gives \(236\) involutions in eight orbits, providing a separate boundary check.

Over \(\mathbf F_5\), the checker generates the six automorphism orbits from the normal forms and obtains sizes
\[
25,\ 25,\ 150,\ 150,\ 600,\ 600,
\]
whose sum is
\[
1550=2\cdot25\cdot31.
\]

The script returns `VERIFY_OK`.

Finite enumeration is not used in place of the arbitrary-field proof.

## Relationship to prior work

Sheng and Tang define product structures on \(3\)-Lie algebras as nontrivial involutions satisfying the Nijenhuis integrability condition and prove the eigenspace-decomposition criterion. Their Example 5.22 uses exactly the algebra
\[
[e_1,e_2,e_3]=e_1
\]
and displays three product structures:
\[
\operatorname{diag}(1,1,-1),
\qquad
\operatorname{diag}(1,-1,1),
\qquad
\operatorname{diag}(-1,1,1).
\]
The first two are strong abelian, while the third is perfect.

Those matrices are presented as examples rather than an orbit classification. In fact, the first two displayed matrices are automorphism-conjugate: an \(\operatorname{SL}_2(K)\) change of the \((e_2,e_3)\)-coordinates interchanges their quotient eigendirections. Thus the three examples occupy only two of the three two-dimensional-\(+1\) orbit types; the generic incidence type is absent from that list.

Hou and Sheng later revisit the same three-dimensional \(3\)-Lie algebra and state that every linear transformation on it is a Nijenhuis operator. This supplies an independent literature bridge from Nijenhuis theory to the product-structure problem, but it does not classify involutions modulo automorphisms.

Targeted searches for product structures, Nijenhuis involutions, automorphism conjugacy, the exact bracket, and three-dimensional \(3\)-Lie normal forms did not locate the six-orbit classification or the finite-field orbit census.

## Limitations

The complete orbit classification is asserted only when
\[
\operatorname{char}K\ne2.
\]
Characteristic \(2\) has different involution geometry and is not covered.

The finite-field formulas count product structures on the fixed algebra and then quotient by its automorphism group; they do not classify arbitrary three-dimensional ternary algebras.

The originality search cannot exclude a differently phrased or unindexed orbit computation.

## References

1. Y. Sheng and R. Tang, “Symplectic, product and complex structures on \(3\)-Lie algebras,” arXiv:1711.08381v1, first public 19 November 2017.
2. R. Hou and Y. Sheng, “Twisted Rota-Baxter operators on \(3\)-Lie algebras and NS-\(3\)-Lie algebras,” arXiv:2107.13950v1, first public 28 July 2021.
