# Complete Rota–Baxter moduli of a two-dimensional Lie–Yamaguti example

## Finding

Let \(K\) be a field and let \(L_K\) be the two-dimensional Lie–Yamaguti algebra with basis
\[
\{e_1,e_2\},
\]
binary bracket
\[
[e_1,e_2]=e_1,
\]
and ternary bracket
\[
\llbracket e_1,e_2,e_2\rrbracket=e_1,
\]
with skew-symmetry in the first two ternary arguments and all other basic products zero.

A weight-zero Rota–Baxter operator is a linear map \(R:L_K\to L_K\) satisfying
\[
[Rx,Ry]
=
R\bigl([Rx,y]-[Ry,x]\bigr)
\]
and
\[
\llbracket Rx,Ry,Rz\rrbracket
=
R\bigl(
\llbracket Rx,Ry,z\rrbracket
+
\llbracket x,Ry,Rz\rrbracket
+
\llbracket Rx,y,Rz\rrbracket
\bigr)
\]
for all \(x,y,z\in L_K\).

Write
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\]
so that
\[
R(e_1)=ae_1+ce_2,
\qquad
R(e_2)=be_1+de_2.
\]

The complete defining system is equivalent, over every field, to
\[
\boxed{
a^2+bc=0,\qquad
c(a+d)=0,\qquad
a^2(a+d)=0.
}
\]

Consequently,
\[
\boxed{
\operatorname{RB}_0(L_K)=\mathcal A\cup\mathcal N,
}
\]
where
\[
\boxed{
\mathcal A=
\left\{
\begin{pmatrix}
0&b\\
0&d
\end{pmatrix}
:b,d\in K
\right\}
}
\]
is the affine plane of maps killing \(e_1\), and
\[
\boxed{
\mathcal N=\{R\in M_2(K):R^2=0\}
}
\]
is the square-zero cone.

Their intersection is the line
\[
\boxed{
\mathcal A\cap\mathcal N=
\left\{
\begin{pmatrix}
0&b\\
0&0
\end{pmatrix}
:b\in K
\right\}.
}
\]

The family displayed in Example 4.16 of Zhao–Qiao is exactly \(\mathcal A\). Thus it is a full irredundant two-parameter component of the operator locus, but not the whole locus: the additional square-zero component contributes all matrices
\[
\begin{pmatrix}
a&b\\
c&-a
\end{pmatrix},
\qquad
bc=-a^2.
\]

For every finite field \(\mathbf F_q\),
\[
\boxed{
|\operatorname{RB}_0(L_{\mathbf F_q})|
=
2q^2-q.
}
\]

Every nonzero operator has rank \(1\), so the exact rank profile is
\[
\boxed{
(1,\ 2q^2-q-1,\ 0)
}
\]
in ranks \(0,1,2\).

The full automorphism group is
\[
\boxed{
\operatorname{Aut}(L_K)
=
\left\{
\begin{pmatrix}
s&t\\
0&1
\end{pmatrix}
:s\in K^\times,\ t\in K
\right\}.
}
\]

Over \(\mathbf F_q\), the \(2q^2-q\) Rota–Baxter operators form exactly
\[
\boxed{q+2}
\]
automorphism-conjugacy classes. Their orbit sizes are
\[
\boxed{
1,\qquad q-1,\qquad
\underbrace{q,\ldots,q}_{q-1\text{ orbits}},\qquad
q(q-1).
}
\]

The extension-field count is
\[
2q^{2m}-q^m,
\]
so the Hasse–Weil zeta function is
\[
\boxed{
Z(T)=\frac{1-qT}{(1-q^2T)^2}.
}
\]

## Assumptions and scope

Zhao and Qiao work over a characteristic-zero field and define Rota–Baxter operators on Lie–Yamaguti algebras as the adjoint special case of relative Rota–Baxter operators. Their equations are the two identities written above.

Their Example 4.16 uses exactly the algebra
\[
[e_1,e_2]=e_1,
\qquad
\llbracket e_1,e_2,e_2\rrbracket=e_1,
\]
and records
\[
R=
\begin{pmatrix}
0&a\\
0&b
\end{pmatrix}
\]
as a Rota–Baxter operator.

