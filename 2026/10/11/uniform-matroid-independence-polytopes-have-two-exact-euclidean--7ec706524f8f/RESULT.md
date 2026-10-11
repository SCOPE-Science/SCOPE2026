# Uniform-matroid independence polytopes have two exact Euclidean radius transitions
## Finding
Let
\[
1\le r<n,
\]
and let
\[
I_{r,n}
=
\mathscr P_I(U_{r,n})
=
\left\{
x\in[0,1]^n:
\sum_{i=1}^n x_i\le r
\right\}
\tag{1}
\]
be the independence polytope of the uniform matroid \(U_{r,n}\).

The standard Euclidean inradius has a sharp saturation transition.

If
\[
2r\le n+\sqrt n,
\]
then the unique incenter is
\[
\boxed{
c_{\mathrm{in}}
=
\frac{r}{n+\sqrt n}\mathbf1
}
\tag{2}
\]
and
\[
\boxed{
r_{\mathrm{in}}(I_{r,n})
=
\frac{r}{n+\sqrt n}.
}
\tag{3}
\]
The inball is tangent to the \(n\) lower coordinate facets
\[
x_i=0
\]
and to the rank facet
\[
\sum_{i=1}^n x_i=r.
\]
When
\[
2r<n+\sqrt n,
\]
no upper coordinate facet is tangent.

If
\[
2r\ge n+\sqrt n,
\]
then
\[
\boxed{
c_{\mathrm{in}}
=
\frac12\mathbf1,
\qquad
r_{\mathrm{in}}(I_{r,n})
=
\frac12.
}
\tag{4}
\]
In the strict regime
\[
2r>n+\sqrt n,
\]
the tangent facets are exactly the \(2n\) coordinate facets
\[
x_i=0,
\qquad
x_i=1,
\]
and the rank facet is not tangent. At equality, all \(2n+1\) facets are tangent.

The minimum enclosing Euclidean ball has a different transition.

If
\[
2r<n,
\]
then its unique center is
\[
\boxed{
c_{\mathrm{out}}
=
\frac rn\mathbf1
}
\tag{5}
\]
and
\[
\boxed{
R_{\mathrm{out}}(I_{r,n})^2
=
\frac{r(n-r)}n.
}
\tag{6}
\]
The contact vertices are exactly the
\[
\binom nr
\]
basis indicators of cardinality \(r\).

If
\[
2r\ge n,
\]
then
\[
\boxed{
c_{\mathrm{out}}
=
\frac12\mathbf1,
\qquad
R_{\mathrm{out}}(I_{r,n})^2
=
\frac n4.
}
\tag{7}
\]
Every vertex of \(I_{r,n}\) is then a contact point.

Hence the inner and outer Euclidean geometry saturate at two genuinely different rank thresholds:
\[
2r=n
\qquad\text{and}\qquad
2r=n+\sqrt n.
\tag{8}
\]

## Assumptions and scope
The realization in (1) is the standard indicator-vector realization.

Ferroni and McGinnis explicitly identify the uniform-matroid independence polytope as
\[
\left\{
x\in[0,1]^n:
\sum_i x_i\le r
\right\}
\]
in their treatment of lattice points in slices of prisms. Their paper has primary MSC \(52B20\).

The vertices are exactly the indicator vectors of the independent sets of \(U_{r,n}\), namely all subsets of \([n]\) of cardinality at most \(r\).

For
\[
r=1,
\]
the inequalities \(x_i\le1\) are redundant as facets, and \(I_{1,n}\) is the standard simplex. For
\[
r\ge2,
\]
each upper coordinate hyperplane \(x_i=1\) supports a facet.

The result concerns the ordinary Euclidean metric of \(\mathbb R^n\), not lattice width, Ehrhart geometry, or affine-invariant ellipsoids.

## Proof
We begin with the inball.

Every point
\[
c=(c_1,\ldots,c_n)
\]
that is the center of an inscribed ball of radius \(\rho\) must have Euclidean clearance at least \(\rho\) from every lower coordinate facet. Therefore
\[
c_i\ge\rho
\qquad
(1\le i\le n).
\tag{9}
\]
The rank facet has unit normal
\[
\frac1{\sqrt n}\mathbf1,
\]
so its clearance condition is
\[
\frac{r-\sum_i c_i}{\sqrt n}\ge\rho.
\tag{10}
\]
Combining (9) and (10) gives
\[
r
\ge
\sum_i c_i+\rho\sqrt n
\ge
\rho(n+\sqrt n).
\]
Hence every inscribed ball satisfies
\[
\rho
\le
\frac{r}{n+\sqrt n}.
\tag{11}
\]

When
\[
2r\le n+\sqrt n,
\]
put
\[
a=\frac{r}{n+\sqrt n}.
\]
Then
\[
a\le\frac12.
\]
At
\[
c=a\mathbf1,
\]
the distance to every lower coordinate facet is \(a\), while the distance to the rank facet is
\[
\frac{r-na}{\sqrt n}
=
a.
\]
For \(r\ge2\), the upper coordinate facets have distance
\[
1-a\ge a.
\]
Thus (11) is attained.

Equality in (11) forces equality throughout its derivation, so
\[
c_i=\rho
\]
for every coordinate and the rank clearance is also tight. Therefore the incenter in this regime is unique.

Now suppose
\[
2r\ge n+\sqrt n.
\]
This regime has
\[
r\ge2.
\]
The two opposite coordinate facets
\[
x_i=0
\qquad\text{and}\qquad
x_i=1
\]
show for every center \(c\) that
\[
\rho\le\min\{c_i,1-c_i\}\le\frac12.
\tag{12}
\]
At
\[
c=\frac12\mathbf1,
\]
all coordinate facets are at distance \(1/2\), and the rank-facet distance is
\[
\frac{r-n/2}{\sqrt n}
\ge
\frac12.
\]
Hence the radius \(1/2\) is attained.

