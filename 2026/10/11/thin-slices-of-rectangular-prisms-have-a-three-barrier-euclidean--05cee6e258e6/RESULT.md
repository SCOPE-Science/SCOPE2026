# Thin slices of rectangular prisms have a three-barrier Euclidean inradius
## Finding
Let
\[
n\ge3,
\qquad
\mathbf c=(c_1,\ldots,c_n)\in\mathbb Z_{>0}^n,
\]
put
\[
C=\sum_{i=1}^n c_i,
\]
and let
\[
0<k<C
\]
be an integer. Consider the thin rectangular-prism slice
\[
R_{k,\mathbf c}
=
\left\{
x\in\mathbb R^n:
0\le x_i\le c_i\ (1\le i\le n),\quad
\sum_{i=1}^n x_i=k
\right\}.
\tag{1}
\]
This is the source family of slices of prisms, also identified there with base polytopes of discrete polymatroids of Veronese type.

Write
\[
c_{\min}=\min_{1\le i\le n}c_i
\tag{2}
\]
and define the coordinate-clearance threshold
\[
\boxed{
\delta_*
=
\min\left\{
\frac{k}{n},
\frac{C-k}{n},
\frac{c_{\min}}2
\right\}.
}
\tag{3}
\]
Then the intrinsic Euclidean inradius of \(R_{k,\mathbf c}\), in its affine hull, is
\[
\boxed{
r_{\mathrm{in}}(R_{k,\mathbf c})
=
\sqrt{\frac{n}{n-1}}\,
\delta_*.
}
\tag{4}
\]

The formula has exactly three geometric barriers:
\[
\frac{k}{n},
\qquad
\frac{C-k}{n},
\qquad
\frac{c_{\min}}2.
\tag{5}
\]
They correspond respectively to the lower coordinate facets, the upper coordinate facets, and a narrowest pair of opposite coordinate facets.

There is also a complete description of every incenter. Put
\[
L=\{i:k<C-c_i\},
\qquad
U=\{i:k>c_i\}.
\tag{6}
\]
Then
\[
\boxed{
\operatorname{Cent}(R_{k,\mathbf c})
=
\left\{
x\in R_{k,\mathbf c}:
x_i\ge\delta_*\ (i\in L),\quad
x_i\le c_i-\delta_*\ (i\in U)
\right\}.
}
\tag{7}
\]

If
\[
\frac{k}{n}
<
\min\left\{
\frac{C-k}{n},
\frac{c_{\min}}2
\right\},
\tag{8}
\]
then the incenter is unique and equals
\[
\boxed{
\frac{k}{n}\mathbf1.
}
\tag{9}
\]
Dually, if
\[
\frac{C-k}{n}
<
\min\left\{
\frac{k}{n},
\frac{c_{\min}}2
\right\},
\tag{10}
\]
then the incenter is unique and equals
\[
\boxed{
\mathbf c-\frac{C-k}{n}\mathbf1.
}
\tag{11}
\]

For the ordinary hypersimplex, where every
\[
c_i=1,
\]
formula (4) specializes to
\[
r_{\mathrm{in}}(\Delta_{k,n})
=
\sqrt{\frac{n}{n-1}}
\min\left\{
\frac{k}{n},
\frac{n-k}{n},
\frac12
\right\}.
\tag{12}
\]
The result therefore extends the standard equal-capacity slice to arbitrary rectangular capacities.

## Assumptions and scope
The metric is the standard Euclidean metric inherited from \(\mathbb R^n\).

Because
\[
0<k<C,
\]
the source proves that \(R_{k,\mathbf c}\) has dimension
\[
n-1.
\]
Its affine hull is
\[
H_k
=
\left\{
x:\sum_i x_i=k
\right\}.
\tag{13}
\]

The restriction
\[
n\ge3
\]
is used so that facets have positive dimension and the coordinate-facet classification in (6) has the stated strict inequalities. One-dimensional slices at \(n=2\) can be handled separately as line segments.

The theorem concerns the thin slices (1). It does not assert the same formula for the source's full-dimensional fat slices, which are only integrally equivalent to thin slices and need not be Euclidean-isometric.

