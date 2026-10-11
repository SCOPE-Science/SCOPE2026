# Exact relative point-reflection volumes of simplices
## Finding
Let
\[
\Delta\subset\mathbb R^n,
\qquad
n\ge2,
\]
be an \(n\)-simplex, and let
\[
M=\frac12(\Delta-\Delta)
\]
be the unit ball of its relative norm. For each of the four standard normed volumes used by Lángi,
\[
\tau\in\{\mathrm{Bus},\mathrm{HT},m,m^*\},
\]
define
\[
c_p^\tau(\Delta)
=
\max_{x\in\Delta}
\operatorname{vol}_M^\tau
\left(
\operatorname{conv}\bigl(\Delta\cup(2x-\Delta)\bigr)
\right).
\]

Write
\[
v_n=\lambda_n(B_2^n)
\]
and let
\[
D_n
=
\max\left\{
|\det A|:
A\in\{0,1\}^{n\times n}
\right\}
\tag{1}
\]
be the classical maximal determinant of an \(n\times n\) zero-one matrix. Then
\[
\boxed{
c_p^{\mathrm{Bus}}(\Delta)
=
\frac{4^n v_n}{\binom{2n}{n}}
}
\tag{2}
\]
and
\[
\boxed{
c_p^{\mathrm{HT}}(\Delta)
=
\frac{4^n(n+1)}{n!\,v_n}
}.
\tag{3}
\]
For Gromov's two normalizations,
\[
\boxed{
c_p^{m}(\Delta)
=
\frac{4^n}{n!}
}
\tag{4}
\]
and
\[
\boxed{
c_p^{m^*}(\Delta)
=
\frac{4^nD_n}{n!}
}.
\tag{5}
\]

For all four quantities, every vertex of the simplex is a maximizing reflection center.

Formula (5) gives a direct bridge from Lángi's normed Rogers--Shephard problem to the classical zero-one maximal-determinant problem.

## Assumptions and scope
The Busemann and Holmes--Thompson normalizations are
\[
\operatorname{vol}_M^{\mathrm{Bus}}(S)
=
\frac{v_n}{\lambda_n(M)}\lambda_n(S)
\]
and
\[
\operatorname{vol}_M^{\mathrm{HT}}(S)
=
\frac{\lambda_n(M^\circ)}{v_n}\lambda_n(S).
\]
For Gromov's mass, the scalar multiple of Lebesgue measure is chosen so that a largest-volume cross-polytope inscribed in \(M\) has volume
\[
\frac{2^n}{n!}.
\]
For Gromov's mass*, the normalization makes a smallest-volume parallelotope circumscribed about \(M\) have volume
\[
2^n.
\]

All four quantities are affine invariant, so it is enough to treat the standard simplex
\[
\Delta_n
=
\operatorname{conv}\{0,e_1,\ldots,e_n\},
\qquad
\lambda_n(\Delta_n)=\frac1{n!}.
\tag{6}
\]

The result computes the four relative point-reflection quantities on the simplex class. It does not determine the global minima or maxima over all convex bodies in Lángi's Problem 4.

## Proof
For the standard simplex (6), set
\[
M=\frac12(\Delta_n-\Delta_n).
\]

The Rogers--Shephard point-reflection theorem states that for every convex body \(K\subset\mathbb R^n\) and every \(x\in K\),
\[
\lambda_n
\left(
\operatorname{conv}(K\cup(2x-K))
\right)
\le
2^n\lambda_n(K),
\tag{7}
\]
and equality on the right occurs exactly when \(K\) is a simplex and \(x\) is one of its vertices. Hence
\[
\max_{x\in\Delta_n}
\lambda_n
\left(
\operatorname{conv}(\Delta_n\cup(2x-\Delta_n))
\right)
=
\frac{2^n}{n!}.
\tag{8}
\]

It remains to compute the four scalar normalizations for the fixed relative unit ball \(M\).

