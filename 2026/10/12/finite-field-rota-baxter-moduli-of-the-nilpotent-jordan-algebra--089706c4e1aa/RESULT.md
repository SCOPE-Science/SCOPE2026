# Finite-field Rota–Baxter moduli of the nilpotent Jordan algebra \(J_5\)

## Finding

Let \(K\) be a field and let \(J_{5,K}\) be the two-dimensional Jordan algebra with basis
\[
\{e_1,e_2\}
\]
and multiplication
\[
e_1\circ e_1=2e_2,
\qquad
e_1\circ e_2=e_2\circ e_1=e_2\circ e_2=0.
\]

This is the base change of the algebra denoted \(J_5\) by Sun–Huang–Zhao–Tian.

A weight-zero Rota–Baxter operator is a linear map \(R:J_{5,K}\to J_{5,K}\) satisfying
\[
R(x)\circ R(y)
=
R\!\left(R(x)\circ y+x\circ R(y)\right)
\]
for all \(x,y\in J_{5,K}\).

Write
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\]
where the columns are \(R(e_1)\) and \(R(e_2)\). The complete basis-pair system is
\[
\boxed{
2b^2=0,\qquad
2b(a-d)=0,\qquad
2a(a-2d)=0,\qquad
4ab=0.
}
\]

If
\[
\operatorname{char}K\ne2,
\]
this is equivalent to
\[
\boxed{
b=0,\qquad a(a-2d)=0.
}
\]
Hence the Rota–Baxter variety is the union of two affine planes
\[
\mathcal A=\left\{
\begin{pmatrix}
0&0\\
c&d
\end{pmatrix}
:c,d\in K
\right\},
\]
and
\[
\mathcal B=\left\{
\begin{pmatrix}
2d&0\\
c&d
\end{pmatrix}
:c,d\in K
\right\},
\]
meeting in the affine line
\[
\mathcal A\cap\mathcal B
=
\left\{
\begin{pmatrix}
0&0\\
c&0
\end{pmatrix}
:c\in K
\right\}.
\]

For every odd prime power \(q\),
\[
\boxed{
|\operatorname{RB}_0(J_{5,\mathbf F_q})|
=
2q^2-q.
}
\]

The exact rank distribution is
\[
\boxed{
\#\{\operatorname{rank}R=0\}=1,
}
\]
\[
\boxed{
\#\{\operatorname{rank}R=1\}=q^2-1,
}
\]
and
\[
\boxed{
\#\{\operatorname{rank}R=2\}=q(q-1).
}
\]

The full automorphism group is
\[
\boxed{
\operatorname{Aut}(J_{5,K})
=
\left\{
\phi_{s,t}=
\begin{pmatrix}
s&0\\
t&s^2
\end{pmatrix}
:s\in K^\times,\ t\in K
\right\}
}
\]
when \(2\) is invertible.

Over \(\mathbf F_q\) with \(q\) odd, the \(2q^2-q\) operators form exactly
\[
\boxed{2q}
\]
automorphism-conjugacy classes. Their orbit-size distribution is
\[
\boxed{
1\text{ orbit of size }1,\qquad
1\text{ orbit of size }q-1,\qquad
2(q-1)\text{ orbits of size }q.
}
\]

If
\[
\operatorname{char}K=2,
\]
the multiplication
\[
e_1\circ e_1=2e_2
\]
vanishes. Thus \(J_{5,K}\) degenerates to the zero Jordan algebra, and every endomorphism is a weight-zero Rota–Baxter operator. Therefore, for every even prime power \(q\),
\[
\boxed{
|\operatorname{RB}_0(J_{5,\mathbf F_q})|=q^4.
}
\]

The rank distribution in characteristic \(2\) is the ordinary rank distribution in \(M_2(\mathbf F_q)\):
\[
\boxed{
1,\qquad
(q-1)(q+1)^2,\qquad
q(q-1)^2(q+1)
}
\]
in ranks \(0,1,2\), respectively.

Here the automorphism group is all of
\[
\operatorname{GL}_2(\mathbf F_q).
\]
Similarity classes of \(2\times2\) matrices are counted by \(q\) scalar classes and one nonscalar cyclic class for each monic quadratic polynomial. Hence there are exactly
\[
\boxed{q^2+q}
\]
Rota–Baxter conjugacy classes in characteristic \(2\).

