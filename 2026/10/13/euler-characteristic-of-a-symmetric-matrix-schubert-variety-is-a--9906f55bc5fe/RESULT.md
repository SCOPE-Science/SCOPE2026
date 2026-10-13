# Euler characteristic of a symmetric matrix Schubert variety is a two-order-statistic count
## Finding
Let
\[
w\in S_n,
\]
and define the north-east rank matrix
\[
R_w(i,j)
=
\#\{k\le i:w(k)\le n+1-j\}.
\]
Let
\[
V_{\mathrm{sym}}(w)
\subset
\operatorname{Sym}_n(\mathbb C)
\]
be the symmetric matrix Schubert variety defined by
\[
\operatorname{rank}\!\left(\Sigma_{[1,i],[j,n]}\right)
\le
R_w(i,j)
\]
for every
\[
1\le i,j\le n,
\]
and let
\[
\mathbb P V_{\mathrm{sym}}(w)
\subset
\mathbb P^{n(n+1)/2-1}
\]
be its projectivization.

For each
\[
a\ge1,
\]
let
\[
m_a
=
\min\{w(1),\ldots,w(a)\},
\]
and for
\[
b\ge2
\]
let
\[
s_b
\]
be the second-smallest value among
\[
w(1),\ldots,w(b).
\]

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\mathbb P V_{\mathrm{sym}}(w)\right)
=
n+
\#\left\{
(a,b):
1\le a<b\le n,\ 
m_a\le n+1-b,\ 
s_b\le n+1-a
\right\}.
}
\]

Equivalently, if
\[
S_{aa}=E_{aa}
\]
and
\[
S_{ab}=E_{ab}+E_{ba}
\qquad(a<b)
\]
denote the symmetric coordinate points, then every diagonal point survives and
\[
\boxed{
[S_{ab}]\in \mathbb P V_{\mathrm{sym}}(w)
\iff
R_w(a,b)\ge1
\ \text{and}\
R_w(b,a)\ge2.
}
\]

Consequently
\[
\boxed{
n
\le
\chi_{\mathrm{top}}\!\left(\mathbb P V_{\mathrm{sym}}(w)\right)
\le
\frac{n(n+1)}2.
}
\]
The lower bound is attained uniquely by the long permutation
\[
n(n-1)\cdots21,
\]
and the upper bound is attained exactly when
\[
w(1)=1.
\]

Thus the global Euler characteristic of a symmetric matrix Schubert variety is governed by only the first two prefix order statistics of its indexing permutation.

## Assumptions and scope
The base field is
\[
\mathbb C.
\]

The rank convention agrees with the symmetric Schubert determinantal ideals of Fink--Rajchgot--Sullivant. Their permutation matrix convention gives
\[
R_w(i,j)
=
\#\{k\le i:w(k)\le n+1-j\}.
\]

The affine variety is a homogeneous cone. The formula includes the possibility that a projectivization is empty, although for permutation-indexed symmetric matrix Schubert varieties the diagonal fixed-point argument below already supplies \(n\) projective points.

No smoothness assumption is used.

## Proof
Let
\[
D(z)
=
\operatorname{diag}\!\left(z^{3^1},z^{3^2},\ldots,z^{3^n}\right).
\]
Act on symmetric matrices by congruence:
\[
\Sigma
\longmapsto
D(z)\Sigma D(z).
\]
Every north-east rank is unchanged by this row-and-column rescaling, so
\[
V_{\mathrm{sym}}(w)
\]
is invariant.

The symmetric coordinate \(\sigma_{ab}\), with \(a\le b\), has weight
\[
3^a+3^b.
\]
These weights are pairwise distinct: in base \(3\), an off-diagonal pair has two digits equal to \(1\), while a diagonal pair has one digit equal to \(2\). Therefore the projective fixed locus consists exactly of the symmetric coordinate points
\[
[S_{ab}],
\qquad
1\le a\le b\le n.
\]

Fix \(a<b\). In the north-east submatrix with rows
\[
[1,p]
\]
and columns
\[
[q,n],
\]
the point \(S_{ab}\) has rank \(0\), \(1\), or \(2\). The entry in position \((a,b)\) appears exactly when
\[
p\ge a,
\qquad
q\le b.
\]
The reflected entry in position \((b,a)\) appears exactly when
\[
p\ge b,
\qquad
q\le a.
\]
The second condition implies the first.

Since \(R_w(p,q)\) is weakly increasing as \(p\) increases and as \(q\) decreases, all rank-one constraints are satisfied exactly when
\[
R_w(a,b)\ge1,
\]
and all rank-two constraints are satisfied exactly when
\[
R_w(b,a)\ge2.
\]
Hence
\[
[S_{ab}]\in\mathbb P V_{\mathrm{sym}}(w)
\iff
R_w(a,b)\ge1
\ \text{and}\
R_w(b,a)\ge2.
\]

