# Exact Euclidean inradius of partial permutohedra
## Finding
For integers \(m\ge 2\) and \(n\ge m-1\), let \(\mathcal P(m,n)\subset\mathbb R^m\) be the partial permutohedron: the convex hull of all vectors in \(\{0,1,\ldots,n\}^m\) whose nonzero entries are distinct. Define its Euclidean inradius to be the largest \(r\) for which some Euclidean ball of radius \(r\) is contained in \(\mathcal P(m,n)\).

Then
\[
r(\mathcal P(m,n))=
\min\!\left\{
\frac n2,
\frac{\sqrt m\,(2n-m+1)}{2(\sqrt m+1)}
\right\}.
\]
The center of the largest inscribed ball is unique and equals
\[
c_{m,n}\mathbf 1=r(\mathcal P(m,n))\mathbf 1.
\]
There is a sharp tangency transition. If \(n<m+\sqrt m\), the ball is tangent to every coordinate facet \(x_i=0\) and to the total-sum facet. If \(n>m+\sqrt m\), it is tangent to every coordinate facet \(x_i=0\) and every singleton upper facet \(x_i=n\). At equality, both upper families are tangent. Since \(m,n\) are integers, equality can occur only when \(m\) is a perfect square and \(n=m+\sqrt m\).

## Assumptions and scope
The parameters satisfy \(m\ge2\) and \(n\ge m-1\). The norm is the standard Euclidean norm in \(\mathbb R^m\). The result uses the inequality description of partial permutohedra from Heuer--Striker. In the stated range, for each nonempty \(S\subseteq[m]\) with \(|S|=k\), every point \(x\in\mathcal P(m,n)\) satisfies
\[
x_i\ge0,
\qquad
\sum_{i\in S}x_i\le R_k,
\qquad
R_k=\binom{n+1}{2}-\binom{n-k+1}{2}
=\frac{k(2n-k+1)}2.
\]
When \(n=m-1\), some inequalities of cardinality \(m-1\) are redundant, but the coordinate, singleton, and total-sum inequalities used for the sharp upper bounds below are valid; the total-sum inequality is facet-defining. Redundant valid inequalities cause no problem in the containment argument.

## Proof
First reduce the center by symmetry. The polytope is invariant under every coordinate permutation. If \(B(z,r)\subseteq\mathcal P(m,n)\), then \(B(\sigma z,r)\subseteq\mathcal P(m,n)\) for every \(\sigma\in\mathfrak S_m\). The Minkowski average of these balls is
\[
\frac1{m!}\sum_{\sigma\in\mathfrak S_m}B(\sigma z,r)
=B(c\mathbf1,r),
\qquad
c=\frac1m\sum_{i=1}^m z_i.
\]
Convexity of \(\mathcal P(m,n)\) therefore implies \(B(c\mathbf1,r)\subseteq\mathcal P(m,n)\). Hence an optimal ball may be chosen with center \(c\mathbf1\).

For this center, the distance to a coordinate hyperplane \(x_i=0\) is \(c\), while the distance to a subset-sum hyperplane of cardinality \(k\) is
\[
d_k(c)=\frac{R_k-kc}{\sqrt k}.
\]
Thus the largest radius supported at \(c\mathbf1\) is
\[
\rho(c)=\min\left\{c,\min_{1\le k\le m}d_k(c)\right\}.
\]
The equation \(c=d_k(c)\) has the unique solution
\[
a_k=\frac{R_k}{k+\sqrt k}
=\frac{\sqrt k\,(2n-k+1)}{2(\sqrt k+1)}.
\]
Let \(A=\min_{1\le k\le m}a_k\). At \(c=A\), every inequality has distance at least \(A\), so \(\rho(A)=A\). If \(c>A\) and \(a_k=A\), then
\[
d_k(c)=A+\sqrt k\,(A-c)<A,
\]
while if \(c<A\) then \(\rho(c)\le c<A\). Therefore the inradius is exactly \(A\).

