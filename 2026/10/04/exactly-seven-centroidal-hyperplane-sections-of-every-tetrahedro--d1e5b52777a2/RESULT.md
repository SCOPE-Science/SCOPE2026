# Exactly seven centroidal hyperplane sections of every tetrahedron

## Finding

Let \(T\subset\mathbb R^3\) be a nondegenerate tetrahedron and let \(g=c(T)\) be its centroid. There are exactly seven unoriented affine planes \(H\) through \(g\) for which
\[
c(T\cap H)=g.
\]

In barycentric coordinates \((\lambda_1,\lambda_2,\lambda_3,\lambda_4)\) with respect to the vertices of \(T\), the seven planes are exactly
\[
\lambda_i=\frac14\qquad (1\le i\le4)
\]
and
\[
\lambda_i+\lambda_j=\frac12,
\]
one for each unordered partition of the four vertices into two pairs. Thus the seven planes are naturally indexed by the seven nontrivial unordered bipartitions of the vertex set.

## Assumptions and scope

A hyperplane section is called centroidal here when the centroid of the two-dimensional section agrees with the three-dimensional centroid of the tetrahedron. Hyperplanes are counted without orientation.

The statement is affine invariant. An invertible affine map sends a tetrahedron centroid to the image centroid and sends the centroid of every planar section to the centroid of the image section. It is therefore enough to work entirely in barycentric coordinates on the abstract simplex
\[
\lambda_i\ge0,
\qquad
\sum_{i=1}^4\lambda_i=1,
\qquad
g=\left(\frac14,\frac14,\frac14,\frac14\right).
\]

No regularity, edge-length, or angle hypothesis is imposed on \(T\).

## Proof

Any plane through \(g\) has an equation
\[
\sum_{i=1}^4 a_i\lambda_i=0
\]
with
\[
\sum_{i=1}^4a_i=0,
\]
and the coefficient vector is determined up to a nonzero scalar.

First suppose one coefficient is positive and the other three are negative. After relabeling, write the coefficients as
\[
\alpha,-\gamma_2,-\gamma_3,-\gamma_4,
\qquad
\alpha>0,
\qquad
\gamma_j>0,
\qquad
\gamma_2+\gamma_3+\gamma_4=\alpha.
\]
The section is the triangle whose vertex on the edge joining vertex \(1\) to vertex \(j\) has
\[
\lambda_j=\frac{\alpha}{\alpha+\gamma_j}.
\]
At the centroid of this section, the \(j\)-th barycentric coordinate is therefore
\[
\frac13\frac{\alpha}{\alpha+\gamma_j}.
\]
Requiring this to equal \(1/4\) gives
\[
\gamma_j=\frac{\alpha}{3}
\]
for each \(j=2,3,4\). Hence the plane is
\[
\lambda_1=\frac14.
\]
The opposite sign pattern gives the same plane, and relabeling yields the four facet-parallel planes.

Now suppose two coefficients are positive and two are negative. Write them as
\[
\alpha,\beta,-\gamma,-\delta,
\qquad
\alpha\ge\beta>0,
\qquad
\delta\ge\gamma>0.
\]
Since the coefficients sum to zero, after a common positive rescaling we may assume
\[
\alpha+\beta=\gamma+\delta=1.
\]
Set
\[
\alpha=\frac{1+u}{2},
\quad
\beta=\frac{1-u}{2},
\quad
\gamma=\frac{1-v}{2},
\quad
\delta=\frac{1+v}{2},
\qquad
0\le u,v<1.
\]

Project the section affinely to the \((\lambda_1,\lambda_3)\)-plane. Its four vertices, in cyclic order, are
\[
O=(0,0),
\quad
A=(p,0),
\quad
C=(r,s),
\quad
B=(0,q),
\]
where
\[
p=\frac{1+v}{2+u+v},
\quad
q=\frac{1-u}{2-u-v},
\quad
r=\frac{1-v}{2+u-v},
\quad
s=\frac{1+u}{2+u-v}.
\]
Because this projection is an affine isomorphism on the section, it preserves centroids. Triangulating the quadrilateral as \(OAC\cup OCB\), its centroid coordinates are
\[
\bar x=\frac{ps(p+r)+rq\,r}{3(ps+rq)},
\qquad
\bar y=\frac{ps\,s+rq(s+q)}{3(ps+rq)}.
\]
The desired barycenter condition is
\[
\bar x=\bar y=\frac14.
\]
Clearing the positive denominators gives two polynomial equations \(P(u,v)=Q(u,v)=0\), with
\[
\begin{aligned}
P={}&3u^4-2u^3v^2+6u^3+2u^2v^2-4u^2+2uv^4+2uv^2-8u+3v^4-4v^2,\\
Q={}&2u^4v-3u^4-2u^2v^3-2u^2v^2+2u^2v+4u^2-3v^4+6v^3+4v^2-8v.
\end{aligned}
\]
Exact elimination gives
\[
\operatorname{Res}_v(P,Q)
=16384u^3(u-1)^6(u+1)^9(3u^2-4).
\]
For \(0\le u<1\), a common zero can therefore have only \(u=0\). Substitution gives
\[
P(0,v)=v^2(3v^2-4),
\]
so \(0\le v<1\) forces \(v=0\). Hence
\[
\alpha=\beta=\gamma=\delta,
\]
and the plane is
\[
\lambda_1+\lambda_2=\frac12.
\]
There are exactly three such planes, one for each partition of four vertices into two pairs.