The present theorem independently reconstructs the full polynomial system and therefore does not rely on characteristic zero. No quotient other than conjugacy by automorphisms of the fixed Lie–Yamaguti algebra is taken.

## Proof

The binary bracket on vectors
\[
x=x_1e_1+x_2e_2,
\qquad
y=y_1e_1+y_2e_2
\]
is
\[
[x,y]=(x_1y_2-x_2y_1)e_1.
\]

The ternary bracket is
\[
\llbracket x,y,z\rrbracket
=
(x_1y_2-x_2y_1)z_2e_1.
\]

Evaluating the binary Rota–Baxter identity on \((e_1,e_2)\) gives
\[
\boxed{
a^2+bc=0,
\qquad
c(a+d)=0.
}
\]
All other ordered basis pairs give the same equations or zero.

For the ternary identity, expansion on the ordered basis triples gives, up to signs and consequences of the binary equations,
\[
c(a^2+bc)=0,
\]
\[
c^2(a+d)=0,
\]
\[
c(2ad-bc+d^2)=0,
\]
and
\[
2a^2d-abc+bcd=0.
\]

Modulo
\[
a^2+bc=0
\]
and
\[
c(a+d)=0,
\]
the first three are automatic, while the last becomes
\[
a^2(a+d)=0.
\]
Thus the complete system is exactly
\[
a^2+bc=0,\qquad c(a+d)=0,\qquad a^2(a+d)=0.
\]

We now solve it without dividing by any integer.

If
\[
a=0,
\]
then
\[
bc=0
\qquad\text{and}\qquad
cd=0.
\]
If \(c=0\), this is exactly \(\mathcal A\). If \(c\ne0\), then
\[
b=d=0,
\]
which lies in \(\mathcal N\).

If
\[
a\ne0,
\]
then
\[
a+d=0,
\]
so
\[
d=-a,
\qquad
bc=-a^2.
\]
These are exactly the nonzero-\(a\) points of \(\mathcal N\).

Conversely, every point of \(\mathcal A\) satisfies the three equations. Every square-zero \(2\times2\) matrix has trace and determinant zero, hence has the form
\[
\begin{pmatrix}
a&b\\
c&-a
\end{pmatrix},
\qquad
bc=-a^2,
\]
and also satisfies the three equations. Therefore
\[
\operatorname{RB}_0(L_K)=\mathcal A\cup\mathcal N.
\]

Over \(\mathbf F_q\), the plane \(\mathcal A\) has \(q^2\) points.

The square-zero cone has \(q^2\) points. Intrinsically, its nonzero elements are rank-one nilpotent maps. Such a map has
\[
\operatorname{im}R=\ker R=L
\]
for a unique line \(L\subset\mathbf F_q^2\). There are \(q+1\) choices of \(L\), and for each \(L\) there are \(q-1\) nonzero maps
\[
\mathbf F_q^2/L\longrightarrow L.
\]
Including zero gives
\[
1+(q+1)(q-1)=q^2.
\]

The intersection \(\mathcal A\cap\mathcal N\) has \(q\) points. Hence
\[
q^2+q^2-q=2q^2-q.
\]

All nonzero points in either component have rank \(1\), proving the rank profile.

For automorphisms, let
\[
P=
\begin{pmatrix}
p&q\\
r&s
\end{pmatrix}.
\]
Preserving the binary bracket forces
\[
r=0,\qquad s=1,
\]
with \(p\ne0\). These matrices also preserve the ternary bracket. Hence
\[
P=
\begin{pmatrix}
s&t\\
0&1
\end{pmatrix},
\qquad
s\ne0.
\]

On
\[
\mathcal A:
\quad
R=
\begin{pmatrix}
0&b\\
0&d
\end{pmatrix},
\]
conjugation sends
\[
b\longmapsto sb+td,
\qquad
d\longmapsto d.
\]
Thus zero is fixed; the nonzero points with \(d=0\) form one orbit of size \(q-1\); and for each fixed
\[
d\in\mathbf F_q^\times,
\]
all \(q\) values of \(b\) form one orbit.

