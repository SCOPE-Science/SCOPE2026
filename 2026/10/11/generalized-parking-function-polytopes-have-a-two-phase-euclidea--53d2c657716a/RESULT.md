# Generalized parking-function polytopes have a two-phase Euclidean inball
## Finding
Let
\[
n\ge2,
\qquad
a,b\in\mathbb Z_{>0},
\]
and let
\[
\mathfrak X_n(a,b)\subset\mathbb R^n
\]
be the generalized parking-function polytope for the parameter vector
\[
(a,b,b,\ldots,b)
\]
in the standard coordinate realization of Hanada, Lentfer, and Vindas-Meléndez.

Put
\[
A=a-1.
\tag{1}
\]
Then its exact Euclidean inradius is
\[
\boxed{
r_{\mathrm{in}}\bigl(\mathfrak X_n(a,b)\bigr)
=
\min\left\{
\frac{A+b(n-1)}2,
\frac{\sqrt n}{\sqrt n+1}
\left(A+\frac{b(n-1)}2\right)
\right\}.
}
\tag{2}
\]

The incenter is unique for every admissible parameter choice. Writing
\[
r=r_{\mathrm{in}}\bigl(\mathfrak X_n(a,b)\bigr),
\]
it is
\[
\boxed{
c=(1+r)\mathbf1.
}
\tag{3}
\]

There are exactly two metric phases.

If
\[
A>b(\sqrt n+1),
\tag{4}
\]
then
\[
r=\frac{A+b(n-1)}2,
\tag{5}
\]
and the insphere is tangent exactly to the \(2n\) coordinate facets
\[
x_i=1,
\qquad
x_i=a+(n-1)b,
\qquad
1\le i\le n.
\tag{6}
\]

If
\[
A<b(\sqrt n+1),
\tag{7}
\]
then
\[
r=
\frac{\sqrt n}{\sqrt n+1}
\left(A+\frac{b(n-1)}2\right),
\tag{8}
\]
and the insphere is tangent exactly to the \(n\) lower coordinate facets
\[
x_i=1
\]
and the unique full-sum facet
\[
\sum_{i=1}^n x_i
=
na+\frac{bn(n-1)}2.
\tag{9}
\]

At the transition
\[
A=b(\sqrt n+1),
\tag{10}
\]
all \(2n+1\) facets in (6) and (9) are tangent. Because \(A\) and \(b\) are integers, (10) can occur only when \(n\) is a perfect square.

For the classical parking-function polytope
\[
\mathsf{PF}_n=\mathfrak X_n(1,1),
\]
only the total-sum phase occurs, and
\[
\boxed{
r_{\mathrm{in}}(\mathsf{PF}_n)
=
\frac{(n-1)\sqrt n}{2(\sqrt n+1)}.
}
\tag{11}
\]
Its unique incenter is \((1+r)\mathbf1\), and exactly \(n+1\) facets support its insphere.

## Assumptions and scope
The metric is the standard Euclidean metric of \(\mathbb R^n\).

The theorem is stated for \(n\ge2\). The one-dimensional case is an interval and has a separate trivial formula.

The source proves that \(\mathfrak X_n(a,b)\) is full-dimensional for the stated parameters and gives a minimal facet description. When \(a=1\), the inequalities using \(n-1\) coordinates are redundant; this omission does not affect the inradius formula because the controlling upper-facet size is always an endpoint, namely \(1\) or \(n\).

The conclusion is realization-sensitive. Integral equivalence with partial permutahedra does not by itself preserve Euclidean inradius.

## Proof
The source gives the following minimal inequalities. Every coordinate satisfies
\[
x_i\ge1.
\tag{12}
\]
For every subset \(I\subseteq[n]\) of cardinality
\[
|I|=k,
\]
there is an upper inequality
\[
\sum_{i\in I}x_i
\le
U_k,
\tag{13}
\]
where
\[
U_k
=
ka+b\left(nk-\frac{k^2+k}{2}\right)
=
k\left(a+b\left(n-\frac{k+1}{2}\right)\right).
\tag{14}
\]
When \(a=1\), the case \(k=n-1\) is redundant; all other sizes, including \(k=1\) and \(k=n\), are facet-defining.

Fix a candidate radius \(\rho\). The set of centers of radius-\(\rho\) balls contained in the polytope is a convex set invariant under every coordinate permutation. Averaging any feasible center over the symmetric group therefore gives a diagonal feasible center
\[
t\mathbf1.
\tag{15}
\]
Consequently the global inradius can be obtained by optimizing only diagonal centers.

At \(t\mathbf1\), the distance to a lower coordinate facet is
\[
t-1.
\tag{16}
\]
A size-\(k\) upper facet has normal of Euclidean norm \(\sqrt k\), so its distance is
\[
\frac{U_k-kt}{\sqrt k}.
\tag{17}
\]
The lower clearance is increasing in \(t\), while every upper clearance is decreasing. For a fixed \(k\), the two are equal exactly when
\[
t-1
=
\frac{U_k-kt}{\sqrt k}.
\]
The common value is
\[
r_k
=
\frac{U_k-k}{k+\sqrt k}
=
\frac{\sqrt k}{\sqrt k+1}
\left(
A+b\left(n-\frac{k+1}{2}\right)
\right).
\tag{18}
\]
It follows that
\[
r=\min_k r_k,
\tag{19}
\]
where the minimum ranges over the facet-defining upper sizes.