First, Rogers--Shephard equality for the difference body of a simplex gives
\[
\lambda_n(\Delta_n-\Delta_n)
=
\binom{2n}{n}\lambda_n(\Delta_n).
\]
Therefore
\[
\lambda_n(M)
=
\frac{\binom{2n}{n}}{2^n n!}.
\tag{9}
\]
Multiplying (8) by
\[
\frac{v_n}{\lambda_n(M)}
\]
immediately gives (2).

Next we compute the polar. Introduce \(e_0=0\). The vertices of \(M\) are
\[
\frac12(e_i-e_j),
\qquad
0\le i\ne j\le n.
\]
Thus \(y\in M^\circ\) exactly when
\[
|y_i-y_j|\le2
\]
for all \(i,j\in\{0,\ldots,n\}\), where \(y_0=0\). Equivalently,
\[
\max(0,y_1,\ldots,y_n)
-
\min(0,y_1,\ldots,y_n)
\le2.
\tag{10}
\]
The vertices of this polytope are
\[
\pm2\,\mathbf1_S,
\qquad
\varnothing\ne S\subseteq\{1,\ldots,n\}.
\tag{11}
\]

To evaluate its volume, partition by coordinate sign pattern. If exactly \(k\) coordinates are positive and \(n-k\) are negative, put \(a\) for the largest positive coordinate and \(b\) for the largest absolute value of a negative coordinate. For
\[
1\le k\le n-1,
\]
condition (10) is
\[
a+b\le2,
\]
and one fixed sign pattern has volume
\[
k(n-k)
\int_{\substack{a,b\ge0\\a+b\le2}}
a^{k-1}b^{n-k-1}\,da\,db
=
2^n\frac{k!(n-k)!}{n!}.
\tag{12}
\]
There are
\[
\binom nk
\]
such sign patterns, so each mixed value of \(k\) contributes exactly \(2^n\). The all-positive and all-negative chambers also have volume \(2^n\) each. Hence
\[
\lambda_n(M^\circ)
=
(n+1)2^n.
\tag{13}
\]
Combining (13) and (8) with the Holmes--Thompson scalar
\[
\frac{\lambda_n(M^\circ)}{v_n}
\]
proves (3).

For Gromov's mass, a centrally symmetric cross-polytope with generators
\[
v_1,\ldots,v_n
\]
has Euclidean volume
\[
\frac{2^n}{n!}
\left|
\det(v_1,\ldots,v_n)
\right|.
\tag{14}
\]
Because the absolute determinant is convex in each generator separately, its maximum over \(M^n\) is achieved when every generator is a vertex of \(M\). After multiplying all generators by \(2\), these vertices become
\[
e_i-e_j,
\qquad
0\le i\ne j\le n.
\]
They are columns of a reduced incidence matrix of the complete directed graph. Such matrices are totally unimodular, so every \(n\times n\) determinant is \(0\), \(1\), or \(-1\). The value \(1\) is attained by the columns
\[
e_1,\ldots,e_n.
\]
Consequently
\[
\max_{v_i\in M}
\left|
\det(v_1,\ldots,v_n)
\right|
=
2^{-n},
\]
and the largest inscribed cross-polytope in \(M\) has volume
\[
\frac1{n!}.
\tag{15}
\]
To normalize (15) to \(2^n/n!\), Gromov's mass multiplies Lebesgue volume by \(2^n\). Equation (4) follows from (8).

Finally consider mass*. If a parallelotope
\[
P=
\{x:|a_i\cdot x|\le1,\ 1\le i\le n\}
\]
contains \(M\), then
\[
P^\circ
=
\operatorname{conv}\{\pm a_1,\ldots,\pm a_n\}
\]
is a cross-polytope contained in \(M^\circ\), and
\[
\lambda_n(P)\lambda_n(P^\circ)
=
\frac{4^n}{n!}.
\tag{16}
\]
Thus minimizing the volume of a parallelotope containing \(M\) is equivalent to maximizing the volume of an inscribed cross-polytope in \(M^\circ\).