It remains to consider
\[
\mathcal N\setminus\mathcal A.
\]
Every such matrix has \(c\ne0\). Conjugating
\[
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}
\]
by
\[
\begin{pmatrix}
s&t\\
0&1
\end{pmatrix}
\]
gives
\[
\begin{pmatrix}
t/s&-t^2/s\\
1/s&-t/s
\end{pmatrix}.
\]
For every point of \(\mathcal N\setminus\mathcal A\), the parameters \(s,t\) are uniquely recovered from \(c\) and \(a\). Therefore this entire set is one free orbit of size
\[
q(q-1).
\]

The orbit count is
\[
1+1+(q-1)+1=q+2.
\]

Finally, replacing \(q\) by \(q^m\) in
\[
2q^2-q
\]
gives the stated zeta function.

## Verification

The included program `artifacts/verify.py` reconstructs the binary and ternary products and expands both Rota–Baxter identities symbolically.

It verifies that the binary equations are generated by
\[
a^2+bc,\qquad c(a+d),
\]
and that, after these are imposed, the ternary equations add exactly
\[
a^2(a+d).
\]

The program then exhaustively checks every \(2\times2\) matrix over
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7.
\]

The exact operator counts are
\[
6,\quad15,\quad45,\quad91,
\]
matching
\[
2q^2-q.
\]

The rank profiles are
\[
(1,5,0),\quad
(1,14,0),\quad
(1,44,0),\quad
(1,90,0).
\]

The automorphism-class counts are
\[
4,\quad5,\quad7,\quad9,
\]
matching
\[
q+2,
\]
and the checker reproduces the stated orbit-size distribution.

It returns `VERIFY_OK`.

Finite enumeration is replay evidence. The theorem over arbitrary fields is proved by the symbolic equations and case analysis above.

## Relationship to prior work

Zhao and Qiao explicitly display the affine plane
\[
\mathcal A=
\left\{
\begin{pmatrix}
0&a\\
0&b
\end{pmatrix}
\right\}
\]
inside the Rota–Baxter locus of this exact two-dimensional Lie–Yamaguti algebra. They do not state that this family is exhaustive.

The earlier Sheng–Zhao paper introduces relative Rota–Baxter operators on Lie–Yamaguti algebras and develops the general pre-Lie–Yamaguti and symplectic theory. Its inspected full text contains no two-dimensional classification of this example.

Later generalized-Reynolds work places ordinary relative Rota–Baxter operators inside a broader operator framework, but does not give a finite-field or automorphism-orbit classification of this two-dimensional operator variety.

Targeted searches for the exact multiplication, the displayed source family, two-dimensional Lie–Yamaguti Rota–Baxter classifications, square-zero formulations, the point-count polynomial
\[
2q^2-q,
\]
and automorphism orbits did not locate a covering result.

## Limitations

The theorem concerns the single two-dimensional Lie–Yamaguti algebra appearing in Zhao–Qiao Example 4.16.

The source family is not erroneous; it is a valid full affine-plane subfamily. The new statement is its exhaustive completion.

No deformation or cohomology group is computed.

A specialized or differently indexed low-dimensional classification may contain an equivalent result. Failed searches do not prove absolute novelty.

## References

1. J. Zhao and Y. Qiao, “Cohomology and deformations of Relative Rota-Baxter operators on Lie-Yamaguti algebras,” arXiv:2204.04872v1, first public 11 April 2022; later published as *Mathematics* 12 (2024), 166, DOI `10.3390/math12010166`.
2. Y. Sheng and J. Zhao, “Relative Rota-Baxter operators and symplectic structures on Lie-Yamaguti algebras,” arXiv:2108.03556v1, first public 8 August 2021; *Communications in Algebra* 50 (2022), 4056–4073.
3. “Generalized Reynolds Operators on Lie-Yamaguti Algebras,” *Axioms* 12 (2023), 934.
