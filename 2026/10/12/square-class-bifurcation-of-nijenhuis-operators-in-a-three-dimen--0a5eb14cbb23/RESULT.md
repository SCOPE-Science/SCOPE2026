# Square-class bifurcation of Nijenhuis operators in a three-dimensional Hom–Lie family

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2.
\]
On
\[
H_{\beta,\gamma}
=
Ke_1\oplus Ke_2\oplus Ke_3
\]
define
\[
\alpha(e_1)=e_1,
\qquad
\alpha(e_2)=2e_2,
\qquad
\alpha(e_3)=2e_3,
\]
and
\[
[e_1,e_2]=\beta e_3,
\qquad
[e_1,e_3]=\gamma e_2,
\qquad
[e_2,e_3]=0.
\]
This is the subfamily obtained from Example 2.3 of Baishya and Das by setting their parameters
\[
a=d=0.
\]
It is multiplicative for every \(\beta,\gamma\).

Assume
\[
\beta\gamma\ne0.
\]
Put
\[
V=\langle e_2,e_3\rangle
\]
and let
\[
A=
\begin{pmatrix}
0&\gamma\\
\beta&0
\end{pmatrix}
\]
be the matrix of
\[
\operatorname{ad}_{e_1}|_V.
\]
Then
\[
A^2=(\beta\gamma)I_2.
\]

A Nijenhuis operator is a linear map \(N\) satisfying
\[
N\alpha=\alpha N
\]
and
\[
[Nx,Ny]
=
N\!\left([Nx,y]+[x,Ny]-N[x,y]\right).
\]

Because the eigenspaces of \(\alpha\) are
\[
Ke_1
\quad\text{and}\quad
V,
\]
every twist-compatible endomorphism has the form
\[
N=
\begin{pmatrix}
x&0\\
0&B
\end{pmatrix}
\]
relative to
\[
Ke_1\oplus V.
\]
The complete Nijenhuis condition is
\[
\boxed{
(xI_2-B)(AB-BA)=0.
}
\]

Over every odd finite field
\[
\mathbf F_q,
\]
the nondegenerate family
\[
\beta\gamma\ne0
\]
splits into exactly two Hom–Lie isomorphism types according to the square class of
\[
\delta=\beta\gamma.
\]

If
\[
\delta\in(\mathbf F_q^\times)^2,
\]
the algebra is isomorphic to the normalized split member
\[
H_+:
\qquad
[e_1,e_2]=e_3,
\qquad
[e_1,e_3]=e_2.
\]
For this member, write
\[
B=
\begin{pmatrix}
p&q_0\\
r&s
\end{pmatrix}.
\]
The Nijenhuis locus is exactly the union
\[
\boxed{
\mathcal C_0\cup\mathcal C_+\cup\mathcal C_-,
}
\]
where
\[
\mathcal C_0
=
\left\{
x\in\mathbf F_q,\quad
B=
\begin{pmatrix}
p&q_0\\
q_0&p
\end{pmatrix}
\right\},
\]
\[
\mathcal C_+
=
\left\{
x=p-q_0,\quad
B=
\begin{pmatrix}
p&q_0\\
q_0+k&p+k
\end{pmatrix}
\right\},
\]
and
\[
\mathcal C_-
=
\left\{
x=p+q_0,\quad
B=
\begin{pmatrix}
p&q_0\\
q_0+k&p-k
\end{pmatrix}
\right\},
\]
with all displayed parameters arbitrary.

Each component is an affine \(3\)-space. Their intersections are
\[
\mathcal C_0\cap\mathcal C_+
\cong\mathbf A^2,
\qquad
\mathcal C_0\cap\mathcal C_-
\cong\mathbf A^2,
\]
and
\[
\mathcal C_+\cap\mathcal C_-
=
\mathcal C_0\cap\mathcal C_+\cap\mathcal C_-
\cong\mathbf A^1.
\]
Hence
\[
\boxed{
|\operatorname{Nij}(H_+)(\mathbf F_q)|
=
3q^3-2q^2.
}
\]

The exact rank distribution in ranks \(0,1,2,3\) is
\[
\boxed{
\left(
1,\,
(q-1)(2q+3),\,
5(q-1)^2,\,
3(q-1)^3
\right).
}
\]

If
\[
\delta\notin(\mathbf F_q^\times)^2,
\]
then every Nijenhuis operator commutes with
\[
A.
\]
Equivalently,
\[
\boxed{
\operatorname{Nij}(H_{\beta,\gamma})
=
\left\{
\operatorname{diag}(x,B):
x\in\mathbf F_q,\ 
B\in\mathbf F_q[A]
\right\}.
}
\]
Because
\[
\mathbf F_q[A]\cong\mathbf F_{q^2},
\]
this locus has
\[
\boxed{q^3}
\]
points and rank profile
\[
\boxed{
\left(
1,\,
q-1,\,
q^2-1,\,
(q-1)(q^2-1)
\right).
}
\]