The extension-field point counts are
\[
2q^{2m}-q^m
\]
in odd characteristic and
\[
q^{4m}
\]
in characteristic \(2\). Consequently,
\[
\boxed{
Z(T)=\frac{1-qT}{(1-q^2T)^2}
}
\]
in odd characteristic and
\[
\boxed{
Z(T)=\frac{1}{1-q^4T}
}
\]
in characteristic \(2\).

## Assumptions and scope

Sun–Huang–Zhao–Tian classify Rota–Baxter operators on complex Jordan algebras of dimensions at most \(3\). Their Lemma 3.2 identifies
\[
J_5:\qquad e_1\circ e_1=2e_2,
\]
with all other products zero, and their Proposition 5.9 gives the two complex matrix families recovered above.

The source works over \(\mathbb C\). The present theorem treats the integral structure constants literally under base change. In particular, characteristic \(2\) is a genuine degeneration of the multiplication to the zero algebra; it is not being identified with the nonzero complex isomorphism type.

No quotient other than conjugacy by automorphisms of the fixed base-changed algebra is used.

## Proof

For vectors
\[
x=x_1e_1+x_2e_2,
\qquad
y=y_1e_1+y_2e_2,
\]
the product is
\[
x\circ y=2x_1y_1e_2.
\]

Let
\[
R(e_1)=ae_1+ce_2,
\qquad
R(e_2)=be_1+de_2.
\]

The Rota–Baxter defect on \((e_1,e_1)\) is
\[
\begin{pmatrix}
-4ab\\
2a(a-2d)
\end{pmatrix}.
\]
On each of \((e_1,e_2)\) and \((e_2,e_1)\) it is
\[
\begin{pmatrix}
-2b^2\\
2b(a-d)
\end{pmatrix},
\]
and on \((e_2,e_2)\) it is
\[
\begin{pmatrix}
0\\
2b^2
\end{pmatrix}.
\]
This proves the displayed complete system.

Assume first that \(2\) is invertible. Then
\[
b^2=0
\]
forces
\[
b=0.
\]
The remaining equation is
\[
a(a-2d)=0.
\]
This gives precisely \(\mathcal A\cup\mathcal B\).

Over \(\mathbf F_q\), each plane has \(q^2\) points and their intersection has \(q\), so
\[
|\mathcal A\cup\mathcal B|
=
2q^2-q.
\]

On \(\mathcal A\), every nonzero matrix has rank \(1\). There are \(q^2-1\) such matrices.

The points of \(\mathcal B\setminus\mathcal A\) are exactly those with \(d\ne0\). Their determinants are
\[
2d^2\ne0,
\]
so all have rank \(2\). There are
\[
q(q-1)
\]
of them. This proves the rank distribution.

For automorphisms, the square ideal
\[
J_{5,K}^2=Ke_2
\]
is characteristic. Hence any automorphism has
\[
\phi(e_2)=u e_2,\qquad u\ne0.
\]
Write
\[
\phi(e_1)=s e_1+t e_2.
\]
Preserving
\[
e_1\circ e_1=2e_2
\]
gives
\[
2s^2e_2=2u e_2.
\]
When \(2\) is invertible,
\[
u=s^2,
\]
and \(s\ne0\). Thus
\[
\phi=\phi_{s,t}
=
\begin{pmatrix}
s&0\\
t&s^2
\end{pmatrix}.
\]

Conjugation on \(\mathcal A\) is
\[
\phi_{s,t}
\begin{pmatrix}
0&0\\
c&d
\end{pmatrix}
\phi_{s,t}^{-1}
=
\begin{pmatrix}
0&0\\
sc-\dfrac{td}{s}&d
\end{pmatrix}.
\]
Conjugation on \(\mathcal B\) is
\[
\phi_{s,t}
\begin{pmatrix}
2d&0\\
c&d
\end{pmatrix}
\phi_{s,t}^{-1}
=
\begin{pmatrix}
2d&0\\
sc+\dfrac{td}{s}&d
\end{pmatrix}.
\]

Thus \(d\) is an orbit invariant. The zero operator is fixed. When \(d=0\) and \(c\ne0\), all nonzero \(c\)'s lie in one orbit of size \(q-1\). For every fixed \(d\ne0\), the parameter \(t\) acts transitively on \(c\), so \(\mathcal A\) contributes one orbit of size \(q\) and \(\mathcal B\) contributes one orbit of size \(q\). Therefore the total is
\[
1+1+2(q-1)=2q
\]
orbits, with the asserted sizes.

