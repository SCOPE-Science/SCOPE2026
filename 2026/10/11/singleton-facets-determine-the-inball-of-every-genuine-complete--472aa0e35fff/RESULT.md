# Singleton facets determine the inball of every genuine complete-bipartite graph associahedron
## Finding
Let
\[
p,q\ge2,
\qquad
N=p+q,
\qquad
M=(2^p-1)(2^q-1).
\]
Write the two vertex classes of
\[
K_{p,q}
\]
as
\[
L=[p],
\qquad
R=\{\bar1,\ldots,\bar q\}.
\]

Consider the translation-normalized standard graph-associahedron realization
\[
\operatorname{Asso}^{0}(K_{p,q})
=
\sum_{\emptyset\ne A\subseteq L}
\sum_{\emptyset\ne B\subseteq R}
\Delta_{A\cup B}
\subset\mathbb R^N.
\tag{1}
\]
There are \(M\) summands, so
\[
\operatorname{Asso}^{0}(K_{p,q})
\subset
H_M
=
\left\{
x\in\mathbb R^N:
\sum_{i=1}^{N}x_i=M
\right\}.
\]
Equip \(H_M\) with its intrinsic Euclidean metric.

Then the incenter is unique and equals
\[
\boxed{
c_*=\frac{M}{N}\mathbf1.
}
\tag{2}
\]
The exact inradius is
\[
\boxed{
r_{\mathrm{in}}
\bigl(\operatorname{Asso}^{0}(K_{p,q})\bigr)
=
\frac{M}{\sqrt{N(N-1)}}
=
\frac{(2^p-1)(2^q-1)}
{\sqrt{(p+q)(p+q-1)}}.
}
\tag{3}
\]

The proper tubes of \(K_{p,q}\) are the \(N\) singletons and the proper subsets meeting both bipartition classes. Hence the number of facets is
\[
\boxed{
N+M-1.
}
\tag{4}
\]
Despite this exponential facet count, the maximal ball is tangent exactly to the
\[
\boxed{N}
\]
singleton-tube facets
\[
x_i=0.
\tag{5}
\]

Some authors include all singleton simplices in the standard nestohedron Minkowski sum. Adding
\[
\sum_{i=1}^N\Delta_{\{i\}}
=
\mathbf1
\]
just translates the polytope. Under that convention the inradius is still (3), while the unique incenter is
\[
\left(1+\frac{M}{N}\right)\mathbf1.
\tag{6}
\]

## Assumptions and scope
The theorem concerns genuine bicliques:
\[
p,q\ge2.
\]
The boundary family \(K_{1,q}\) consists of stars and gives stellohedra; it has a separate two-dimensional tangency exception and is intentionally excluded here.

The realization in (1) is the standard Postnikov nestohedron attached to the graphical building set, with singleton summands removed only to fix a convenient translation. Removing those point summands does not change the intrinsic Euclidean metric, inradius, or facet-normal geometry.

The metric is realization-specific. General affine realizations of the same graph-associahedron face lattice need not have the same inradius.

## Proof
For a Minkowski sum of coordinate simplices
\[
P=\sum_I y_I\Delta_I,
\]
Postnikov's generalized-permutohedron coordinates give
\[
x(T)\ge z(T),
\qquad
z(T)=\sum_{I\subseteq T}y_I.
\tag{7}
\]
For (1), every non-singleton connected subset of \(K_{p,q}\) contains at least one left and one right vertex, and every such subset occurs once as a summand.

Therefore a singleton tube has
\[
z(\{i\})=0.
\tag{8}
\]
A connected tube \(T\) containing \(a\) left vertices and \(b\) right vertices has
\[
a,b\ge1,
\qquad
k=|T|=a+b,
\]
and
\[
z(T)
=
(2^a-1)(2^b-1).
\tag{9}
\]
Proper tubes index the facets.

Inside the tangent space
\[
\mathbf1^\perp,
\]
the intrinsic normal to a singleton hyperplane \(x_i=0\) is
\[
e_i-\frac1N\mathbf1,
\]
whose norm is
\[
\sqrt{\frac{N-1}{N}}.
\tag{10}
\]
If a radius-\(r\) ball centered at \(c\in H_M\) lies inside the polytope, every singleton facet requires
\[
c_i
\ge
r\sqrt{\frac{N-1}{N}}.
\]
Summing over all \(N\) coordinates gives
\[
M
\ge
Nr\sqrt{\frac{N-1}{N}},
\]
hence
\[
r
\le
\frac{M}{\sqrt{N(N-1)}}.
\tag{11}
\]
Equality in (11) forces equality in every singleton constraint, so any optimal ball attaining the bound must have the unique center
\[
c_*=\frac{M}{N}\mathbf1.
\]

It remains to prove that every non-singleton tube facet is strictly farther from \(c_*\).

For positive integers \(r,s\), define the density
\[
F(r,s)
=
\frac{(2^r-1)(2^s-1)}
{(r+s)(r+s-1)}.
\tag{12}
\]
This density is coordinatewise nondecreasing. Indeed, writing \(t=r+s\),
\[
\frac{F(r+1,s)}{F(r,s)}
=
\left(
2+\frac1{2^r-1}
\right)
\frac{t-1}{t+1}.
\tag{13}
\]
If \(t=2\), then \(r=s=1\) and the ratio is \(1\). If \(t\ge3\), then
\[
\frac{t+1}{t-1}\le2
<
2+\frac1{2^r-1},
\]
so the ratio in (13) is strictly larger than \(1\). The same argument applies to increasing \(s\).

