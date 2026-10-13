# The deformed Mendelian family has one nonzero baric isomorphism class

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2.
\]
For \(\varepsilon\in K\), let \(A_\varepsilon\) be the two-dimensional commutative algebra with basis
\[
\{e_1,e_2\}
\]
and multiplication
\[
e_1^2=(1-\varepsilon)e_1+\varepsilon e_2,
\qquad
e_1e_2=\frac12(e_1+e_2),
\qquad
e_2^2=e_2.
\]
This is the deformed Mendelian family in Example 3 of Bustamante, Mellon, and Velasco. It is baric with
\[
\xi(e_1)=\xi(e_2)=1.
\]

The exact evolution-algebra boundary is
\[
\boxed{
A_\varepsilon\text{ is an evolution algebra if and only if }\varepsilon\ne0.
}
\]

More strongly, every nonzero member of the family has the same baric isomorphism type. Let \(B\) have natural basis
\[
\{x,y\}
\]
with
\[
x^2=-x,\qquad
xy=0,\qquad
y^2=-x+2y,
\]
and baric weight
\[
\omega(x)=0,\qquad
\omega(y)=2.
\]
Then for every \(\varepsilon\ne0\),
\[
\boxed{
(A_\varepsilon,\xi)\cong(B,\omega).
}
\]

The fixed algebra \(B\) is rigid in two elementary senses:
\[
\boxed{\operatorname{Aut}(B)=\{I\},}
\]
and its ordered natural bases are exactly
\[
\boxed{
(\lambda x,\mu y)
\quad\text{and}\quad
(\lambda y,\mu x),
\qquad
\lambda,\mu\in K^\times.
}
\]

Hence over every odd finite field \(\mathbf F_q\), all \(q-1\) nonzero parameters \(\varepsilon\) represent one baric-isomorphism class, and \(B\) has
\[
\boxed{2(q-1)^2}
\]
ordered natural bases.

## Assumptions and scope

The primary source was published on 12 August 2020 and lists \(17D92\) first among its Mathematics Subject Classification codes. Its Example 3 introduces this deformed Mendelian family, proves the evolution-algebra criterion over the real or complex field used in the paper, and gives the natural basis
\[
e_1-e_2,\qquad e_1+(2\varepsilon-1)e_2
\]
when \(\varepsilon\ne0\).

The result here addresses the isomorphism type of the family rather than only the existence of a natural basis. It works over every field of characteristic different from \(2\).

A later correction to the source changes the wording of a simultaneous-diagonalization theorem; it does not alter the displayed multiplication table of Example 3.

## Proof

For \(\varepsilon\ne0\), set
\[
u=e_1-e_2,
\qquad
v=e_1+(2\varepsilon-1)e_2.
\]
Direct multiplication gives
\[
u^2=-\varepsilon u,
\qquad
uv=0,
\qquad
v^2=\varepsilon(-u+2v).
\]
Since
\[
\det
\begin{pmatrix}
1&1\\
-1&2\varepsilon-1
\end{pmatrix}
=
2\varepsilon,
\]
the pair \(\{u,v\}\) is a basis.

Define
\[
\Phi_\varepsilon(u)=\varepsilon x,
\qquad
\Phi_\varepsilon(v)=\varepsilon y.
\]
Then
\[
\Phi_\varepsilon(u^2)
=
-\varepsilon^2x
=
\Phi_\varepsilon(u)^2,
\]
\[
\Phi_\varepsilon(uv)=0
=
\Phi_\varepsilon(u)\Phi_\varepsilon(v),
\]
and
\[
\Phi_\varepsilon(v^2)
=
\varepsilon^2(-x+2y)
=
\Phi_\varepsilon(v)^2.
\]
Thus \(\Phi_\varepsilon\) is an algebra isomorphism.

The baric weights are also preserved:
\[
\xi(u)=0,
\qquad
\xi(v)=2\varepsilon,
\]
while
\[
\omega(\Phi_\varepsilon(u))=0,
\qquad
\omega(\Phi_\varepsilon(v))=2\varepsilon.
\]
Therefore \(\Phi_\varepsilon\) is a baric algebra isomorphism.

