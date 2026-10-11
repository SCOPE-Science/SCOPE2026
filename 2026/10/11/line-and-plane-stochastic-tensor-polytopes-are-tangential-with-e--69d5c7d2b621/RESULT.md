# Line- and plane-stochastic tensor polytopes are tangential with exact inradii
## Finding
Let
\[
n\ge3.
\]
Let
\[
\mathcal L_n\subset\mathbb R^{n^3}
\]
be the polytope of nonnegative \(n\times n\times n\) line-stochastic tensors, meaning that every one-dimensional line sum is \(1\). Let
\[
\mathcal P_n\subset\mathbb R^{n^3}
\]
be the polytope of nonnegative plane-stochastic tensors, meaning that every two-dimensional plane sum is \(1\).

Equip each affine hull with the Euclidean metric induced by the Frobenius inner product.

Then both polytopes are tangential.

For the line-stochastic polytope, the unique incenter is the uniform tensor
\[
U_L=\left(\frac1n\right)_{i,j,k},
\tag{1}
\]
every one of its \(n^3\) coordinate facets is tangent to the maximal intrinsic ball, and
\[
\boxed{
r_{\mathrm{in}}(\mathcal L_n)
=
\frac{\sqrt n}{(n-1)^{3/2}}.
}
\tag{2}
\]

For the plane-stochastic polytope, the unique incenter is the uniform tensor
\[
U_P=\left(\frac1{n^2}\right)_{i,j,k},
\tag{3}
\]
every one of its \(n^3\) coordinate facets is tangent to the maximal intrinsic ball, and
\[
\boxed{
r_{\mathrm{in}}(\mathcal P_n)
=
\frac1{\sqrt{n(n^3-3n+2)}}.
}
\tag{4}
\]

The common mechanism is a dimension-controlled normal law. If \(T\) denotes the translation space of either affine hull and \(\Pi_T\) its orthogonal projector, then for every coordinate vector \(e_{ijk}\),
\[
\boxed{
\|\Pi_T e_{ijk}\|^2
=
\frac{\dim T}{n^3}.
}
\tag{5}
\]
Thus the source dimensions alone determine the intrinsic length of every coordinate-facet normal.

## Assumptions and scope
The result concerns the standard coordinate realizations of the order-\(3\), dimension-\(n\) line- and plane-stochastic tensor polytopes.

Distances and balls are intrinsic to the affine hulls, but use the ambient Frobenius inner product on \(\mathbb R^{n^3}\). Since both polytopes have codimension greater than zero, an ambient full-dimensional inradius would be zero and is not the quantity asserted here.

The range \(n\ge3\) avoids the low-dimensional coincidence in the line-stochastic case in which several coordinate supporting hyperplanes determine the same zero-dimensional facet.

## Proof
The primary source proves
\[
\dim\mathcal L_n=(n-1)^3
\tag{6}
\]
and
\[
\dim\mathcal P_n=n^3-3n+2.
\tag{7}
\]
It also proves, in the stated range, that the coordinate hyperplanes
\[
x_{ijk}=0
\tag{8}
\]
cut out the \(n^3\) facets of each polytope.

We first establish the intrinsic normal law (5).

Let \(T\) be the translation space of the relevant affine hull. The group
\[
S_n\times S_n\times S_n
\]
acts orthogonally by independently permuting the three indices. This action preserves both translation spaces and is transitive on the \(n^3\) coordinates. Therefore the orthogonal projector
\[
\Pi_T
\]
commutes with the group action, so all diagonal entries
\[
\langle e_{ijk},\Pi_T e_{ijk}\rangle
=
\|\Pi_T e_{ijk}\|^2
\]
are equal.

The trace of an orthogonal projector is its rank. Hence
\[
\sum_{i,j,k}
\|\Pi_T e_{ijk}\|^2
=
\operatorname{tr}(\Pi_T)
=
\dim T.
\]
There are \(n^3\) summands, proving (5).

For \(\mathcal L_n\), equations (5)--(6) give
\[
\|\Pi_{T_L}e_{ijk}\|
=
\sqrt{\frac{(n-1)^3}{n^3}}
=
\left(\frac{n-1}{n}\right)^{3/2}.
\tag{9}
\]
At the uniform tensor \(U_L\), the coordinate slack to \(x_{ijk}=0\) is \(1/n\). Therefore the intrinsic distance to every coordinate facet is
\[
\frac{1/n}{((n-1)/n)^{3/2}}
=
\frac{\sqrt n}{(n-1)^{3/2}},
\]
which proves feasibility of the ball in (2).

For \(\mathcal P_n\), equations (5) and (7) give
\[
\|\Pi_{T_P}e_{ijk}\|
=
\sqrt{\frac{n^3-3n+2}{n^3}}.
\tag{10}
\]
At \(U_P\), the coordinate slack is \(1/n^2\), hence every facet has intrinsic distance
\[
\frac{1/n^2}
{\sqrt{(n^3-3n+2)/n^3}}
=
\frac1{\sqrt{n(n^3-3n+2)}},
\]
which proves feasibility of the ball in (4).

It remains to prove optimality and uniqueness.