## Proof
The translation space of \(H_k\) is
\[
H_0
=
\left\{
u:\sum_i u_i=0
\right\}.
\tag{14}
\]
The ambient normal of a coordinate hyperplane
\[
x_i=\text{constant}
\]
is \(e_i\). Its orthogonal projection to \(H_0\) is
\[
e_i-\frac1n\mathbf1,
\]
whose squared norm is
\[
1-\frac1n
=
\frac{n-1}{n}.
\tag{15}
\]
Therefore an intrinsic Euclidean distance \(r\) from a coordinate facet corresponds to coordinate clearance
\[
\delta
=
r\sqrt{\frac{n-1}{n}}.
\tag{16}
\]

We next identify the actual facets.

The lower face
\[
x_i=0
\]
is a facet exactly when the remaining coordinates admit a relative-interior point with sum \(k\), equivalently
\[
0<k<C-c_i.
\]
Since \(k>0\), this is exactly
\[
i\in L.
\tag{17}
\]

Likewise the upper face
\[
x_i=c_i
\]
is a facet exactly when the remaining coordinates admit a relative-interior point with sum
\[
k-c_i,
\]
equivalently
\[
0<k-c_i<C-c_i.
\]
Since \(k<C\), this is exactly
\[
i\in U.
\tag{18}
\]

We now prove the upper bound in (3)--(4).

Suppose first that
\[
\frac{k}{n}
\le
\min\left\{
\frac{C-k}{n},
\frac{c_{\min}}2
\right\}.
\tag{19}
\]
Then every lower coordinate inequality is facet-defining. Indeed, if some \(i\notin L\), then
\[
k\ge C-c_i=\sum_{j\ne i}c_j.
\]
But (19) gives
\[
c_j\ge\frac{2k}{n}
\]
for every \(j\), so
\[
\sum_{j\ne i}c_j
\ge
\frac{2k(n-1)}n
>
k
\]
because \(n\ge3\), a contradiction.

Thus a radius-\(r\) inscribed ball has
\[
x_i\ge\delta
\]
for every \(i\), where \(\delta\) is defined by (16). Summing gives
\[
n\delta\le k,
\]
hence
\[
\delta\le\frac{k}{n}.
\tag{20}
\]

By applying the same argument to the complementary coordinates
\[
y_i=c_i-x_i,
\qquad
\sum_i y_i=C-k,
\]
we obtain
\[
\delta\le\frac{C-k}{n}
\tag{21}
\]
whenever the second barrier is minimal.

Finally, suppose
\[
\frac{c_{\min}}2
\le
\min\left\{
\frac{k}{n},
\frac{C-k}{n}
\right\}.
\tag{22}
\]
Choose \(i\) with
\[
c_i=c_{\min}.
\]
Since \(n\ge3\), (22) gives
\[
k\ge\frac{nc_{\min}}2>c_{\min}
\]
and
\[
C-k\ge\frac{nc_{\min}}2>c_{\min}.
\]
Hence both
\[
x_i=0
\quad\text{and}\quad
x_i=c_i
\]
are facets. Their coordinate separation is \(c_{\min}\), so a ball with coordinate clearance \(\delta\) from both must satisfy
\[
2\delta\le c_{\min}.
\tag{23}
\]

Equations (20)--(23) prove
\[
\delta\le\delta_*.
\tag{24}
\]

It remains to prove that \(\delta_*\) is feasible.

By definition,
\[
n\delta_*\le k,
\qquad
n\delta_*\le C-k,
\qquad
2\delta_*\le c_i
\quad
\text{for every }i.
\tag{25}
\]
Thus the intervals
\[
[\delta_*,c_i-\delta_*]
\]
are nonempty, and their lower endpoints have total at most \(k\), while their upper endpoints have total at least \(k\):
\[
\sum_i\delta_*
\le k
\le
\sum_i(c_i-\delta_*).
\tag{26}
\]
The elementary interval-sum criterion therefore gives a point \(x\) with
\[
x_i\in[\delta_*,c_i-\delta_*]
\]
and
\[
\sum_i x_i=k.
\tag{27}
\]
Such a point has coordinate clearance at least \(\delta_*\) from every coordinate hyperplane, and hence in particular from every actual facet. By (15)--(16), the intrinsic ball of radius
\[
\sqrt{\frac{n}{n-1}}\delta_*
\]
centered at \(x\) lies in \(R_{k,\mathbf c}\). Combined with (24), this proves (4).

