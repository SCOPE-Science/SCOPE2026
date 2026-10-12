# Reynolds moduli of the three-dimensional \(3\)-Lie algebra

## Finding

Let \(K\) be a field and let \(A_K\) be the three-dimensional \(3\)-Lie algebra with basis
\[
\{e_1,e_2,e_3\}
\]
and alternating bracket determined by
\[
[e_1,e_2,e_3]=e_1.
\]

A Reynolds operator is a linear map \(R:A_K\to A_K\) satisfying
\[
[Rx,Ry,Rz]
=
R\!\left(
[Rx,Ry,z]+[x,Ry,Rz]+[Rx,y,Rz]-[Rx,Ry,Rz]
\right)
\]
for all \(x,y,z\in A_K\).

Write
\[
R=
\begin{pmatrix}
a&b&c\\
d&e&f\\
g&h&i
\end{pmatrix},
\qquad
D=\det R,
\]
and define
\[
\sigma_2(R)
=
ae-bd+ai-cg+ei-fh,
\]
the sum of the three principal \(2\times2\) minors.

Then the entire Reynolds identity is equivalent to the single vector equation
\[
\boxed{
D e_1=(\sigma_2(R)-D)R(e_1).
}
\]

Consequently \(R\) is Reynolds if and only if exactly one of the following mutually exclusive alternatives holds:
\[
\boxed{R(e_1)=0;}
\]
\[
\boxed{
R(e_1)\notin K e_1,\qquad D=0,\qquad \sigma_2(R)=0;
}
\]
or
\[
\boxed{
R(e_1)=a e_1,\quad a\ne0,\qquad \det\bar R=\operatorname{tr}\bar R,
}
\]
where
\[
\bar R:A_K/K e_1\longrightarrow A_K/K e_1
\]
is the induced two-dimensional map.

For every prime power \(q\), the exact rank distribution over \(\mathbf F_q\), in ranks \(0,1,2,3\), is
\[
\boxed{
\left(
1,\,
(q-1)(q^2+q+1)^2,\,
q(q-1)^2(q+1)(q^3+3q^2+2q+1),\,
q^3(q-1)(q^2-q-1)
\right).
}
\]
Hence
\[
\boxed{
|\operatorname{Reyn}(A_{\mathbf F_q})|
=
q^7+3q^6-3q^5-2q^4+2q^3.
}
\]

The invertible Reynolds operators are exactly the maps
\[
\boxed{
R=
\begin{pmatrix}
a&u_1&u_2\\
0&&\\
0&&B
\end{pmatrix},
\qquad
a\ne0,
\qquad
\det B=\operatorname{tr}B\ne0.
}
\]
Equivalently,
\[
B-I_2\in\operatorname{SL}_2(K)
\]
and
\[
\det B\ne0.
\]
Over \(\mathbf F_q\), their exact number is
\[
\boxed{
q^3(q-1)(q^2-q-1).
}
\]

Replacing \(q\) by \(q^m\) gives the point count over every extension field. Therefore the Reynolds-operator variety has Hasse--Weil zeta function
\[
\boxed{
Z(T)=
\frac{(1-q^5T)^3(1-q^4T)^2}
{(1-q^7T)(1-q^6T)^3(1-q^3T)^2}.
}
\]

## Assumptions and scope

Hou and Sheng introduce Reynolds operators on \(3\)-Lie algebras by the identity used above. In the same paper, their finite-dimensional Example 4.4 uses exactly the algebra
\[
[e_1,e_2,e_3]=e_1
\]
for a Nijenhuis-operator construction. Their Reynolds subsection then gives general theory and infinite-dimensional examples rather than a finite-dimensional classification.

The source works over characteristic zero. The theorem here is reconstructed directly from the alternating determinant bracket, and no division by a field characteristic is used. It is therefore valid over every field.

The later paper on Reynolds \(n\)-Lie algebras develops cohomology, deformations, and general constructions. The accepted claim is the explicit finite-dimensional operator variety and its arithmetic.

No quotient by the \(3\)-Lie automorphism group is taken.

## Proof

For vectors \(x,y,z\in K^3\), let
\[
\omega(x,y,z)
\]
be the determinant with columns \(x,y,z\). Then
\[
[x,y,z]=\omega(x,y,z)e_1.
\]

