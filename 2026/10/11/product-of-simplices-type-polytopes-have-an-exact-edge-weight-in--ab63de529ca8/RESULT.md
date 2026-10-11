# Product-of-simplices type polytopes have an exact edge-weight inball
## Finding
Let
\[
k\ge2,
\qquad
d_1,\ldots,d_k\ge1,
\]
and let
\[
P
=
\Delta_{d_1}\times\cdots\times\Delta_{d_k}
\tag{1}
\]
be the standard product of simplices.

Write
\[
D=\sum_{i=1}^k d_i,
\qquad
V=\prod_{i=1}^k(d_i+1),
\tag{2}
\]
and
\[
S
=
\sum_{i=1}^k
\sqrt{d_i(D-d_i)}.
\tag{3}
\]

The normalized type polytope in edge-Minkowski-weight coordinates is
\[
\mathbb{TP}(P)
=
\left\{
\omega:
\omega\text{ is a nonnegative one-Minkowski weight and }
\sum_{E\in\mathcal F_1(P)}\omega(E)=f_1(P)
\right\}.
\tag{4}
\]

For the standard product (1), every Minkowski weight is constant on all edges varying in one simplex factor. Let that common value be
\[
\lambda_i
\]
for factor \(i\). Then
\[
\boxed{
\mathbb{TP}(P)
=
\left\{
\lambda_i\ge0:
\sum_{i=1}^k d_i\lambda_i=D
\right\},
}
\tag{5}
\]
where the Euclidean metric is inherited from the full edge-coordinate space
\[
\mathbb R^{f_1(P)}.
\]

The number of edge coordinates belonging to factor \(i\) is
\[
\boxed{
E_i=\frac{Vd_i}{2}.
}
\tag{6}
\]

The unique Euclidean incenter has factor weights
\[
\boxed{
\lambda_i^*
=
\frac{D}{S}
\sqrt{\frac{D-d_i}{d_i}}
\qquad
(1\le i\le k),
}
\tag{7}
\]
and the exact intrinsic inradius is
\[
\boxed{
r_{\mathrm{in}}\bigl(\mathbb{TP}(P)\bigr)
=
\frac{D^{3/2}\sqrt{V/2}}{S}.
}
\tag{8}
\]
Every one of the \(k\) facets is tangent to this inball.

The \(k\) vertices are the pure-factor weights
\[
\lambda_i=\frac D{d_i},
\qquad
\lambda_j=0
\quad
(j\ne i).
\tag{9}
\]
For distinct factors \(i,j\),
\[
\boxed{
\|v_i-v_j\|^2
=
\frac{VD^2}{2}
\left(
\frac1{d_i}+\frac1{d_j}
\right).
}
\tag{10}
\]

For
\[
k=2,
\]
the type polytope is a segment and is therefore Euclidean-regular. For
\[
k\ge3,
\]
\[
\boxed{
\mathbb{TP}(P)\text{ is Euclidean-regular if and only if }
d_1=\cdots=d_k.
}
\tag{11}
\]

For the standard \(d\)-cube,
\[
P=[0,1]^d
=
\Delta_1^{\,d},
\]
the unique incenter is the all-ones edge weight and
\[
\boxed{
r_{\mathrm{in}}\bigl(\mathbb{TP}([0,1]^d)\bigr)
=
2^{(d-1)/2}
\sqrt{\frac d{d-1}}.
}
\tag{12}
\]

## Assumptions and scope
The type polytope and its normalization are exactly those of the primary source. A coordinate of the ambient space is one edge of \(P\), and the metric in this result is the standard Euclidean metric in those edge-weight coordinates.

The theorem concerns the standard Cartesian product of standard simplices. The primary source proves that every realization combinatorially isomorphic to a product of simplices has a simplicial type cone, but the metric formula here is realization-sensitive because the edge-coordinate embedding and its balancing relations depend on the chosen realization.

The restriction
\[
k\ge2
\]
avoids the zero-dimensional type polytope of a single simplex.

## Proof
Every edge of the product \(P\) varies in exactly one factor. Let
\[
\mathcal E_i
\]
be the edges varying in factor \(i\).

We first determine the Minkowski weights.

A triangular two-face inside one simplex factor has three edge vectors summing to zero. The balancing equation therefore forces the three corresponding edge weights to be equal. A square two-face involving factors \(i\) and \(j\) has two pairs of parallel opposite edges; its balancing equation forces the two \(i\)-edges to have equal weights and the two \(j\)-edges to have equal weights.

Using the connectedness of simplex edge graphs and square faces that move between choices of the other factor vertices, every edge in
\[
\mathcal E_i
\]
has one common weight
\[
\lambda_i.
\]
This also covers segment factors, where square faces provide the propagation.

There are
\[
\binom{d_i+1}{2}
\prod_{j\ne i}(d_j+1)
=
\frac{Vd_i}{2}
\tag{13}
\]
edges in \(\mathcal E_i\). Thus
\[
f_1(P)
=
\sum_i E_i
=
\frac{VD}{2}.
\tag{14}
\]
The normalization in (4) becomes
\[
\sum_i E_i\lambda_i
=
\frac{VD}{2},
\]
which is equivalent to (5).

Now pass to Euclidean coordinates
\[
y_i=\sqrt{E_i}\lambda_i.
\tag{15}
\]
Because the edge classes have disjoint coordinate supports, this is an isometry from the class-constant weight subspace to ordinary
\[
\mathbb R^k.
\]
Equation (5) becomes
\[
y_i\ge0,
\qquad
\sum_{i=1}^k\sqrt{d_i}\,y_i
=
D\sqrt{\frac V2}.
\tag{16}
\]

