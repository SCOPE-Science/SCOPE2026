# Adjoint embedding tensors on the three-dimensional \(3\)-Lie algebra

## Finding

Let \(K\) be a field and let
\[
A_K=Ke_1\oplus Ke_2\oplus Ke_3
\]
carry the alternating ternary bracket determined by
\[
[e_1,e_2,e_3]=e_1.
\]

For the adjoint representation, an embedding tensor is a linear map
\[
T:A_K\to A_K
\]
satisfying
\[
[Tx,Ty,Tz]
=
T([Tx,Ty,z])
\]
for every
\[
x,y,z\in A_K.
\]

The complete classification is by rank:
\[
\boxed{
\operatorname{rank}T\le1
\quad\Longrightarrow\quad
T\text{ is an embedding tensor},
}
\]
\[
\boxed{
\operatorname{rank}T=2
\quad\Longrightarrow\quad
T\text{ is an embedding tensor}
\iff
T(e_1)=0,
}
\]
and
\[
\boxed{
\operatorname{rank}T=3
\quad\Longrightarrow\quad
T\text{ is an embedding tensor}
\iff
T=\lambda I
\text{ for some }\lambda\in K^\times.
}
\]

Equivalently,
\[
\boxed{
\operatorname{ET}_{\mathrm{ad}}(A_K)
=
\{T:\operatorname{rank}T\le1\}
\cup
\{T:T(e_1)=0\}
\cup
\{\lambda I:\lambda\in K^\times\}.
}
\]

For every prime power \(q\), the exact rank distribution over \(\mathbf F_q\), in ranks \(0,1,2,3\), is
\[
\boxed{
\left(
1,\,
(q-1)(q^2+q+1)^2,\,
(q^3-1)(q^3-q),\,
q-1
\right).
}
\]

Therefore
\[
\boxed{
|\operatorname{ET}_{\mathrm{ad}}(A_{\mathbf F_q})|
=
q^6+q^5-q^2+q-1.
}
\]

The same classification holds over every extension field. Thus
\[
|\operatorname{ET}_{\mathrm{ad}}(A_{\mathbf F_q})(\mathbf F_{q^m})|
=
q^{6m}+q^{5m}-q^{2m}+q^m-1,
\]
and the Hasse--Weil zeta function is
\[
\boxed{
Z(T)
=
\frac{(1-q^2T)(1-T)}
{(1-q^6T)(1-q^5T)(1-qT)}.
}
\]

There is a sharp distinction from the adjoint \(\mathcal O\)-operator problem. If
\[
T=I,
\]
then the embedding-tensor identity is tautological. By contrast, the adjoint \(\mathcal O\)-operator identity has three terms on its right-hand side, so for \(T=I\) it reads
\[
[x,y,z]=3[x,y,z].
\]
Hence, when
\[
\operatorname{char}K\ne2,
\]
the identity map is not an adjoint \(\mathcal O\)-operator, despite being an embedding tensor.

## Assumptions and scope

Hu, Hou, Song, and Zhou introduce embedding tensors on \(3\)-Lie algebras and define them by
\[
[Tu,Tv,Tw]
=
T(\rho(Tu,Tv)w).
\]
For the adjoint representation,
\[
\rho(x,y)z=[x,y,z],
\]
which gives the identity used here.

Their paper works over an algebraically closed field of characteristic \(0\). The calculation in this result uses the defining alternating bracket and determinant identities directly and is valid over every field.

The model
\[
[e_1,e_2,e_3]=e_1
\]
is the unique nontrivial three-dimensional complex \(3\)-Lie algebra in the later classification used by Cheng, Kang, and Lü. The arbitrary-field theorem here concerns this fixed integral model; it does not claim an isomorphism classification of all three-dimensional \(3\)-Lie algebras over every field.

## Proof

Let
\[
\omega(x,y,z)
\]
be the determinant of the coordinate matrix with columns \(x,y,z\). Then
\[
[x,y,z]=\omega(x,y,z)e_1.
\]