For a diagonal point \(S_{aa}\), the analogous condition is only
\[
R_w(a,a)\ge1.
\]
Among the first \(a\) values of a permutation, at least one is at most
\[
n-a+1,
\]
so every diagonal point survives.

Now
\[
R_w(a,b)\ge1
\iff
m_a\le n+1-b,
\]
and
\[
R_w(b,a)\ge2
\iff
s_b\le n+1-a.
\]
Counting the fixed points gives the stated formula, because for any complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}),
\]
and projectivity identifies
\[
\chi_c
\]
with ordinary topological Euler characteristic.

The lower bound follows because all \(n\) diagonal points survive. To characterize equality, suppose first that
\[
w=n(n-1)\cdots21.
\]
Then for \(a<b\),
\[
R_w(a,b)=0,
\]
so no off-diagonal point survives.

Conversely, suppose \(w\) first differs from the long permutation in position \(a\). Then
\[
w(k)=n+1-k
\qquad(k<a),
\]
while
\[
w(a)<n+1-a.
\]
Set
\[
b=n+1-w(a).
\]
Then
\[
b>a
\]
and
\[
R_w(a,b)\ge1.
\]
The first \(a-1\) entries are precisely values larger than
\[
n+1-a.
\]
Every remaining value is at most
\[
n+1-a,
\]
so the entries in positions \(a\) and \(a+1\) already give
\[
R_w(b,a)\ge2.
\]
Thus an off-diagonal point survives, proving uniqueness of the minimum.

For the upper bound, the ambient projective space has
\[
n(n+1)/2
\]
coordinate fixed points. If
\[
w(1)=1,
\]
then for every \(a<b\),
\[
R_w(a,b)\ge1.
\]
Also, among the first \(b\) values at most \(a-1\) are larger than
\[
n+1-a.
\]
Since
\[
b>a,
\]
at least two are at most this threshold, so
\[
R_w(b,a)\ge2.
\]
Hence every symmetric coordinate point survives.

Conversely, if every coordinate point survives, then in particular
\[
[S_{1n}]
\]
survives. The condition
\[
R_w(1,n)\ge1
\]
forces
\[
w(1)=1.
\]
This proves the upper equality classification.

## Verification
The bundled checker enumerates every permutation for
\[
1\le n\le7.
\]

For each permutation it constructs the full north-east rank matrix directly. For every symmetric coordinate point it tests every north-east rank condition without using the closed formula, and compares the result with both the two-rank criterion and the prefix order-statistic criterion.

Across the complete census it also verifies the sharp minimum and maximum and their equality cases.

These finite computations are regression evidence only. The theorem for all \(n\) is proved by the symbolic fixed-point argument above.

## Relationship to prior work
Fink, Rajchgot, and Sullivant define the same symmetric Schubert determinantal ideals, prove them prime, obtain diagonal-term Gröbner bases, and interpret them through type-\(C\) Schubert geometry. Their paper also gives parametrizations and applications to Gaussian conditional independence.

Escobar, Fink, Rajchgot, and Woo later develop Gröbner bases, subword complexes, multigraded Hilbert series, and torus multigradings for a larger type-\(C\) Kazhdan--Lusztig class containing these symmetric Schubert determinantal ideals.

LeVan and Raicu compute local Euler obstructions for Lagrangian-Grassmannian Schubert strata and, on the big cell, recover local Euler obstructions for the symmetric matrix rank stratification. Local Euler obstruction is a different invariant from the global ordinary Euler characteristic computed here.

The inspected sources do not state the global projective Euler formula, its two-prefix-order-statistic interpretation, or the sharp extremal classification above.

## Limitations
Ordinary Euler characteristic is coarse. Different permutations can have the same first two prefix order statistics relevant to the count while defining varieties with different dimensions, degrees, singularities, or Hilbert series.

The result concerns the permutation-indexed symmetric Schubert determinantal varieties of Fink--Rajchgot--Sullivant. It does not claim the same formula for arbitrary symmetric ladder determinantal varieties or for all type-\(C\) Kazhdan--Lusztig varieties.

The torus-localization argument is short, so an older or unindexed observation remains a residual novelty risk.

## References
Alex Fink, Jenna Rajchgot, and Seth Sullivant, *Matrix Schubert varieties and Gaussian conditional independence models*, arXiv:1510.04124, first submitted 14 October 2015; *Journal of Algebraic Combinatorics* 44 (2016), DOI 10.1007/s10801-016-0698-2.

Laura Escobar, Alex Fink, Jenna Rajchgot, and Alexander Woo, *Gröbner bases, symmetric matrices, and type C Kazhdan--Lusztig varieties*, arXiv:2104.09589; *Journal of the London Mathematical Society* 109 (2024), DOI 10.1112/jlms.12856.

Paul LeVan and Claudiu Raicu, *Euler obstructions for the Lagrangian Grassmannian*, *Algebraic Combinatorics* 5 (2022), 299--318, DOI 10.5802/alco.211.
