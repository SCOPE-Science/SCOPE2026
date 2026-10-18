# Largest inscribed tetrahedra of the snub cube

## Finding

Let \(\tau\) be the unique real root of \(\tau^3-\tau^2-\tau-1=0\), and set \(\xi=\tau^{-1}=\tau^2-\tau-1\). Define the snub cube \(P\) as the convex hull of all even coordinate permutations of \((\pm1,\pm\xi,\pm\tau)\) with an even number of positive signs, together with all odd coordinate permutations having an odd number of positive signs. There are \(24\) vertices.

The sharp unrestricted inscribed-tetrahedron volume is
\[
\max_{x_0,x_1,x_2,x_3\in P}
\operatorname{vol}_3\bigl(\operatorname{conv}\{x_0,x_1,x_2,x_3\}\bigr)
=\frac23(\tau^2+\tau+2)\approx4.814841682080265.
\]
The polyhedron has edge length \(a=\sqrt{2+4\tau-2\tau^2}\); the maximum volume after scaling to unit edge is \(\frac{2(\tau^2+\tau+2)}{3a^3}\approx1.154334681740913\).

More strongly, **every** maximizing tetrahedron lies in exactly one of eight two-dimensional continuous families. An explicit representative has a fixed equilateral base
\[
B=\operatorname{conv}\{(-1,-\xi,-\tau),(\xi,-\tau,1),(\tau,1,-\xi)\}
\]
and its fourth vertex anywhere in the triangular face
\[
F=\operatorname{conv}\{(-1,\xi,\tau),(-\xi,\tau,1),(-\tau,1,\xi)\}.
\]
Let \(G\) be the group of all signed coordinate permutations of determinant \(+1\), of order \(24\). Precisely the eight distinct pairs \((gB,gF)\), for \(g\in G\), provide all equality families \(\operatorname{conv}(gB\cup\{z\})\) with \(z\in gF\). The families are disjoint as sets of tetrahedra. Among maxima, exactly \(24\) have all four vertices at vertices of \(P\); in any other maximum exactly one tetrahedron vertex varies inside one of the eight specified triangular facets.

## Assumptions and scope

All vertices and volumes use ordinary Euclidean three-dimensional geometry. Tetrahedra can use arbitrary points of the full convex body, not merely vertices of the polyhedron. A tetrahedron is a nondegenerate convex hull of four points and is counted without ordering its four vertices. Reflection exchanges the two chiral snub cubes and preserves every assertion. The coordinate normalization fixes the three distinct positive coordinate magnitudes at \(1,\xi,\tau\), respectively; unit-edge scaling uses the value \(a\) displayed above.

## Proof

**1. Reduction to algebraic vertex determinants.** For four points \(x_0,x_1,x_2,x_3\in P\), their oriented sixfold volume is
\[
D(x_0,x_1,x_2,x_3)=\det(x_1-x_0,x_2-x_0,x_3-x_0).
\]
The determinant is affine in each point separately, holding the other three fixed. Expressing the four points in convex combinations of the \(24\) vertices therefore represents \(D\) as a convex combination of oriented vertex determinants. The maximum of \(|D|\) on \(P^4\) is consequently the largest absolute value of a vertex determinant.

**2. Exact finite determinant bound and extremizers.** All coordinates belong to \(\mathbb Z[\tau]\), and reduction by \(\tau^3=\tau^2+\tau+1\) produces unique canonical integer triples for the coefficients of \(1,\tau,\tau^2\). (Uniqueness follows because this cubic is irreducible over \(\mathbb Q\).) The standalone `snub_exact_verifier.py` builds the \(24\) vertices in explicit, reproducible order and checks all \(\binom{24}{4}=10626\) distinct unordered four-vertex subsets with exact integer polynomial arithmetic. It obtains exactly \(191\) distinct oriented determinant polynomials, with the sharp bound
\[
|D|\le D_*:=8+4\tau+4\tau^2.
\]
Exactly \(24\) subsets attain equality. The comparison of algebraic numbers uses the rational isolating interval
\[
\frac{1839286755214}{10^{12}}<\tau<\frac{1839286755215}{10^{12}}.
\]
Both endpoints are checked by exact rational substitution into the cubic; every asserted strict determinant sign is certified by rational interval bounds on the degree-two remainder polynomial. This is an exhaustive algebraic verification, not a floating-point sample. Dividing \(D_*\) by \(6\) gives the asserted volume.

**3. The eight movable-apex faces.** For every triangle \(A\) obtained by selecting three of the vertices from an equality tetrahedron, record the set \(S(A)\) of vertex indices \(v\) such that \(A\cup\{v\}\) is an equality tetrahedron. The same exact exhaustive computation gives \(80\) such triangles, with
\[
\#\{A:|S(A)|=1\}=72,\qquad
\#\{A:|S(A)|=3\}=8.
\]
Moreover **each** of the \(24\) maximal vertex tetrahedra contains exactly one of the eight triangles with three possible opposite apex vertices. The corresponding three-apex sets are actual triangular facets of \(P\): a cross-product facet-normal check, using the same exact \(\mathbb Z[\tau]\) sign certification, shows all remaining \(21\) vertices lie strictly on the same side of each facet plane. The eight ordered pairs (fixed base, variable triangular face) form one orbit under the \(24\) determinant-one signed coordinate permutations. The displayed pair \((B,F)\) is one such representative. Every apex in \(F\) gives the same determinant \(D_*\) by affinity in that fourth point; thus each orbit pair yields a full continuous family of maximizers.

