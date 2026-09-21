# Exact Jung-defect decomposition for minimum enclosing-ball certificates

## Result

Let \(K\subset\mathbb R^n\), \(n\ge 2\), be compact with positive diameter
\[
D=\operatorname{diam}K,
\]
and let \(B(c,R)\) be its minimum enclosing Euclidean ball. Choose an
inclusion-minimal set of contact points
\[
x_1,\ldots,x_m\in K\cap \partial B(c,R)
\]
such that \(c\in\operatorname{conv}\{x_1,\ldots,x_m\}\). Then
\(2\le m\le n+1\), the contact points are affinely independent, and there
are unique weights
\[
\lambda_i>0,\qquad \sum_{i=1}^m\lambda_i=1,\qquad
\sum_{i=1}^m\lambda_i(x_i-c)=0.
\]
Write \(d_{ij}=\|x_i-x_j\|\), and define the squared Jung deficit
\[
\Delta_J=\frac{n}{2(n+1)}D^2-R^2.
\]

Then the deficit has the exact decomposition
\[
\boxed{
\Delta_J=
\frac{D^2}2\left(\frac1m-\frac1{n+1}\right)
+\frac{D^2}2\sum_{i=1}^m\left(\lambda_i-\frac1m\right)^2
+\sum_{1\le i<j\le m}\lambda_i\lambda_j(D^2-d_{ij}^2).
}
\tag{1}
\]

Thus every part of the Jung deficit is resolved into three
nonnegative effects:

1. too few active contact points;
2. nonuniform barycentric weights;
3. active edges shorter than the global diameter.

In particular, (1) recovers Jung's inequality and makes its equality case
transparent: \(\Delta_J=0\) forces \(m=n+1\), all
\(\lambda_i=1/(n+1)\), and all \(d_{ij}=D\), so the active contacts are
the vertices of a regular \(n\)-simplex.

## Why the contact certificate exists

For the convex function
\[
F(y)=\max_{x\in K}\|x-y\|^2,
\]
the minimum is attained at the minimum-enclosing-ball center \(c\).
The active set is \(C=K\cap\partial B(c,R)\). The standard
subgradient optimality condition gives
\[
0\in\operatorname{conv}\{2(c-x):x\in C\},
\]
hence \(c\in\operatorname{conv}C\). Carathéodory's theorem gives a
contact certificate with at most \(n+1\) points. Making it
inclusion-minimal makes all barycentric coefficients positive and the
points affinely independent, hence the coefficients are unique.

For finite point sets this is the familiar support-set characterization
of the smallest enclosing ball: a boundary set \(T\) determines its
smallest enclosing ball exactly when the center belongs to
\(\operatorname{conv}T\).

## Proof of the exact decomposition

Put \(q_i=x_i-c\). Since every contact lies on the enclosing sphere,
\(\|q_i\|=R\), while the barycentric condition is
\(\sum_i\lambda_iq_i=0\). The weighted pairwise-variance identity gives
\[
\begin{aligned}
\sum_{i<j}\lambda_i\lambda_j d_{ij}^2
&=\frac12\sum_{i,j}\lambda_i\lambda_j\|q_i-q_j\|^2\\
&=\sum_i\lambda_i\|q_i\|^2
-\left\|\sum_i\lambda_iq_i\right\|^2\\
&=R^2.
\end{aligned}
\tag{2}
\]
Also
\[
\sum_{i<j}\lambda_i\lambda_j
=\frac12\left(1-\sum_i\lambda_i^2\right)
\]
and
\[
\sum_i\lambda_i^2
=\frac1m+\sum_i\left(\lambda_i-\frac1m\right)^2.
\tag{3}
\]
Using (2), add and subtract
\(D^2\sum_{i<j}\lambda_i\lambda_j\):
\[
\begin{aligned}
\Delta_J
&=\frac{n}{2(n+1)}D^2
-D^2\sum_{i<j}\lambda_i\lambda_j
+\sum_{i<j}\lambda_i\lambda_j(D^2-d_{ij}^2)\\
&=\frac{D^2}2
\left(\sum_i\lambda_i^2-\frac1{n+1}\right)
+\sum_{i<j}\lambda_i\lambda_j(D^2-d_{ij}^2).
\end{aligned}
\]
Substitution of (3) is exactly (1). Every summand is nonnegative because
\(m\le n+1\) and \(d_{ij}\le D\).