Now let the characteristic be \(2\). Then every product in \(J_{5,K}\) is zero. Both sides of the Rota–Baxter identity vanish for every \(R\), so the operator variety is
\[
M_2(K).
\]
The stated total and rank distribution are the standard rank counts for \(2\times2\) matrices.

Since every invertible linear transformation is now an algebra automorphism, the conjugacy relation is ordinary matrix similarity. There are \(q\) scalar classes. Every nonscalar \(2\times2\) matrix is cyclic, so its similarity class is uniquely determined by its monic quadratic characteristic polynomial, and every monic quadratic occurs. There are \(q^2\) such polynomials. Hence the class count is
\[
q+q^2.
\]

Finally, the same arguments apply over \(\mathbf F_{q^m}\). Substituting
\[
Q=q^m
\]
in the point-count polynomials and applying
\[
Z(T)=\exp\!\left(\sum_{m\ge1}\frac{N_mT^m}{m}\right)
\]
gives the two zeta functions.

## Verification

The included program `artifacts/verify.py` reconstructs the Rota–Baxter defect directly from the multiplication table.

Symbolically it obtains exactly the four scalar equations used in the proof.

It exhaustively checks every \(2\times2\) map over
\[
\mathbf F_2,\qquad
\mathbf F_3,\qquad
\mathbf F_5,\qquad
\mathbf F_7.
\]

The direct operator counts are
\[
16,\qquad15,\qquad45,\qquad91.
\]
For the odd fields these equal
\[
2q^2-q,
\]
and for \(\mathbf F_2\) the count is
\[
2^4.
\]

The odd-field rank profiles are
\[
(1,8,6),\qquad
(1,24,20),\qquad
(1,48,42),
\]
and the automorphism-orbit counts are
\[
6,\qquad10,\qquad14.
\]

The checker also verifies the stated orbit-size distributions and, over \(\mathbf F_2\), the six ordinary similarity classes.

It returns `VERIFY_OK`.

Finite enumeration is a replay check. The arbitrary-prime-power formulas follow from the field-level proof above.

## Relationship to prior work

Sun, Huang, Zhao, and Tian give all Rota–Baxter operators on complex Jordan algebras of dimensions at most \(3\). Their Proposition 5.9 gives exactly the two complex \(J_5\) families
\[
\begin{pmatrix}
0&0\\
r_{21}&r_{22}
\end{pmatrix}
\]
and
\[
\begin{pmatrix}
2r_{22}&0\\
r_{21}&r_{22}
\end{pmatrix},
\qquad r_{22}\ne0.
\]
Their classification does not count finite-field points, ranks, or automorphism-conjugacy classes, and it does not treat the characteristic-\(2\) base-change degeneration.

Gubarev studies weight-zero Rota–Baxter operators on broad classes of Jordan algebras and, in separate work, finite-field simple Jordan algebras of Clifford type. Those results concern unital or simple Jordan settings and do not give the finite-field moduli of this nilpotent two-dimensional algebra.

Focused searches for \(J_5\), the multiplication \(e_1\circ e_1=2e_2\), finite-field Rota–Baxter counts, automorphism conjugacy, and the polynomial
\[
2q^2-q
\]
did not locate a covering result.

## Limitations

The theorem concerns the specific integral model
\[
e_1\circ e_1=2e_2.
\]
Its characteristic-\(2\) fiber is the zero algebra, so the jump is a degeneration of the algebra itself rather than a hidden extra branch on a fixed nonzero multiplication.

The automorphism-orbit formulas are for the fixed-coordinate base-changed algebra and do not compare different Jordan algebra isomorphism types.

A specialized or differently indexed finite-field computation may contain the same point or orbit counts. Failed searches do not prove novelty.

## References

1. Y. Sun, Z. Huang, S. Zhao, and Z. Tian, “Classification of pre-Jordan Algebras and Rota-Baxter Operators on Jordan Algebras in Low Dimensions,” arXiv:2111.02035v1, first public 3 November 2021.
2. V. Gubarev, “Rota-Baxter operators on unital algebras,” *Moscow Mathematical Journal* 21 (2021), 325–364.
3. V. Gubarev, “Rota–Baxter operators of weight zero on simple Jordan algebra of Clifford type,” *Siberian Electronic Mathematical Reports* 14 (2017), 1524–1532.
