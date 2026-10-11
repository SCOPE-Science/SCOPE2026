# The redundant-facet regime of partial permutohedra has a simplex-controlled inball
## Finding
Let
\[
n\ge1,\qquad m\ge n+2,
\]
and let
\[
\mathcal P(m,n)
=
\operatorname{conv}\left\{
x\in\{0,1,\ldots,n\}^m:
\text{the nonzero coordinates of }x\text{ are distinct}
\right\}
\]
be the standard partial permutohedron.

Write
\[
T_n=\binom{n+1}{2}.
\tag{1}
\]
Then the exact Euclidean inradius is
\[
\boxed{
r_{m,n}
=
\frac{T_n}{m+\sqrt m}
=
\frac{n(n+1)}{2(m+\sqrt m)}.
}
\tag{2}
\]
The unique incenter is
\[
\boxed{
c_{m,n}=r_{m,n}\mathbf1.
}
\tag{3}
\]

The maximal ball is tangent exactly to the \(m\) coordinate facets
\[
x_i=0
\qquad
(1\le i\le m)
\tag{4}
\]
and the total-sum facet
\[
\sum_{i=1}^m x_i=T_n.
\tag{5}
\]
Every proper subset-sum facet is strictly farther from \(c_{m,n}\).

Thus, in the parameter range in which the intermediate large-subset inequalities become redundant, the inball is completely controlled by the simplex envelope consisting of coordinate nonnegativity together with the total-sum cap.

## Assumptions and scope
The metric is the standard Euclidean metric in \(\mathbb R^m\), exactly the coordinate realization used in the source.

The theorem covers the regime
\[
m\ge n+2.
\]
This is precisely the range in which the source facet description has proper upper facets only for subset cardinalities at most \(n-1\), together with the single total-sum facet.

The result includes \(n=1\), where \(\mathcal P(m,1)\) is the standard \(m\)-simplex.

## Proof
The source gives the complete facet description
\[
x_i\ge0
\qquad
(1\le i\le m),
\tag{6}
\]
together with
\[
\sum_{i\in S}x_i
\le
\binom{n+1}{2}
-
\binom{n+1-|S|}{2}
\tag{7}
\]
for every nonempty \(S\subseteq[m]\) satisfying
\[
|S|\le n-1
\quad\text{or}\quad
S=[m].
\]

For a proper upper facet with
\[
k=|S|\le n-1,
\]
its support value is
\[
z_k
=
kn-\binom{k}{2}
=
\frac{k(2n-k+1)}2.
\tag{8}
\]
The full-set support is
\[
z_m=T_n.
\tag{9}
\]

Put
\[
r=\frac{T_n}{m+\sqrt m},
\qquad
c=r\mathbf1.
\tag{10}
\]
The distance from \(c\) to each coordinate facet is \(r\). The distance to the full-set facet is
\[
\frac{T_n-mr}{\sqrt m}
=
r.
\tag{11}
\]
So the proposed ball is tangent to all facets in (4)--(5).

It remains to show that every proper upper facet is strictly farther away.

For a \(k\)-element subset, the distance from \(c\) to its supporting hyperplane is
\[
d_k
=
\frac{z_k-kr}{\sqrt k}.
\tag{12}
\]
The inequality
\[
d_k>r
\]
is equivalent to
\[
r<h_k,
\qquad
h_k
=
\frac{z_k}{k+\sqrt k}
=
\frac{\sqrt k(2n-k+1)}{2(\sqrt k+1)}.
\tag{13}
\]

Since \(m\ge n+2\),
\[
r
\le
r_0
=
\frac{n(n+1)}{2(n+2+\sqrt{n+2})}.
\tag{14}
\]
If \(n=1\), there are no proper upper facets, so there is nothing further to prove.

Assume \(n\ge2\). Regard (13) as the function
\[
\phi(x)
=
\frac{x(2n+1-x^2)}{2(x+1)}
\]
on
\[
1\le x\le\sqrt{n-1}.
\]
Its derivative is
\[
\phi'(x)
=
\frac{2n+1-3x^2-2x^3}{2(x+1)^2}.
\tag{15}
\]
The numerator in (15) is strictly decreasing for \(x>0\). Hence \(\phi\) is either monotone or increases and then decreases, so its minimum on the interval occurs at an endpoint. Therefore
\[
\min_{1\le k\le n-1}h_k
=
\min\{h_1,h_{n-1}\}.
\tag{16}
\]

First,
\[
h_1=\frac n2>r_0,
\tag{17}
\]
because
\[
n+2+\sqrt{n+2}>n+1.
\]