Because the Reynolds defect is alternating and trilinear, it is enough to evaluate it on
\[
(e_1,e_2,e_3).
\]
The left side is
\[
[Re_1,Re_2,Re_3]=D e_1.
\]
The scalar multiplying \(e_1\) inside the outer \(R\) on the right is
\[
\omega(Re_1,Re_2,e_3)
+
\omega(e_1,Re_2,Re_3)
+
\omega(Re_1,e_2,Re_3)
-
\omega(Re_1,Re_2,Re_3).
\]
The first three terms are the three principal \(2\times2\) minors, while the final term is \(D\). Thus the scalar is
\[
\sigma_2(R)-D.
\]
Therefore the Reynolds identity is exactly
\[
D e_1=(\sigma_2(R)-D)R(e_1).
\]

Put
\[
s=\sigma_2(R)-D.
\]
In coordinates the vector equation is
\[
D=sa,\qquad sd=0,\qquad sg=0.
\]

If
\[
R(e_1)=0,
\]
all three equations hold automatically.

If
\[
R(e_1)\notin Ke_1,
\]
then at least one of \(d,g\) is nonzero, so \(s=0\). Hence \(D=0\) and
\[
\sigma_2(R)=0.
\]
The converse is immediate.

Finally suppose
\[
R(e_1)=a e_1,\qquad a\ne0.
\]
Write
\[
R=
\begin{pmatrix}
a&u_1&u_2\\
0&&\\
0&&B
\end{pmatrix}.
\]
Then
\[
D=a\det B,
\qquad
\sigma_2(R)=a\operatorname{tr}B+\det B.
\]
The equation
\[
D=sa
\]
reduces to
\[
\det B=\operatorname{tr}B.
\]
This proves the structural classification.

We now count over \(\mathbf F_q\). The first alternative contains
\[
q^6
\]
matrices.

For the third alternative,
\[
\det(B-I_2)=\det B-\operatorname{tr}B+1
\]
shows that
\[
\det B=\operatorname{tr}B
\]
is equivalent to
\[
B-I_2\in\operatorname{SL}_2(\mathbf F_q).
\]
Hence this alternative contributes
\[
(q-1)q^2|\operatorname{SL}_2(\mathbf F_q)|
=
q^3(q-1)(q^2-1).
\]

For the second alternative, put
\[
\mathcal Z=\{R:\det R=0,\ \sigma_2(R)=0\}.
\]
Every matrix in \(\mathcal Z\) has characteristic polynomial
\[
X^2(X-\operatorname{tr}R).
\]

The trace-zero fiber is the nilpotent cone in \(M_3(\mathbf F_q)\). Its three Jordan types \(1+1+1\), \(2+1\), and \(3\) have respectively
\[
1,
\qquad
(q-1)(q+1)(q^2+q+1),
\]
and
\[
q(q-1)^2(q+1)(q^2+q+1)
\]
members, totaling
\[
q^6.
\]

For each fixed nonzero trace \(t\), there are two similarity types:
\[
0_2\oplus(t)
\]
and
\[
J_2(0)\oplus(t).
\]
Their class sizes are
\[
q^2(q^2+q+1)
\]
and
\[
q^2(q^2-1)(q^2+q+1).
\]
Thus
\[
|\mathcal Z|
=
q^6+(q-1)q^4(q^2+q+1)
=
q^7+q^6-q^4.
\]

The matrices in \(\mathcal Z\) that preserve \(Ke_1\) have block form
\[
\begin{pmatrix}
a&u\\
0&B
\end{pmatrix}.
\]
When \(a=0\), one needs only
\[
\det B=0,
\]
giving \(q^3+q^2-q\) possibilities for \(B\). When \(a\ne0\), one needs
\[
\det B=\operatorname{tr}B=0,
\]
so \(B\) is nilpotent, giving \(q^2\) possibilities. Since \(u\) is free,
\[
|\{R\in\mathcal Z:R(Ke_1)\subseteq Ke_1\}|
=
2q^5-q^3.
\]

Therefore the second alternative contributes
\[
q^7+q^6-2q^5-q^4+q^3.
\]
Adding the three disjoint alternatives gives
\[
q^7+3q^6-3q^5-2q^4+2q^3.
\]

Every rank-at-most-one matrix is Reynolds, so the rank-one count is
\[
\frac{(q^3-1)^2}{q-1}
=
(q-1)(q^2+q+1)^2.
\]