Let
\[
a=(\sqrt{d_1},\ldots,\sqrt{d_k}).
\]
Then
\[
\|a\|^2=D.
\tag{17}
\]
The tangent space of the affine hull in (16) is
\[
a^\perp.
\]

The facet opposite the \(i\)-th vertex is
\[
y_i=0.
\]
The norm of the gradient of \(y_i\) after restriction to \(a^\perp\) is
\[
\left\|
e_i-\frac{\sqrt{d_i}}D a
\right\|
=
\sqrt{1-\frac{d_i}{D}}
=
\sqrt{\frac{D-d_i}{D}}.
\tag{18}
\]
Hence the intrinsic distance from a point \(y\) to the \(i\)-th facet is
\[
\delta_i(y)
=
y_i
\sqrt{\frac D{D-d_i}}.
\tag{19}
\]

At the incenter all \(k\) facet distances are equal, so
\[
y_i
=
r
\sqrt{\frac{D-d_i}{D}}.
\tag{20}
\]
Substituting (20) into (16) gives
\[
r
\frac1{\sqrt D}
\sum_i\sqrt{d_i(D-d_i)}
=
D\sqrt{\frac V2}.
\]
This yields (8).

Dividing (20) by
\[
\sqrt{E_i}
=
\sqrt{\frac{Vd_i}{2}}
\]
and substituting (8) gives (7). A nondegenerate Euclidean simplex has a unique incenter, so uniqueness and all-facet tangency follow.

The vertices of (5) are obtained by making one coordinate nonzero:
\[
\lambda_i=\frac D{d_i}.
\]
The edge-coordinate supports of two such vertices are disjoint. Therefore
\[
\begin{aligned}
\|v_i-v_j\|^2
&=
E_i\left(\frac D{d_i}\right)^2
+
E_j\left(\frac D{d_j}\right)^2\\
&=
\frac{VD^2}{2}
\left(
\frac1{d_i}+\frac1{d_j}
\right),
\end{aligned}
\]
which is (10).

For
\[
k=2,
\]
there is only one edge between the two vertices, so the one-dimensional type simplex is regular.

Now suppose
\[
k\ge3.
\]
If all \(d_i\) are equal, (10) makes all pairwise vertex distances equal, so the simplex is regular.

Conversely, suppose all pairwise distances are equal. Choose three distinct indices \(i,j,\ell\). Comparing the distances from \(v_i\) to \(v_j\) and \(v_\ell\) in (10) gives
\[
\frac1{d_j}=\frac1{d_\ell}.
\]
Varying the triple shows that all factor dimensions agree. This proves (11).

For a \(d\)-cube, take
\[
k=d,
\qquad
d_i=1.
\]
Then
\[
V=2^d,
\qquad
D=d,
\qquad
S=d\sqrt{d-1}.
\]
Equation (7) gives
\[
\lambda_i^*=1
\]
for every direction class, and (8) simplifies to (12).

## Verification
The proof is symbolic for every
\[
k\ge2
\]
and every positive factor-dimension vector.

The primary full text was inspected at the definition of one-Minkowski weights, the type-cone and type-polytope normalization, the standard-cube example, and the theorem proving that products of simplices have simplex type polytopes.

The accompanying `verify.py` independently constructs the reduced edge-coordinate simplex for deterministic dimension vectors. It computes the orthogonal projection needed for every intrinsic facet distance, checks the closed incenter and inradius formulas, compares all vertex distances with (10), checks the regularity criterion in dimensions at least two, and independently solves the max-min facet-distance problem by linear programming. The finite replay is corroborative only.

## Relationship to prior work
Castillo, Doolittle, Goeckner, Ross, and Ying prove that the type polytope of every realization combinatorially equivalent to a product of simplices is a simplex. For the regular cube, they also state that the balancing equations make all parallel edges share one weight.

Their result is combinatorial and deformation-theoretic: it identifies the type cone and its face structure. The inspected full text does not state an intrinsic Euclidean inradius or incenter for the normalized edge-weight type polytope.

The metric in this theorem is natural for the source's edge parametrization because every ambient coordinate is precisely one edge-deformation weight. The incenter therefore maximizes the smallest Euclidean clearance from every vanishing-factor boundary of the normalized deformation parameter space.

Targeted searches under “type polytope”, “type cone”, “product of simplices”, “Minkowski weights”, “edge deformation space”, “inradius”, and “incenter” did not locate a statement implying (7)--(12).

## Limitations
The Euclidean formulas are for the source's normalized edge-weight embedding of the standard product of standard simplices.

A different realization of the same product-of-simplices combinatorial type still has a simplex type polytope by the primary theorem, but need not have the metric in (6)--(12).

The theorem does not compute the minimum enclosing ball, volume, or John ellipsoid of the type polytope.

The incenter calculation becomes elementary after the balancing equations have collapsed the full edge-coordinate system to factor classes. This makes independent rediscovery possible and is retained as an originality risk.

## References
1. Federico Castillo, Joseph Doolittle, Bennet Goeckner, Michael S. Ross, and Li Ying, *Minkowski summands of cubes*, arXiv:2009.07252, first public version 2020-09-15; *Bulletin of the London Mathematical Society* 54 (2022), DOI 10.1112/blms.12610.
2. Peter McMullen, *Weights on polytopes*, *Discrete & Computational Geometry* 15 (1996), 363--388.
3. Alex Postnikov, Victor Reiner, and Lauren Williams, *Faces of generalized permutohedra*, *Documenta Mathematica* 13 (2008), 207--273.