By (11) and the same separate-convexity argument, the determinant maximum is attained at vertices. Ignoring independent column signs, every vertex is
\[
2\,\mathbf1_S
\]
for a nonempty zero-one column \(\mathbf1_S\). Hence
\[
\max_{a_i\in M^\circ}
\left|
\det(a_1,\ldots,a_n)
\right|
=
2^nD_n.
\]
Using (14), the largest cross-polytope in \(M^\circ\) therefore has volume
\[
\frac{4^nD_n}{n!}.
\tag{17}
\]
Equations (16)--(17) show that the smallest parallelotope circumscribed about \(M\) has Euclidean volume
\[
\frac1{D_n}.
\tag{18}
\]
Mass* consequently multiplies Lebesgue volume by
\[
2^nD_n.
\]
Combining this scalar with (8) gives (5).

## Verification
The supplied `verify.py` independently reconstructs the standard simplex relative unit ball and its polar for dimensions
\[
2\le n\le4.
\]
It checks their Euclidean volumes against (9) and (13), enumerates all root-column determinants to verify the determinant bound behind (15), and exhaustively computes \(D_n\) for these dimensions to check (17)--(18).

For the same dimensions it also evaluates all four formulas from the independently reconstructed normalization data and verifies the special planar values
\[
c_p^{\mathrm{Bus}}(\Delta_2)=\frac{8\pi}{3},
\qquad
c_p^{\mathrm{HT}}(\Delta_2)=\frac{24}{\pi},
\qquad
c_p^m(\Delta_2)=8,
\qquad
c_p^{m^*}(\Delta_2)=8.
\]

These finite checks are regression tests only. The all-dimensional proof rests on Rogers--Shephard equality, the exact sign-chamber integral (12), total unimodularity of incidence matrices, and the determinant reduction (17).

## Relationship to prior work
Lángi introduced the relative norm and the four quantities
\[
c_p^\tau(K)
\]
for point-reflection bodies and asked, in Problem 4, for their extremal values in every dimension. The paper gives the four normed-volume normalizations explicitly but does not provide the all-dimensional simplex formulas (2)--(5).

Rogers and Shephard proved the Euclidean reflection-body estimate (7) and the sharp difference-body inequality used in (9). The new calculation keeps their simplex equality case fixed and evaluates the four non-Euclidean normalization factors of its relative norm exactly.

The mass* case adds a structural feature absent from the Euclidean reflection theorem: the exact simplex value is controlled by the zero-one maximal determinant \(D_n\). Thus even this canonical simplex benchmark already imports a classical discrete determinant invariant into the normed reflection-body problem.

Targeted searches under relative norm, reflection body, Busemann volume, Holmes--Thompson volume, Gromov mass, mass*, simplex, central symmetral, and maximal determinant did not locate an implication-equivalent all-dimensional simplex formula.

## Limitations
This does not solve Lángi's global Problem 4. In particular, formulas (2)--(5) do not assert that simplices minimize or maximize the corresponding quantities among all \(n\)-dimensional convex bodies.

Formula (5) is exact but contains the classical zero-one maximal determinant \(D_n\), whose value is not known in closed form for every dimension.

The verification code exhaustively checks low dimensions only; total unimodularity and the vertex reduction are the infinite-dimensional-in-\(n\) proof ingredients.

Because each normalization is elementary once the relative unit ball of a simplex is understood, an equivalent benchmark may exist in later normed-volume literature under different terminology. The most relevant primary source and exact formulation searches were checked, but that historical residual risk remains.

## References
1. Z. Lángi, *On a normed version of a Rogers--Shephard type problem*, arXiv:1308.2500v1, 12 August 2013.
2. C. A. Rogers and G. C. Shephard, *Some extremal problems for convex bodies*, *Mathematika* 5 (1958), 93--102. DOI: 10.1112/S0025579300001418.
3. Á. G. Horváth and Z. Lángi, *On the volume of the convex hull of two convex bodies*, arXiv:1302.6164v1, 25 February 2013.