Equality in (12) for radius \(1/2\) forces
\[
c_i=\frac12
\]
for every \(i\), so the incenter is again unique.

The tangency statements follow immediately from the three exact clearances
\[
c_i,
\qquad
1-c_i,
\qquad
\frac{r-\sum_i c_i}{\sqrt n}.
\]

We now turn to the minimum enclosing ball.

A compact set has a unique minimum-enclosing-ball center. The full symmetric group \(S_n\) acts isometrically on \(I_{r,n}\) by coordinate permutations. By uniqueness, the minimum-enclosing center is fixed by this action, so it has the form
\[
c=t\mathbf1.
\tag{13}
\]

A vertex of cardinality \(k\), with
\[
0\le k\le r,
\]
has squared distance
\[
\begin{aligned}
d_k(t)^2
&=
k(1-t)^2+(n-k)t^2\\
&=
nt^2+k(1-2t).
\end{aligned}
\tag{14}
\]
For fixed \(t\), the expression is affine in \(k\).

If
\[
t\le\frac12,
\]
the largest vertex distance occurs at
\[
k=r,
\]
and the relevant function is
\[
nt^2+r(1-2t).
\]
Its unconstrained minimum occurs at
\[
t=\frac rn.
\]
When
\[
2r<n,
\]
this lies strictly below \(1/2\), giving
\[
R_{\mathrm{out}}^2
=
n\left(\frac rn\right)^2
+
r\left(1-\frac{2r}{n}\right)
=
\frac{r(n-r)}n.
\]
Because the coefficient
\[
1-\frac{2r}{n}
\]
is positive, equality in the vertex-distance maximum occurs exactly on the cardinality-\(r\) layer.

If
\[
2r\ge n,
\]
the unconstrained minimum \(r/n\) lies at or above \(1/2\). On the region
\[
t\le\frac12,
\]
the best value is therefore attained at \(t=1/2\).

For
\[
t\ge\frac12,
\]
the affine coefficient in (14) is nonpositive, so the farthest layer is \(k=0\), with squared distance
\[
nt^2.
\]
This is also minimized at the boundary
\[
t=\frac12.
\]
Thus
\[
c_{\mathrm{out}}
=
\frac12\mathbf1,
\qquad
R_{\mathrm{out}}^2
=
\frac n4.
\]
At this center the coefficient of \(k\) in (14) vanishes, so every vertex has exactly the same distance.

This proves all claims.

## Verification
The proof is exact for every
\[
1\le r<n.
\]

The primary full text was inspected at its statement of the uniform-matroid independence polytope and at the surrounding prism-slice framework. The paper gives the realization (1), its role in Ehrhart theory, and primary MSC \(52B20\). Targeted full-text searches found no inradius, circumradius, Chebyshev-center, minimum-enclosing-ball, or Euclidean-radius theorem.

Ferroni's earlier paper on the same independence polytopes was also inspected. It defines matroid independence polytopes as convex hulls of indicator vectors of independent sets, records the \(0/1\)-vertex structure, and treats the uniform family through half-open hypersimplex tilings. Targeted full-text searches again found no Euclidean-radius statement.

The accompanying `verify.py` checks all parameter pairs
\[
2\le n\le40,
\qquad
1\le r<n.
\]
It solves the complete inradius linear program from every genuine facet, verifies the closed centers and tangency phases, evaluates every vertex layer for the outer sphere, and independently minimizes the exact one-variable maximum-distance function. The finite replay is corroborative only.

## Relationship to prior work
Ferroni and McGinnis study these polytopes as a canonical application of their prism-slice Ehrhart theory. Their main invariants are Ehrhart coefficients, \(h^*\)-data, normalized volumes, and weighted-permutation enumerators.

Ferroni's earlier same-object paper studies Ehrhart positivity and half-open hypersimplex tilings.

Neither inspected source develops the Euclidean inball or minimum-enclosing-ball geometry.

The metric statement is also not a restatement of the hypersimplex geometry. The independence polytope contains every cardinality layer from \(0\) through \(r\), and the outer transition at \(2r=n\) is caused by competition between the top layer and the origin. The inball transition occurs later, at \(2r=n+\sqrt n\), because it is controlled instead by competition between the rank facet and opposite coordinate facets.

The separation of these two thresholds is the structural feature of the result.

## Limitations
The theorem concerns uniform matroids and the standard indicator-vector realization.

No analogous formula is claimed for arbitrary matroid independence polytopes, where coordinate symmetry can disappear and rank inequalities for many subsets can become active.

The result determines Euclidean inradius, incenter, minimum-enclosing radius, center, and contact phases, but not John or Löwner ellipsoids, lattice covering radius, or intrinsic volume data.

The formulas become elementary after the full \(S_n\)-symmetry and facet structure are recognized, so independent rediscovery under truncated-cube terminology remains a residual originality risk.

## References
1. Luis Ferroni and Daniel McGinnis, *Lattice points in slices of prisms*, arXiv:2202.11808, first public version 2022-02-23; *Canadian Journal of Mathematics* 77 (2025), 1013--1040, DOI 10.4153/S0008414X24000233.
2. Luis Ferroni, *Integer point enumeration on independence polytopes and half-open hypersimplices*, arXiv:2012.04711, first public version 2020-12-08; *Discrete Mathematics* 344 (2021), 112446, DOI 10.1016/j.disc.2021.112446.
