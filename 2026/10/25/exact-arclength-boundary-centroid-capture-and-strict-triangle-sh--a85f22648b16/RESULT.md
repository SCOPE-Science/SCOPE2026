# Exact arclength-boundary centroid capture and strict triangle-shape ordering

## Finding

Let \(T\) be any nondegenerate Euclidean triangle with side lengths \(\ell_1,\ell_2,\ell_3\), perimeter \(P\), and centroid \(G\). Draw three independent points \(X_1,X_2,X_3\) from the uniform arclength distribution on the entire boundary of \(T\). Put \(p_i=\ell_i/P\), \(e_2=p_1p_2+p_2p_3+p_3p_1\), and \(e_3=p_1p_2p_3\). Then the probability of **centroid capture** is exactly

\[
\Pr\bigl(G\in\operatorname{conv}\{X_1,X_2,X_3\}\bigr)
=\left(\frac13+\frac{4\log 2}{9}\right)e_2
+\left(\frac{8\log 2}{3}-1\right)e_3.
\]

This probability is strictly Schur-concave in the normalized side-length vector. Consequently,

\[
\frac1{12}+\frac{\log2}{9}
<\Pr\bigl(G\in\operatorname{conv}\{X_1,X_2,X_3\}\bigr)
\le\frac{6+20\log2}{81}.
\]

The upper bound is attained exactly by equilateral triangles. The lower endpoint is a sharp *unattained* infimum, approached when the normalized side lengths tend to \((1/2,1/2,0)\). The upper bound equals the classical probability that three independent **area-uniform interior** points in *any* triangle capture its centroid, established by Prékopa (1972). Thus, for the same triangle, perimeter-arclength sampling yields strictly smaller centroid-capture probability than area-uniform sampling unless the triangle is equilateral. The classical upper value itself is not claimed as new; the new statement is the complete non-equilateral arclength law and its strict shape ordering and comparison.

## Assumptions and scope

The triangle has positive area and strictly positive side lengths satisfying the strict triangle inequalities; its perimeter is finite and positive. Independence means the three points are drawn with replacement from boundary arclength measure divided by \(P\). Vertices and configurations placing \(G\) exactly on a sampled segment have probability zero. A symmetric majorization comparison means a pair of normalized length vectors with the same sum, with one majorizing the other; any such admissible vectors satisfying \(\max p_i<1/2\) represent actual nondegenerate triangle shapes (up to similarity). The result is for three points, not arbitrary sample sizes, and for the geometric centroid, not the incenter or circumcenter.

## Proof

**Step 1: reduce to the edge-occupation distribution.** Each chosen point lies on edge \(i\) with probability \(p_i\), and conditional on its edge, its affine parameter is uniform on \([0,1]\). Any invertible affine transformation preserves centroid containment, so every conditional capture probability depends only on which of the three edges were sampled, not on the Euclidean angles or lengths. All three points on one edge cannot capture \(G\). There are two remaining occupancy patterns: two on one edge and one on another, with conditional probability \(a\); and one on each edge, with conditional probability \(b\). Therefore

\[
\Pr(G\in\operatorname{conv}\{X_i\})
=3a\sum_{i\ne j}p_i^2p_j+6b\,p_1p_2p_3.
\]

The factor \(3\) selects the position of the singleton in the three independent draws; the factor \(6\) counts all permutations in the all-distinct case. There is no contribution with all points on a single edge.

**Step 2: two-one conditional configuration.** Work in the reference triangle with vertices \((0,0),(1,0),(0,1)\) and centroid \((1/3,1/3)\). Two sampled points on the bottom edge have independent coordinates \((u,0),(v,0)\), and a singleton on the left edge is \((0,r)\), with \(u,v,r\) uniform on \([0,1]\). The horizontal section of their triangle at height \(1/3\) exists only for \(r\ge1/3\). At that height the centroid is captured exactly when

\[
\min(u,v)\le \frac{r}{3r-1}\le\max(u,v).
\]

Since the middle fraction is at most \(1\) only for \(r\ge1/2\), and for \(0\le w\le1\) two independent uniforms bracket \(w\) with probability \(2w(1-w)\),

\[
a=\int_{1/2}^1 \frac{2r(2r-1)}{(3r-1)^2}\,dr
=\frac19+\frac{4\log2}{27}.
\]

The case with the singleton on the third edge is congruent under a reflection of the reference triangle.

**Step 3: one-one-one conditional configuration.** Parametrize the three points cyclically by \((x,0),(1-y,y),(0,z)\), with independent \(x,y,z\sim U[0,1]\). The three consistently oriented barycentric half-plane tests for capturing \((1/3,1/3)\) are

\[
1-x-2y+3xy\ge0,\qquad 2y+2z-1-3yz\ge0,\qquad x+z-3xz\ge0.
\]

Define \(L(t)=(1-2t)/(2-3t)\) for \(0\le t\le1/2\), and \(L(t)=0\) for \(1/2<t\le1\). The first two tests are equivalent to \(L(z)\le y\le1-L(x)\). Their two forbidden intervals are disjoint because \(L(x)+L(z)\le1\). The third test removes a region only when both \(x\) and \(z\) exceed \(1/2\), in which case \(y\) is unrestricted by the first two tests. Thus all three forbidden sets are pairwise disjoint up to their null boundaries. Their respective volumes are