Let an intrinsic ball of radius \(\rho\) centered at a line-stochastic tensor \(Q=(q_{ijk})\) lie in \(\mathcal L_n\). Every coordinate facet gives
\[
q_{ijk}
\ge
\rho
\left(\frac{n-1}{n}\right)^{3/2}.
\tag{11}
\]
Summing all \(n^3\) inequalities and using that the total sum of a line-stochastic tensor is \(n^2\),
\[
n^2
\ge
n^3\rho
\left(\frac{n-1}{n}\right)^{3/2}.
\]
Thus
\[
\rho
\le
\frac{\sqrt n}{(n-1)^{3/2}}.
\tag{12}
\]
This matches the feasible uniform ball.

If equality holds in (12), then equality must hold in every coordinate inequality (11), because their sum is already saturated. Hence every entry of \(Q\) equals \(1/n\), so
\[
Q=U_L.
\]
The line-stochastic incenter is unique.

Similarly, if an intrinsic radius-\(\rho\) ball centered at \(Q\in\mathcal P_n\) lies in the plane-stochastic polytope, then
\[
q_{ijk}
\ge
\rho
\sqrt{\frac{n^3-3n+2}{n^3}}
\tag{13}
\]
for every coordinate. A plane-stochastic tensor has total sum \(n\). Summing (13) therefore gives
\[
n
\ge
n^3\rho
\sqrt{\frac{n^3-3n+2}{n^3}},
\]
or
\[
\rho
\le
\frac1{\sqrt{n(n^3-3n+2)}}.
\tag{14}
\]
Again the uniform ball attains equality. Equality in (14) forces equality in every coordinate lower bound, so every entry is \(1/n^2\). Thus
\[
Q=U_P,
\]
and the plane-stochastic incenter is unique.

Since the source coordinate hyperplanes are the complete facet families and every one is at the common distance from the corresponding uniform center, both polytopes are tangential.

## Verification
The proof is symbolic for every
\[
n\ge3.
\]

The source-dependent premises were checked directly in the primary full text: the definitions of line- and plane-stochastic tensors, the independent-index permutation symmetry, the dimensions
\[
(n-1)^3
\quad\text{and}\quad
n^3-3n+2,
\]
and the statement that the coordinate supporting hyperplanes give the \(n^3\) facets.

The accompanying `verify.py` builds the defining equality matrices for
\[
n=3,4.
\]
Using exact rational linear algebra, it verifies the two source rank formulas, forms the orthogonal projector onto each translation space, checks that every projector diagonal equals the affine dimension divided by \(n^3\), and replays the two inradius identities. These finite checks are corroborative only.

## Relationship to prior work
Zhang and Zhang study the same two tensor polytopes from the viewpoint of extreme points, coefficient-matrix ranks, dimensions, and facet counts. Their paper emphasizes that vertex enumeration is difficult even though the defining linear systems are highly symmetric. It does not state an intrinsic Euclidean inradius, an incenter theorem, or tangentiality.

Earlier work on stochastic tensor polytopes and multistochastic tensors studies Birkhoff-type decomposition questions, extreme points, permanents, and vertex bounds. Those results supply historical and combinatorial context, but do not give the Frobenius-metric facet distances used here.

The metric statement is not a formal consequence of knowing only that the facets are coordinate hyperplanes: their intrinsic normal lengths depend on how the affine constraint space sits inside \(\mathbb R^{n^3}\). Equation (5) is the additional geometric step. The independent-index symmetry makes those projected normal lengths equal, while the source dimensions determine their common value by the trace of the orthogonal projector.

Targeted literature and published-result searches under “line-stochastic tensor”, “plane-stochastic tensor”, “tangential polytope”, “inradius”, “Chebyshev center”, “insphere”, and “multiway transportation polytope” did not locate a theorem implying (2)--(5).

## Limitations
The theorem concerns order-\(3\) tensors with equal side length \(n\) and the standard Euclidean/Frobenius metric.

It does not determine circumradii, John or Löwner ellipsoids, vertex-distance distributions, or inradii for arbitrary nonuniform multiway transportation margins.

The proof uses the unusually strong coordinate transitivity of these uniform stochastic tensor polytopes. A general multiway transportation polytope need not have equal projected coordinate-normal lengths.

The argument is structurally related to Chebyshev-center calculations for matrix transportation polytopes, but the order-\(3\) affine constraint spaces and their normal lengths are different; the paired exact tensor formulas require the tensor-specific rank and facet data of the source.

## References
1. Fuzhen Zhang and Xiao-Dong Zhang, *Enumerating extreme points of the polytopes of stochastic tensors: an optimization approach*, conference abstract presented at the 50th Southeastern International Conference on Combinatorics, Graph Theory, and Computing, March 2019; later published in *Optimization* 69 (2020), 729--741, DOI 10.1080/02331934.2019.1647198; arXiv:2008.04655.
2. Zhongshan Li, Fuzhen Zhang, and Xiao-Dong Zhang, *On the number of vertices of the stochastic tensor polytope*, arXiv:1702.04288; *Linear and Multilinear Algebra* 65 (2017), 2064--2075, DOI 10.1080/03081087.2017.1310178.
3. Maolin Che, Changjiang Bu, Liqun Qi, and Yimin Wei, *Nonnegative tensors revisited: plane stochastic tensors*, *Linear and Multilinear Algebra* 67 (2019), 1364--1391, DOI 10.1080/03081087.2018.1453469.