Thus the Nijenhuis moduli detect the split versus nonsplit square class of
\[
\beta\gamma.
\]
The point-count jump is
\[
3q^3-2q^2
\quad\text{versus}\quad
q^3.
\]

Among all ordered pairs
\[
(\beta,\gamma)\in(\mathbf F_q^\times)^2,
\]
exactly half have square product and half have nonsquare product. Therefore the total number of triples
\[
(\beta,\gamma,N)
\]
with
\[
N\in\operatorname{Nij}(H_{\beta,\gamma})
\]
is
\[
\boxed{
q^2(q-1)^2(2q-1).
}
\]

For the normalized split member, over every extension field
\[
\mathbf F_{q^m}
\]
the same component decomposition gives
\[
N_m=3q^{3m}-2q^{2m}.
\]
Consequently its Hasse–Weil zeta function is
\[
\boxed{
Z(T)
=
\frac{(1-q^2T)^2}{(1-q^3T)^3}.
}
\]

## Assumptions and scope

Baishya and Das give a four-parameter three-dimensional Hom–Lie example with
\[
\alpha=\operatorname{diag}(1,2,2).
\]
Their later Nijenhuis theory is developed for multiplicative Hom–Lie algebras. The specialization
\[
a=d=0
\]
used here is directly multiplicative, and the theorem concerns its nondegenerate part
\[
\beta\gamma\ne0.
\]

The finite-field square-class classification assumes odd characteristic.

No claim is made here about the degenerate fibers
\[
\beta\gamma=0.
\]

The nonsplit fixed algebra changes square class after some field extensions, so no fixed nonsplit Hasse–Weil formula is asserted. The displayed zeta function concerns the normalized split member only.

## Proof

Write an element as
\[
(r,u)\in Ke_1\oplus V.
\]
Then
\[
[(r,u),(s,v)]
=
\left(
0,\,
rAv-sAu
\right).
\]

A map commuting with
\[
\alpha=\operatorname{diag}(1,2I_2)
\]
must have the form
\[
N(r,u)=(xr,Bu).
\]

It is enough to evaluate the Nijenhuis identity on one input in
\[
Ke_1
\]
and one input in
\[
V,
\]
because
\[
[V,V]=0.
\]
For
\[
u\in V,
\]
the left side is
\[
[xe_1,Bu]
=
xABu.
\]
The vector inside the outer \(N\) on the right is
\[
xAu+ABu-BAu.
\]
Applying \(B\) gives
\[
xBAu+BABu-B^2Au.
\]
Thus the defect is
\[
\left(
xAB-xBA-BAB+B^2A
\right)u,
\]
which factors as
\[
(xI_2-B)(AB-BA)u.
\]
This proves the matrix criterion.

Now set
\[
\delta=\beta\gamma.
\]
Since
\[
A^2=\delta I_2,
\]
changing basis in \(V\) and scaling \(e_1\) changes \(\delta\) only by a nonzero square. Conversely, two nonzero values in the same square class give isomorphic Hom–Lie algebras. Thus over an odd finite field there are two nondegenerate types.

