# A complete repair of a two-dimensional Hom-Jordan Rota–Baxter example

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2,
\]
and for \(\lambda\in K\) let \(H_\lambda\) be the two-dimensional Hom-Jordan algebra with basis
\[
\{e_1,e_2\},
\]
multiplication
\[
e_1\circ e_1=2e_1,
\qquad
e_1\circ e_2=e_2\circ e_1=2\lambda e_2,
\qquad
e_2\circ e_2=0,
\]
and twist
\[
\alpha(e_1)=e_1,
\qquad
\alpha(e_2)=\lambda e_2.
\]

Using the Rota–Baxter definition in Chtioui–Mabrouk–Makhlouf, namely
\[
R\alpha=\alpha R
\]
together with
\[
R(x)\circ R(y)
=
R\!\left(R(x)\circ y+x\circ R(y)\right),
\]
the complete classification is
\[
\boxed{
\lambda=1:
\quad
R=
\begin{pmatrix}
0&0\\
u&0
\end{pmatrix},
\qquad u\in K,
}
\]
\[
\boxed{
\lambda=0:
\quad
R=
\begin{pmatrix}
0&0\\
0&v
\end{pmatrix},
\qquad v\in K,
}
\]
and
\[
\boxed{
\lambda\notin\{0,1\}:
\quad
R=0.
}
\]

Chtioui–Mabrouk–Makhlouf Example 2.2 prints, for arbitrary parameters \(\lambda,b\),
\[
R(e_1)=b e_2,
\qquad
R(e_2)=0,
\]
and calls \(R\) a Rota–Baxter operator. This map satisfies the product equation for every \(\lambda,b\), but
\[
R\alpha(e_1)=b e_2,
\qquad
\alpha R(e_1)=\lambda b e_2.
\]
Therefore it satisfies the required twist compatibility precisely when
\[
\boxed{
(\lambda-1)b=0.
}
\]

Thus the printed two-parameter assertion is too large: for
\[
\lambda\ne1,\qquad b\ne0,
\]
the displayed map is not a Rota–Baxter operator under the paper's own Definition 1.3. In particular, Corollary 2.1 cannot be invoked for those parameters.

There is also a second family, omitted by Example 2.2:
\[
\lambda=0,
\qquad
R(e_1)=0,
\qquad
R(e_2)=v e_2.
\]

As a finite-field corollary, for every odd prime power \(q\),
\[
\boxed{
\#\{(\lambda,R):\lambda\in\mathbf F_q,\ R\in\operatorname{RB}(H_\lambda)\}
=
3q-2.
}
\]

## Assumptions and scope

The multiplication and twist are exactly those of Example 2.2 in Chtioui–Mabrouk–Makhlouf.

The source works over a field of characteristic \(0\). The proof below works unchanged over every field in which \(2\) is invertible.

The source defines a weight-zero Rota–Baxter operator on a Hom-Jordan algebra as an \(\mathcal O\)-operator associated to the adjoint representation. Its Definition 1.3 therefore imposes two separate conditions:
\[
R\alpha=\alpha R
\]
and the weight-zero product equation.

This finding concerns that exact definition. It does not replace the source's Rota–Baxter notion by the product equation alone.

Matrices use the column convention
\[
R(e_1)=x e_1+z e_2,
\qquad
R(e_2)=y e_1+w e_2.
\]

## Proof

First, the displayed Hom-Jordan structure itself is characteristic-free at the level of the defining identity: direct substitution into
\[
\operatorname{as}_\alpha(x\circ x,\alpha(y),\alpha(x))=0
\]
gives zero identically. We now assume \(2\) is invertible in order to solve the Rota–Baxter equations in the form below.

Write
\[
R=
\begin{pmatrix}
x&y\\
z&w
\end{pmatrix}.
\]

The twist-commutation equation
\[
R\alpha=\alpha R
\]
is equivalent to
\[
\boxed{
(\lambda-1)y=0,
\qquad
(\lambda-1)z=0.
}
\]

The Rota–Baxter product defect is bilinear, so it is enough to evaluate it on
\[
(e_1,e_1),\qquad(e_1,e_2),\qquad(e_2,e_2).
\]
After division by the invertible scalar \(2\), the resulting equations are
\[
x^2+2\lambda yz=0,
\]
\[
z\bigl(\lambda(x-w)-x\bigr)=0,
\]
\[
\lambda y(w+x)=0,
\]
\[
\lambda w^2+(1-\lambda)yz=0,
\]
and
\[
(2\lambda-1)y^2=0.
\]

Suppose first that
\[
\lambda\ne1.
\]
Twist compatibility gives
\[
y=z=0.
\]
The first product equation then gives
\[
x^2=0,
\]
hence
\[
x=0
\]
because \(K\) is a field. The fourth gives
\[
\lambda w^2=0.
\]