Since
\[
p,q\ge2
\]
and \((a,b)\ne(p,q)\), any coordinatewise path from \((a,b)\) to \((p,q)\) contains a strict step. Thus
\[
F(a,b)<F(p,q).
\]
Equivalently,
\[
\frac{(2^a-1)(2^b-1)}{M}
<
\frac{k(k-1)}{N(N-1)}.
\tag{14}
\]

The projected normal of the tube hyperplane \(x(T)=z(T)\) has norm
\[
\sqrt{\frac{k(N-k)}{N}}.
\tag{15}
\]
At the uniform point \(c_*\), its slack is
\[
\frac{kM}{N}-z(T).
\]
Using (14),
\[
\frac{kM}{N}-z(T)
>
\frac{M}{N}
\left(
k-\frac{k(k-1)}{N-1}
\right)
=
\frac{M}{N}
\frac{k(N-k)}{N-1}.
\tag{16}
\]
Therefore the distance \(d_T\) from \(c_*\) to this tube facet satisfies
\[
d_T
>
\frac{M}{\sqrt{N(N-1)}}
\sqrt{\frac{k(N-k)}{N-1}}.
\tag{17}
\]
Every connected non-singleton proper tube has
\[
2\le k\le N-1.
\]
Hence
\[
k(N-k)\ge N-1,
\]
and (17) gives
\[
d_T
>
\frac{M}{\sqrt{N(N-1)}}.
\tag{18}
\]

Thus the radius in (11) is feasible at \(c_*\), no larger ball exists, the center is unique, and every non-singleton facet is strictly farther away. This proves (2)--(5).

## Verification
The argument is symbolic and covers every
\[
p,q\ge2.
\]

The source-dependent structural input was checked directly in the standard generalized-permutohedron literature: graph associahedra are nestohedra obtained as Minkowski sums of coordinate simplices, and for
\[
\sum_I y_I\Delta_I
\]
the lower support constant of a subset \(T\) is
\[
z(T)=\sum_{I\subseteq T}y_I.
\]
The recent deformation-cone paper independently reviews graph associahedra as graphical nested-fan realizations and gives their facet-normal framework.

The accompanying `verify.py` checks all pairs
\[
2\le p,q\le35
\]
and every proper connected tube cardinality pair \((a,b)\). It verifies the strict density inequality (14), the exact squared facet distances, the unique singleton minimum, the center formula, and the facet count. This finite replay is corroborative only and does not replace the arbitrary-parameter proof.

## Relationship to prior work
Padrol, Pilaud, and Poullot study deformation cones of graph associahedra and nestohedra. Their paper reviews the Minkowski-sum and facet-normal realizations and gives an irredundant description of the full deformation cone, but does not state an Euclidean inradius or Chebyshev-center theorem.

Cardinal, Pournin, and Valencia-Pabon study graph-associahedron diameters and treat complete bipartite graphs explicitly. Their diameter is the graph-theoretic diameter of the one-skeleton; it does not determine the Euclidean largest-inscribed-ball problem. Their inspected text contains no “inradius” or “Euclidean” occurrence.

Postnikov's standard realization supplies the exact Minkowski-sum and subset-inequality formulas used in the proof. Those structural formulas do not themselves identify the closest facet orbit or optimize a Euclidean ball.

The star boundary \(K_{1,q}\) is the stellohedron. The present theorem deliberately starts at
\[
p,q\ge2.
\]
In that genuine-biclique regime, the two-variable density monotonicity (12)--(14) proves that every connected tube larger than a singleton is strictly inactive at the inball.

Targeted literature and published-result searches for “complete bipartite graph associahedron”, “inradius”, “Chebyshev center”, “uniform incenter”, and facet-distance formulations did not locate a theorem implying (2)--(5).

## Limitations
The theorem treats only the standard Minkowski-sum realization of complete-bipartite graph associahedra. Other realizations with the same face lattice can have different Euclidean radii.

The star boundary is excluded because it has its own low-dimensional equality phenomenon.

No formula is claimed here for complete multipartite graph associahedra with three or more parts. Their building-set subset counts involve a different inclusion-exclusion structure.

A residual originality risk remains that the metric consequence appears as folklore or as a specialization of a general Chebyshev-center theorem for symmetric nestohedra under terminology not exposed by the searches.

## References
1. Arnau Padrol, Vincent Pilaud, and Germain Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200, first public version 2021-09-19; European Journal of Combinatorics 107 (2023), 103594, DOI 10.1016/j.ejc.2022.103594.
2. Jean Cardinal, Lionel Pournin, and Mario Valencia-Pabon, *Diameter estimates for graph associahedra*, arXiv:2106.16130, first public version 2021-06-30; Annals of Combinatorics 26 (2022), 873--902, DOI 10.1007/s00026-022-00598-z.
3. Alexander Postnikov, *Permutohedra, associahedra, and beyond*, arXiv:math/0507163, first public version 2005-07-07; International Mathematics Research Notices 2009(6), 1026--1106, DOI 10.1093/imrn/rnn153.