\[
I=\int_0^{1/2}\frac{1-2t}{2-3t}\,dt
=\frac13-\frac{2\log2}{9},\qquad
I,\qquad
J=\int_{1/2}^1\frac{2t-1}{3t-1}\,dt=I.
\]

It follows that

\[
b=1-2I-J=\frac{2\log2}{3}.
\]

**Step 4: the polynomial law.** The identity \(\sum_{i\ne j}p_i^2p_j=e_2-3e_3\) holds whenever \(\sum_i p_i=1\). Substituting the computed values of \(a,b\) into Step 1 gives

\[
3a=e_2\text{-coefficient}=\frac13+\frac{4\log2}{9},\qquad
6b-9a=e_3\text{-coefficient}=\frac{8\log2}{3}-1.
\]

Both coefficients are strictly positive.

**Step 5: sharp geometry and order.** For a strict triangle, \(0<p_i<1/2\) and \(\sum_i p_i=1\). Conversely these inequalities characterize its normalized side-length triples. Since \(\sum_i p_i^2<\frac12\sum_i p_i=1/2\), we have \(e_2=(1-\sum_i p_i^2)/2>1/4\) and \(e_3>0\); hence the stated strict lower inequality. It is sharp as \((p_1,p_2,p_3)\to(1/2,1/2,0)\) within the triangle domain. Standard equalization gives \(e_2\le1/3\) and \(e_3\le1/27\), simultaneously with equality only at \((1/3,1/3,1/3)\), yielding the upper value.

Finally, \(e_2=(1-\sum_i p_i^2)/2\) is strictly Schur-concave, and \(e_3\) is Schur-concave on the positive simplex (equivalently, \(\log(e_3)=\sum_i\log(p_i)\) is strictly concave and symmetric). Their positive linear combination is strictly Schur-concave. This proves the ordering including all triangle-shape comparisons under majorization.

## Verification

Exact symbolic integration gives the values \(a=1/9+4\log2/27\), \(I=J=1/3-2\log2/9\), and \(b=2\log2/3\). The equilateral specialization of the polynomial is \(2/27+20\log2/81\), independently matching Prékopa's equation (5.24). The accompanying standalone `verify.py` performs deterministic numerical quadrature of the three critical integrals, checks symbolic identities numerically at nontrivial side-length vectors, and uses independently sampled *Euclidean boundary points* to check centroid inclusion for several non-similar triangles. A finite simulation is diagnostic only; the infinite-domain statements follow from the analytic proof above.

## Relationship to prior work

Prékopa, **On the number of vertices of random convex polyhedra** (1972), Section 5, equations (5.19)–(5.24) and Lemma 2, proves the exact centroid-capture constant \(2/27+20\log2/81\) for three area-uniform interior points of a triangle. Lemma 2 explains the equality with the case of *uniform equal mass on the three sides* via radial projection from the centroid. It does **not** give the formula for Euclidean arclength sampling on a general non-equilateral triangle, whose edge masses are proportional to three unequal side lengths. The known constant is explicitly credited; the present contribution is the complete length-weighted law, strict shape ordering, and the equality-rigid comparison of arclength and area sampling.

Wendel (1962) gives an exact center-containment probability \(1/4\) for three points from a centrally symmetric distribution in the plane; perimeter sampling on a triangle is not centrally symmetric. Halász and Kleitman (1974) studied area-uniform random triangles and the best containing point; their context and Prékopa's work encompass the known area-uniform benchmark, not the unequal-length perimeter model. Bárány, Fodor, and Vígh (arXiv:0906.0309, first posted 2009-06-01) study intrinsic volumes of interior-uniform random polytopes in smooth convex bodies, with different object, sampling and asymptotic questions.

## Limitations

The exact equality case uses strict nondegeneracy; the lower endpoint is an infimum and never attained by a genuine triangle. The formula does not address arclength distributions with nonuniform within-edge densities, polygons with four or more sides, interior points other than the centroid, or four-or-more-point capture. Bibliographic searches and primary-text comparisons cannot prove that no unindexed earlier equivalent weighted-side formulation exists; a broad geometric probability integration formula could imply the result after a nontrivial specialization. Independent third-party verification has not been performed. The earlier Prékopa constant must not be interpreted as a new discovery.

## References

1. A. Prékopa, *On the number of vertices of random convex polyhedra*, Periodica Mathematica Hungarica **2** (1972), 259–282, Section 5 and Lemma 2, DOI: 10.1007/BF02018666; author's open text: https://rutcor.rutgers.edu/~prekopa/number.pdf.
2. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica **11** (1962), 109–112, DOI: 10.7146/math.scand.a-10655.
3. S. Halász and D. J. Kleitman, *A Note on Random Triangles*, Studies in Applied Mathematics **53** (1974), 225–237, DOI: 10.1002/sapm1974533225.
4. I. Bárány, F. Fodor and V. Vígh, *Intrinsic volumes of inscribed random polytopes in smooth convex bodies*, arXiv:0906.0309, first posted 2009-06-01; DOI: 10.1239/aap/1282924055.