## Sharp support-cardinality thresholds

For every \(k=2,\ldots,n\), (1) implies
\[
\boxed{
\Delta_J<
\frac{D^2}2\left(\frac1k-\frac1{n+1}\right)
\quad\Longrightarrow\quad
m\ge k+1.
}
\tag{4}
\]
Equivalently,
\[
\frac{R^2}{D^2}>\frac{k-1}{2k}
\quad\Longrightarrow\quad m\ge k+1.
\tag{5}
\]

Every threshold is sharp. Embed a regular \((k-1)\)-simplex of edge
length \(D\) in \(\mathbb R^n\). Its minimum enclosing ball has
\(m=k\) active vertices and
\[
\frac{R^2}{D^2}=\frac{k-1}{2k},
\]
with equality in (4).

The last transition is especially simple:
\[
\Delta_J<\frac{D^2}{2n(n+1)}
\quad\Longrightarrow\quad m=n+1.
\tag{6}
\]
So a set sufficiently close to the ambient \(n\)-dimensional Jung
constant must have a full-dimensional active simplex in its minimum
enclosing ball.

## Quantitative near-regularity of the active simplex

Normalize
\[
\varepsilon=\frac{\Delta_J}{D^2}
<\frac1{2n(n+1)}.
\]
By (6), \(m=n+1\). Formula (1) then gives
\[
\sum_{i=1}^{n+1}
\left(\lambda_i-\frac1{n+1}\right)^2\le 2\varepsilon.
\tag{7}
\]
Because the deviations sum to zero, for each \(i\),
\[
\left|\lambda_i-\frac1{n+1}\right|
\le
\sqrt{\frac{2n}{n+1}\varepsilon}.
\tag{8}
\]
Hence
\[
\lambda_{\min}\ge
a_n(\varepsilon):=
\frac1{n+1}-
\sqrt{\frac{2n}{n+1}\varepsilon}>0.
\tag{9}
\]

The edge-defect term in (1) gives, for every \(i<j\),
\[
\boxed{
1-\frac{d_{ij}^2}{D^2}
\le
\frac{\varepsilon}{a_n(\varepsilon)^2}.
}
\tag{10}
\]
Thus near equality in Jung's inequality forces not merely the existence
of \(n+1\) active points: their barycentric weights become uniformly
close to \(1/(n+1)\), and every edge of the active simplex becomes close
to the global diameter.

A simple volume consequence makes the geometric nondegeneracy explicit.
Put
\[
\eta=\frac{\varepsilon}{a_n(\varepsilon)^2}.
\]
If \(\eta<1/(2n)\), let \(S\) be the active \(n\)-simplex and let
\(S_{\rm reg}\) be a regular \(n\)-simplex of edge \(D\). Then
\[
\frac{\operatorname{Vol}(S)}{\operatorname{Vol}(S_{\rm reg})}
\ge
\left[
(1-2n\eta)^{n-1}
\frac{n+1-2n\eta}{n+1}
\right]^{1/2}.
\tag{11}
\]
Indeed, using one vertex as origin, the edge Gram matrix of \(S\)
differs entrywise by at most \(\eta D^2\) from the regular-simplex Gram
matrix, whose eigenvalues are \(D^2/2\) with multiplicity \(n-1\) and
\(D^2(n+1)/2\) once. The operator-norm perturbation is at most
\(n\eta D^2\); Weyl's inequality followed by the determinant formula for
simplex volume gives (11). No optimality is claimed for the constant in
(11).

## A Rips--Cech interpretation

Let \(\sigma\) be a finite subset of \(\mathbb R^n\). Define its
Vietoris--Rips birth value to be
\[
D(\sigma)=\max_{x,y\in\sigma}\|x-y\|,
\]
and its Cech birth radius to be
\[
R(\sigma)=\inf_y\max_{x\in\sigma}\|x-y\|.
\]
With these conventions, Jung's theorem is the simplexwise comparison
\[
R(\sigma)\le
D(\sigma)\sqrt{\frac{n}{2(n+1)}}.
\]

The support certificate above refines this comparison at the level of an
individual simplex. If the minimum-enclosing-ball certificate of
\(\sigma\) has \(m\) vertices, then
\[
R(\sigma)\le D(\sigma)\sqrt{\frac{m-1}{2m}},
\]
and (4)--(10) show exactly how approaching the worst Euclidean
Rips--Cech ratio forces the Cech birth to be supported by a
full-dimensional, quantitatively near-regular face. The cardinality
transition values are sharp, being attained by embedded regular
lower-dimensional simplices.