The Fundamental Identity follows from the determinant expansion
\[
\begin{aligned}
\omega(a,b,c)\omega(x,y,e_1)
={}&
\omega(x,y,a)\omega(e_1,b,c)\\
&+
\omega(x,y,b)\omega(a,e_1,c)\\
&+
\omega(x,y,c)\omega(a,b,e_1).
\end{aligned}
\]
Thus this bracket defines a \(3\)-Lie algebra over every field.

For a linear map \(T\), the embedding-tensor identity becomes
\[
\det(T)\,\omega(x,y,z)e_1
=
\omega(Tx,Ty,z)\,T(e_1)
\]
for every \(x,y,z\).

Suppose first that
\[
\operatorname{rank}T\le1.
\]
Then
\[
\det(T)=0
\]
and \(Tx,Ty\) are always linearly dependent, so both sides vanish. Every rank-at-most-one map is therefore an embedding tensor.

Now suppose
\[
\operatorname{rank}T=2.
\]
Again
\[
\det(T)=0.
\]
The identity is therefore
\[
\omega(Tx,Ty,z)\,T(e_1)=0
\]
for all \(x,y,z\).

Because the image of \(T\) has dimension \(2\), there exist \(x,y\) such that
\[
Tx,\ Ty
\]
are linearly independent, and then there exists \(z\) with
\[
\omega(Tx,Ty,z)\ne0.
\]
Hence
\[
T(e_1)=0.
\]

Conversely, if
\[
\operatorname{rank}T=2
\qquad\text{and}\qquad
T(e_1)=0,
\]
then the right side is zero and the left side is zero because
\[
\det(T)=0.
\]
Thus this condition is also sufficient.

Finally suppose
\[
\operatorname{rank}T=3.
\]
Then \(T\) is invertible. The embedding identity implies
\[
T(e_1)\in Ke_1,
\]
because there exist \(x,y,z\) for which
\[
\omega(Tx,Ty,z)\ne0
\]
while the left side is a multiple of \(e_1\). Write
\[
T(e_1)=\lambda e_1,
\qquad
\lambda\ne0.
\]

Now replace \(z\) by \(Tw\). Since
\[
\omega(Tx,Ty,Tw)
=
\det(T)\omega(x,y,w),
\]
the embedding identity gives
\[
\det(T)\,\omega(x,y,Tw)e_1
=
\lambda\det(T)\,\omega(x,y,w)e_1.
\]
Canceling the nonzero determinant yields
\[
\omega(x,y,Tw)
=
\lambda\omega(x,y,w)
\]
for all \(x,y,w\).

The volume form is nondegenerate in the third slot: if
\[
\omega(x,y,v)=0
\]
for every \(x,y\), then \(v=0\). Therefore
\[
Tw=\lambda w
\]
for every \(w\), so
\[
T=\lambda I.
\]

Conversely, every scalar map
\[
T=\lambda I
\]
satisfies
\[
[\lambda x,\lambda y,\lambda z]
=
\lambda^3[x,y,z]
=
\lambda[\lambda x,\lambda y,z].
\]
This completes the classification.

For the finite-field count, the number of rank-one \(3\times3\) matrices is
\[
\frac{(q^3-1)^2}{q-1}
=
(q-1)(q^2+q+1)^2.
\]

A rank-two embedding tensor must have
\[
T(e_1)=0.
\]
Its second and third columns must therefore be an ordered independent pair in
\[
\mathbf F_q^3.
\]
There are
\[
(q^3-1)(q^3-q)
\]
such pairs.

The invertible embedding tensors are exactly the
\[
q-1
\]
nonzero scalar matrices. Adding the four rank strata gives
\[
1+(q-1)(q^2+q+1)^2+(q^3-1)(q^3-q)+(q-1)
=
q^6+q^5-q^2+q-1.
\]

Replacing \(q\) by \(q^m\) gives the extension-field count and the displayed zeta function.

## Verification