For the incenter set, a point \(x\in R_{k,\mathbf c}\) supports an optimal-radius ball exactly when its normalized clearance from every actual facet is at least the optimum. By (15), these conditions are precisely
\[
x_i\ge\delta_*
\quad(i\in L)
\]
and
\[
x_i\le c_i-\delta_*
\quad(i\in U),
\]
which proves (7).

Under the strict inequality (8), all lower facets occur and
\[
\delta_*=\frac{k}{n}.
\]
Every incenter therefore has
\[
x_i\ge\frac{k}{n}
\]
for all \(i\), while the coordinates sum to \(k\). Equality is forced coordinatewise, proving (9). The proof of (11) is the complementary argument.

## Verification
The proof is symbolic for every parameter choice in the stated domain.

The source-dependent premises were checked directly in the primary full text: the definition of \(R_{k,\mathbf c}\), its dimension for \(0<k<C\), its interpretation as a hyperplane slice of a rectangular prism, and its equivalence with base polytopes of discrete polymatroids of Veronese type.

The accompanying `verify.py` performs an independent active-set replay on deterministic capacity vectors in dimensions three and four. It constructs the true coordinate facets using (17)--(18), formulates the Chebyshev linear program in the coordinate-clearance variable \(\delta\), enumerates candidate LP vertices by Gaussian elimination, and checks that the optimum equals (3). It also checks that the stated incenter inequalities are exactly the normalized actual-facet constraints. These finite computations are corroborative only.

## Relationship to prior work
Ferroni and McGinnis systematically study the Ehrhart theory of the slices \(R_{k,\mathbf c}\). Their paper proves Ehrhart positivity, gives coefficient and volume formulas, relates the family to polypositroids, and identifies these slices with base polytopes of discrete polymatroids of Veronese type.

The inspected full text contains no occurrence of “inradius”, “Chebyshev”, “Euclidean”, or “inscribed” in the metric sense used here. The paper's focus is lattice-point enumeration, volumes, \(h^*\)-polynomials, weighted permutations, and Hilbert functions.

The equal-capacity specialization
\[
\mathbf c=\mathbf1
\]
is the ordinary hypersimplex. Metric results for that symmetric specialization do not determine the arbitrary-capacity family, where coordinate facets can disappear and the narrowest-capacity barrier can dominate independently of the two total-mass barriers.

The result is also distinct from full-dimensional slab intersections of a cube: \(R_{k,\mathbf c}\) is intrinsically \((n-1)\)-dimensional, and the Euclidean normalization of each coordinate normal is
\[
\sqrt{\frac{n-1}{n}}.
\]
This projected-normal factor is essential in (4).

Targeted searches under “slice of a rectangular prism”, “polymatroid of Veronese type”, “box slice”, “inradius”, “Chebyshev center”, and “largest inscribed ball” did not locate a theorem implying (3)--(7).

## Limitations
The theorem is realization-sensitive and concerns the standard rectangular-prism coordinates.

It covers thin slices with
\[
n\ge3
\]
and does not claim the same Euclidean formula for the source's integrally equivalent fat slices.

The result determines the inradius and every incenter, but not the minimum enclosing sphere, John ellipsoid, or other extremal bodies.

The formula is elementary once the intrinsic facet normals and facet-disappearance thresholds are organized. Its mathematical content is the exact all-capacity three-barrier collapse and the complete center classification for the natural polymatroid family.

A broader theorem for Chebyshev centers of affine box sections could subsume the calculation under different terminology; no such dominating statement was located in the targeted comparisons.

## References
1. Luis Ferroni and Daniel McGinnis, *Lattice points in slices of prisms*, arXiv:2202.11808, first public version 2022-02-23; *Canadian Journal of Mathematics* 77 (2025), 1013--1040, DOI 10.4153/S0008414X24000233.