This is a statement about simplex birth values and their enclosing-ball
certificates; it does not assert a new global persistence-stability
theorem.

## Relation to prior work and originality check

Jung's 1901 theorem gives the sharp Euclidean bound
\(R/D\le\sqrt{n/(2(n+1))}\), with regular simplices as extremizers.
Modern minimum-enclosing-ball work uses the standard support-set
criterion \(c\in\operatorname{conv}T\) for boundary points \(T\).
Lim and McCann give a modern variance-based proof of Jung's theorem and
characterize the equality case by the uniform measure on the vertices
of a regular simplex. These are precisely the two classical ingredients
that meet in identity (1).

Finite-cardinality Jung constants and related bounds are also well
studied, including recent Banach-space work. Accordingly, the mere bound
\(R/D\le\sqrt{(m-1)/(2m)}\) for an \(m\)-point Euclidean support is
not claimed as new. Likewise, the weighted pairwise-variance identity
used in (2) is standard.

The contribution claimed here is narrower: the exact decomposition (1)
of the *ambient Jung deficit* for a minimum-enclosing-ball contact
certificate into cardinality, weight-imbalance, and edge-shortfall
terms, together with the sharp deficit thresholds (4), explicit
near-uniformity and all-edge estimates (7)--(10), the volume consequence
(11), and the enclosing-ball interpretation for simplexwise Rips--Cech
birth values.

A literature check covering Jung inequalities and equality cases,
minimum-enclosing-ball support sets, isodiametric variance bounds,
finite Jung constants, simplex stability results, and Rips--Cech
comparisons did not locate this exact three-term decomposition or the
stated package of quantitative consequences. Schneider's 2009 stability
results concern affine/Minkowski covering inequalities and Banach--Mazur
type simplex closeness rather than this Euclidean contact-certificate
identity. The 2024 minimum-enclosing-ball survey by Vrahatis records
Jung's theorem and several refinements/generalizations but not the
decomposition above.

Originality is therefore asserted **to the best of our knowledge**.
Because (1) follows from elementary standard identities, residual risk
remains that the same formula, or an equivalent one, appears as folklore
or under different terminology in computational geometry, convex
optimization, or variance inequalities.

## Scientific limitations

1. The result controls the active minimum-enclosing-ball certificate,
   not all of \(K\). Extra points of \(K\) may be geometrically far from
   a regular simplex while remaining inside the same enclosing ball.
2. The support-cardinality thresholds are sharp, but no optimality is
   claimed for the per-edge estimate (10) or volume estimate (11).
3. The Rips--Cech statement uses the explicit birth-value conventions
   above; other scale conventions introduce the usual factors of two.
4. Originality is to the best of our knowledge, with residual risk from
   equivalent formulations of the elementary weighted-variance
   calculation.

## References

1. H. W. E. Jung, *Über die kleinste Kugel, die eine räumliche Figur
   einschließt*, J. Reine Angew. Math. **123** (1901), 241--257.
   DOI: 10.1515/CRLL.1901.123.241.
2. K. Fischer, B. Gärtner, M. Kutz,
   *Fast Smallest-Enclosing-Ball Computation in High Dimensions*,
   ESA 2003, 630--641. DOI: 10.1007/978-3-540-39658-1_57.
3. T. Lim, R. J. McCann,
   *Geometrical Bounds for Variance and Recentered Moments*,
   Math. Oper. Res. **47** (2022), 286--296.
   DOI: 10.1287/moor.2021.1125.
4. R. Schneider,
   *Stability for Some Extremal Properties of the Simplex*,
   J. Geom. **96** (2009), 135--148.
   DOI: 10.1007/s00022-010-0028-0.
5. J. M. F. Castillo, P. L. Papini,
   *The finite Jung constant in Banach spaces*,
   Banach J. Math. Anal. **18** (2024), article 32.
   DOI: 10.1007/s43037-024-00341-1.
6. M. N. Vrahatis,
   *Towards the mathematical foundation of the minimum enclosing ball
   and related problems*, arXiv:2402.06629 (2024).
7. F. Chazal, V. de Silva, S. Oudot,
   *Persistence stability for geometric complexes*,
   Geom. Dedicata **173** (2014), 193--214.
   DOI: 10.1007/s10711-013-9937-z.