It remains to treat \(\varepsilon=0\) without using simultaneous diagonalization. Write
\[
z=ae_1+be_2.
\]
For
\[
w=ce_1+de_2,
\]
the equation \(zw=0\), after multiplying coordinates by \(2\), is
\[
\begin{pmatrix}
2a+b&a\\
b&a+2b
\end{pmatrix}
\begin{pmatrix}
c\\d
\end{pmatrix}
=0.
\]
The determinant is
\[
2(a+b)^2.
\]
If \(a+b\ne0\), the multiplication map by \(z\) has trivial kernel. If \(a+b=0\) and \(z\ne0\), its kernel is exactly \(Kz\). Hence no two linearly independent nonzero vectors multiply to zero. A two-dimensional evolution algebra would require such a pair as a natural basis, so \(A_0\) is not an evolution algebra.

For the automorphism statement, let
\[
F(x)=ax+cy,
\qquad
F(y)=bx+dy.
\]
The equations \(F(r s)=F(r)F(s)\) for \(r,s\in\{x,y\}\) imply
\[
a^2+c^2=a,
\qquad
c(2c+1)=0,
\qquad
ab+cd=0,
\qquad
cd=0,
\]
\[
b^2+d^2=a-2b,
\qquad
2d^2=-c+2d.
\]
If \(c=0\), invertibility forces
\[
a=d=1,\qquad b=0.
\]
If \(c=-\frac12\), then \(cd=0\) gives \(d=0\), while invertibility and \(ab+cd=0\) force \(a=0\); this contradicts
\[
a^2+c^2=a.
\]
Therefore \(F=I\).

Finally, for
\[
X=rx+sy,
\qquad
Y=tx+uy,
\]
one has
\[
XY=-(rt+su)x+2su\,y.
\]
Thus \(XY=0\) implies
\[
su=0,\qquad rt=0.
\]
If \(X,Y\) are independent, exactly one vector lies on each coordinate axis. This gives precisely the two displayed natural-basis families.

## Verification

The included program `artifacts/verify.py` reconstructs the multiplication of \(A_\varepsilon\) and verifies symbolically that
\[
u^2=-\varepsilon u,\qquad
uv=0,\qquad
v^2=\varepsilon(-u+2v).
\]

It verifies the explicit baric isomorphism to \(B\), reconstructs the automorphism equations of \(B\), and checks the natural-basis classification.

As finite replay evidence, it exhaustively checks
\[
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7,\quad
\mathbf F_{11}.
\]
For every tested field, \(A_0\) has no ordered natural basis; each \(A_\varepsilon\) with \(\varepsilon\ne0\) has exactly
\[
2(q-1)^2
\]
ordered natural bases; and \(B\) has exactly one automorphism.

The checker returns `VERIFY_OK`.

The finite computations are not used as a proof for arbitrary fields; the arbitrary-field conclusions follow from the displayed symbolic identities and kernel argument.

## Relationship to prior work

The primary paper proves that its deformed Mendelian algebra is an evolution algebra exactly in the nonzero-parameter regime considered there and supplies the natural basis used above. It does not identify all nonzero parameters as one baric-isomorphism class, nor does it state the automorphism or natural-basis classification of the resulting fixed algebra.

Targeted searches were made for the family under “deformed Mendelian inheritance,” for isomorphism and baric-isomorphism classifications, for the exact natural basis printed in Example 3, and for equivalent two-dimensional evolution-algebra normal forms. No source located in those searches states the nonzero moduli collapse.

General low-dimensional evolution-algebra classifications can contain an algebra isomorphic to \(B\) under another label. Such a classification by itself does not identify the entire genetic deformation family with one fixed baric algebra; this remains the main residual literature risk.

## Limitations

The result concerns this specific two-dimensional Mendelian deformation family.

The characteristic-\(2\) case is excluded because the source multiplication uses \(\frac12\).

The originality search cannot rule out an equivalent normal form under different low-dimensional evolution-algebra notation.

Failed searches do not prove absolute historical novelty.

## References

1. M. D. Bustamante, P. Mellon, and M. V. Velasco, “Determining When an Algebra Is an Evolution Algebra,” *Mathematics* 8 (2020), 1349, DOI `10.3390/math8081349`; author postprint arXiv:2102.04493.
2. M. D. Bustamante, P. Mellon, and M. V. Velasco, “Correction: Determining When an Algebra Is an Evolution Algebra,” *Mathematics* 9 (2021), 1289, DOI `10.3390/math9111289`.