If
\[
\lambda\ne0,
\]
then
\[
w=0,
\]
so only the zero operator remains.

If
\[
\lambda=0,
\]
then \(w\) is arbitrary. This yields exactly
\[
R=
\begin{pmatrix}
0&0\\
0&w
\end{pmatrix}.
\]

Now suppose
\[
\lambda=1.
\]
The fourth product equation gives
\[
w^2=0,
\]
hence \(w=0\). The fifth becomes
\[
y^2=0,
\]
hence \(y=0\). The first then gives
\[
x^2=0,
\]
hence \(x=0\). No equation remains on \(z\), so
\[
R=
\begin{pmatrix}
0&0\\
z&0
\end{pmatrix}
\]
with arbitrary \(z\).

This proves the classification.

For the operator printed in Example 2.2,
\[
x=y=w=0,
\qquad
z=b.
\]
Every product-defect equation above vanishes identically, but twist commutation reduces to
\[
(\lambda-1)b=0.
\]
Thus the precise defect in the generic printed family is the omitted twist-compatibility condition.

Finally, over an odd finite field \(\mathbf F_q\), there are \(q\) operators at \(\lambda=0\), \(q\) at \(\lambda=1\), and only the zero operator for each of the other \(q-2\) parameters. Hence
\[
q+q+(q-2)=3q-2.
\]

## Verification

The included program `artifacts/verify.py` reconstructs the Hom-Jordan associator, the twist commutator, and the Rota–Baxter defect from the multiplication table.

Symbolically it verifies that the Hom-Jordan identity vanishes, that
\[
R\alpha-\alpha R
\]
has exactly the two off-diagonal factors
\[
(\lambda-1)y,
\qquad
(1-\lambda)z,
\]
and that the product defect yields the five equations used in the proof.

For the source's printed map
\[
R(e_1)=b e_2,\qquad R(e_2)=0,
\]
the checker verifies that the product defect is identically zero while
\[
(R\alpha-\alpha R)(e_1)=(1-\lambda)b e_2.
\]

It then exhaustively enumerates every parameter \(\lambda\) and every \(2\times2\) matrix over
\[
\mathbf F_3,\qquad
\mathbf F_5,\qquad
\mathbf F_7.
\]
For each field it obtains exactly \(q\) solutions at \(\lambda=0\), \(q\) at \(\lambda=1\), and one solution at every other parameter, for a total of
\[
3q-2.
\]

The script returns `VERIFY_OK`.

The finite enumeration is a replay check; the arbitrary-field classification is proved symbolically above.

## Relationship to prior work

Chtioui, Mabrouk, and Makhlouf introduce Hom-pre-Jordan and Hom-J-dendriform algebras and define weight-zero Rota–Baxter operators on Hom-Jordan algebras by requiring both twist commutation and the product identity. Their Example 2.2 is the exact family treated here. The published example states that
\[
R(e_1)=b e_2,\qquad R(e_2)=0
\]
is Rota–Baxter for arbitrary parameters, but the same paper's Definition 1.3 forces the additional condition
\[
(\lambda-1)b=0.
\]

The later classification of Sun, Huang, Zhao, and Tian treats ordinary complex Jordan algebras in dimensions at most \(3\). It contains no Hom-Jordan occurrence in the inspected full text and therefore does not classify the twisted family here.

Targeted searches for the paper title together with Example 2.2, the displayed operator, twist commutation, corrections, and errata did not locate a published repair. Semantic-database searches likewise returned only unrelated low-dimensional operator classifications.

## Limitations

The complete classification is for the one-parameter two-dimensional Hom-Jordan family of Example 2.2.

The theorem assumes that \(2\) is invertible. Characteristic \(2\) degenerates the displayed multiplication and is a separate problem.

The finding does not claim that the multiplication produced in the source for generic invalid parameters necessarily fails every Hom-pre-Jordan identity; the precise claim is that Corollary 2.1 cannot certify it through a Rota–Baxter operator when the required twist-commutation condition fails.

An unindexed correction or erratum may exist. Failed searches do not prove novelty.

## References

1. T. Chtioui, S. Mabrouk, and A. Makhlouf, “Construction of Hom-Pre-Jordan algebras and Hom-J-dendriform algebras,” arXiv:2007.01078v1, first public 2 July 2020; *Extracta Mathematicae* 38 (2023), 27–50, DOI `10.17398/2605-5686.38.1.27`.
2. Y. Sun, Z. Huang, S. Zhao, and Z. Tian, “Classification of pre-Jordan Algebras and Rota-Baxter Operators on Jordan Algebras in Low Dimensions,” arXiv:2111.02035v1, first public 3 November 2021.