**4. Exhaustion of all continuous equality cases.** Suppose an arbitrary maximizing tetrahedron had two vertices that were not vertices of \(P\). Each of these two points has a convex representation using at least two distinct polyhedron vertices. Fixing vertex representatives for its other two points, separate affinity says every combination of representatives from the two varying supports must be a vertex-supported maximizing tetrahedron with the same determinant sign. In particular, one such vertex tetrahedron could have either of two different three-vertex bases with at least two maximizing opposite apices, contrary to the unique such base per maximal vertex tetrahedron established in step 3. Hence at most one point can be nonvertex. If one is nonvertex, the three remaining points form a fixed base with at least two maximizing opposite vertex choices, so they must form one of the eight special bases; the varying point lies in the convex hull of its three allowed apices. If all four points are polyhedron vertices, the unique-special-base result places the tetrahedron at a vertex of exactly one family. This also proves that the eight equality families do not overlap.

**5. Geometry of the representative.** Direct algebra using \(\tau^3=\tau^2+\tau+1\) gives the squared edge lengths
\[
\ell_B^2=2\tau^2+4\tau-2,\qquad
\ell_F^2=2+4\tau-2\tau^2.
\]
Both are equilateral triangles in parallel planes. Their affine determinant is \(D_*\), agreeing with the exact sixfold volume. In particular, the continuum of optimal fourth vertices is a genuine two-dimensional face, not merely an interpolation between collinear vertices.

## Verification

Execute `python snub_exact_verifier.py` with Python 3 and the standard library. The program constructs all \(24\) algebraic vertices, exhausts the \(10626\) vertex quadruples, certifies every maximum comparison by rational root isolation, proves the counts \(24\), \(72\), and \(8\), checks that the eight variable-apex triangles are supporting facets, and checks the single rotation orbit. It prints `all_exact_checks_passed` only after the assertions have succeeded. The complete source is part of this result; no external datasets, floating-point libraries, network access, or other packages are needed to reproduce the proof-critical computation.

As an independent approximate normalization check, standard three-dimensional convex-hull arithmetic gives \(\operatorname{vol}_3(P)\approx32.90777383379\), and hence the extremal volume fraction is about \(0.146313199623\). These floating-point figures are **not** used to prove the theorem.

## Relationship to prior work

The snub cube, also called the snub cuboctahedron or *cubus simus*, has classical geometry and \(24\)-vertex rotational octahedral symmetry. Longuet-Higgins studies its role in the Tammes spherical-cap problem, including its geometry and symmetry, but does not optimize volumes of tetrahedra contained in the polyhedron. Horváth and Lángi study maximal-volume polytopes with a prescribed number of vertices *on a sphere*, rather than the largest tetrahedron *inside a fixed snub cube*. Standard geometric reference tables give the snub cube's own metric data, such as edge length, circumradius and total volume, not the four-point extremal tetrahedron determinant or its equality locus. The distinction persists even under the larger bounding-sphere simplex inequality: a bound sharp for a regular tetrahedron on a sphere does not determine which four vertices of this particular snub cube attain equality.

A reported homotopy calculation for the independence complex of the snub cubical graph concerns combinatorics, which is unchanged under metric deformations, and therefore cannot determine tetrahedral Euclidean volumes. The exact determinant maximum and classification into eight triangular-face families are not obtained from those source statements. The value lies in an exact natural extremal invariant of a canonical chiral Archimedean solid and a complete classification of a positive-dimensional equality locus; it is not a table recomputation of the volume of the containing solid.

## Limitations

The result concerns one of the two mirror-equivalent snub cubes at the indicated scale, not an arbitrary deformation or a general class of Archimedean solids. It uses an exhaustive \(10626\)-case exact algebraic certificate for the vertex step, rather than a short synthetic inequality; the mathematical deduction from that finite computation to *all* points of \(P\) is independent of discretization. It does not describe near-extremizers or quantitative stability. Literature searching cannot eliminate the possibility of a previously unindexed computation or an inaccessible historical treatment of the same precise invariant. Independent audit has not been performed.

## References

1. M. S. Longuet-Higgins, “Snub polyhedra and organic growth,” *Proceedings of the Royal Society A* **465** (2009), 477–491, published online 30 October 2008, DOI: 10.1098/rspa.2008.0219. Full article available at https://www.researchgate.net/publication/252528216_Snub_polyhedra_and_organic_growth .
2. Á. G. Horváth and Z. Lángi, “Maximum volume polytopes inscribed in the unit sphere,” arXiv:1402.6496 (first posted 26 February 2014), https://arxiv.org/abs/1402.6496 .
3. E. W. Weisstein, “Snub Cube,” *MathWorld—A Wolfram Web Resource*, https://mathworld.wolfram.com/SnubCube.html .
4. D. McCooey, “Laevo Snub Cube,” *Visual Polyhedra*, https://dmccooey.com/polyhedra/LsnubCube.html .