For the split type take
\[
A=
J=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
For
\[
B=
\begin{pmatrix}
p&q_0\\
r&s
\end{pmatrix},
\]
put
\[
u=r-q_0,
\qquad
v=s-p.
\]
Then
\[
JB-BJ
=
\begin{pmatrix}
u&v\\
-v&-u
\end{pmatrix}
\]
and
\[
\det(JB-BJ)=v^2-u^2.
\]

If
\[
u=v=0,
\]
then \(B\) commutes with \(J\) and \(x\) is arbitrary, giving
\[
\mathcal C_0.
\]

If the commutator is nonzero and singular, then
\[
v=u
\qquad\text{or}\qquad
v=-u.
\]
In the first case the image of the commutator is spanned by
\[
(1,-1)^T,
\]
and the equation
\[
(xI_2-B)(JB-BJ)=0
\]
is equivalent to
\[
x=p-q_0.
\]
This is
\[
\mathcal C_+.
\]
The second case similarly gives
\[
x=p+q_0
\]
and
\[
\mathcal C_-.
\]

An invertible nonzero commutator cannot occur: it would force
\[
B=xI_2,
\]
which makes the commutator zero. Hence the three components are exhaustive.

The component intersections are obtained by setting
\[
u=0
\]
in the two singular branches. Inclusion–exclusion gives
\[
3q^3-2q^2.
\]

For the rank count, diagonalize \(J\). On
\[
\mathcal C_0
\]
the two eigenvalues of \(B\) are
\[
p+q_0
\quad\text{and}\quad
p-q_0,
\]
so the rank multiplicities are
\[
\left(
1,\,
3(q-1),\,
3(q-1)^2,\,
(q-1)^3
\right).
\]

On either of
\[
\mathcal C_+,\mathcal C_-,
\]
a fixed change of basis puts \(N\) into a triangular form with parameters
\[
x,y,k
\]
and diagonal
\[
(x,y,x).
\]
Hence each such component has rank profile
\[
\left(
1,\,
q^2-1,\,
q(q-1),\,
q(q-1)^2
\right).
\]
Each plane
\[
\mathcal C_0\cap\mathcal C_\pm
\]
has profile
\[
\left(
1,\,
q-1,\,
q-1,\,
(q-1)^2
\right).
\]
The line
\[
\mathcal C_+\cap\mathcal C_-
\]
is also the triple intersection and therefore cancels in rankwise inclusion–exclusion. This yields the displayed split rank profile.

For the nonsplit case, after a change of basis take
\[
A=
\begin{pmatrix}
0&\delta\\
1&0
\end{pmatrix}
\]
with \(\delta\) a nonsquare. If
\[
B=
\begin{pmatrix}
p&q_0\\
r&s
\end{pmatrix},
\]
then
\[
\det(AB-BA)
=
\delta(p-s)^2-(q_0-\delta r)^2.
\]
Because \(\delta\) is a nonsquare, vanishing of this determinant implies
\[
p=s,
\qquad
q_0=\delta r,
\]
so
\[
AB=BA.
\]
If the determinant does not vanish, the Nijenhuis equation would again force
\[
B=xI_2
\]
and hence a zero commutator, a contradiction. Thus
\[
B\in\mathbf F_q[A].
\]

The algebra
\[
\mathbf F_q[A]
\]
is the quadratic field
\[
\mathbf F_{q^2}.
\]
Every nonzero \(B\) is therefore invertible. Combining the choice of \(x\) with \(B=0\) or \(B\ne0\) gives the nonsplit rank profile.

Finally, for each fixed
\[
\delta\in\mathbf F_q^\times
\]
there are exactly
\[
q-1
\]
ordered pairs
\[
(\beta,\gamma)
\]
with
\[
\beta\gamma=\delta.
\]
There are
\[
\frac{q-1}{2}
\]
square and the same number of nonsquare values of \(\delta\), which gives
\[
q^2(q-1)^2(2q-1)
\]
parameter-operator triples.

## Verification

The included program `artifacts/verify.py` reconstructs the Hom–Lie bracket and twisting map.

It verifies multiplicativity and the Hom–Jacobi identity symbolically for arbitrary
\[
\beta,\gamma.
\]

For a general twist-compatible block matrix
\[
N=\operatorname{diag}(x,B),
\]
it reconstructs the complete Nijenhuis defect and verifies the factorization
\[
(xI_2-B)(AB-BA).
\]

It then exhaustively checks every block endomorphism in the twist centralizer over
\[
\mathbf F_3,\qquad
\mathbf F_5,\qquad
\mathbf F_7
\]
for both the split and nonsplit square classes.

For the split representatives the totals are
\[
63,\qquad325,\qquad931,
\]
with rank profiles
\[
(1,18,20,24),
\qquad
(1,52,80,192),
\qquad
(1,102,180,648).
\]

For nonsplit representatives the totals are
\[
27,\qquad125,\qquad343,
\]
with rank profiles
\[
(1,2,8,16),
\qquad
(1,4,24,96),
\qquad
(1,6,48,288).
\]

These agree exactly with the stated formulas.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field matrix criterion and the finite-field split/nonsplit classifications are proved symbolically above.

## Relationship to prior work

Baishya and Das introduce the Frölicher–Nijenhuis bracket for Hom–Lie algebras and recover Nijenhuis operators as the corresponding Maurer–Cartan-type objects. Their Example 2.3 supplies the four-parameter three-dimensional Hom–Lie family used here, while Definition 4.8 gives the Nijenhuis identity. The inspected full text does not solve Nijenhuis operators on Example 2.3 or give finite-field square-class moduli.

Das and Sen previously developed the general cohomology and deformation theory of Nijenhuis operators on Hom–Lie algebras. The publicly accessible abstract and bibliographic record expose no low-dimensional finite-field classification. The complete article text was not available through the public sources inspected, so an unindexed same-object example inside that article remains a residual comparison risk.

Targeted searches for the exact brackets, the twist
\[
\operatorname{diag}(1,2,2),
\]
three-dimensional Hom–Lie Nijenhuis classifications, square-class formulations, and the exact polynomial
\[
3q^3-2q^2
\]
did not locate a covering result.

## Limitations

The theorem treats the nondegenerate multiplicative subfamily
\[
a=d=0,
\qquad
\beta\gamma\ne0
\]
inside the source's Example 2.3.

Odd characteristic is assumed for the square-class dichotomy and rank formulas.

The degenerate fibers
\[
\beta\gamma=0
\]
are not classified here.

The earlier general Nijenhuis article could not be inspected in full, which leaves a specific bibliographic residual risk.

Failed searches do not prove absolute novelty.

## References

1. A. Baishya and A. Das, “Cup product, Frölicher-Nijenhuis bracket and the derived bracket associated to Hom-Lie algebras,” arXiv:2409.01865v1, first public 3 September 2024.
2. A. Das and S. Sen, “Nijenhuis operators on Hom-Lie algebras,” *Communications in Algebra* 50 (2022), 1038–1054, DOI `10.1080/00927872.2021.1977942`, first published online 16 October 2021.