An invertible Reynolds operator lies in the third alternative. Put
\[
C=B-I_2\in\operatorname{SL}_2(\mathbf F_q).
\]
Since
\[
\det B=\operatorname{tr}C+2,
\]
\(B\) is singular exactly when
\[
\operatorname{tr}C=-2.
\]
The number of matrices in \(\operatorname{SL}_2(\mathbf F_q)\) with trace \(-2\) is \(q^2\): after writing the diagonal entries as \(r\) and \(-2-r\), the determinant equation reduces to one product equation, and the repeated root \(r=-1\) contributes the unique zero-product exception. Thus the number of invertible \(B\) is
\[
q(q^2-1)-q^2
=
q(q^2-q-1).
\]
Multiplying by the choices of \(a,u_1,u_2\) yields
\[
q^3(q-1)(q^2-q-1)
\]
rank-three operators.

The rank-two count is the total minus the rank-zero, rank-one, and rank-three counts, which simplifies to
\[
q(q-1)^2(q+1)(q^3+3q^2+2q+1).
\]

Finally, replacing \(q\) by \(q^m\) gives the extension-field count and the displayed zeta function.

## Verification

The included program `artifacts/verify.py` reconstructs the alternating bracket and the Reynolds defect directly.

Symbolically, it verifies that the full defect is the alternating trilinear map determined by
\[
D e_1-(\sigma_2(R)-D)R(e_1).
\]

It then exhaustively checks every \(3\times3\) matrix over
\[
\mathbf F_2
\qquad\text{and}\qquad
\mathbf F_3.
\]
The direct totals are
\[
208
\qquad\text{and}\qquad
3537,
\]
with rank profiles
\[
(1,49,150,8)
\]
and
\[
(1,338,2928,270).
\]
These agree exactly with the closed formulas.

The program also verifies the rank and total formulas algebraically for
\[
q=2,3,5,7.
\]
It returns `VERIFY_OK`.

Finite enumeration is replay evidence only. The arbitrary-field classification and finite-field formulas are proved above.

## Relationship to prior work

Hou and Sheng introduce Reynolds operators on \(3\)-Lie algebras and prove their connection with twisted Rota–Baxter operators and derivations. In the same paper, Example 4.4 uses exactly
\[
[e_1,e_2,e_3]=e_1
\]
as the canonical three-dimensional example for Nijenhuis-induced structures. The Reynolds subsection explicitly proceeds to infinite-dimensional examples; it does not give the finite-dimensional classification above.

Their subsequent paper extends the Reynolds theory to \(n\)-Lie algebras, develops cohomology and deformations, and gives general constructions. It does not state the finite-field Reynolds locus or rank distribution for the three-dimensional model.

A complete classification of adjoint embedding tensors on the same \(3\)-Lie model concerns the one-term identity
\[
[Tx,Ty,Tz]=T([Tx,Ty,z]),
\]
which is different from the four-term Reynolds identity here. Likewise, the complete low-dimensional adjoint \(\mathcal O\)-operator classification uses a three-term identity and does not imply this Reynolds classification.

Targeted semantic-database and literature searches for three-dimensional Reynolds \(3\)-Lie algebras, finite-field counts, rank classifications, the exact polynomial
\[
q^7+3q^6-3q^5-2q^4+2q^3,
\]
and the invertible count found no covering result.

## Limitations

The theorem concerns the fixed three-dimensional model
\[
[e_1,e_2,e_3]=e_1.
\]

No automorphism-conjugacy quotient is computed.

The count of the second alternative uses the standard similarity classification of \(3\times3\) matrices with characteristic polynomial
\[
X^2(X-t).
\]

A specialized or differently indexed Reynolds-operator classification may exist. Failed searches do not prove absolute novelty.

## References

1. S. Hou and Y. Sheng, “Twisted Rota-Baxter operators on \(3\)-Lie algebras and NS-\(3\)-Lie algebras,” arXiv:2107.13950v1, first public 28 July 2021; *International Journal of Geometric Methods in Modern Physics* 18 (2021), 2150223, DOI `10.1142/S0219887821502236`.
2. S. Hou and Y. Sheng, “Reynolds \(n\)-Lie algebras and NS-\(n\)-Lie algebras,” arXiv:2108.04407v1, first public 10 August 2021; *Communications in Algebra* 51 (2023), 779–798, DOI `10.1080/00927872.2022.2113403`.