For the other endpoint, let
\[
a=\sqrt{n-1},
\qquad
b=\sqrt{n+2}.
\]
After clearing the positive denominators, the inequality
\[
h_{n-1}>r_0
\]
is equivalent to
\[
(n+2)a(n+2+b)>n(n+1)(a+1).
\tag{18}
\]
Using
\[
n=a^2+1
\]
and \(b>a\), the left side minus the right side in (18) is
\[
-a^4+a^3b+3a^3-3a^2+3ab+7a-2
>
3a^3+7a-2
>
0,
\tag{19}
\]
since \(a\ge1\). Thus every proper upper facet satisfies
\[
d_k>r.
\tag{20}
\]
The ball \(B(c,r)\) is therefore contained in \(\mathcal P(m,n)\).

To prove optimality, let a Euclidean ball of radius \(\rho\) centered at \(q\) be contained in the polytope. The coordinate facets give
\[
q_i\ge\rho
\]
for every \(i\), while the total-sum facet gives
\[
\sum_iq_i+\rho\sqrt m\le T_n.
\]
Hence
\[
(m+\sqrt m)\rho\le T_n,
\]
so
\[
\rho\le r.
\tag{21}
\]
This matches the feasible ball.

If equality holds in (21), equality must hold in every lower bound \(q_i\ge\rho\), because their sum already saturates the full-set inequality. Therefore
\[
q_1=\cdots=q_m=r,
\]
which proves uniqueness of the incenter.

## Verification
The proof is symbolic for every
\[
n\ge1,\qquad m\ge n+2.
\]

The source-dependent facts were checked directly in the full primary text: the definition and full dimension of \(\mathcal P(m,n)\), its vertex description, and Proposition 2.8's complete irredundant facet description. In particular, the source explicitly separates the proper subset facets \(|S|\le n-1\) from the full-set facet in this regime.

The accompanying `verify.py` checks all pairs
\[
1\le n\le60,\qquad n+2\le m\le120.
\]
For every proper facet cardinality it verifies the strict distance inequality at the proposed center, checks equality for every coordinate facet and the total-sum facet, and independently checks the global upper-bound identity. These finite checks are corroborative only.

## Relationship to prior work
Behrend, Castillo, Chavez, Diaz-Lopez, Escobar, Harris, and Insko study partial permutohedra through their face lattices, volume, Ehrhart theory, generalized-permutohedron structure, anti-blocking structure, and specializations to stellohedra and parking-function polytopes. Their Proposition 2.8 reproduces the complete facet description needed here.

The earlier paper of Heuer and Striker introduced the family and originally proved the facet inequalities. That paper is supporting combinatorial literature; the geometry-classified later paper is the primary source used for this result.

A previously available exact inradius formula covered the complementary near-square regime
\[
n\ge m-1.
\]
It does not imply the present theorem, whose domain
\[
m\ge n+2
\]
is disjoint and whose proof uses the redundant-facet structure characteristic of the opposite parameter regime.

The source itself emphasizes that when \(m>n\), the combinatorial type depends on both parameters and the large-redundancy regime behaves differently in volume and Ehrhart questions. The metric result here shows that, despite that richer face structure, the Euclidean inball is exactly the inball of the enclosing simplex determined by nonnegativity and the total-sum cap.

Targeted searches under “partial permutohedron”, “inradius”, “Chebyshev center”, “largest inscribed Euclidean ball”, “redundant regime”, and “full-sum facet” did not locate a theorem covering this parameter range.

## Limitations
The theorem concerns only the standard coordinate realization and Euclidean balls.

It does not determine the circumradius, John ellipsoid, or metric behavior under affine equivalence.

The proof exploits the complete symmetry and the specific arithmetic support values of partial permutohedra. It is not asserted for general anti-blocking generalized permutohedra.

A residual originality risk remains for a general Chebyshev-center theorem for symmetric polymatroid-type bodies under different terminology.

## References
1. Roger E. Behrend, Federico Castillo, Anastasia Chavez, Alexander Diaz-Lopez, Laura Escobar, Pamela E. Harris, and Erik Insko, *Partial Permutohedra*, arXiv:2207.14253, first public version 2022-07-28.
2. Dylan Heuer and Jessica Striker, *Partial Permutation and Alternating Sign Matrix Polytopes*, arXiv:2012.09901, first public version 2020-12-17; SIAM Journal on Discrete Mathematics 36 (2022), 2863--2888, DOI 10.1137/21M1417958.