It remains to minimize \(a_k\). Put \(t=\sqrt k\) and \(Q=2n+1\). On the continuous interval \(1\le t\le\sqrt m\), define
\[
f(t)=\frac{t(Q-t^2)}{2(t+1)}.
\]
Then \(a_k=f(\sqrt k)\) and
\[
f'(t)=\frac{Q-3t^2-2t^3}{2(t+1)^2}.
\]
The numerator has derivative \(-6t-6t^2<0\), so \(f'\) changes sign at most once, and only from positive to negative. Hence \(f\) has no interior minimum: its minimum on the interval is attained at an endpoint. Consequently
\[
A=\min\{a_1,a_m\}
=\min\!\left\{
\frac n2,
\frac{\sqrt m\,(2n-m+1)}{2(\sqrt m+1)}
\right\}.
\]
Direct comparison gives
\[
a_1\le a_m
\quad\Longleftrightarrow\quad
n\ge m+\sqrt m.
\]
This proves the radius formula and the phase transition.

Finally, the center is unique. In the strict total-sum regime, any radius-\(A\) ball has center \(z\) satisfying \(z_i\ge A\) for every coordinate facet and
\[
\sum_i z_i\le R_m-A\sqrt m=mA,
\]
so every \(z_i=A\). In the strict singleton regime, \(z_i\ge A\) and the singleton upper facets give \(z_i\le n-A=A\), again forcing \(z=A\mathbf1\). At the transition either argument applies.

## Verification
The accompanying standard-library script evaluates all subset-cardinality distances for \(m=2,\ldots,200\) and \(n=m-1,\ldots,m+100\). It checks that the minimum of all \(a_k\) equals the stated endpoint formula, that the proposed ball satisfies every defining halfspace with the claimed radius, and that the predicted active upper family is tangent. This is a finite consistency check only; the derivative argument above proves the statement for all admissible \(m,n\).

The boundary case \(\mathcal P(2,1)\) is the right triangle \(\operatorname{conv}\{(0,0),(1,0),(0,1)\}\), and the formula gives \(1-1/\sqrt2\), its usual Euclidean inradius.

## Relationship to prior work
Heuer and Striker introduced partial permutohedra and proved the subset-sum inequality description used here (arXiv:2012.09901, Theorem 5.9), together with the facet count. Behrend, Castillo, Chavez, Diaz-Lopez, Escobar, Harris, and Insko subsequently studied the face lattice, volume, and Ehrhart theory of the same family (arXiv:2207.14253); their paper lists \(52B05\) first among its MSC classifications. Neither inspected full text contains an inradius, largest-inscribed-ball, or Euclidean-center theorem.

The later generalized parking-function-polytope literature gives broader facet descriptions and connections to partial permutohedra, but its inspected 2024 full text studies vertices, facets, generalized-permutahedron structure, face types, and combinatorial/circuit diameters rather than Euclidean inradii (arXiv:2403.07387). Targeted literature and research-record searches for partial-permutohedron inradii, Chebyshev centers, and generalized-permutahedron inradii did not locate an equivalent statement. The present result is not inferred from search failure: the formula and uniqueness are proved directly from the published halfspace description.

## Limitations
The theorem is restricted to \(n\ge m-1\), the range in which the displayed endpoint reduction has the stated simple form. It does not give the inradius for arbitrary \(m,n\) with \(n<m-1\), where more upper inequalities are redundant and the effective facet structure changes. It concerns Euclidean balls only, not John ellipsoids, circumradii, or other norms. A residual originality risk is that a general unpublished or differently worded theorem on Chebyshev centers of symmetric polymatroid-type polytopes could specialize to the same formula; targeted searches did not locate one.

## References
1. Dylan Heuer and Jessica Striker, “Partial Permutation and Alternating Sign Matrix Polytopes,” arXiv:2012.09901, first posted 2020-12-17; SIAM Journal on Discrete Mathematics 36 (2022), DOI 10.1137/21M1417958.
2. Roger E. Behrend, Federico Castillo, Anastasia Chavez, Alexander Diaz-Lopez, Laura Escobar, Pamela E. Harris, and Erik Insko, “Partial permutohedra,” arXiv:2207.14253, first posted 2022-07-28.
3. Margaret M. Bayer et al., “Combinatorics of generalized parking-function polytopes,” arXiv:2403.07387, first posted 2024-03-12.