We now show that only the endpoint sizes \(k=1\) and \(k=n\) can minimize (18). Regard \(k\) temporarily as a real variable and put
\[
y=\sqrt k,
\qquad
C=A+b\left(n-\frac12\right).
\]
Then
\[
r_k
=
\frac{y}{y+1}
\left(C-\frac b2y^2\right).
\tag{20}
\]
The sign of the derivative with respect to \(y\) is the sign of
\[
C-\frac b2y^2(2y+3).
\tag{21}
\]
The expression in (21) is strictly decreasing for \(y>0\). Hence (20) increases and then decreases, with at most one interior critical point, which is a maximum. Its minimum on
\[
1\le k\le n
\]
therefore occurs at an endpoint. The possible omission of \(k=n-1\) when \(a=1\) is irrelevant.

Substituting the two endpoints gives
\[
r_1
=
\frac{A+b(n-1)}2,
\tag{22}
\]
and
\[
r_n
=
\frac{\sqrt n}{\sqrt n+1}
\left(A+\frac{b(n-1)}2\right).
\tag{23}
\]
This proves (2).

Both endpoint intersections occur at
\[
t=1+r,
\]
which proves the center formula (3). The comparison
\[
r_1\le r_n
\]
is equivalent to
\[
b(n-1)\le(\sqrt n-1)A,
\]
and therefore to
\[
A\ge b(\sqrt n+1).
\tag{24}
\]
This proves the phase criterion.

We next prove uniqueness and the exact contact sets.

In the coordinate-width phase, equality in (22) says that the distance between the two coordinate supporting hyperplanes
\[
x_i=1
\quad\text{and}\quad
x_i=a+(n-1)b
\]
is exactly \(2r\). Any center of a radius-\(r\) ball must therefore lie at their midpoint in every coordinate. Thus the center is uniquely (3), and all \(2n\) coordinate facets are tangent.

In the total-sum phase, every lower facet gives
\[
x_i\ge1+r.
\tag{25}
\]
The shifted full-sum facet gives
\[
\sum_i x_i
\le
U_n-r\sqrt n.
\tag{26}
\]
Equation (23) is exactly the identity
\[
U_n-r\sqrt n=n(1+r).
\tag{27}
\]
Summing (25) and comparing with (26) forces equality in every coordinate, so again the center is uniquely (3). The \(n\) lower facets and the full-sum facet are tangent.

The unimodality argument above is strict away from the endpoints. Hence no intermediate subset-size facet is tangent at the incenter. At equality in (24), both endpoint families are tangent simultaneously, giving \(2n+1\) tangent facets. Finally, equality in (10) would make
\[
\sqrt n=\frac{A}{b}-1
\]
rational, so integral \(a,b\) force \(n\) to be a perfect square.

Setting \(a=b=1\) in (23) gives (11).

## Verification
The proof is symbolic for all \(n\ge2\) and all positive integer \(a,b\).

The source-dependent input was checked in the primary full text: Proposition 3.6 gives the complete minimal inequality description (12)--(14), including the single redundancy when \(a=1\) and \(k=n-1\). The same paper proves the family is full-dimensional and simple.

A later full paper treating arbitrary parking-function parameter vectors was also inspected because it is a natural possible covering source. It gives a broader minimal inequality description, generalized-permutahedron and polymatroid interpretations, and combinatorial diameter results, but no Euclidean inradius or Chebyshev-center theorem.

The accompanying `verify.py` performs two independent finite checks. First, it evaluates every facet-size intersection \(r_k\) for many \((n,a,b)\) and confirms that the minimum is always one of the two endpoint values and that the predicted contact-size classes are exact. Second, for small dimensions it constructs every source facet and independently solves the full Chebyshev linear program with `scipy.optimize.linprog`; every optimum agrees with (2) and (3). These computations are corroborative only.

## Relationship to prior work
Hanada, Lentfer, and Vindas-Meléndez introduced the two-parameter family \(\mathfrak X_n(a,b)\), determined its vertices and minimal inequalities, proved smoothness, analyzed its faces, related it to partial permutahedra and Pitman--Stanley polytopes, and derived volume formulas. Their work does not state a largest-inscribed-ball theorem.

Bayer and collaborators later study parking-function polytopes for arbitrary parameter vectors. They give a general facet description and identify the polytopes with generalized permutahedra and polymatroids, but the inspected full text contains no inradius, Chebyshev-center, or inscribed-ball result.

The formula here uses the source symmetry and every facet orbit. A priori there are upper facets of every subset size, but their normalized clearance thresholds form a one-peak sequence, so only the singleton and full-set orbits can ever control the Euclidean inball. This produces the sharp transition (24) and the corresponding jump in the number of tangent facets.

Targeted published-result searches under “parking function polytope”, “generalized parking function polytope”, “partial permutahedron”, “inradius”, “insphere”, “largest inscribed ball”, and “Chebyshev center” did not locate a theorem implying (2)--(10).

## Limitations
The theorem concerns the two-parameter family \((a,b,b,\ldots,b)\), not the full arbitrary-parameter family introduced later.

It determines the Euclidean inball, but not the minimum enclosing sphere, John ellipsoid, or other extremal bodies.

The result is specific to the standard coordinate realization. Non-orthogonal unimodular equivalences to other polytope families do not preserve the radius.

The symmetry-averaging step is general, while the two-phase collapse relies on the explicit arithmetic progression of source facet offsets. A broader theorem for symmetric polymatroids with concave cardinality rank functions may subsume the calculation under different terminology; no such covering result was located.

## References
1. Mitsuki Hanada, John Lentfer, and Andrés R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885, first public version 2022-12-13; *Annals of Combinatorics* 28 (2024), 575--613, DOI 10.1007/s00026-023-00671-1.
2. Margaret M. Bayer, Steffen Borgwardt, Teressa Chambers, Spencer Daugherty, Aleyah Dawkins, Danai Deligeorgaki, Hsin-Chieh Liao, Tyrrell McAllister, Angela Morrison, Garrett Nelson, and Andrés R. Vindas-Meléndez, *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, first public version 2024-03-12.