It remains to exclude zero coefficients. If exactly one coefficient is zero, the section is a triangle containing that simplex vertex, while its other two vertices have zero in that barycentric coordinate; the section centroid therefore has that coordinate \(1/3\), not \(1/4\). If exactly two coefficients are zero, the same argument applies to either contained simplex vertex. Three zero coefficients are impossible for a nonzero coefficient vector with zero sum.

Finally, every listed plane is indeed centroidal. A section \(\lambda_i=1/4\) is a triangle whose three vertices have the remaining mass \(3/4\) on one coordinate each, so its centroid is \(g\). A section \(\lambda_i+\lambda_j=1/2\) is a parallelogram centrally symmetric about \(g\), so its centroid is \(g\). This proves both existence and completeness.

## Verification

The standalone checker `verify.py` recomputes the quadrilateral centroid formulas in exact symbolic arithmetic, clears denominators, reconstructs the two displayed polynomials, and recomputes the resultant
\[
16384u^3(u-1)^6(u+1)^9(3u^2-4).
\]
It also checks the one-positive/three-negative equation and the \(4+3=7\) bipartition count.

The replay output is:

`VERIFY_OK tetrahedron seven centroidal sections`

The checker is a certificate for the algebraic elimination step. The geometric reduction, sign-pattern split, affine covariance, and zero-coefficient exclusion are proved above and do not follow merely from numerical experimentation.

## Relationship to prior work

Myroshnychenko, Tatarko, and Yaskin formulate the Grünbaum–Loewner centroid-section problem and define \(\mu(K)\) as the number of hyperplane sections through \(c(K)\) whose centroid is \(c(K)\). Their 2024 work proves \(\mu(n)=1\) for \(n\ge5\), records dimensions \(3\) and \(4\) as the remaining cases at that time, and lists primary MSC classes \(52A20\) and \(52A40\). Its inspected full text contains no occurrence of “tetrahedron” or “simplex.”

Patáková, Tancer, and Wagner study barycentric hyperplanes and show that the earlier general argument of Grünbaum had a gap. Their inspected paper treats a triangular prism and a triangular bipyramid as explicit three-dimensional examples, but contains no occurrence of “tetrahedron.”

Wang, Xiong, and Yang subsequently proved in 2026 that the minimum over all convex bodies is \(\mu(3)=\mu(4)=1\). That global minimization result does not determine \(\mu(T)\) for a tetrahedron; its inspected full text also contains no occurrence of “tetrahedron” or “simplex.” The present result is instead an exact object-level classification:
\[
\mu(T)=7
\]
for every tetrahedron \(T\).

Targeted searches for tetrahedra, simplex centroid sections, vertex bipartitions, facet-parallel centroid sections, and midpoint sections did not locate a published statement equivalent to the seven-plane classification. This negative search evidence is not by itself a proof of originality; it is combined with the full-text implication comparisons above.

## Limitations

The proof is special to dimension three. Although the seven planes are indexed by all nontrivial unordered vertex bipartitions of a tetrahedron, no claim is made that an \(n\)-simplex has exactly \(2^n-1\) centroidal hyperplanes in higher dimension.

The result concerns sections through the centroid of the tetrahedron. It does not classify barycentric hyperplanes through arbitrary interior points, depth-realizing hyperplanes, or centroidal sections of general three-dimensional convex bodies.

A residual originality risk remains because the classification is elementary enough that an equivalent observation could appear in older simplex-geometry literature under terminology not captured by the searches performed.

## References

S. Myroshnychenko, K. Tatarko, and V. Yaskin, “Answers to questions of Grünbaum and Loewner,” arXiv:2404.15188, first submitted 2024-04-23.

Z. Patáková, M. Tancer, and U. Wagner, “Barycentric Cuts Through a Convex Body,” arXiv:2003.13536; SoCG 2020, Article 62; Discrete & Computational Geometry 68 (2022), 1133–1154.

S. Wang, X. Ge, and K. Yang, “A complete solution to the Grünbaum–Loewner centroid problems,” arXiv:2606.19865, 2026.