The included program `artifacts/verify.py` constructs the alternating bracket
\[
[e_1,e_2,e_3]=e_1
\]
and verifies the Fundamental Identity on every ordered basis quintuple.

It then reconstructs the adjoint embedding-tensor defect for a general matrix and directly tests the rank classification over
\[
\mathbf F_2
\qquad\text{and}\qquad
\mathbf F_3.
\]

The exhaustive totals are
\[
93
\qquad\text{and}\qquad
965.
\]
The corresponding rank profiles are
\[
(1,49,42,1)
\]
and
\[
(1,338,624,2).
\]

These are exactly the values predicted by
\[
\left(
1,\,
(q-1)(q^2+q+1)^2,\,
(q^3-1)(q^3-q),\,
q-1
\right).
\]

The checker also verifies the closed formulas algebraically for
\[
q=2,3,5,7.
\]

It returns `VERIFY_OK`.

Finite enumeration is a replay check. The theorem over arbitrary fields follows from the rank proof above.

## Relationship to prior work

Hu, Hou, Song, and Zhou introduce embedding tensors on \(3\)-Lie algebras, characterize them by graphs in a hemisemidirect product \(3\)-Leibniz algebra, and develop their cohomology and deformation theory. Their examples are general constructions from square-zero derivations, strict \(3\)-Lie \(2\)-algebras, crossed modules, and a sufficient representation identity. The inspected full text does not classify embedding tensors on the three-dimensional nontrivial \(3\)-Lie algebra.

Cheng, Kang, and Lü later give a complete classification of adjoint \(\mathcal O\)-operators on the unique nontrivial three-dimensional complex \(3\)-Lie algebra
\[
[e_1,e_2,e_3]=e_1.
\]
That result does not cover the present theorem because an adjoint \(\mathcal O\)-operator satisfies
\[
[Tx,Ty,Tz]
=
T\!\left(
[Tx,Ty,z]+[Ty,Tz,x]+[Tz,Tx,y]
\right),
\]
with three terms, whereas an adjoint embedding tensor has only the first term. In characteristic different from \(2\), \(I\) is an embedding tensor but not an \(\mathcal O\)-operator, so neither condition implies equality of the two classifications.

A later paper on relative Rota–Baxter operators on \(3\)-Leibniz algebras gives an explicit three-dimensional \(3\)-Leibniz example, but it uses a non-skew ternary multiplication and the three-term Rota–Baxter identity. It therefore does not cover this \(3\)-Lie embedding-tensor problem.

Targeted searches for three-dimensional \(3\)-Lie embedding tensors, averaging operators, the adjoint problem, rank classifications, and the exact finite-field polynomial
\[
q^6+q^5-q^2+q-1
\]
did not locate a covering result.

## Limitations

The theorem concerns the fixed three-dimensional \(3\)-Lie model
\[
[e_1,e_2,e_3]=e_1.
\]

No quotient by the automorphism group is computed.

The uniqueness statement for the nontrivial three-dimensional algebra is used only over the complex field, as stated in the supporting classification source.

A specialized or differently indexed averaging-operator classification may exist. Failed searches do not prove novelty.

## References

1. M. Hu, S. Hou, L. Song, and Y. Zhou, “Deformations and cohomologies of embedding tensors on \(3\)-Lie algebras,” arXiv:2302.08725v1, first public 17 February 2023; *Communications in Algebra* 52 (2024), DOI `10.1080/00927872.2023.2214215`.
2. Z. Cheng, C. Kang, and J. Lü, “From \(\mathcal O\)-operators of 3-Dimensional 3-Lie algebras to 3-Pre-Lie algebras,” arXiv:2310.19490v1, first public 30 October 2023.
3. M. Hu, S. Hou, L. Song, and Y. Zhou, “3-pre-Leibniz Algebras, Deformations and Cohomologies of Relative Rota-Baxter Operators on 3-Leibniz Algebras,” *Journal of Nonlinear Mathematical Physics* 31 (2024), article 37, DOI `10.1007/s44198-024-00198-w`.
